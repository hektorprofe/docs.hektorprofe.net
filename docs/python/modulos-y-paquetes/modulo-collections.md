title: Módulo collections | Curso de Python | Hektor Profe
description: Los módulos son ficheros que contienen definiciones que se pueden importar en otros scripts para reutilizar sus funcionalidades.

# Módulo collections

El módulo integrado de colecciones nos proveé otros tipos o mejoras de las colecciones clásicas.    

## Contadores

La clase **Counter** es una subclase de diccionario utilizada para realizar cuentas:

!!! info "" 

    ```python
    from collections import Counter

    l = [1,2,3,4,1,2,3,1,2,1]
    Counter(l)
    ```

    ```
    Counter({1: 4, 2: 3, 3: 2, 4: 1})
    ```

!!! info "" 

    ```python
    Counter("palabra")
    ```

    ```
    Counter({'a': 3, 'b': 1, 'l': 1, 'p': 1, 'r': 1})
    ```

!!! info "" 

    ```python
    animales = "gato perro canario perro canario perro"
    c = Counter(animales.split())
    priunt(c)
    ```

    ```
    Counter({'canario': 2, 'gato': 1, 'perro': 3})
    ```

Algunas formas de utilizar un contador, sus métodos y conversiones:

!!! info "" 

    ```python
    animales = "gato perro canario perro canario perro"
    c = Counter(animales.split())

    print(c.most_common(1))  # Primeros elemento más repetido
    print(c.most_common(2))  # Primeros dos elementos más repetidos
    print(c.most_common())   # Elementos ordenadores por repeticiones
    ```

    ```
    [('perro', 3)]
    [('perro', 3), ('canario', 2)]
    [('perro', 3), ('canario', 2), ('gato', 1)]
    ```

!!! info "" 

    ```python
    l = [10,20,30,40,10,20,30,10,20,10]
    c = Counter(l)

    print(c.items())        # Registros del contador por clave-valor
    print(c.keys())         # Registros del contador por clave
    print(c.values())       # Registros del contador por valor

    print(sum(c.values()))  # Suma total de elementos del contador

    print(list(c))          # Conversión a lista
    print(dict(c))          # Conversión a conjunto
    print(set(c))           # Conversión a conjunto
    ```

    ```
    dict_items([(40, 1), (10, 4), (20, 3), (30, 2)])
    dict_keys([40, 10, 20, 30])
    dict_values([1, 4, 3, 2])

    10

    [40, 10, 20, 30]
    {10: 4, 20: 3, 30: 2, 40: 1}
    {10, 20, 30, 40}
    ```

## Diccionarios por defecto

La clase **defaultdict** se utilizan para crear diccionarios con un valor por defecto aunque el registro no haya sido definido anteriormente. Para ello hay que indicar un tipo de dato por defecto al diccionario:

!!! info "" 

    ```python
    from collections import defaultdict

    d = defaultdict(float)  # tipo flotante por defecto
    print(d['algo'])
    print(d)
    ```

    ```
    0.0
    defaultdict(float, {'algo': 0.0})
    ```

!!! info "" 

    ```python
    d = defaultdict(str)  # tipo cadena por defecto
    print(d['algo'])
    print(d)
    ```

    ```
    ''
    defaultdict(str, {'algo': ''})
    ```

!!! info "" 

    ```python
    d = defaultdict(object)  # tipo objeto por defecto
    print(d['algo'])
    print(d)
    ```

    ```
    <object at 0x1ad7f3201f0>
    defaultdict(object, {'algo': <object at 0x1ad7f3201f0>})
    ```

## Diccionarios ordenados

La clase **OrderedDict** es otra subclase de diccionario, pero esta vez con la capacidad de conservar el orden en que añadimos los registros:

!!! info "" 

    ```python
    from collections import OrderedDict

    n = OrderedDict()
    n['uno'] = 'one'
    n['dos'] = 'two'
    n['tres'] = 'three'

    print(n)
    ```

    ```
    OrderedDict([('uno', 'one'), ('dos', 'two'), ('tres', 'three')])
    ```

El siguiente experimento permite comprobar como los diccionarios normales cambian el orden automáticamente.

Dos diccionarios normales con los mismos elementos en orden distinto:

!!! info "" 

    ```python
    n1 = {}
    n1['uno'] = 'one'
    n1['dos'] = 'two'

    n2 = {}
    n2['dos'] = 'two'
    n2['uno'] = 'one'

    # ¿Tienen los mismos elementos y en el mismo orden?
    print(n1 == n2)
    ```

    ```
    True
    ```

Dos diccionarios ordenados con los mismos elementos en orden distinto:

!!! info "" 

    ```python
    n1 = OrderedDict()
    n1['uno'] = 'one'
    n1['dos'] = 'two'

    n2 = OrderedDict()
    n2['dos'] = 'two'
    n2['uno'] = 'one'

    # ¿Tienen los mismos elementos y en el mismo orden?
    print(n1 == n2)
    ```

    ```
    False
    ```

## Tuplas con nombre

La subclase **namedtuple** es utilizada para crear pequeñas estructuras inmutables, parecidas a una clase y sus objetos, pero mucho más simples:

!!! info "" 

    ```python
    from collections import namedtuple

    Persona = namedtuple('Persona','nombre apellido edad')
    p = Persona(nombre="Hector",apellido="Costa",edad=27)

    print(p)

    # Podemos acceder a los elementos como si fueran atributos de un objeto
    print(p.nombre)
    print(p.edad)

    # O utilizando índices como con las tuplas clásicas
    print(p[0])
    print(p[-1])
    ```

    ```
    Persona(nombre='Hector', apellido='Costa', edad=27)

    'Hector'
    27

    'Hector'
    27
    ```

___
<small class="edited"><i>Última edición: 2 de Octubre de 2018</i></small>