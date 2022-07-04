title: Sobrecarga de funciones | Apuntes lenguaje C++ | Hektor Profe
description: Sobrecarga de funciones | Apuntes lenguaje C++

# Sobrecarga de funciones en C++

Es posible que en un momento determinado tengamos la necesidad de que una misma función permita distintos tipos de entrada.

Un ejemplo muy simple sería una función para determinar el mayor de dos valores, pero diferenciando entre diferentes tipos como enteros, double y cadenas. Para ello podemos sobrecargar funciones, es decir, definir múltiples veces una declaración y/o definición de manera que, si no concuerda la primera definición el sistema prueba con la siguiente hasta encontrar una forma de cumplir la llamada:

```cpp
int max(int a, int b)
{
    std::cout << "int sobrecargado" << std::endl;
    return (a > b) ? a : b;
}
 
double max(double a, double b)
{
    std::cout << "double sobrecargado" << std::endl;
    return (a > b) ? a : b;
}
 
std::string_view max(std::string_view a, std::string_view b)
{
    std::cout << "string_view sobrecargado" << std::endl;
    return (a.length() > b.length()) ? a : b;
}
 
max(10, 5);           // int sobrecargado
max(15.5, -4.23);     // double sobrecargado
max("Hola", "mundo"); // string_view sobrecargado
```

Sobrecargar funciones permite cambiar el **orden**, la **cantidad** y el **tipo** de los parámetros, pero debemos ser conscientes que hay situaciones ambiguas que ocasionarán problemas, así que repasemos algunos ejemplos.

Al trabajar sobrecargando **punteros**, las siguientes definiciones serían equivalentes para arreglos:

```cpp
// Declaraciones equivalentes con punteros de arreglos
int max(int *numeros, size_t contador);
int max(int numeros[], size_t contador);
int max(int numeros[10], size_t contador);
```

Trabajando con referencias de `std::string`, estos dos llamadas serían ambiguas, el compilador no sabría cuál elegir y daría error:

```cpp
// Declaraciones ambiguas
void saludar(const std::string &nombre);
void saludar(const std::string nombre);
```

En el caso de dos definiciones variando que una sea **constante** y la otra no, estaremos ante una redefinición, de manera que se sobrescribirá la que venga por debajo:

```cpp
// Declaraciones redefinidas
int max(int a, int b);
int max(const int a, const int b);
```

Ahora bien, si cambia el tipo de dato, por ejemplo a un **puntero**, entonces la sobrecarga sí es posible:

```cpp
// Declaración permitida no redefinida
int max(const int a, const int b);
int max(const int *a, const int *b);
```

Pero sobrecargar un **puntero constante** y un **puntero constante a un valor constante** también se considera redefinición:

```cpp
// Declaraciones redefinidas
int max(const int *a, const int *b);
int max(const int const *a, const int const *b);
```

Por último, trabajando con **referencias**, sí está permitido sobrecargar una referencia y una referencia constante, pues estas si implican dos tipos distintos:

```cpp
// Declaraciones permitida no redefinida
int max(int &a, int &b);
int max(const int &a, const int &b);
```

___
<small class="edited"><i>Última edición: 09 de Mayo de 2022</i></small>