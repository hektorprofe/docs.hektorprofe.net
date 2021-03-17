title: Definición y llamada | Curso de Python | Hektor Profe
description: Las funciones son fragmentos de código que se pueden ejecutar múltiples veces, pueden recibir y devolver información para comunicarse con el proceso principal.

# Definición y llamada

Se definen con la palabra reservada *def*, el nombre de la función y unos paréntesis, que también se utilizan para hacer la llamada:

!!! info "" 
    
    ```python
    def saludar():
        print("Hola! Este print se llama desde la función saludar()")

    saludar()
    ```

    ```
    Hola! Este print se llama desde la función saludar()
    ```

Dentro de una función podemos utilizar variables y sentencias de control:

!!! info "" 
    
    ```python
    def dibujar_tabla_del_5():
        for i in range(10):
            print("5 * {} = {}".format(i,i*5))

    dibujar_tabla_del_5()
    ```

    ```
    5 * 0 = 0
    5 * 1 = 5
    5 * 2 = 10
    5 * 3 = 15
    5 * 4 = 20
    5 * 5 = 25
    5 * 6 = 30
    5 * 7 = 35
    5 * 8 = 40
    5 * 9 = 45
    ```

## Ámbito de las variables

Una variable declarada en una función no existe en la función principal:

!!! info "" 
    
    ```python
    def test():
        n = 10
        
    test()
    print(n)
    ```

    ```
    ---------------------------------------------------------------------------
    NameError                                 Traceback (most recent call last)
    <ipython-input-4-667d7c7a2c02> in <module>()
    ----> 1 print(n)

    NameError: name 'n' is not defined
    ```
    
Sin embargo, una variable declarada fuera de la función (al mismo nivel), sí que es accesible desde la función:

!!! info "" 

    ```python
    m = 10

    def test():
        print(m)

    test()
    ```

    ```
    10
    ```

Siempre que declaremos la variable antes de la ejecución, podemos acceder a ella desde dentro:

!!! info "" 

    ```python
    def test():
        print(l)
        
    l = 10
    test()
    ```

    ```
    10
    ```

En el caso que declaremos de nuevo una variable en la función, se creará un copia de la misma que sólo funcionará dentro de la función. 

**Por tanto no podemos modificar una variable externa dentro de una función**:

!!! info "" 

    ```python
    def test():
        o = 5  # variable que sólo existe dentro de la función
        print(o)
        
    o = 10  # variable externa, no modificable
    test()
    print(o)
    ```

    ```
    5
    10
    ```

## La instrucción global

Para poder modificar una variable externa en la función, debemos indicar que es global de la siguiente forma:

!!! info "" 

    ```python
    def test():
        global o  # variable que hace referencia a la o externa
        o = 5
        print(o)

    o = 10
    test()
    print(o)
    ```

    ```
    5
    5
    ```

___
<small class="edited"><i>Última edición: 25 de Septiembre de 2018</i></small>