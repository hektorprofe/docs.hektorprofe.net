title: Funciones y clases amigas | Apuntes lenguaje C++ | Hektor Profe
description: Funciones y clases amigas | Apuntes lenguaje C++

# Funciones y clases amigas en C++

## Funciones amigas

Una función amiga es una función externa de una clase que es capaz de acceder a los miembros privados de la misma. Para conseguirlo se declaran en la propia clase con la cláusula `friend`.

Si una función no es amiga no podremos hacer lo siguiente:

```cpp
#include <iostream>
 
class Punto
{
private:
    double x{}, y{};
public:
    Punto(double x, double y) : x(x), y(y) {}
};
 
// Error al no tener acceso a los miembros
void print(const Punto &p)
{
    std::cout << "(" << p.x << ", " << p.y << ") "
              << "[" << &p << "]" << std::endl;
}
 
int main()
{    
    Punto p1(5, 4);
    print(p1);
    return 0;
}
```

Si la marcamos como amiga tendremos acceso a sus miembros:

```cpp
#include <iostream>
 
class Punto
{
private:
    double x{}, y{};
public:
    Punto(double x, double y) : x(x), y(y) {}
    friend void print(const Punto &p); // ¡Soy amiga!
};
 
// Ahora funcionará porque somos amigos de la clase
void print(const Punto &p)
{
    std::cout << "(" << p.x << ", " << p.y << ") "
              << "[" << &p << "]" << std::endl;
}
 
int main()
{    
    Punto p1(5, 4);
    print(p1);  // (5, 4) [0x8d725ff700]
    return 0;
}
```

Consideraciones acerca de las funciones amigas:

* Debe declararse primero en la clase y no importa donde esté definida mientras lo esté.
* La clase determinará quién es amigo a través de la declaración.
* No importa si se declara en la parte pública o privada.
* Pueden tenerse múltiples funciones amigas y **sobrecargarlas** si es necesario.
* Las funciones amigas no son funciones miembro.
* Las funciones amigas no tienen acceso al puntero `this`.

## Clases amigas

De forma similar al funcionamiento de las funciones amigas, una clase no tiene por defecto acceso a los miembros de otra.

Supongamos el siguiente ejemplo donde tenemos una clase `Perro` y una clase `Gato`, donde la clase `Gato` tiene un puntero a un objeto de tipo `Perro` llamado `*amigoPerruno`. Si bien podemos establecer el puntero mediante el método del gato `setAmigoPerruno()`, cuando queramos comprobar los miembros del perro no podremos hacerlo porque las clases `Perro` y `Gato` no son amigas por defecto:

```cpp
#include <iostream>
 
class Perro
{
public:
    Perro(std::string nombre, int edad) 
        : nombre(nombre), edad(edad) {}
 
private:
    std::string nombre;
    int edad;
};
 
class Gato
{
public:
    Gato(std::string nombre, int edad)
        : nombre(nombre), edad(edad) {}
 
    void setAmigoPerruno(Perro *p)
    {
        this->amigoPerruno = p;
    }
 
    void amigo()
    {
        if (this->amigoPerruno)
        {
            // No podemos acceder a los miembros del perro
            std::cout << this->nombre << " es amigo de "
                << this->amigoPerruno->nombre << std::endl;
        }
        else
        {
            std::cout << this->nombre 
                << " no tiene amigos" << std::endl;
        }
    }
 
private:
    std::string nombre;
    int edad;
    Perro *amigoPerruno;
};
```

Si establecemos que `Gato` es amigo de `Perro` en la declaración de la clase:

```cpp
class Perro
{
public:
    // Establecemos que Gato es una clase amigui
    friend class Gato;
 
    Perro(std::string nombre, int edad)
        : nombre(nombre), edad(edad) {}
 
private:
    std::string nombre;
    int edad;
};
```

Entonces podremos hacer algo como esto:

```cpp
int main()
{
    Perro perro("Ronnie", 4);
    Gato gato("Sky", 2);
 
    gato.setAmigoPerruno(&perro);
    gato.amigos();
  
    Gato gatoSolitario("Nick", 8);
    gatoSolitario.amigos();
 
    return 0;
}
```

```
Sky es amigo de Ronnie
Nick no tiene amigos
```

___
<small class="edited"><i>Última edición: 09 de Mayo de 2022</i></small>