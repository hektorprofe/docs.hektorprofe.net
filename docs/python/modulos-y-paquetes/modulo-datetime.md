title: Módulo datetime | Curso de Python | Hektor Profe
description: Los módulos son ficheros que contienen definiciones que se pueden importar en otros scripts para reutilizar sus funcionalidades.

<style>

.admonition.note > .superfences-tabs > label:hover, .headerlink{
    color: #018dc5 !important;
}

.admonition.info{
    font-size: 100%;
}

.admonition.info label{
    font-size: 91%;
}

.admonition.note > .admonition-title {
    display: none;
}

</style>

# Módulo datetime

Este módulo contiene las clases time y datetime esenciales para manejar tiempo, horas y fechas.

## Clase datetime

Esta clase permite crear objetos para manejar fechas y horas:

!!! info "" 

    ```python
    from datetime import datetime

    dt = datetime.now()    # Fecha y hora actual

    print(dt)
    print(dt.year)         # año
    print(dt.month)        # mes
    print(dt.day)          # día

    print(dt.hour)         # hora
    print(dt.minute)       # minutos
    print(dt.second)       # segundos
    print(dt.microsecond)  # microsegundos

    print("{}:{}:{}".format(dt.hour, dt.minute, dt.second))
    print("{}/{}/{}".format(dt.day, dt.month, dt.year))

    ```

    ```
    datetime.datetime(2016, 6, 18, 21, 29, 28, 607208)
    2016
    6
    18
    21
    29
    28
    607208
    21:29:28
    18/6/2016
    ```

Es posible crear un datetime manualmente pasando los parámetros (year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None). Sólo son obligatorios el año, el mes y el día.

!!! info "" 

    ```python
    from datetime import datetime

    dt = datetime(2000,1,1)
    print(dt)
    ```

    ```
    datetime.datetime(2000, 1, 1, 0, 0)
    ```

No se puede cambiar un atributo al vuelo:

!!! info "" 

    ```python
    dt.year = 3000
    ```

    ```
    ---------------------------------------------------------------------------
    AttributeError                            Traceback (most recent call last)
    <ipython-input-18-f655491f2afa> in <module>()
    ----> 1 dt.year = 3000

    AttributeError: attribute 'year' of 'datetime.date' objects is not writable
    ```

Hay que utilizar el método replace:

!!! info "" 

    ```python
    dt = dt.replace(year=3000)
    print(dt)
    ```

    ```
    datetime.datetime(3000, 1, 1, 0, 0)
    ```

## Formateos

Formato automático ISO (Organización Internacional de Normalización):

!!! info "" 

    ```python
    dt = datetime.now()
    print(dt.isoformat())
    ```

    ```
    2016-06-18T21:37:10.303386
    ```

Formateo munual (inglés por defecto):

!!! info "" 

    ```python
    dt.strftime("%A %d %B %Y %I:%M")
    ```

    ```
    Saturday 18 June 2016 09:37
    ```

!!! Info "Código de los campos"
    Disponibles en esta enlace: [https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior)

Por defecto salen los nombres en inglés, pero podemos cambiar el idioma de configuración de Python: 

!!! info "" 

    ```python
    import locale
    
    # Idioma "es-ES" (código para el español de España)
    locale.setlocale(locale.LC_ALL, 'es-ES') 

    print(dt.strftime("%A %d %B %Y %I:%M"))
    print(dt.strftime("%A %d de %B del %Y - %H:%M"))  # %I 12h - %H 24h
    ```

    ```
    sábado 18 junio 2016 09:37
    sábado 18 de junio del 2016 - 21:37
    ```

!!! Info "Código de los países disponibles"

    ```python
    import locale
    print(locale.locale_alias)
    ```

## Operaciones

Podemos sumar y restar tiempo con la función *timedelta()*:

!!! info "" 

    ```python
    from datetime import datetime, timedelta

    dt = datetime.now()
    print(dt.strftime("%A %d de %B del %Y - %H:%M"))

    # Generamos 14 días con 4 horas y 1000 segundos de tiempo
    t = timedelta(days=14, hours=4, seconds=1000)

    # Lo operamos con el datetime de la fecha y hora actual
    dentro_de_dos_semanas = dt + t
    print(dentro_de_dos_semanas.strftime("%A %d de %B del %Y - %H:%M"))
    hace_dos_semanas = dt - t
    print(hace_dos_semanas.strftime("%A %d de %B del %Y - %H:%M"))
    ```

    ```
    sábado 18 de junio del 2016 - 21:47
    domingo 03 de julio del 2016 - 02:03
    sábado 04 de junio del 2016 - 17:30
    ```

## Zonas horarias

Para establecer zonas horarias en nuestras fechas y horas necesitamos instalar el módulo pytz desde Anaconda Prompt:

    pip install pytz

Una vez instalado podemos consultar las diferentes zonas horarias disponibles con:

!!! info "" 
    ```python
    print(pytz.all_timezones)
    ```

Ahora por ejemplo para crear la hora actual en Tokyo (Japón) haríamos lo siguiente:

!!! info "" 
    ```python
    dt = datetime.now(pytz.timezone('Asia/Tokyo'))
    print(dt.strftime("%A %d de %B del %Y - %H:%M"))  # %I 12h - %H 24h
    ```

    ```
    domingo 19 de junio del 2016 - 04:52
    ```

___
<small class="edited"><i>Última edición: 2 de Octubre de 2018</i></small>