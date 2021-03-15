title: Métodos de las cadenas | Curso de Python | Hektor Profe
description: Ahora que conocemos los objetos y tenemos una idea más clara de cómo funciona Python, es un buen momento para revisitar las colecciones y aprender algunos de sus métodos de clase.

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

# Métodos de las cadenas

## upper()

Devuelve la cadena con todos sus caracteres a mayúscula:

!!! info ""
    
    ```python
    "Hola Mundo".upper()
    ```

    ```
    'HOLA MUNDO'
    ```     

## lower()

Devuelve la cadena con todos sus caracteres a minúscula:

!!! info ""
    
    ```python
    "Hola Mundo".lower()
    ```

    ```
    'hola mundo'
    ```   

## capitalize()

Devuelve la cadena con su primer carácter en mayúscula:

!!! info ""
    
    ```python
    "hola mundo".capitalize()
    ```

    ```
    'Hola mundo'
    ```   

## title()

Devuelve la cadena con el primer carácter de cada palabra en mayúscula:

!!! info ""
    
    ```python
    "hola mundo".title()
    ```

    ```
    'Hola Mundo'
    ``` 

## count()

Devuelve una cuenta de las veces que aparece una subcadena en la cadena:

!!! info ""
    
    ```python
    "Hola mundo".count('mundo')
    ```

    ```
    1
    ``` 

## find()

Devuelve el índice en el que aparece la subcadena (-1 si no aparece):

!!! info ""
    
    ```python
    "Hola mundo".find('mundo')
    ```

    ```
    5
    ``` 

!!! info ""
    
    ```python
    "Hola mundo".find('mundoz')
    ```

    ```
    -1
    ``` 

## rfind()

Devuelve el índice en el que aparece la subcadena, empezando por el final:

!!! info ""
    
    ```python
    "Hola mundo mundo mundo".rfind('mundo')
    ```

    ```
    17
    ```

## isdigit()

Devuelve True si la cadena es todo números (False en caso contrario):

!!! info ""
    
    ```python
    c = "100"
    c.isdigit()
    ```

    ```
    True
    ```

## isalnum()

 Devuelve True si la cadena es todo números o carácteres alfabéticos:

!!! info ""
    
    ```python
    c = "ABC10034po"
    c.isalnum()
    ```

    ```
    True
    ```

## isalpha()

Devuelve True si la cadena es todo carácteres alfabéticos:

!!! info ""
    
    ```python
    c = "ABC10034po"
    c.isalpha()
    ```

    ```
    False
    ```

!!! info ""
    
    ```python
    "Holamundo".isalpha()
    ```

    ```
    True
    ```

## islower()

Devuelve True si la cadena es todo minúsculas:

!!! info ""
    
    ```python
    "Hola mundo".islower()
    ```

    ```
    False
    ```     

## isupper()

Devuelve True si la cadena es todo mayúsculas:

!!! info ""
    
    ```python
    "Hola mundo".isupper()
    ```

    ```
    False
    ``` 

## istitle()

Devuelve True si la primera letra de cada palabra es mayúscula:

!!! info ""
    
    ```python
    "Hola Mundo".istitle()
    ```

    ```
    True
    ``` 

## isspace()

Devuelve True si la cadena es todo espacios:

!!! info ""
    
    ```python
    "  -  ".isspace()
    ```

    ```
    False
    ``` 

## startswith()

Devuelve True si la cadena empieza con una subcadena:

!!! info ""
    
    ```python
    "Hola mundo".startswith("Mola")
    ```

    ```
    False
    ``` 

## endswith()

Devuelve True si la cadena acaba con una subcadena:

!!! info ""
    
    ```python
    "Hola mundo".endswith('mundo')
    ```

    ```
    True
    ``` 

## split()

Separa la cadena en subcadenas a partir de sus espacios y devuelve una lista:

!!! info ""
    
    ```python
    "Hola mundo mundo".split()[0]
    ```

    ```
     'Hola'
    ``` 
   
Podemos indicar el carácter a partir del que se separa:

!!! info ""
    
    ```python
    "Hola,mundo,mundo,otra,palabra".split(',')
    ```

    ```
    ['Hola', 'mundo', 'mundo', 'otra', 'palabra']
    ```     

## join()

Une todos los caracteres de una cadena utilizando un caracter de unión:

!!! info ""
    
    ```python
    ",".join("Hola mundo")
    ```

    ```
    'H,o,l,a, ,m,u,n,d,o'
    ``` 

!!! info ""
    
    ```python
    " ".join("Hola")
    ```

    ```
    'H o l a'
    ``` 

## strip()

Borra todos los espacios por delante y detrás de una cadena y la devuelve:

!!! info ""
    
    ```python
    "   Hola mundo     ".strip()
    ```

    ```
    'Hola mundo'
    ```     

Podemos indicar el carácter a borrar:

!!! info ""
    
    ```python
    "-----Hola mundo---".strip('-')
    ```

    ```
    'Hola mundo'
    ```     

## replace()

Reemplaza una subcadena de una cadena por otra y la devuelve:

!!! info ""
    
    ```python
    "Hola mundo".replace('o','0')
    ```

    ```
    'H0la mund0'
    ```     

Podemos indicar un límite de veces a reemplazar:

!!! info ""
    
    ```python
    "Hola mundo mundo mundo mundo mundo".replace(' mundo','',4)
    ```

    ```
    'Hola mundo'
    ``` 

___
<small class="edited"><i>Última edición: 1 de Octubre de 2018</i></small>