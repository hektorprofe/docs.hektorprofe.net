title: Miembros estáticos | Apuntes lenguaje C++ | Hektor Profe
description: Miembros estáticos | Apuntes lenguaje C++

# Miembros estáticos en C++

Un miembro estático (variable, constante o función) es un miembro enlazado a la propia clase y no a sus instancias, es decir, se utiliza a nivel de la propia clase. Puede utilizarse para realizar bibliotecas y también compartir información entre las instancias de la misma clase como miembro común para todas ellas:

```cpp
#include <iostream>
 
class Punto
{
public:
    // Miembro estático común
    static size_t contador;
 
    Punto(double x, double y) : x(x), y(y)
    {
        std::cout << "Puntos en memoria: "
                  << ++contador << std::endl;
    };
 
    ~Punto(){
        std::cout << "Puntos en memoria: "
                  << --contador << std::endl;
    }
 
    void print()
    {
        std::cout << "(" << x << ", " << y << ")\n";
    }
 
private:
    double x{}, y{};
};

// Inicialización del miembro estático
size_t Punto::contador = 0;
 
int main()
{
    Punto p1(14.76, 84.25);
    Punto p2(24.21, 52.62);
    Punto p3(12.17, 82.12);
 
    return 0;
}
```

```
Puntos en memoria: 1
Puntos en memoria: 2
Puntos en memoria: 3
Puntos en memoria: 2
Puntos en memoria: 1
Puntos en memoria: 0
```

Desde C++17 podemos utilizar la cláusula `inline` para que la función se expanda en tiempo de compilación, lo cuál nos permitirá inicializarla sin necesidad de hacerlo fuera de la función principal:

```cpp
inline static size_t contador{0};
``` 

También pueden ser constantes, lo cuál en algunos casos nos ahorraría espacio al estar definidas de forma común en todos los objetos:

```cpp
inline static const double PI{3.141592653589793238};
```

Otra opción posible de los miembros estático es la definición de miembros estáticos de la propia clase, ya sea el objeto o un puntero al objeto, pero nunca un objeto no estático. Lo inicializaremos antes de utilizarlo de forma clásica:

```cpp
class Punto
{
public:
    // Miembro estático común de la propia clase
    static Punto origen;
    //...
};
 
// Inicialización del punto de origen
// Punto Punto::origen = Punto(0, 0);
Punto Punto::origen{0, 0};
 
int main()
{
    std::cout << "Punto origen: ";
    Punto::origen.print();
}
```

```
Puntos en memoria: 1
Punto origen: (0, 0)
Puntos en memoria: 0
```

De forma similar podemos definir funciones estáticas, aunque hay que tener en cuenta que éstas no tienen acceso a miembros de instancia, únicamente a otros miembros estáticos:

```cpp
static void print_origen()
{
    std::cout << "Punto origen: ";
    std::cout << "(" << origen.x << ", " << origen.y << ")\n";
}
 
Punto Punto::origen = Punto(0, 0);
int main()
{
    Punto::origen.print_origen();
    return 0;
}
```

Sin embargo, una forma de utilizarlas de forma óptima sería, por ejemplo, para nuestra función `print`, en lugar de encontrarse en todas las instancias, tener un método estático que a partir de la referencia de un punto lo muestre en pantalla. Eso reducirá mucho el espacio de memoria ocupado:

```cpp
// Función print optimizada para reducir memoria
static void print(const Punto &p)
{
    std::cout << "(" << p.x << ", " << p.y << ")\n";
}
```

___
<small class="edited"><i>Última edición: 09 de Mayo de 2022</i></small>