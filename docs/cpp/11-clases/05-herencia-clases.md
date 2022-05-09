title: Herencia de clases | Apuntes lenguaje C++ | Hektor Profe
description: Herencia de clases | Apuntes lenguaje C++

# Herencia de clases en C++

No soy un gran fan de la herencia de clases porque creo que en la práctica solo es aplicaba en arquitectura de software. Muchos programadores defienden que la programación funcional es mucho mejor para resolver problemas que aplicar POO y herencia, la verdad es que cada vez estoy más convencido de ello. Aún así intentaré resumir las partes más esenciales de la herencia en C++.

La herencia es la capacidad de una clase (derivada) de heredar y extender los miembros de otra clase (base). En la herencia pública, las clases derivadas pueden acceder y utilizar los miembros públicos de la clase base, pero la clase derivada no tiene acceso directo a los miembros privados. Lo mismo aplica a los amigos de la clase derivada, que tienen acceso a los miembros privados derivados, pero no a la clase base:

```cpp
/* Clase base Persona */
class Persona
{
    friend std::ostream &operator<<(std::ostream &os, const Persona &p);
 
public:
    Persona() = default;
    Persona(std::string nombre) : nombre(nombre){};
    std::string getNombre() const { return this->nombre; }
    void setNombre(std::string nombre) { this->nombre = nombre; }
 
private:
    std::string nombre{"?"};
};
 
std::ostream &operator<<(std::ostream &os, const Persona &p)
{
    os << p.nombre;
    return os;
}

/* Clase derivada Jugador */
class Jugador : public Persona
{
    friend std::ostream &operator<<(std::ostream &os, const Jugador &j);
 
public:
    Jugador(std::string juego) : juego(juego){};
 
private:
    std::string juego{"?"};
};
 
std::ostream &operator<<(std::ostream &os, const Jugador &j)
{
    os << j.getNombre() << " (" << j.juego << ")";
    return os;
}

int main()
{
    Jugador jugador("Volleyball");
    jugador.setNombre("Marcos");  
    std::cout << jugador << std::endl;  // Marcos (Volleyball)
    return 0;
}
```

Como vemos no es posible acceder a los miembros privados de la clase base desde la clase derivada y para ello necesitamos crear getters públicos. 

El kit de la cuestión es que mediante la cláusula `protected` podemos definir miembros que sean accesibles solo desde clases derivadas:

```cpp
/* Clase base Persona */
class Persona
{
// Bloque de miembros accesibles en clases derivadas
protected:
    std::string nombre{"?"};  
};
 
// La clase derivada ahora tiene acceso directo a los miembros
std::ostream &operator<<(std::ostream &os, const Jugador &j)
{
    os << j.nombre << " (" << j.juego << ")";
    return os;
}
```

Volviendo al tipo de herencia, hay tres formas de heredar los miembros de una clase base:

* En la **herencia pública**, los miembros públicos y protegidos permanecen igual en la clase derivada.
* En la **herencia protegida**, los miembros públicos y protegidos se hacen protegidos en la clase derivada.
* En la **herencia privada**, los miembros públicos y protegidos de la clase base se vuelven privados en la clase derivada.

```cpp
class Base
{
public:
    int x;
 
protected:
    int y;
 
private:
    int z;
};
 
// Herencia pública
class PublicaDerivada : public Base
{
    // x es public
    // y es protected
    // z no es accesible desde PublicaDerivada 
};
 
// Herencia protegida
class ProtegidaDerivada: protected Base
{
    // x es protected
    // y es protected
    // z no es accesible desde ProtegidaDerivada
};
 
// Herencia privada
class PrivadaDerivada: private Base
{
    // x is privada
    // y is privada
    // z no es accesible desde PrivadaDerivada
};
```

Debemos tener en cuenta lo anterior, especialmente al heredar de clases derivadas, pues los miembros habrán cambiado su visibilidad.

## Resurrección de miembros

Sin embargo existe un método para recuperar o cambiar la visibilidad de los miembros en las clases heredadas conocido como **resurrección de miembros en el contexto**.

La resurrección solo funcionará en miembros públicos y protegidos, los miembros privados de la clase base no se pueden resucitar:

```cpp
class Base
{
public:
    int x;
 
protected:
    int y;
 
private:
    int z;
};
 
// La herencia privada hará x e y privadas
class PrivadaDerivada : private Base
{
public:
    using Base::x; // Resucitamos x como pública
protected:
    using Base::y; // Resucitamos y como protected
};
```

## Constructores en la herencia

Los constructores por defecto se llaman en cada una de las clases derivadas al crear una instancia, podemos comprobarlo con el siguiente experimento:

```cpp
#include <iostream>
 
class A
{
public:
    A() { std::cout << "Constructor de A" << std::endl; }
};
 
class B : public A
{
public:
    B() { std::cout << "Constructor de B" << std::endl; }
};
 
class C : public B
{
public:
    C() { std::cout << "Constructor de C" << std::endl; }
};
 
class D : public C
{
public:
    D() { std::cout << "Constructor de D" << std::endl; }
};
 
int main()
{
    D d;
    return 0;
}
```

```
Constructor de A
Constructor de B
Constructor de C
Constructor de D
```

En caso de que las clases derivadas extiendan los parámetros de inicialización en el constructor, la forma de abordar el problema es mediante inicialización listada con los propios constructores y luego los miembros de la clase derivada, tal como ilustra este ejemplo:

```cpp
class A
{
public:
    int a;
    A(int a) : a(a)
    {
        std::cout << "Constructor de A: "
                  << "a -> " << a << std::endl;
    }
};
 
class B : public A
{
public:
    int b;
    B(int a, int b) : A(a), b(b)
    {
        std::cout << "Constructor de B: "
                  << "a -> " << a
                  << ", b -> " << b << std::endl;
    }
};
 
class C : public B
{
public:
    int c;
    C(int a, int b, int c) : B(a, b), c(c)
    {
        std::cout << "Constructor de C: "
                  << "a -> " << a
                  << ", b -> " << b
                  << ", c -> " << c << std::endl;
    }
};
 
class D : public C
{
public:
    int d;
    D(int a, int b, int c, int d) : C(a, b, c), d(d)
    {
        std::cout << "Constructor de D: "
                  << "a -> " << a
                  << ", b -> " << b
                  << ", c -> " << c
                  << ", d -> " << d << std::endl;
    }
};
 
int main()
{
    D d(1, 2, 3, 4);
    return 0;
}
```

```
Constructor de A: a -> 1
Constructor de B: a -> 1, b -> 2
Constructor de C: a -> 1, b -> 2, c -> 3
Constructor de D: a -> 1, b -> 2, c -> 3, d -> 4
```

## Herencia de los símbolos

Comentar por último que si en una clase derivada se redefinen los miembros de una clase base, se tomará el comportamiento de la clase derivada y se descartará el de la clase base:

```cpp
class Base
{
public:
    std::string texto{"Hola mundo"};
 
    void print()
    {
        std::cout << texto << " (publico) desde base\n";
    }
};
 
class Derivada : public Base
{
 
private:
    std::string texto{"Adios mundo"};
 
public:
    void print()
    {
        std::cout << texto << " (privado) desde derivada\n";
    }
};
 
main()
{
    Base b;
    b.print();
    Derivada d;
    d.print();
    return 0;
}
```

```
Hola mundo (publico) desde base
Adios mundo (privado) desde derivada
```
___
<small class="edited"><i>Última edición: 09 de Mayo de 2022</i></small>