title: Sobrecarga de operadores | Apuntes lenguaje C++ | Hektor Profe
description: Sobrecarga de operadores | Apuntes lenguaje C++

# Sobrecarga de operadores en C++

La sobrecarga de operadores nos permite establecer el comportamiento deseado que una instancia tiene en conjunto con los diferentes operadores con los que contamos. Podemos ver la lista completa es la página [https://en.cppreference.com/w/cpp/language/operator_precedence](https://en.cppreference.com/w/cpp/language/operator_precedence).

Existen operadores **unarios** y **binarios** que pueden programarse como **miembros** y **no miembros**:

* **Unario**: requieren un único operando:
    * Miembro (interna): `ReturnType operator X()`
    * No miembro (externa): `ReturnType operator X (Type op)`
 * **Binario**: requieren dos operandos:
    * Miembro (interna): `ReturnType operator X(Type op_der)`
    * No miembro (externa): `ReturnType operator X(Type op_izq, Type op_der)`

Veamos algunos ejemplos a partir de la clase `Punto` para sobrecargar diferentes operadores:

```cpp
#include <iostream>
 
class Punto
{
public:
    Punto() = default;
    Punto(double x, double y) : x(x), y(y){};
    void print() { 
        std::cout << "(" << x << ", " << y << ")\n"; }
 
private:
    double x{}, y{};
};
```

## Operador + como miembro

```cpp
class Punto
{
public:
    // Definición de la sobrecarga del operador + miembro
    Punto operator+(const Punto &p) const
    {
        return Punto(x + p.x, y + p.y);
    }
 
private:
    double x{}, y{};
};

int main()
{
    Punto p1(3, 4), p2(6, 2);
    Punto pr{p1 + p2};
    pr.print(); // (9, 6)
    return 0;
}
```

## Operador + como no miembro

```cpp
class Punto
{
    // Declaración de la sobrecarga del operador + no miembro
    friend inline Punto operator+(const Punto &p1, const Punto &p2);
 
    // ...
};
 
// Definición de la sobrecarga del operador + no miembro
inline Punto operator+(const Punto &p1, const Punto &p2)
{
    return Punto(p1.x + p2.x, p1.y + p2.y);
}

int main()
{
    Punto p1(3, 4), p2(6, 2);
    Punto pr{p1 + p2};
    pr.print(); // (9, 6)
    return 0;
}
```

## Operador stream insertion

Este operador es el que se ejecuta implícitamente al mostrar un objeto con `std::cout <<`. Éste se debe implementar como no miembro:

```cpp
#include <iostream>
 
class Punto
{
    // Declaración como amiga de la sobrecarga no miembro
    friend std::ostream &operator<<(std::ostream &os, const Punto &p);
 
public:
    // ...
};
 
// Definición de la sobrecarga no miembro
inline std::ostream &operator<<(std::ostream &os, const Punto &p)
{
    os << "(" << p.x << ", " << p.y << ")";
    return os;
}

int main()
{
    Punto p1(3, 4);
    std::cout << p1 << std::endl; // (3, 4)
    return 0;
}
```

También existe la forma de extracción `>>` para implementar una lectura de valores pero no voy a explicarlo aquí.

## Conversiones de tipos

Supongamos que nos gustaría que la conversión `static_cast<int>(punto)` devuelva la suma de las coordenadas, es un ejemplo tonto pero nos servirá para ilustrar el funcionamiento:

```cpp
#include <iostream>
 
class Punto
{
    // ...
 
    explicit operator int() const
    {
        return x + y;
    }
};

int main()
{
    Punto p1(3, 4);
    std::cout << static_cast<int>(p1) << std::endl; // 7
    return 0;
}
```

## Conversiones de funtor

Por funtor nos referimos a sobrecargar el operador `()` en los objetos de una clase. La forma más sencilla de ver la implementación es crear nuestra propia clase **Impresor** y sobrecargar su funtor `()` para ejecutar la impresión del contenido enviado al operador:

```cpp
class Impresor
{
public:
    void operator()(std::string nombre)
    {
        std::cout << "Nombre: " << nombre << std::endl;
    }
    void operator()(std::string nombre, std::string apellido)
    {
        std::cout << "Nombre y apellido: "
                  << nombre << " " << apellido << std::endl;
    }
    void operator()(Punto p)
    {
        std::cout << "Punto: (" << p.getX()
                  << ", " << p.getY() << ")" << std::endl;
    }
};

int main()
{
    Punto p1(3, 4);
    Impresor impresor;
 
    impresor("Mario");          
    impresor("Mario", "Perez"); 
    impresor(p1);               
 
    return 0;
}
```

```
Nombre: Mario
Nombre y apellido: Mario Perez
Punto: (3, 4)
```

Las posibilidades que nos ofrece la sobrecarga de operadores son enormes.

___
<small class="edited"><i>Última edición: 09 de Mayo de 2022</i></small>