title: Sistema de películas de usuario | Curso de Django Rest Framework | Hektor Profe
description: Sistema de películas favoritas para nuestra API con Django Rest Framework.

# Sistema de películas de usuario en DRF

En esta última unidad vamos a programar la interacción entre los usuarios y las películas. Esto nos permitirá que puedan gestionar diferentes opciones en las películas:

* Marcarlas como favoritas
* Configurar estados (vista, por ver...)
* Añadir una puntuación
* Escribir reseñas

Además esto implicará que las películas deberán mostrar el número de favoritos y la nota media en su endpoint, por lo que deberemos configurar estos campos.

## Modelo de películas de usuario

Para poder gestionar todo el tinglado necesitamos dar de alta un nuevo modelo para manejar la relación entre usuario y película, lo llamaremos FilmUser:

**`server/films/models.py`**

```python
from django.conf import settings  # new
from django.core.validators import MaxValueValidator  # new

class FilmUser(models.Model):

    STATUS_CHOICES = (
        (0, "Sin estado"),
        (1, "Vista"),
        (2, "Quiero verla"))

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)

    # Se podría hacer en tres modelos separados para que sea más eficiente
    # pero a nivel de desarrollo habría que hacer lo mismo tres veces

    state = models.PositiveSmallIntegerField(
        choices=STATUS_CHOICES, default=0)  # Al crearse sin estado se borra
    favorite = models.BooleanField(
        default=False)
    note = models.PositiveSmallIntegerField(
        null=True, validators=[MaxValueValidator(10)])
    review = models.TextField(null=True)

    class Meta:
        unique_together = ['film', 'user']
        ordering = ['film__title']
```

Migramos:

```bash
pipenv run makemigrations
pipenv run migrate
```

Ahora vamos a crear una vista de tipo `APIView` para manejar estas interacciones, pero antes necesitamos crear un serializador para las películas de usuario:

**`server/films/serializers.py`**

```python
from .models import Film, FilmGenre, FilmUser  #updated

class FilmUserSerializer(serializers.ModelSerializer):

    film = FilmSerializer(read_only=True)

    class Meta:
        model = FilmUser
        fields = ['film', 'favorite', 'note', 'state', 'review']

```

Y ahora la viewset para nuestro modelo `FilmUser`:

**`server/films/views.py`**

```python
from rest_framework import viewsets, filters, status, views  # updated
from .models import Film, FilmGenre, FilmUser  # updated
from .serializers import (FilmSerializer, FilmGenreSerializer, 
                            FilmUserSerializer)  # updated

class FilmUserViewSet(views.APIView):

    # El método GET devolverá las peliculas del usuario
    def get(self, request, *args, **kwargs):
        queryset = FilmUser.objects.filter(user=self.request.user)
        serializer = FilmUserSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # El método POST permitirá gestionar su información de la película
    def post(self, request, *args, **kwargs):
        try:
            film = Film.objects.get(id=request.data['uuid'])
        except Film.DoesNotExist:
            return Response(
                {'status': 'Film not found'},
                status=status.HTTP_404_NOT_FOUND)

        # Una vez recuperada la película creamos o recuperamos su FilmUser
        film_user, created = FilmUser.objects.get_or_create(
            user=request.user, film=film)

        # Configuramos cada campo
        film_user.state = request.data.get('state', 0)
        film_user.favorite = request.data.get('favorite', False)
        film_user.note = request.data.get('note', -1)
        film_user.review = request.data.get('review', None)

        # Si se marca la pelicula como NO VISTA la borramos automáticamente
        if int(film_user.state) == 0:
            film_user.delete()
            return Response(
                {'status': 'Deleted'}, status=status.HTTP_200_OK)

        # En otro caso guardamos los campos de la película de usuario
        else:
            film_user.save()

        return Response(
            {'status': 'Saved'}, status=status.HTTP_200_OK)
```

Damos de alta la URL en un nuevo endpoint:

**`server/server/urls.py`**

```python
urlpatterns = [
    # ...
    path('api/userfilms/', film_views.FilmUserViewSet.as_view())
]
```

En este punto deberíamos ser capaces de acceder a `http://127.0.0.1:8000/api/userfilms/` y ver las películas del usuario identificado en el administrador. 

Como no hemos creado ninguna esa respuesta estará vacía, pero podemos crear una película de usuario de prueba haciendo una petición `POST`. 

Por ejemplo para añadir la información de la película de **Apocalypse Now**, cuyo **uuid** es **d1d5acd7-5f76-4faa-aca7-fdb9cc88eb02** escribiremos lo siguiente:

```json
{   "uuid": "d1d5acd7-5f76-4faa-aca7-fdb9cc88eb02", 
    "favorite": 1, 
    "note": 10, 
    "state": 1, 
    "review": "Me encanta esta película..."
}
```

Esto nos devolverá:

```json
{
    "status": "Saved"
}
```

Indicando que el registro de la película de usuario se ha guardado correctamente.

Podemos consultar de nuevo la lista recargando el endpoint y ahora sí veremos la lista con las películas favoritas del usuario:

```json
[
    {
        "film": {
            "id": "d1d5acd7-5f76-4faa-aca7-fdb9cc88eb02",
            "genres": [
                {
                    "id": 15,
                    "name": "Bélica",
                    "slug": "belica"
                },
                {
                    "id": 3,
                    "name": "Drama",
                    "slug": "drama"
                },
                {
                    "id": 10,
                    "name": "Misterio",
                    "slug": "misterio"
                }
            ],
            "title": "Apocalypse Now",
            "year": 1979,
            "review_short": "En 1969, durante la guerra de Vietnam, el coronel Kurtz (Marlon Brando), de las Fuerzas Especiales del Ejército de Estados Unidos, se ha vuelto loco y ahora manda a sus propias tropas de montañeses, dentro de la neutral Camboya, como un semidiós.",
            "review_large": "En 1969, durante la guerra de Vietnam, el coronel Kurtz (Marlon Brando), de las Fuerzas Especiales del Ejército de Estados Unidos, se ha vuelto loco y ahora manda a sus propias tropas de montañeses, dentro de la neutral Camboya, como un semidiós. \r\n\r\nEl coronel Lucas (Harrison Ford) y el general Corman (G. D. Spradlin), cada vez más preocupados por las operaciones de vigilancia de Kurtz, asignan al capitán de MACV-SOG Benjamin L. Willard (Martin Sheen) para que «ponga fin» a Kurtz «con extremo perjuicio» (asesinarlo).",
            "trailer_url": "https://www.youtube.com/watch?v=9l-ViOOFH-s",
            "image_thumbnail": "http://localhost:8000/media/films/d1d5acd7-5f76-4faa-aca7-fdb9cc88eb02/17.jpg",
            "image_wallpaper": "http://localhost:8000/media/films/d1d5acd7-5f76-4faa-aca7-fdb9cc88eb02/17-1.jpg"
        },
        "favorite": true,
        "note": 10,
        "state": 1,
        "review": "Me encanta esta película..."
    }
]
```

Si queremos modificar la película de usuario basta con enviar de nuevo los campos deseados a la petición:

```json
{   "uuid": "d1d5acd7-5f76-4faa-aca7-fdb9cc88eb02", 
    "favorite": 0, 
    "note": 0, 
    "state": 1,
    "review": "Ya no me gusta esta película"
}
```

Pero si enviamos una petición sin estado, o con el estado en cero (que es de película no vista), la película de usuario se borrará de la base de datos:

```json
{ 
    "uuid": "d1d5acd7-5f76-4faa-aca7-fdb9cc88eb02"
}
```

Devolviendo:

```json
{
    "status": "Deleted"
}
```

Evidentemente esto es solo mi forma de manejar toda la lógica, cada uno puede decidir como y cuando borrar los campos.

## Reseñas y películas favoritas

Ahora que manejamos favoritos y notas de película, podemos almacenarlas dinámicamente en las películas. Para ello vamos a crear dos nuevos campos en el modelo de película:

**`server/films/models.py`**

```python
from django.db.models import Sum  # new
from django.db.models.signals import post_save  # new

class Film(models.Model):
    
    # ...

    # Estadisticas actualizadas con señales
    favorites = models.IntegerField(
        default=0, verbose_name="favoritos")
    average_note = models.FloatField(
        default=0.0, verbose_name="nota media", 
        validators=[MaxValueValidator(10.0)])
```

Para actualizar estos campos lo haremos usando una señal `post_save` a nivel de `FilmUser`:

**`server/films/models.py`**

```python
def update_film_stats(sender, instance, **kwargs):
    # Actualizamos los favoritos contando los favoritos de esa película
    count_favorites = FilmUser.objects.filter(
        film=instance.film, favorite=True).count()
    instance.film.favorites = count_favorites
    # Actualizamos la nota recuperando el número de notas y haciendo la media
    notes = FilmUser.objects.filter(
        film=instance.film).exclude(note__isnull=True)
    count_notes = notes.count()
    sum_notes = notes.aggregate(Sum('note')).get('note__sum')
    # Intentamos hacer la media con dos decimales usando un try
    # Fallará si sum_notes es None como count_notes es 0
    # Esto sucede las primeras veces porque aún no hay notas establecidas
    try:
        instance.film.average_note = round(sum_notes/count_notes, 2)
    except:
        pass
    # Guardamos la película
    instance.film.save()

# en el post delete se pasa la copia de la instance que ya no existe
post_save.connect(update_film_stats, sender=FilmUser)
```

Migramos:

```bash
pipenv run makemigrations
pipenv run migrate
```

Ahora podemos añadir los campos favorites y average_note como campos de ordenación en el viewset:

**`server/films/views.py`**

```python
class FilmViewSet(viewsets.ReadOnlyModelViewSet):
    # ...
    ordering_fields = ['title', 'year',
                    'genres__name', 'favorites', 'average_note']
```

Y si creamos una petición de película de usuario en `http://127.0.0.1:8000/api/userfilms/`, por ejemplo la de antes:

```json
{   "uuid": "d1d5acd7-5f76-4faa-aca7-fdb9cc88eb02", 
    "favorite": 1, 
    "note": 10, 
    "state": 1, 
    "review": "Me encanta esta película..."
}
```

Deberíamos ser capaces de ver la información de esta película en su viewset con la nota media y el número de favoritos `http://127.0.0.1:8000/api/films/d1d5acd7-5f76-4faa-aca7-fdb9cc88eb02/`:

```json
{
    "id": "d1d5acd7-5f76-4faa-aca7-fdb9cc88eb02",
    // ...
    "favorites": 1,
    "average_note": 10.0
}
```

¡Perfecto! Ya tenemos el viewset de `UserFilm` casi listo y el proyecto acabado, solo falta un pequeñísimo detalle.

## Proteger las urls con interacción de usuario

Si intentamos acceder al endpoint de `UserFilm` sin estar autenticados `http://127.0.0.1:8000/api/userfilms/` aparece un error `TypeError at /api/userfilms/`.

Podemos mejorar la seguridad estableciendo un requisito en la `APIView` para requerir autenticación en esta vista, es muy sencillo:

**`server/films/views.py`**

```python
from rest_framework import (viewsets, filters, status, views, 
                            authentication, permissions) # updated

class FilmUserViewSet(views.APIView):
    authentication_classes = [authentication.SessionAuthentication]  # new
    permission_classes = [permissions.IsAuthenticated] # new
```

Ahora al acceder sin estar autenticado a `http://127.0.0.1:8000/api/userfilms/` nos devolverá el siguiente error, pero en esta ocasión a nivel de API, evitando el fallo de código:

```json
{
    "detail": "Las credenciales de autenticación no se proveyeron."
}
```

Y con esto acabamos este curso fallido de Django Rest Framework.

Si os ha gustado este curso y aún no sois alumnos de mi curso de Django en Udemy <u>[considerad adquirirlo en este enlace](https://www.udemy.com/course/curso-django-2-practico-desarrollo-web-python-3/?referralCode=4299F3A993394B53F7A1)</u>, en él explico todas las claves de este framework web.

___
<small class="edited"><i>Última edición: 19 de Marzo de 2021</i></small>
