title: Polimorfismo de clases | Apuntes lenguaje C++ | Hektor Profe
description: Polimorfismo de clases | Apuntes lenguaje C++

# Polimorfismo de clases en C++

El **polimorfismo** es la capacidad de manejar distintas clases heredadas de una clase base de la misma forma. Este ejemplo simplificado muestra un posible resultado a implementar polimorfismo:

```cpp
// Tenemos tres punteros con formas heredadas de Shape
Shape *shape1 = new Circle;
Shape *shape2 = new Rectangle;
Shape *shape3 = new Oval;
 
// Una función que toma una Shape de cualquier tipo derivado
void draw_shape(Shape* shape_ptr)
{
    shape_ptr->draw();
}
```

La función `draw_shape` utiliza el polimorfismo de clases para llamar al método `draw()` que tiene cualquier `Shape`, independientemente que su implementación sea distinta en cada caso. Gracias a los punteros y la gestión por referencia esto es posible.

## Enlace dinámico con funciones virtuales

Una **función virtual** es una función miembro que se declara dentro de una clase base y es redefinida (anulada) por una clase derivada. Cuando se hace referencia a un objeto de clase derivada mediante un puntero o una referencia a la clase base, se puede llamar a una función virtual para ese objeto y ejecutar la versión de la función de la clase derivada:

* Las funciones virtuales garantizan que se llame a la función correcta para un objeto, independientemente del tipo de referencia (o puntero) utilizado para la llamada a la función.
* Se utilizan principalmente para lograr **el polimorfismo en tiempo de ejecución**.
* Las funciones se declaran con una palabra clave `virtual` en la clase base.
* La resolución de la llamada a la función se realiza en tiempo de ejecución.

**Reglas para funciones virtuales**

1. Las funciones virtuales no pueden ser estáticas.
Una función virtual puede ser una función amiga de otra clase.
2. Se debe acceder a las funciones virtuales utilizando el puntero o la referencia del tipo de clase base para lograr el polimorfismo en tiempo de ejecución.
3. El prototipo de funciones virtuales debe ser el mismo en la base, así como en la clase derivada.
4. Siempre se definen en la clase base y se anulan en una clase derivada. No es obligatorio que la clase derivada anule (o redefina la función virtual), en ese caso se utiliza la versión de la base.
5. Una clase puede tener un destructor virtual, pero no puede tener un constructor virtual. Para construir un objeto, un constructor necesita el tipo exacto del objeto que a crea y no se puede tener un puntero a un constructor (el objeto aún no existe).

```cpp
#include <iostream>
 
class Shape
{
public:
    Shape() = default;
    Shape(std::string description) 
        : description(description){};
 
    // Función virtual a implementar en clase derivada
    virtual void draw() const
    {
        std::cout << "Dibujando " << description << "\n";
    }
 
protected:
    std::string description{""};
};
 
class Circle : public Shape
{
public:
    Circle() = default;
    Circle(std::string description, double radius)
        : Shape(description), radius(radius){};
 
    // Implementación de la función virtual
    virtual void draw() const
    {
        std::cout << "Dibujando " << description
                  << " con radio " << radius << "\n";
    }
 
protected:
    double radius{};
};

main()
{
    Shape shape("Forma");
    Circle circulo("Circulo", 4.5);
 
    shape.draw();   // Dibujando Forma
    circulo.draw(); // Dibujando Circulo con radio 4.5
 
    return 0;
}
```

Ahora que tenemos un método virtual en la clase derivada podemos crear una función que simplemente reciba un puntero o referencia de una instancia de `Shape` o sus clases derivadas y ejecutar su método `draw()` sin preocuparnos por su tipo:


```cpp
// Funciones que llaman a una base o sus derivadas
void draw_shape_puntero(Shape *s)
{
    s->draw();
}
 
void draw_shape_referencia(Shape &s)
{
    s.draw();
}

main()
{
    Shape shape("Forma");
    Circle circulo("Circulo", 4.5);
 
    draw_shape_puntero(&shape);
    draw_shape_referencia(shape);
    draw_shape_puntero(&circulo);
    draw_shape_referencia(circulo); 
 
    return 0;
}
```

```
Dibujando Forma
Dibujando Forma
Dibujando Circulo con radio 4.5
Dibujando Circulo con radio 4.5
``` 

## Objetos polimórficos en arreglos

Es posible manejar secuencialmente objetos de una clase base y sus derivadas. La forma simple pero que más espacio cuesta en la memoria es mediante la copia de los objetos o a partir de las referencias.

Vamos a suponer una nueva clase derivada `Square` (cuadrado) para tener algo más con lo que jugar:

```cpp
#include <iostream>

class Square : public Shape
{
public:
    Square() = default;
    Square(std::string description, double side)
        : Shape(description), side(side){};
 
    // Implementación de la función virtual
    virtual void draw() const
    {
        std::cout << "Dibujando " << description
                  << " con costado " << side << std::endl;
    }
 
protected:
    double side{};
};

main()
{
    // Array con diferentes formas
    Shape shapes[]{
        Shape("Forma"), 
        Circle("Circulo", 4.5), 
        Square("Cuadrado", 3)};
 
    // for (Shape s : shapes)
    for (Shape &s : shapes)
    {
        s.draw();
        // (&s)->draw(); 
    }
 
    return 0;
}
```

```
Dibujando Forma
Dibujando Circulo
Dibujando Cuadrado
```

Como podemos observar esta forma no nos funciona del todo bien. Eso es debido a que el tipo `Shape` del `for` establece la función llamada, esa es la razón por la que al llamar a `draw()` se ejecuta la forma de la clase base `Shape`.

Para lograr que las funciones se ejecuten desde las clases derivadas una forma de hacerlo sería con **punteros inteligentes**. Estos punteros saben la clase del dato almacenado y nos permitirán en conjunto al tipo `auto` llamar al `draw()` específico de las clases derivadas:

```cpp
#include <memory>
 
main()
{
    // Arreglo de punteros inteligentes
    std::shared_ptr<Shape> shapes[]{
        std::make_shared<Shape>("Forma"),
        std::make_shared<Circle>("Circulo", 4.5),
        std::make_shared<Square>("Cuadrado", 3)};
 
    // Con smart pointers detectamos el tipo automáticamente
    for (auto &s : shapes)
    {
        s->draw();
    }
 
    return 0;
}
```

```
Dibujando Forma
Dibujando Circulo con radio 4.5
Dibujando Cuadrado con costado 3
```

Trataré el tema de los punteros inteligentes en profundidad próximamente.

## Especificador override en funciones virtuales

Puede ser que mientras estamos definiendo los métodos de la clase base en las derivadas tengamos un despiste y en lugar de referirnos a un método por su nombre lo llamemos distinto, por ejemplo en lugar de `draw` pongamos por error `draW`. Esto generará un método nuevo que no substituirá al original.

Para evitar esta situación, podemos establecer el especificador `override` como una buena práctica en todos los métodos de las derivadas que estén implementados sobre un método `virtual`, de esa manera el propio editor o compilador nos avisará de que tengamos cuidado, pues ese método no se encuentra en la clase base:

![]({{cdn}}/cpp/image-60.png)

!!! warning "Cuidado al sobrescribir funciones virtuales sobrecargadas"

    Debemos tener cuidado con esta cláusula cuando utilizamos sobrecarga de las funciones (más de una implementación) porque en ese caso, **si sobrescribimos una sobrecarga de la función virtual en una clase base todas las demás serán ocultadas** y no tendrás otra opción que sobrescribirlas explícitamente para que estén disponibles en las demás clases descendientes.

## Miembros estáticos en clases polimórficas

Recordemos que un miembro estático era un miembro especial a nivel de clase y no de instancia, común para todas las instancias de la clase. ¿Cómo se comportan estos miembros en clases heredades polimórficas? Hagamos un experimento partiendo de una nueva clase `Rect` que hereda de `Square`:

```cpp
class Rect : public Square
{
public:
    Rect() = default;
    Rect(std::string description, double side, double height)
        : Square(description, side), height(height){};
 
    // Implementación de la función virtual
    virtual void draw() const override
    {
        std::cout << "Dibujando " << description
                  << " con ancho " << side
                  << " y alto " << height << std::endl;
    }
 
protected:
    double height{};
};
```

Ahora vamos a añadir un miembro estático llamado contador para llevar un conteo del número de instancias tanto en `Base`, como `Square` y `Rect` que incrementaremos en sus respectivos consuctores:

```cpp
static int contador;
 
// Constructor forma
Shape(std::string description)
    : description(description)
{
    contador++;
};
 
// Constructor cuadrado
Square(std::string description, double side)
    : Shape(description), side(side)
{
    contador++;
};
 
// Constructor rectángulo
Rect(std::string description, double side, double height)
    : Square(description, side), height(height)
{
    contador++;
};
```

Inicializaremos los contadores de las tres clases antes de la función `main` y consultaremos sus valores después de crear unas cuantas instancias:

```cpp
#include <iostream>
#include <memory>
 
int Shape::contador{0};
int Square::contador{0};
int Rect::contador{0};
 
main()
{
    // Arreglo de punteros inteligentes
    std::shared_ptr<Shape> shapes[]{
        std::make_shared<Shape>("Forma 1"),
        std::make_shared<Shape>("Forma 2"),
        std::make_shared<Shape>("Forma 3"),
        std::make_shared<Square>("Cuadrado 1", 3),
        std::make_shared<Square>("Cuadrado 2", 5),
        std::make_shared<Rect>("Rectangulo 1", 5, 8),
        std::make_shared<Rect>("Rectangulo 2", 2, 3),
        std::make_shared<Rect>("Rectangulo 3", 1, 4)};
 
    // Consultamos los contadores
    std::cout << "N formas: " << Shape::contador << std::endl;
    std::cout << "N cuadrados: " << Square::contador << std::endl;
    std::cout << "N rectangulos: " << Rect::contador << std::endl;
 
    return 0;
}
```

```
N formas: 8
N cuadrados: 5
N rectangulos: 3
```

Lo que podemos observar es que:

* El contador de la clase base `Shape` se incrementa al crear una instancia de su clase y también de cualquiera de sus clases derivadas. Un total de 8 para 3 formas, 2 cuadrados y 3 rectángulos.
* El contador de la clase derivada `Square` se incrementa al crear una instancia de su clase y también de cualquiera de sus clases derivadas. Un total de 5 para 2 cuadrados y 3 rectángulos.
* El contador de la clase derivada `Rect` se incrementa al crear una instancia de su clase para un total de 3 rectángulos.

En conclusión los miembros estáticos en el polimorfismo son comunes en las clases base.

## Especificador final en la herencia

Si en algún momento queremos impedir que una clase derivada pueda sobrescribir un método de su clase base podemos utilizar el especificador `final` para evitarlo, el editor o compilador nos avisará de que no es posible hacerlo:

```cpp
class Square : public Shape
{
public:
    virtual void draw() const override final {} // Final
};
 
class Rect : public Square
{
public:
    virtual void draw() const override {} // Error
};
```

Esta cláusula también se puede aplicar a la propia clase para impedir que pueda tener clases derivadas:

```cpp
class Square final : public Shape {}; // Final
class Rect : public Square {}; // Error
```

## Especificadores de acceso en clases polimórficas

Supongamos que tenemos una clase base `A` con dos métodos, uno público y uno privado. Y una clase derivada de `A` llamada `B` en cuyos métodos heredados cambiamos los especificadores de acceso, siendo el que era público privado, y el privado público:

```cpp
#include <iostream>
 
class A
{
public:
    virtual void foo()
    {
        std::cout << "foo() de A() llamada" << std::endl;
    }
 
private:
    virtual void bar()
    {
        std::cout << "bar() de A() llamada" << std::endl;
    }
};
 
class B : public A
{
public:
    virtual void bar()
    {
        std::cout << "bar() de B() llamada" << std::endl;
    }
 
private:
    virtual void foo()
    {
        std::cout << "foo() de B() llamada" << std::endl;
    }
};
```

En este contexto, a partir de un puntero de clase base, podemos llamar a un **método virtual polimórfico privado** en la clase derivada, pero no a uno que sea público en la clase derivada y privado en la base:

```cpp
std::shared_ptr<A> a = std::make_shared<B>();
a->foo(); // foo() de B() llamada
a->bar(); // Error, bar() es privada
```

Por contra, un puntero de la clase derivada tendrá solo acceso a los miembros virtuales públicos, como es de esperar:

```cpp
std::shared_ptr<B> b = std::make_shared<B>();
b->bar(); // bar() de B() llamada
b->foo(); // Error, bar() es privada
```

## Especificadores de acceso en clases no polimórficas

En cuanto al funcionamiento anterior pero en clases no polimórficas (no virtuales) obtendremos el resultado esperado para cada tipo del puntero:

```cpp
#include <iostream>
 
class A
{
public:
    void foo()
    {
        std::cout << "foo() de A() llamada" << std::endl;
    }
 
private:
    void bar()
    {
        std::cout << "bar() de A() llamada" << std::endl;
    }
};
 
class B : public A
{
public:
    void bar()
    {
        std::cout << "bar() de B() llamada" << std::endl;
    }
 
private:
    void foo()
    {
        std::cout << "foo() de B() llamada" << std::endl;
    }
};
```

A partir de un puntero de clase base no podemos llamar a un **método privado** en la instancia de la clase derivada, pero sí a uno que sea público en la clase derivada y privado en la base:

```cpp
std::shared_ptr<A> a = std::make_shared<B>();
a->bar(); // Error, bar() es privada
a->foo(); // foo() de A() llamada
```

En un puntero de `B` a una instancia de `B`, tendremos acceso a los métodos públicos de la clase `B`, como es lógico:

```cpp
std::shared_ptr<B> b = std::make_shared<B>();
b->bar(); // bar() de B() llamada
b->foo(); // Error, foo() es privada
```

En definitiva no ocurre la sobreescritura, solo se esconden los métodos privados de la clase base.

## Funciones virtuales con argumentos por defecto en clases polimórficas

Es mejor evitar el uso de argumentos por defecto en la polimorfia, pues los resultados dependen del tipo de dato. Por ejemplo en una instancia de `A`, si almacenamos una instancia de `B` (derivada de `A`), los argumentos por defecto serán los de `A`:

```cpp
#include <iostream>
 
class A
{
public:
    virtual void plus(int a = 10)
    {
        std::cout << a << std::endl;
    }
};
 
class B : public A
{
public:
    virtual void plus(int a = 20)
    {
        std::cout << a << std::endl;
    }
};
 
main()
{
 
    B b;
    b.plus(); // 20
 
    A a = b;
    a.plus(); // 10 ???
}
```

Esto hace que esta funcionalidad sea tendiente a crear confusiones y por eso es mejor no llevarla a cabo.

## Destructores virtuales en clases polimórficas

El tema de los destructores es interesante, pues de forma parecida a los constructores en clases heredadas, se ejecutan de forma inversa en toda su rama hereditaria:

```cpp
#include <iostream>
 
class A
{
public:
    A() { std::cout << "Constructor A" << std::endl; }
    ~A() { std::cout << "Destructor A" << std::endl; }
};
 
class B : public A
{
public:
    B() { std::cout << "Constructor B" << std::endl; }
    ~B() { std::cout << "Destructor B" << std::endl; }
};
 
class C : public B
{
public:
    C() { std::cout << "Constructor C" << std::endl; }
    ~C() { std::cout << "Destructor C" << std::endl; }
};
 
main()
{
    C c;
}
```

```
Constructor A
Constructor B
Constructor C
Destructor C
Destructor B
Destructor A
```

Esto tiene un pequeño inconveniente y es que si manejamos memoria dinámica para almacenar un objeto de clase base `A` y en él establecemos una referencia a un objeto de clase `C`, los destructores de `B` y `C` nunca se ejecutarán y ocurrirá una fuga de memoria:

```cpp
main()
{
    A *a = new C();
    delete a;
}
```

```
Constructor A
Constructor B
Constructor C
Destructor C
    <----- ¿Y los destructores A y C?
```

Para solucionar este problema haremos que los destructores heredados sean virtuales, activando así la polimorfia:

```cpp
#include <iostream>
 
class A
{
public:
    A() { std::cout << "Constructor A" << std::endl; }
    virtual ~A() { std::cout << "Destructor A" << std::endl; }
};
 
class B : public A
{
public:
    B() { std::cout << "Constructor B" << std::endl; }
    virtual ~B() { std::cout << "Destructor B" << std::endl; }
};
 
class C : public B
{
public:
    C() { std::cout << "Constructor C" << std::endl; }
    virtual ~C() { std::cout << "Destructor C" << std::endl; }
};
 
main()
{
    A *a = new C();
    delete a;
}
```

```
Constructor A
Constructor B
Constructor C
Destructor C
Destructor B
Destructor A
```

Recordemos que las **funciones virtuales** garantizan que se llame a la función correcta para un objeto, independientemente del tipo de referencia (o puntero) utilizado para la llamada a la función.

De hecho, como un puntero inteligente es consciente de su tipo no haría falta declarar los destructores virtuales:

```cpp
// Un smart pointer no requiere los destructores virtuales
std::shared_ptr<A> a = std::make_shared<C>();
```

```
Constructor A
Constructor B
Constructor C
Destructor C
Destructor B
Destructor A
```

## Conversiones dinámicas para llamar funciones no polimórficas

En algunas ocasiones quizá nos interese tener funciones no polimórficas en nuestras clases derivadas. Si tenemos un puntero de clase base podemos utilizar la función `dynamic_cast<>()` para intentar transformar el puntero a un tipo derivado y poder acceder a la función no polimórfica. Esto funcionará si es posible la conversión al tipo derivado o fallará dando lugar a un puntero nulo.

En el siguiente ejemplo partimos de una clase base `A` y dos clases derivadas de ella: `B` y `C`. La clase `B` tiene un método `especial()` no polimórfico (no virtual en la clase base), mientras que la clase `C` no lo tiene:

```cpp
#include <iostream>
 
class A
{
public:
    A() {}
    virtual ~A() {}
};
 
class B : public A
{
public:
    B() {}
    virtual ~B() {}
    void especial() { std::cout << "Especial B: " << std::endl; }
};
 
class C : public A
{
public:
    C() {}
    virtual ~C() {}
};
```

Vamos a implementar dos funciones sobrecargadas que tomen un puntero o referencia de la clase base `A` para intentar hacer la conversión dinámica al puntero `B` y ejecutar cuando sea posible el método especial que únicamente tiene esa clase:

```cpp
// Conversión de tipo por puntero para funcion no polimorfica
void ejecutar_especial(A *a_ptr)
{
    std::cout << "Casting de *A -> *B" << std::endl;
    B *b_ptr = dynamic_cast<B *>(a_ptr);
    if (b_ptr)
    {
        b_ptr->especial();
    }
    else
    {
        std::cout << "Casting no posible" << std::endl;
    }
}
 
// Conversión de tipo por referencia para funcion no polimorfica
void ejecutar_especial(A &a_ptr)
{
    std::cout << "Casting de &A -> *B" << std::endl;
    B *b_ptr = dynamic_cast<B *>(&a_ptr);
    if (b_ptr)
    {
        b_ptr->especial();
    }
    else
    {
        std::cout << "Casting no posible" << std::endl;
    }
}
```

Si partimos de una instancia de la clase derivada `B` en un puntero o referencia de clase base `A` y los enviamos a la función, ambos casos deberían funcionar:

```cpp
A *a1 = new B();
ejecutar_especial(a1);
// Casting de *A -> *B
// Especial B
 
B b;
A &a2 = b;
ejecutar_especial(a2);
// Casting de &A -> *B
// Especial B
```

Por contra veremos que no es posible realizar la conversión dinámica mediante una instancia de clase derivada `C`, eso nos impedirá llamar la función especial porque realmente esta clase no la tiene:

```cpp
A *a3 = new C();
ejecutar_especial(a3);
// Casting no posible
```

Abusar de las conversiones en clases heredadas se considera un mal diseño, si hay demasiadas llamadas a funciones no polimórficas lo mejor es hacerlas polimórficas desde el principio:

```cpp
// Mismo ejemplo usando funciones virtuales polimórficas
class A
{
public:
    A() {}
    virtual ~A() {}
    virtual void especial()
    {
        std::cout << "Especial: No implementada " << std::endl;
    }
};
 
class B : public A
{
public:
    B() {}
    virtual ~B() {}
    virtual void especial() override
    {
        std::cout << "Especial B: " << std::endl;
    }
};
 
class C : public A
{
public:
    C() {}
    virtual ~C() {}
};
 
void ejecutar_especial(A *a_ptr) { a_ptr->especial(); }
 
main()
{
    A *a1 = new B();
    ejecutar_especial(a1);
 
    A *a2 = new C();
    ejecutar_especial(a2);
}
```

```
Especial B: 
Especial: No implementada 
``` 

## Llamar funciones virtuales (polimórficas) desde constructores y destructores

Supongamos una clase `Base` y una clase `Derivada`:

```cpp
// Para usar polimorfia hacemos...
Base *b = new Derivada;
```

Si repasamos el orden de llamada de constructores y destructores es el siguiente:

* Constructor Base
* Constructor Derivada
    * Uso del objeto construido
* Destructor Derivada
* Destructor Base

Ahora que hemos considerado este orden, supongamos que llamamos una función `virtual` para una instancia `Derivada` pero desde el constructor `Base` (usando polimorfismo). Si hacemos eso, el objeto `Derivada` (la especialización) todavía no se habrá construido, por lo que no se llamará desde la especialización, sino desde la clase `Base`.

Por tanto, llamar a una función virtual desde un constructor o destructor no arrojará resultados polimórficos. La llamada nunca llegará a una clase derivada más específica que la que tiene el propio constructor o destructor. En otras palabras, se obtendrán lo que se conoce como resultados de vínculo estático (llamadas a funciones no virtuales/polimórficas).

!!! Warning "Recordatorio"
    Nunca hay que llamar funciones virtuales desde constructores ni destructores.

## Operador typeid()

A través de esta funcionalidad podemos conseguir información sobre la clase de una instancia polimórfica y actuar en consecuencia si lo necesitamos:

```cpp
#include <iostream>
 
class A
{
public:
    A() {}
    virtual ~A() {}
};
 
class B : public A
{
public:
    B() {}
    virtual ~B() {}
};
 
class C : public B
{
public:
    C() {}
    virtual ~C() {}
};
main()
{
    A a;
    B b;
    C c;
 
    std::cout << typeid(a).name() << std::endl; // 1A
    std::cout << typeid(b).name() << std::endl; // 1B
    std::cout << typeid(c).name() << std::endl; // 1C
 
    A *p_a = &a;
    B *p_b = &b;
    C *p_c = &c;
 
    if (typeid(b) == typeid(B))
    {
        std::cout << "b es de clase B" << std::endl;
    }
 
    std::cout << typeid(p_a).name() << std::endl; // P1A
    std::cout << typeid(p_b).name() << std::endl; // P1B
    std::cout << typeid(p_c).name() << std::endl; // P1C
 
    if (typeid(*p_c) == typeid(C))
    {
        std::cout << "p_a es de clase *A" << std::endl;
    }
 
    delete (p_a);
    delete (p_b);
    delete (p_c);
}
```

## Funciones virtuales puras y clases abstractas

A veces, la implementación de las funciones no se puede proporcionar en una clase base porque no conocemos la implementación. Esa clase se llama **clase abstracta**.

Por ejemplo, supongamos que `Shape` sea una clase base. No podemos proporcionar la implementación de la función `draw()` de `Shape` porque en sí misma no puede ser dibujada, por lo que cada clase derivada tendrá que tener la implementación de `draw()` obligatoriamente. Del mismo modo una clase `Animal` no tiene implementación de `move()` (asumiendo que todos los animales se mueven), pero todos los animales deben saber cómo moverse. No podemos crear objetos de clases abstractas.

Una **función virtual pura** (o función abstracta) en C++ es una función virtual para la cual podemos tener una implementación, pero debemos anular esa función en la clase derivada, de lo contrario la clase derivada también se convertirá en clase abstracta.

Una función virtual pura se declara asignando `0` en la declaración:

```cpp
// Clase abstracta
class Test
{   
    // Miembros de la clase
public:
    // Función virtual pura
    virtual void show() = 0;
     
   /* Otros miembros */
};
```

Se implementa por clases que se derivan de una **clase abstracta**. A continuación se muestra un ejemplo para ilustrar el funcionamiento:

```cpp
#include <iostream>
 
class Base
{
    int x;
 
public:
    virtual void fun() = 0;
    int getX() { return x; }
};
 
// Esta clase hereda de Base e implementa la funcion fun()
class Derived : public Base
{
    int y;
 
public:
    void fun() { std::cout << "fun() called"; }
};
 
int main()
{
    Base b; // Error, no se permite instanciar clases abstracta
 
    Derived d;
    d.fun(); // fun() called
    return 0;
}
```

## Clases abstractas como interfaces

Una **clase abstracta con únicamente funciones virtuales puras y sin variables miembros**  puede ser utilizada como lo que se conoce como **modelo interfaz**.

Una interfaz es una especificación de algo que será completamente implementado en una clase derivada, aunque la especificación en sí misma resida en la clase abstracta:

```cpp
#include <iostream>
 
// Interfaz ultra mega simple
class Base
{
public:
    virtual void saludar() = 0;
};
 
// Implementación de una clase derivada
class Derivada : Base
{
public:
    virtual void saludar()
    {
        std::cout << "Hola mundo!" << std::endl;
    }
};
 
int main()
{
    Derivada d;
    d.saludar(); // Hola mundo!
}
```

Con esto terminamos el tema dedicado a la polimorfia en C++.

___
<small class="edited"><i>Última edición: 09 de Mayo de 2022</i></small>