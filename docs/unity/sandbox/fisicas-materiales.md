title: Físicas y materiales | Curso Unity desde cero | Hektor Profe

# Físicas y materiales

Muy bien, vamos a empezar esta lección con un reto:

!!! warning "Ejercicio"
    Crea una esfera de color rojo, reinicia su componente `Transform` y haz que flote encima del borde del cubo.

Más o menos así:

![]({{cdn}}/unity/Screenshot_49.png)

Venga, otro reto:

!!! warning "Ejercicio"
    Añade un componente `RigidBody` a la esfera para activar sus físicas y luego prueba el juego para ver qué ocurre.

Tal que así:

![]({{cdn}}/unity/Record_03.gif)

El caso es que la esfera choca contra el borde del cubo y empieza a rodar hasta caer y desaparecer.

Tengo una idea, para evitar que la bola caiga por los bordes vamos a bordear el suelo para hacer un tope, pero antes haremos el suelo el doble de grande, escalando su tamaño a (2,2,2), así tendremos más espacio para jugar.

![]({{cdn}}/unity/Screenshot_50.png)

Para crear los topes usaremos como base un cubo, que alargándolos y rotaremos hasta conseguir el tamaño deseado.

!!! warning "Ejercicio"
    Crea un cubo, estíralo y posiciónalo a los lados del suelo para evitar que la esfera caiga al vacío. Luego clónalo y bordea el suelo en sus cuatro lados.

Al final debería quedarnos algo así, con 4 cubos haciendo de topes:

![]({{cdn}}/unity/Screenshot_51.png)

Las propiedades de `Transformación` de cada cubo pueden establecerse manualmente para conseguir una alineación y tamaño perfectos:

* (0.0, 0.5, 0.0) (0,0,0) (20,1,1)
* (9.5, 0.5, 0.0) (0,90,0) (20,1,1)
* (0.0, 0.5, 9.5) (0,0,0) (20,1,1)
* (-9.5, 0.5, 0.0) (0,90,0) (20,1,1)

Con esto conseguiremos que el cubo no caiga:

![]({{cdn}}/unity/Record_04.gif)

Vamos a hacer algo interesante, demos al cubo la posición de origen y hagámoslo mucho más alto y el doble de grande, como si fuera una columna en medio del escenario:

![]({{cdn}}/unity/Screenshot_52.png)

Si dejamos caer la esfera desde el borde, ¿os habéis fijado que no rebota contra el suelo? Eso es porque si bien, tiene un material para manejar el aspecto, no tiene un material físico establecido.

![]({{cdn}}/unity/Record_05.gif)

Para crear un material físico haremos clic derecho en `Assets/Materials > Create > Physic Material` y le daremos el nombre `Goma`.

Arrastraremos el material a la esfera y se añadirá al componente `Sphere Collider` en su propiedad `Material` automáticamente:

![]({{cdn}}/unity/Screenshot_53.png)

Si bien este material está configurado para tener una fricción, tenemos que añadir un coheficiente de rebote. Este número debe establecerse entre 0 y 1, siendo 0 un rebote nulo y 1 el máximo, pongamos 1 para ver como queda:
 
![]({{cdn}}/unity/Screenshot_54.png)

Si probamos de nuevo, ahora la esfera rebotará contra el suelo como si fuera de goma:

![]({{cdn}}/unity/Record_06.gif)

El problema es que ahora la "pelota" no frena hasta toparse de nuevo con el pilar. Para solucionarlo debemos indicarle a la "pelota" que debe tener en cuenta una resistencia al movimiento, esta se puede configurar en la propiedad `Angular Drag` del `RigidBody`. Un arrastre angular de 0.05 es muy pequeño, pero si lo subimos por ejemplo a 2.5, el resultado será algo diferente: 

![]({{cdn}}/unity/Screenshot_55.png)

Y este será el nuevo resutado:

![]({{cdn}}/unity/Record_07.gif)

Con esto hemos visto cómo afectan los `materiales físicos` a los objetos y también cómo la propiedad `Angular Drag` resta aceleración a los cuerpos en movimiento.

Poco a poco nos vamos intoduciendo en el sistema de físicas, en la siguiente lección vamos a profundizar un poco más.

___
<small class="edited"><i>Última edición: 12 de Abril de 2021</i></small>