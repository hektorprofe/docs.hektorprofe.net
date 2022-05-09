title: Function Templates | Apuntes lenguaje C++ | Hektor Profe
description: Function templates | Apuntes lenguaje C++

# Function Templates en C++

## Definición de Function Templates

Con el objetivo de reducir la sobrecarga de funciones existen los templates o plantillas, que permiten al propio compilador generar las sobrecargas pertinentes en base a las potenciales llamadas de la función.

El siguiente código ilustra una función que devuelve el mayor de dos datos:

```cpp
template <typename T>
T max(T a, T b)
{
    return (a > b) ? a : b;
}
```

Siempre que un mismo dos datos de un mismo tipo `T` permitan la expresión `a > b`, el compilador generará la sobrecarga de la función de ese tipo:

```cpp
int x{4}, y{6};
int *p_x{&x}, *p_y{&y};
 
std::cout << max(5.0, 6.0) << std::endl;        // 6
std::cout << max(5.0f, 6.0f) << std::endl;      // 6
std::cout << max(x, y) << std::endl;            // 6
std::cout << max(&x, &y) << std::endl;          // 0xc4771ff69c
std::cout << max(p_x, p_y) << std::endl;        // 0x7dcf5ffbbc
std::cout << max("Hola", "Mundo") << std::endl; // Hola
```

Como se puede apreciar, independientemente del tipo, sean estos enteros, double, float, punteros, referencias e incluso cadenas de texto (además de las conversiones de tipos implícitas), la misma plantilla nos sirve.

No debemos olvidar que un valor y una referencia son equivalentes en los function templates y por ello el compilador no sabrá cuál elegir:

```cpp
// Definición con tipos por valor
template <typename T>
T max(T a, T b)
{
    return (a > b) ? a : b;
}
 
// Definición con tipos por referencia
template <typename T>
const T &max(const T &a, const T &b)  
{
    return (a > b) ? a : b;
}
 
// Error, compilador confuso al no saber elegir cuál utilizar
std::cout << max(5, 6) << std::endl; 
```

En resumen:

* Los templates de función son planos y no código real de C++, consumidos por el compilador para generar el código pertinente en función de las llamadas que se hacen a la función.
* La función generada por el compilador se denomina instancia del template.
* Una instancia del templates se reutilizará de forma similar a la llamada de una función clásica en lugar de generarse duplicados.

## Especialización y sobrecarga de Templates

En algunas ocasiones es posible que necesitemos adaptar una de las sobrecargas generadas por el function template. Por ejemplo, al comprobar cual de dos cadenas `const char*` es mayor, nos devuelve la comparación lexicográfica pero nosotros queremos comparar las longitudes. En ese caso deberemos definir un template especializado para ese tipo de dato:

```cpp
#include <cstring>
 
// Template generalizado
template <typename T>
T max(T a, T b)
{
    return (a > b) ? a : b;
}
 
// Especialización para puntero de carácter
template <>
const char *max<const char *>(const char *a, const char *b)
{
    return (strlen(a) > strlen(b)) ? a : b;
}
 
std::cout << max("Hola", "Adios") << std::endl; // Adios
```

En este sentido, un comportamiento similar se puede conseguir mediante la sobrecarga de funciones.

Una sobrecarga en crudo (raw) tendrá precedencia antes que cualquier instancia de template:

```cpp
#include <cstring>
 
// Template general
template <typename T>
T max(T a, T b)
{
    std::cout << "Template general (T)" << std::endl;
    return (a > b) ? a : b;
}
 
// Sobrecarga en crudo para *char con preferencia
const char *max(const char *a, const char *b)
{
    std::cout << "Sobrecarga en crudo (char*)" << std::endl;
    return (strlen(a) > strlen(b)) ? a : b;
}
 
int x{10}, y{5};
std::cout << max("Hola", "Adios") << std::endl;
std::cout << max(x, y) << std::endl;
std::cout << max(&x, &y) << std::endl;
```

```
Sobrecarga en crudo (char*) -> Adios
Template general (T) -> 10
Template general (T) -> 0x494bdff6ac
```

Otra opción es una sobrecarga con templates, que tendrá precedencia antes que la función en crudo, por ejemplo para cualquier puntero:

```cpp
#include <cstring>
 
// Template general
template <typename T>
T max(T a, T b)
{
    std::cout << "Template general (T)" << std::endl;
    return (a > b) ? a : b;
}
 
// Sobrecarga en crudo para *char con preferencia
const char *max(const char *a, const char *b)
{
    std::cout << "Sobrecarga en crudo (char*)" << std::endl;
    return (strlen(a) > strlen(b)) ? a : b;
}
 
// Sobrecarga de template para punteros
template <typename T>
T *max(T *a, T *b)
{
    std::cout << "Sobrecarga de template (T*)" << std::endl;
    return (*a > *b) ? a : b;
}
 
int x{10}, y{5};
std::cout << max("Hola", "Adios") << std::endl;
std::cout << max(x, y) << std::endl;
std::cout << max(&x, &y) << std::endl;
```

```
Sobrecarga en crudo (char*) -> Adios
Template general (T) -> 10
Sobrecarga de template (T*) -> 0x8f107ff63c
```

## Tipos de parámetros y retorno en Templates

Los templates de las funciones nos permiten jugar con diferentes tipos de parámetros, así como el tipo del valor de retorno que podemos pasar explícitamente a la plantilla:

```cpp
// Tipo de retorno con valor por defecto y tipos de los parámetros
template <typename ReturnType = double, typename T, typename P>
ReturnType max(T a, P b)
{
    return (a > b) ? a : b;
}
 
double a{6}, b{9.5};
auto resultado = max<int, double, int>(a, b);    // int
auto resultado = max<long, double, int>(a, b);   // long
auto resultado = max<float, double, int>(a, b);  // float
auto resultado = max<double, double, int>(a, b); // double
```

## Deducción del tipo de retorno en Templates

Para indicarle a un template que deduzca automáticamente el tipo de retorno se utiliza la función `decltype()`, que devolverá el tipo resultante de una expresión evaluada:

```cpp
template <typename T, typename P>
decltype(auto) sumar( T a, P b){
    return a + b;
}
 
auto r1 = sumar(7, 3);       // int
auto r2 = sumar(7, 6.5);     // double
auto r3 = sumar(4.0f, 7.0f); // float
```

Esto se puede simplificar creando una definición con resultado `auto` y parámetros auto sin plantilla, que C++ interpretará como que debe generar el template automáticamente para los tipos llamados:

```cpp
auto sumar(auto a , auto b){
    return a + b;
}
 
auto r1 = sumar(7, 3);       // int
auto r2 = sumar(7, 6.5);     // double
auto r3 = sumar(4.0f, 7.0f); // float
```

## Rasgos de tipado en Templates

Si necesitamos realizar una aserción de tipo en nuestros templates para impedir que una función se ejecute con un tipo de dato específico, podemos usar un los `<type_traits>` para generar una excepción en el caso de que el tipo no concuerdo con lo esperado:

```cpp
#include <type_traits>
 
template <typename T>
void imprimir(T n)
{
    // static_assert(std::is_integral<T>::value, "Error...");
    static_assert(std::is_integral_v<T>, "Error, solo enteros");
    std::cout << "Numero : " << n << std::endl;
}
 
imprimir(5);            // funciona
imprimir(5.4);          // error
imprimir("Hola mundo"); // error
```

La lista completa de **type traits** la podemos encontrar en al documentación: [https://en.cppreference.com/w/cpp/header/type_traits](https://en.cppreference.com/w/cpp/header/type_traits)

## Conceptos restrictivos en Templates

___
<small class="edited"><i>Última edición: 09 de Mayo de 2022</i></small>