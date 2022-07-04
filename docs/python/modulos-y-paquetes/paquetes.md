title: Paquetes | Curso de Python | Hektor Profe
description: Los módulos son ficheros que contienen definiciones que se pueden importar en otros scripts para reutilizar sus funcionalidades.

# Paquetes

Utilizar paquetes nos ofrece varias ventajas. En primer lugar nos permite unificar distintos módulos bajo un mismo nombre de paquete, pudiendo crear jerarquías de módulos y submódulos, o también subpaquetes. 

Por otra parte nos permiten distribuir y manejar fácilmente nuestro código como si fueran librerías instalables de Python. De esta forma se pueden utilizar como módulos estándar desde el intérprete o scripts sin cargarlos previamente.

Para crear un paquete lo que tenemos que hacer es crear un fichero especial *init* **vacío** en el directorio donde tengamos todos los módulos que queremos agrupar. De esta forma cuando Python recorra este directorio será capaz de interpretar una jerarquía de módulos:

    paquete/
        __init__.py
        saludos.py
        script.py
        
Ahora, si utilizamos un script desde el mismo directorio donde se encuentra el paquete podemos acceder a los módulos, pero esta vez refiriéndonos al paquete y al módulo, así que debemos hacerlo con from import:

    from paquete.saludos import Saludo

    s = Saludo()

Esta jerarquía se puede expandir tanto como queramos creando subpaquetes, pero siempre añadiendo el fichero *init* en cada uno de ellos:

    script.py
    paquete/
        __init__.py
        hola/
            __init__.py
            saludos.py
        adios/
            __init__.py
            despedidas.py


`paquete/hola/saludos.py`
!!! info ""
    
    ```python
    def saludar():
        print("Hola, te estoy saludando desde la función saludar() " \
              "del módulo saludos")

    class Saludo():
        def __init__(self):
            print("Hola, te estoy saludando desde el __init__"  \
                  "de la clase Saludo")
    ```
    
`paquete/adios/despedidas.py`
!!! info ""
    ```python
    def despedir():
        print("Adiós, me estoy despidiendo desde la función despedir() " \
                "del módulo despedidas")

    class Despedida():
        def __init__(self):
            print("Adiós, me estoy despidiendo desde el __init__ " \
                    "de la clase Despedida")
    ```

Ahora de una forma bien sencilla podemos ejecutar las funciones y métodos de los módulos de cada subpaquete:

`script.py`
!!! info ""
    
    ```python
    from paquete.hola.saludos import saludar
    from paquete.adios.despedidas import Despedida

    saludar()
    Despedida()
    ```

Como véis los paquetes son muy útiles, pero si intentamos ejecutarlos desde un directorio distinto a donde se encuentran, pasa lo mismo que los módulos y no funcionan.

¿Como podemos solucionarlo? Bueno pues esta vez si podemos hacerlo de una forma elegante, instalando el paquete dentro de Python. Para hacerlo hay que convertir nuestro paquete en un distribuible. Más adelante dedicaré un tema a hablar sobre la distribución de código, pero por ahora os daré cuatro pinceladas.

## Distribución

Para crear un paquete distribuible tenemos que crear un fichero *setup.py* fuera de la raíz, indicando una información básica, de la siguiente forma:

    setup.py
    paquete/
        __init__.py
        hola/
            __init__.py
            saludos.py
        adios/
            __init__.py
            despedidas.py

`setup.py`
!!! info ""
    
    ```python
    from setuptools import setup
    setup(
        name="paquete",
        version="0.1",
        description="Este es un paquete de jemplo",
        author="Hector Costa",
        author_email="hola@hektorprofe.com",
        url="http://www.hektorprofe.net",
        packages=['paquete','paquete.hola','paquete.adios']
        scripts=[]
    )
    ```

Una vez hemos definido el distribuible con su información básica, incluyendo los paquetes y subpaquetes que lo forman, así como los posibles scripts, debemos crearlo. Para hacerlo utilizaremos el siguiente comando allí donde tenemos el *setup.py*:

	python setup.py sdist

Ahora, si todo ha funcionado correctamente, se habrá creado una nueva carpeta llamada dist, y en ella encontraremos un fichero zip en Windows o tar.gz si estamos en Linux. Este fichero es nuestro distribuible y ahora podríamos compartirlo con todo el mundo para que puedan instalar nuestro paquete.

Para instalar un paquete en Python, y finalmente hacer que éste se pueda utilizar desde cualquier lugar lo haremos de la siguiente forma, desde el directorio donde tenemos el paquete comprimido:

	pip install paquete-0.1.zip

Ahora, si utilizamos el comando pip3 list, podremos consultar todos los paquetes instalados en nuestro Python, y podremos ver también el nuestro. Si aparece correctamente podremos utilizar nuestro paquete desde cualquier script, pues se encuentra instalado dentro de Python. 

Finalmente utilizando el comando *pip uninstall* para desinstalarlo:

    pip uninstall paquete 

Bueno, esto solo era un ejemplo muy sencillo de como distribuir un paquete, pero como ya he dicho el tema daría para hablar muchísimo, así que me lo reservo para el final del curso. Por ahora espero que hayáis aprendido mucho sobre los módulos y los paquetes porque utilizarlos es la clave para conseguir una buena organización de código. 

___
<small class="edited"><i>Última edición: 2 de Octubre de 2018</i></small>