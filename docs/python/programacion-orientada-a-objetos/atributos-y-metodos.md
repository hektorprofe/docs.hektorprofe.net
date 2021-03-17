title: Atributos y métodos | Curso de Python | Hektor Profe
description: En esta unidad aprenderemos sobre un paradigma de programación distinto que cambió la forma de entender la programación.

# Atributos y métodos

Si hay algo que ilustre el potencial de la POO esa es la capacidad de definir variables y funciones dentro de las clases, aunque aquí se conocen como atributos y métodos respectivamente.

## Atributos

A efectos prácticos los atributos no son muy distintos de las variables, la diferencia fundamental es que sólo existen dentro del objeto.

### Atributos dinámicos


Dado que Python es muy flexible los atributos pueden manejarse de distintas formas, por ejemplo se pueden crear dinámicamente (al vuelo) en los objetos.

!!! info ""

    ```python 
    class Galleta:
        pass

    galleta = Galleta()
    galleta.sabor = "salado"
    galleta.color = "marrón"

    print(f"El sabor de esta galleta es {galleta.sabor} "
          f"y el color {galleta.color}")
    ```

    ``` 
    El sabor de esta galleta es Salado y el color Marrón
    ```

### Atributos de clase

Aunque la flexibilidad de los atributos dinámicos puede llegar a ser muy útil, tener que definir los atributos de esa forma es tedioso. Es más práctico definir unos atributos básicos en la clase. De esa manera todas las galletas podrían tener unos atributos por defecto:

!!! info ""

    ```python 
    class Galleta:
        chocolate = False

    galleta = Galleta()

    if galleta.chocolate:
        print("La galleta tiene chocolate")
    else:
        print("La galleta no tiene chocolate")
    ```

    ``` 
    La galleta no tiene chocolate
    ```

Luego podemos cambiar su valor en cualquier momento:

!!! info ""

    ```python
    galleta.chocolate = True

    if galleta.chocolate:
        print("La galleta tiene chocolate")
    else:
        print("La galleta no tiene chocolate")
    ```

    ``` 
    La galleta tiene chocolate
    ```

Por lo menos de esta forma nos aseguraremos de que el atributo chocolate existe en todas las galletas desde el principio. Además es posible consultar el valor por defecto que deben tener las galletas haciendo referencia al atributo en la definición de la clase:

!!! info ""

    ```python
    print(Galleta.chocolate)
    ```

    ```
    False
    ```

Lo curioso es que si cambiamos ese atributo de clase (que no de objeto) a *True*, las siguientes galletas se crearán con chocolate, es decir, habremos modificado las instrucciones de creación de los objetos:

!!! info ""

    ```python
    class Galleta:
        chocolate = False

    Galleta.chocolate = True
        
    galleta = Galleta()

    if galleta.chocolate:
        print("La galleta tiene chocolate")
    else:
        print("La galleta no tiene chocolate")
    ```

    ``` 
    La galleta tiene chocolate
    ```

Ya les gustaría a otros lenguajes ser tan flexibles. 😁😁😁

## Métodos

Si por un lado tenemos las "variables" de las clases, por otro tenemos sus "funciones", que evidentemente nos permiten definir funcionalidades para llamarlas desde las instancias.

Definir un método es bastante simple, sólo tenemos que añadirlo en la clase y luego llamarlo desde el objeto con los paréntesis, como si de una función se tratase:

!!! info ""

    ```python
    class Galleta:
        chocolate = False

        def saludar():
            print("Hola, soy una galleta muy sabrosa")
            
    galleta = Galleta()
    galleta.saludar()
    ```

    ``` 
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    <ipython-input-27-74df06911b9b> in <module>()
        6 
        7 galleta = Galleta()
    ----> 8 galleta.saludar()

    TypeError: saludar() takes 0 positional arguments but 1 was given
    ```

Sin embargo, al intentar ejecutar el código anterior desde una galleta veréis que no funciona. Nos indica que el método saludar() requiere 0 argumentos pero se está pasando uno.

¿Cómo puede ser? Si en ningún momento hemos enviado ninguna información a al galleta...

Lo que tenemos aquí, estimados alumnos, es la diferencia fundamental entre métodos de clase y métodos de instancia.

Probad a ejecutar el método llamando a la clase en lugar del objeto:

!!! info ""

    ```python
    class Galleta:
        chocolate = False

        def saludar():
            print("Hola, soy una galleta muy sabrosa")
            
    Galleta.saludar()
    ```

    ``` 
    Hola, soy una galleta muy sabrosa
    ```

¡Ahora sí ha funcionado! ¿Cómo es posible? Y más importante, ¿por qué al llamarlo desde el objeto dice que estamos enviando un argumento?

### Primer argumento self

Los objetos tienen una característica muy importante: son conscientes de que existen. Y no, no es broma.

Cuando se ejecuta un método desde un objeto (que no desde una clase), se envía un primer argumento implícito que hace referencia al propio objeto. Si lo definimos en nuestro método podremos capturarlo y ver qué es:

!!! info ""

    ```python
    class Galleta:
        chocolate = False

        def saludar(soy_el_propio_objeto):
            print("Hola, soy una galleta muy sabrosa")
            print(soy_el_propio_objeto)
            
    galleta = Galleta()
    galleta.saludar()
    ```

    ``` 
    Hola, soy una galleta muy sabrosa
    <__main__.Galleta object at 0x0000028E65476748> 
    ```

¿Curioso que haya funcionado verdad? Además ¿no os suena de algo ese resultado que muestra el parámetro que hemos definido? Se trata de la propia representación del objeto.

!!! info ""

    ```python
    class Galleta:
        chocolate = False

        def saludar(soy_el_propio_objeto):
            print("Hola, soy una galleta muy sabrosa")
            print(soy_el_propio_objeto)
            
    galleta = Galleta()
    galleta.saludar()
    print(galleta)
    ```

    ``` 
    Hola, soy una galleta muy sabrosa
    <__main__.Galleta object at 0x0000028E654769E8>
    <__main__.Galleta object at 0x0000028E654769E8>
    ```

Pues sí, podemos acceder al propio objeto desde el interior de sus métodos. Lo único que como este argumento hace referencia al objeto en sí mismo por convención se le llama **self**.

Poder acceder al propio objeto desde un método es muy útil, ya que nos permite acceder a sus atributos. Fijaros, el siguiente código no funcionaría como esperamos:

!!! info ""

    ```python
    class Galleta:
        chocolate = False

        def chocolatear(self):
            chocolate = True
            
    galleta = Galleta()
    galleta.chocolatear()
    print(galleta.chocolate)
    ```

    ``` 
    False
    ```

En cambio, si hacemos ver que *self* es el propio objeto...

!!! info ""

    ```python
    class Galleta:
        chocolate = False

        def chocolatear(self):
            self.chocolate = True
            
    galleta = Galleta()
    galleta.chocolatear()
    print(galleta.chocolate)
    ```

    ``` 
    True
    ```

¿No es interesante? Da la sensación como os decía antes de que las instancias tienen que saber quienes son porque sino no pueden acceder sus atributos internos y por eso tienen que enviarse asimismas a los métodos.

Sea como sea con este ejemplo podemos entender que por defecto el valor de un atributo se busca en la clase, pero para modificarlo en la instancia es necesario hacer referencia al objeto.

## Métodos especiales

Ahora que sabemos crear métodos y hemos aprendido para qué sirve el argumento **self**, es momento de introducir algunos métodos especiales de las clases.

Se llaman especiales porque la mayoría ya existen de forma oculta y sirven para tareas específicas. 

### Constructor

El constructor es un método que se llama automáticamente al crear un objeto, se define con el nombre *init*:

!!! info ""

    ```python
    class Galleta:

        def __init__(self):
            print("Soy una galleta acabada de hornear!")

    galleta = Galleta()
    ```

    ``` 
    Soy una galleta acabada de hornear!
    ```

La finalidad del constructor es, como su nombre indica, construir los objetos. Por esa razón permite sobreescribir el método que crea los objetos, permitiéndonos enviar datos desde el principio para construirlo:

!!! info ""

    ```python
    class Galleta:
        chocolate = False
        
        def __init__(self, sabor, color):
            self.sabor = sabor
            self.color = color
            print(f"Se acaba de crear una galleta {self.color} y {self.sabor}.")

    galleta_1 = Galleta("marrón", "amarga")
    galleta_2 = Galleta("blanca", "dulce")
    ```

    ``` 
    Se acaba de crear una galleta marrón y amarga.
    Se acaba de crear una galleta blanca y dulce.
    ```

Como los métodos se comportan como funciones tienen sus mismas características, permitiéndonos definir valores nulos, valores por posición y nombre, argumentos indeterminadas, etc.

### Destructor

Si existe un constructor también debe existir un destructor que se llame al eliminar el objeto para que encargue de las tareas de limpieza como vaciar la memoria. Ese es el papel del método especial *del*. Es muy raro sobreescribir este método porque se maneja automáticamente, pero es interesante saber que existe.

Todos los objetos se borran automáticamente de la memoria al finalizar el programa, aunque también podemos eliminarlos automáticamente pasándolos a la función *del()*:

!!! info ""

    ```python
    class Galleta:

        def __del__(self):
            print("La galleta se está borrando de la memoria")

    galleta = Galleta()

    del(galleta)
    ```

    ``` 
    La galleta se está borrando de la memoria
    ```

En este punto vale comentar algo respecto a los métodos especiales como éste, y es que pese a que tienen accesores en forma de función para facilitar su llamada, es totalmente posible ejecutarlos directamente como si fueran métodos normales:

!!! info ""

    ```python
    class Galleta:

        def __del__(self):
            print("La galleta se está borrando de la memoria")

    galleta = Galleta()

    galleta.__del__()
    ```

    ``` 
    La galleta se está borrando de la memoria
    ```

Si tenéis memoria seguro que ahora mismo os estáis acordando de funciones como *str()* y *len()*, y es que en efecto, esas también son accesores de los métodos especiales *str* y *len* que tienen los objetos.

### String

El método *str* es el que devuelve la representación de un objeto en forma de cadena. Un momento en que se llama automáticamente es cuando imprimirmos una variable por pantalla.

Por defecto los objetos imprimen su clase y una dirección de memoria, pero eso puede cambiarse sobreescribiendo el comportamiento:

!!! info ""

    ```python
    class Galleta:

        def __init__(self, sabor, color):
            self.sabor = sabor
            self.color = color

        def __str__(self):
           return f"Soy una galleta {self.color} y {self.sabor}."

    galleta = Galleta("dulce", "blanca")

    print(galleta)
    print(str(galleta))
    print(galleta.__str__())
    ```

    ``` 
    Soy una galleta blanca y dulce.
    Soy una galleta blanca y dulce.
    Soy una galleta blanca y dulce.
    ```

Hay que tener en cuenta que este método debe devolver la cadena en lugar de mostrar algo por pantalla, ese es el funcionamiento que se espera de él.

### Length

Finalmente otro método especial interesante es el que devuelve la longitud. Normalmente está ligado a colecciones, pero nada impide definirlo en una clase. Y sí, digo definirlo y no redefinirlo porque por defecto no existe en los objetos aunque sea el que se ejecuta al pasarlos a la función *len()*.

!!! info ""

    ```python
    class Cancion:

        def __init__(self, autor, titulo, duracion):  # en segundos
            self.duracion = duracion

        def __len__(self):
           return self.duracion

    cancion = Cancion("Queen", "Don't Stop Me Now", 210)

    print(len(cancion))
    print(cancion.__len__())
    ```

    ``` 
    210
    210
    ```

Mientras devolvamos un número, este método no debería dar problemas.

___
<small class="edited"><i>Última edición: 27 de Septiembre de 2018</i></small>