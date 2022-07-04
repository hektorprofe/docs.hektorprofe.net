title: Ejercicios « Manejo de ficheros | Curso de Python | Hektor Profe
description: Tradicionalmente existen dos tipos de persistencia básica: con ficheros o con bases de datos y en esta unidad vamos a centrarnos en la primera.

# Ejercicios « Manejo de ficheros

## Ejercicio 1

En este ejercicio deberás crear un script llamado **personas.py** que lea los datos de un fichero de texto, que transforme cada fila en un diccionario y lo añada a una lista llamada personas. Luego rocorre las personas de la lista y paracada una muestra de forma amigable todos sus campos.

El fichero de texto se denominará **personas.txt** y tendrá el siguiente contenido en texto plano (créalo previamente):

```
1;Carlos;Pérez;05/01/1989
2;Manuel;Heredia;26/12/1973
3;Rosa;Campos;12/06/1961
4;David;García;25/07/2006
```

Los campos del diccionario serán por orden: **id**, **nombre**, **apellido** y **nacimiento**.

!!! warning "Importante"
    Si quieres leer un fichero que no se ha escrito directamente con Python, entonces es posible que encuentres errores de codificación al mostrar algunos caracteres. Asegúrate de indicar la codificación del fichero manualmente durante la apertura como argumento en el **open**, por ejemplo con UTF-8:

    ```python
    open(..., encoding="utf8")
    ```

## Ejercicio 2

En este ejercicio deberás crear un script llamado **contador.py** que realice varias tareas sobre un fichero llamado **contador.txt** que almacenará un contador de visitas (será un número):

* Nuestro script trabajará sobre el fichero **contador.txt**. Si el fichero no existe o está vacío lo crearemos con el número 0. Si existe simplemente leeremos el valor del contador.
* Luego a partir de un argumento:
    * Si se envía el argumento **inc**, se incrementará el contador en uno y se mostrará por pantalla.
    * Si se envía el argumento **dec**, se decrementará el contador en uno y se mostrará por pantalla.
    * Si no se envía ningún argumento (o algo que no sea inc o dec), se mostrará el valor del contador por pantalla.
* Finalmente guardará de nuevo el valor del contador de nuevo en el fichero.
* Utiliza excepciones si crees que es necesario, puedes mostrar el mensaje: **Error: Fichero corrupto.**

## Ejercicio 3

Utilizando como base el ejercicio de los personajes que hicimos, en este ejercicio tendrás que crear un gestor de personajes **gestor.py** para añadir y borrar la información de los siguientes personajes:

|           | Vida | Ataque | Defensa | Alcance |
|-----------|------|--------|---------|---------|
| Caballero | 4    | 2      | 4       | 2       |
| Guerrero  | 2    | 4      | 2       | 4       |
| Arquero   | 2    | 4      | 1       | 8       |

**Deberás hacer uso del módulo pickle y todos los cambios que realices se irán guardando en un fichero binario personajes.pckl, por lo que aunque cerremos el programa los datos persistirán.**

* Crea dos clases, una **Personaje** y otra **Gestor**.
* La clase **Personaje** deberá permitir crear un personaje con el nombre (que será la clase), y sus propiedades de vida, ataque, defensa y alcance (que deben ser números enteros mayor que cero obligatoriamente).
* Por otro lado la clase **Gestor** deberá incorporar todos los métodos necesarios para **añadir personajes, mostrarlos y borrarlos** (a partir de su nombre por ejemplo, tendrás que pensar una forma de hacerlo), además de los métodos esenciales para guardar los cambios en el fichero personajes.pckl que se deberían ejecutar automáticamente. 
* En caso de que el personaje ya exista en el Gestor entonces no se creará.

**Una vez lo tengas listo realiza las siguientes prueba en tu código:**

* Crea los tres personajes de la tabla anterior y añádelos al Gestor.
* Muestra los personajes del Gestor.
* Borra al Arquero.
* Muestra de nuevo el Gestor.

!!! tip "Sugerencia"
    El ejemplo con pickle que realizamos anteriormente puede servirte como base.

## Soluciones

Disponibles solo para los alumnos <u>[matriculados en el curso](https://www.hektorprofe.net/cupon/python)</u>.

___
<small class="edited"><i>Última edición: 3 de Octubre de 2018</i></small>