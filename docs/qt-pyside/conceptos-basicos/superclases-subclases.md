title: Superclases y subclases | Curso Qt/PySide | Hektor Profe

# Superclases y subclases

En la próxima lección vamos a transformar el código de nuestro programa a clases y objetos. Para hacerlo necesitaremos trabajar con la herencia de clases, así que repasemos un poco los conceptos básicos.

En Python, cuando una clase (llamada subclase) hereda de otra (llamada superclase) obtiene todo su comportamiento.

```python
class Madre:
    def __init__(self):
        print(f"Soy Madre")

class Hijo(Madre):
    pass


hijo = Hijo()
```

La subclase puede sobreescribe los métodos de la superclase para realizar sus propias acciones:

```python
class Madre:
    def __init__(self):
        print(f"Soy Madre")

class Hijo(Madre):
    def __init__(self):
        print(f"Soy Hijo")


hijo = Hijo()
```

Ahora bien, en algunas ocasiones quizá nos interesa no sobreescribir completamente, sino extender una funcionalidad de la superclase. Cuando necesitemos este comportamiento podemos hacer uso de la función `super()`, un accesor directo a la superclase:

```python
class Madre:
    def __init__(self):
        print(f"Soy Madre")

class Hijo(Madre):
    def __init__(self):
        super().__init__()
        print(f"Soy Hijo")


hijo = Hijo()
```

Queda claro entonces que también es posible extender el comportamiento de una superclase sin sobreescribirlo si hacemos uso del accesor `super()`.

¿Y qué pasa con la herencia múltiple? ¿Cómo se comportaría `super()` si heredamos de más de una superclase?

```python
class Madre:
    def __init__(self):
        print(f"Soy Madre")


class Padre:
    def __init__(self):
        print(f"Soy Padre")


class Hijo(Madre, Padre):
    def __init__(self):
        super().__init__()
        print(f"Soy Hijo")


hijo = Hijo()
```

Pues en este caso se sigue la lógica de la prioridad de herencia, teniendo más prioridad la clase de izquierda, y por lo tanto `super()` es el accesor de `Madre`.

Si quisiéramos extender el comportamiento del padre, en lugar de `super()` utilizaremos su propio nombre:

```python
class Hijo(Madre, Padre):
    def __init__(self):
        Padre.__init__(self)
        print(f"Soy Hijo")
```

Sin embargo aquí deberemos pasar `self` al método porque `super` lo hace implícitamente.

Para rizar el rizo nada nos impediría extender el funcionamiento tanto de la madre como del padre:

```python
class Hijo(Madre, Padre):
    def __init__(self):
        Madre.__init__(self)
        Padre.__init__(self)
        print(f"Soy Hijo")
```

Con esto queda repasado el concepto de herencia múltiple, necesario para extender los componentes de Pyside.



___
<small class="edited"><i>Última edición: 22 de Marzo de 2021</i></small>