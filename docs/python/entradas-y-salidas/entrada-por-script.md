title: Entrada por script | Curso de Python | Hektor Profe
description: En esta sección aprenderemos sobre las distintas formas de leer y visualizar información.

# Entrada por script

Hasta ahora todo lo que hemos hecho ha sido escribir código en el intérprete, pero los programas informáticos no funcionan así. Se basan en escribir todas las instrucciones en ficheros llamados scripts (o guiones de instrucciones). Luego se envía este fichero al intérprete desde la terminal (si es un lenguaje interpretado como Python) y éste ejecutará todas las instrucciones en bloque.

A parte de ser la base de los programas, la gracia de los Scripts es que pueden recibir datos desde la propia terminal en el momento de la ejecución, algo muy útil para añadirles dinamismo.

Para poder crear y ejecutar scripts hace falta un editor y una terminal, por suerte Anaconda trae el editor *Spyder* y el intérprete es accesible a través de la terminal *Anaconda Prompt*, ambos programas accesibles desde Inicio (o con  Anaconda Navigator si utilizáis Linux/MAC).

## Script de prueba

Utilizando Spyder deberíais ser capaces de crear un fichero *hola.py* con este contenido:
    
!!! info "" 

    ```python
    print("Hola, bienvenido a tu primer script")
    ```

Lo podéis guardar en el directorio que queráis, yo lo guardaré en una carpeta del disco, en *C:\Scripts* para tenerlo a mano.

A continuación para ejecutarlo abríramos *Anaconda Prompt* y navegaríamos con el comando *cd* (change directory) al directorio donde tenemos los scripts:

!!! info "" 

    ```bash
    cd C:\Scripts
    ```

Por último ejecutaremos el script pasándolo al intérprete de *python* y veremos el resultado del *print()* en la terminal:

!!! info "" 

    ```bash
    python hola.py
    ```

    ``` 
    Hola, bienvenido a tu primer script
    ```

## Scripts con argumentos

Para poder enviar información a un script y manejarla, tenemos que utilizar la librería de sistema *sys*. En ella encontraremos la lista *argv* que almacena los argumentos enviados al script. Cread el siguiente script y ejecutadlo:

!!! info "" 

    ```python
    import sys
    print(sys.argv)
    ```

    ```bash
    python argumentos.py
    ```

    ``` 
    ['argumentos.py']
    ```

Al ejecutarlo veréis que devuelve una lista con una cadena que contiene el nombre del script. Quedaros con la idea pues, de que el primer argumento de la lista *sys.argv* (sys.argv[0]) es el propio nombre del script.

Ahora intentad ejecutarlo de nuevo pasando algunos valores como números y cadenas de texto entre comillas dobles, todo separado por espacios:

!!! info "" 

    ```bash
    python argumentos.py 100 "Hola" 3.14
    ```

    ``` 
    ['argumentos.py', '100', 'Hola', '3.14']
    ```

Cada valor que enviamos al script durante la llamada se llama argumento e implica una forma de entrada de datos alternativa sin usar el **input()**.

El siguiente ejemplo es un script que recibe dos argumentos: un texto y un número entero. Lo que hace es imprimir la cadena de texto tantas veces como le indiquemos en el número. Tomaos el tiempo necesario para analizar y entender cada línea:

!!! info "" 

    ```python
    import sys

    # Comprobación de seguridad, ejecutar sólo si se reciben 2 argumentos reales
    if len(sys.argv) == 3:
        texto = sys.argv[1]
        repeticiones = int(sys.argv[2])
        for r in range(repeticiones):
            print(texto)
    else:
        print("Error - Introduce los argumentos correctamente")
        print('Ejemplo: escribir_lineas.py "Texto" 5')
    ```

    ```bash
    python escribir_lineas.py "Hola Mundo!!!" 5
    ```

    ``` 
    Hola Mundo!!!
    Hola Mundo!!!
    Hola Mundo!!!
    Hola Mundo!!!
    Hola Mundo!!!
    ```


___
<small class="edited"><i>Última edición: 25 de Septiembre de 2018</i></small>