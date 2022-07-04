title: Primeros pasos con funciones | Apuntes lenguaje C++ | Hektor Profe
description: Primeros pasos con funciones | Apuntes lenguaje C++

# Primeros pasos con funciones en C++

## Declaración y definición de funciones

Las funciones son bloques de código reutilizable identificados con un nombre que pueden recibir y devolver información para comunicarse con el contexto de la llamada.

En C++ una función debe estar declarada o definida antes de su utilización, de ahí que se puedan dividir en dos ficheros distintos, los de cabeceras con declaraciones y los ficheros con las definiciones.

```cpp
#include <iostream>
 
// Declaración
void saludar(const char *nombre);
 
int main()
{
    saludar("Hector");
}
 
// Definición
void saludar(const char *nombre)
{
    std::cout << "Hola " << nombre << std::endl;
}
```

## Tipos de paso a funciones

El paso es la forma como nos referimos a la forma en que se envían y se reciben los argumentos de una función. Dada la flexibilidad del lenguaje C++ a la hora de manejar la información encontramos muchos tipos, desde el paso por valor al paso con punteros y referencias.

**Paso por valor**

En este paso se crea una copia local de las variables dentro de la función, por tanto no tienen nada que ver con los valores externas y su modificación solo afecta al propio contexto de la función:

```cpp
// Declaración
int sumar_valores(int a, int b);
 
// Definición
int sumar_valores(int a, int b)
{
    // a es una variable local modificable
    a = 50;
    std::cout << a + b << std::endl;
    return a + b;
}
 
// Llamada
int n1{10}, n2{25};
sumar_valores(n1, n2); // 75
```

**Paso por valor constante**

En este paso las variables las variables también son locales, pero al ser constantes no permiten la modificación de su valor en la función:

```cpp
// Declaración
int sumar_valores_constantes(const int a, const int b);
 
// Definición
int sumar_valores_constantes(const int a, const int b)
{
    // a es una variable local no modificable
    // a = 10;
    std::cout << a + b << std::endl;
    return a + b;
}
 
// Llamada
int n1{10}, n2{25};
sumar_valores_constantes(n1, n2); // 35
```

**Paso por puntero**

En este paso los punteros apuntan a las variables externas, de manera que los cambios modificarán también los valores del exterior, así como si decidimos cambiar la dirección del puntero:

```cpp
// Declaración
int sumar_valores_punteros(int *a, int *b);
 
// Definición
int sumar_valores_punteros(int *a, int *b)
{
    // a es una puntero externo
    // el valor de a se puede modificar y su dirección también
    *a = 50;
    a = b;
    std::cout << *a + *b << std::endl;
    return *a + *b;
}
 
// Llamada
int n1{10}, n2{25};
sumar_valores_punteros(&n1, &n2); // 50
```

**Paso por puntero constante**

En este paso los punteros apuntan a las variables externas, al ser constantes no se puede modificar su valor, pero sí se puede cambiar la dirección y eso afectará a la variable externa:

```cpp
// Declaración
int sumar_valores_punteros_constantes(const int *a, const int *b);
 
// Definición
int sumar_valores_punteros_constantes(const int *a, const int *b)
{
    // a es una puntero externo
    // el valor de a no se puede modificar pero su dirección sí
    // *a = 50;
    a = b;
    std::cout << *a + *b << std::endl;
    return *a + *b;
}
 
// Llamada
int n1{10}, n2{25};
sumar_valores_punteros_constantes(&n1, &n2); // 50
```

**Paso por puntero constante con valor constante**

En este paso, los punteros apuntan al exterior, pero no permiten ni modificar el valor ni la dirección en la memoria del puntero:

```cpp
// Declaración
int sumar_valores_constantes_punteros_constantes(const int *const a, const int *const b);
 
// Definición
int sumar_valores_constantes_punteros_constantes(const int *const a, const int *const b)
{
    // a es una puntero externo
    // el valor de a no se puede modificar y su dirección tampoco
    // *a = 50;
    // a = b;
    std::cout << *a + *b << std::endl;
    return *a + *b;
}
 
// Llamada
int n1{10}, n2{25};
sumar_valores_constantes_punteros_constantes(&n1, &n2); // 75
```

**Paso por referencia**

En este paso, la referencia es un alias de la variable exterior y su valor se puede modificar, pero no su dirección en la memoria (parecido a un puntero constante):

```cpp
// Declaración
int sumar_valores_referencia(int &a, int &b);
 
// Definición
int sumar_valores_referencia(int &a, int &b)
{
    // a es una referencia externa
    // el valor de a se puede modificar pero su referencia no
    a = b;
    //&a = &b;
    std::cout << a + b << std::endl;
    return a + b;
}
 
// Llamada
int n1{10}, n2{25};
sumar_valores_referencia(n1, n2); // 50
```

**Paso por referencia constante**

En este paso también se hace referencia a la variable exterior, pero no se puede modificar ni el valor ni su dirección en la memoria:

```cpp
// Declaración
int sumar_valores_referencia_constantes(const int &a, const int &b);
 
// Definición
int sumar_valores_referencia_constantes(const int &a, const int &b)
{
    // a es una referencia externa
    // el valor de a no se puede modificar y su referencia tampoco
    // a = b;
    // &a = &b;
    std::cout << a + b << std::endl;
    return a + b;
}
 
// Llamada
int n1{10}, n2{25};
sumar_valores_referencia_constantes(n1, n2); // 50
```

## Paso de arreglos a funciones

Si queremos enviar los datos de un arreglo a una función podemos hacerlo de dos formas, mediante el arreglo en sí mismo, el cuál es un puntero al primer elementos del arreglo, o a partir de su referencia.

En ambos casos tendremos un problema para determinar el número de elementos del arreglo para recorrerlo dinámicamente, por eso necesitaremos enviarlo como dato a la función:

```cpp
double sumar_array_valor(double array[], size_t count)
{
    double total{};
    for (size_t i{}; i < count; i++)
    {
        total += *(array + i);
    }
    return total;
}
 
double numeros[]{11.0, 22.0, 33.0, 44.0};
std::cout << sumar_array_valor(numeros, 4) << std::endl; // 110
```

O si enviamos la referencia, la trataremos de forma constante con un número preestablecido de elementos:

```cpp
double sumar_array_referencia(const double (&array)[4])
{
    double total{};
    for (size_t i{}; i < std::size(array); i++)
    {
        total += array[i];
    }
    return total;
}
 
double numeros[]{11.0, 22.0, 33.0, 44.0};
std::cout << sumar_array_referencia(numeros) << std::endl; // 110
```

Si queremos trabajar con arreglos multidimensionales seguiremos los mismos pasos, en el caso del arreglo en forma de puntero:

```cpp
double sumar_multiarray_valor(double array[][3], size_t count_i, size_t count_j)
{
    double total{};
    for (size_t i{}; i < count_i; i++)
    {
        for (size_t j{}; j < count_j; j++)
        {
            total += *(*(array + i) + j);
        }
    }
    return total;
}
 
double num2d[][3]{
    {5.0, 10.0, 15.0},
    {6.0, 12.0, 18.0},
    {7.0, 14.0, 21.0}};
std::cout << sumar_multiarray_valor(num2d, 3, 3) << std::endl; // 108
```

Y para el arreglo multidimensional pasado con la referencia:

```cpp
double sumar_multiarray_referencia(const double (&array)[3][3])
{
    double total{};
    for (size_t i{}; i < std::size(array); i++)
    {
        for (size_t j{}; j < std::size(array[i]); j++)
        {
            total += array[i][j];
        }
    }
    return total;
}
 
double num2d[][3]{
    {5.0, 10.0, 15.0},
    {6.0, 12.0, 18.0},
    {7.0, 14.0, 21.0}};
std::cout << sumar_multiarray_referencia(num2d) << std::endl; // 108
```

## Funciones constexpr y consteval

Tal como expliqué en el apartado expresiones e inicializaciones constantes, debemos separar dos formas de almacenar la memoria de los valores: en tiempo de compilación y en tiempo de ejecución.

Almacenar el espacio en tiempo de compilación es más eficaz y ahorra tiempo al programa, almacenarlo en tiempo de ejecución requiere tareas extras antes de utilizarlo.

En este caso, una función `constexpr` indica que su valor, o valor de retorno, es una constante, posiblemente computada en tiempo de compilación:

```cpp
constexpr int prod(int a, int b)
{
    return a * b;
}
 
// interpretado en tiempo de compilación
const int res1 = prod(3, 5);
 
// interpretado en tiempo de ejecución
int a{5}, b{10};
int res2 = prod(a, b);
```

Desde C++20 se puede garantizar que una función es evaluada en tiempo de compilación con el modificador `consteval`, en caso contrario dará error:

```cpp
consteval int prod(int a, int b)
{
    return a * b;
}
 
// interpretado en tiempo de compilación
const int res1 = prod(3, 5);
 
// error de compilación
int a{5}, b{10};
int res2 = prod(a, b);
```

## Argumentos por defecto a funciones

Si lo necesitamos podemos establecer valores por defecto en los parámetros de las funciones, actuarán como inicialización de las variables en caso de que no se envíen. Cabe decir que se manejan por posición:

```cpp
double area(double width = 0.0, double height = 0.0)
{
    return width * height;
}
 
std::cout << area() << std::endl;     // 0
std::cout << area(3, 5) << std::endl; // 15
```

A comentar que, en caso de trabajar con cadenas de caracteres, utilizaríamos recomendablemente `std::string_view` para no malgastar memoria:

```cpp
void info(std::string_view name = "Hector", int age = 32)
{
    std::cout << "Nombre: " << name 
              << ", edad: " << age << std::endl;
}
 
info();           // Nombre: Hector, edad: 32
info("Juan", 47); // Nombre: Juan, edad: 47
```

## Argumentos de la función main

Ahora que entendemos como enviar arreglos a las funciones podemos echar un vistazo a cómo procesar argumentos en los programas mediante la función main.

Ya que un programa se empieza a ejecutar siempre por esta función única, podemos configurar un par de parámetros para capturar los argumentos enviados al programa en su ejecución.

Tenemos dos argumentos posicionales, el primero es un entero con el número de argumentos enviados al que se suele llamar `argc` (contador de argumentos), el segundo un arreglo de punteros `char*`, es decir, unas cadenas de caracteres y suele tener el nombre `argv` (argument values). El primero nos servirá para recorrer el segundo:

```cpp
#include <iostream>
 
int main(int argc, char *argv[])  // También definible como char **argv
{
    for (int i{0}; i < argc; i++)
    {
        std::cout << "Argumento [" << i << "]: " << argv[i] << std::endl;
    }
}
```

```bash
> main.exe hola que tal
Argumento [0]: C:\Curso-Cpp\main.exe
Argumento [1]: hola
Argumento [2]: que
Argumento [3]: tal
```

Como vemos el primer argumento siempre contiene la ruta de ejecución del script, y a partir del segundo los diferentes parámetros que enviamos a la función main al ejecutar el programa.

Jugando con estos valores y los castings de tipos podemos crear scripts funcionales para la terminal, elaborar sistemas de ayuda y un montón de posibilidades.

## Tipos de retorno para funciones

Por defecto los datos de las funciones se **devuelven por valor**, eso significa que se crea una copia del dato en el exterior:

```cpp
int suma(int a, int b)
{
    int resultado = a + b; // 0x316cbffb9c
    std::cout << "Dentro: " << &resultado << std::endl;
    return resultado;
}
 
int resultado = suma(2, 5); // 0x316cbffbdc
std::cout << "Fuera: " << &resultado << std::endl;
```

Algunos compiladores modernos optimizan los retornos cuando es posible, como GCC al devolver una `std::string` que lo hace con el puntero para ahorrar memoria:

```cpp
std::string suma(std::string a, std::string b)
{
    std::string resultado = a + b; // 0xcbb2bff610
    std::cout << "Dentro: " << &resultado << std::endl;
    return resultado;
}
 
std::string resultado = suma("Hola ", "mundo"); // 0xcbb2bff610
std::cout << "Fuera: " << &resultado << std::endl;
```

También podemos **devolver por referencia**, siempre y cuando se haya enviado previamente a la función:

```cpp
int &max(int &a, int &b)
{
    return a > b ? a : b; // bien, referencias externos
}
 
int a{11}, b{14};
std::cout << "Max: " << max(a, b) << std::endl;
```

En caso contrario, si la referencia es de una variable local definida en la propia función, al finalizar la ejecución se borrará y el programa dará error:

```cpp
int &max(int &a, int &b)
{
    int resultado = a > b ? a : b;
    return resultado; // error, referencia local
}
 
int a{11}, b{14};
std::cout << "Max: " << max(a, b) << std::endl;
```

Exactamente lo mismo ocurre con los punteros, si se devuelve un puntero externo funcionará:

```cpp
int *max(int *a, int *b)
{
    return *a > *b ? a : b; // bien, puntero externo
}
 
int a{11}, b{14};
std::cout << "Max: " << *max(&a, &b) << std::endl;
```

Pero si devolvemos un puntero local de la función, se borrará y no existirán:

```cpp
int *max(int *a, int *b)
{
    int resultado = *a > *b ? *a : *b;
    return &resultado; // error, puntero local
}
 
int a{11}, b{14};
std::cout << "Max: " << *max(&a, &b) << std::endl;
```

## Retorno de elemento en arreglo

Supongamos que necesitaremos realizar una tarea sobre un arreglo de números, por ejemplo devolver el mayor número del arreglo. Si lo identificamos y lo devolvemos de forma normal, estaremos devolviendo una copia del valor, duplicando el espacio en la memoria:

```cpp
const double max(const double numeros[], size_t contador)
{
    double max{};
 
    for (size_t i{}; i < contador; i++)
    {
        if (numeros[i] > max)
        {
            max = numeros[i];
        }
    }
 
    std::cout << &max << std::endl; // 0x61d4bff9e0
    return max;
}
 
double arreglo[]{11, 22, 33, 44, 55};
const double mayor{max(arreglo, 5)};
std::cout << &mayor << std::endl; // 0x61d4bffa28
```

En estos casos lo que podemos hacer es devolver una referencia la elemento del arreglo, eso nos ahorrará duplicar la memoria:

```cpp
const double *max(const double numeros[], size_t contador)
{
    size_t max_i{};
 
    for (size_t i{}; i < contador; i++)
    {
        if (numeros[i] > numeros[max_i])
        {
            max_i = i;
        }
    }
    std::cout << &numeros[max_i] << std::endl; // 0x4a50dff850
    return &numeros[max_i];
}
 
double arreglo[]{11, 22, 33, 44, 55};
const double *mayor{max(arreglo, 5)};
std::cout << mayor << std::endl; // 0x4a50dff850
```

## Retorno std::optional para funciones

Supongamos que en algún momento necesitamos programar una función que devuelva si se encontró un número en un arreglo. Para ahorrar memoria podemos definir una variable booleana y enviar su referencia a la función para que establezca el resultado ahí:

```cpp
void numero_encontrado(int numeros[], const size_t &contador, const int &numero, bool &encontrado)
{
    for (size_t i{}; i < contador; i++)
    {
        if (numeros[i] == numero)
        {
            encontrado = true;
            return;
        }
    }
}
 
int arreglo[]{11, 22, 33, 44, 55};
bool encontrado{};
numero_encontrado(arreglo, 5, 44, encontrado);
 
if (encontrado) std::cout << "Numero encontrado" << std::endl;
else std::cout << "Numero no encontrado" << std::endl;
```

Desde C++17 encontramos un tipo de dato llamado `std::optional` que por defecto contiene un valor vacío y a parte el tipo de dato que necesitemos almacenar. Esta estructura contiene diferentes métodos para saber si la variable está inicializada `has_value()` y consultar su valor `value()`:

```cpp
#include <optional>
 
std::optional<int> numero{10};
if (numero.has_value())
    std::cout << numero.value() << std::endl;
else
    std::cout << "Valor no inicializado" << std::endl;
```

El inicializador nulo por defecto para un `std::optional` es `std::nullopt`:

```cpp
#include <optional>
 
std::optional<int> numero{std::nullopt}; // por defecto
if (numero.has_value())
    std::cout << numero.value() << std::endl;
else
    std::cout << "Valor no inicializado" << std::endl;
```

Su utilidad en nuestro contexto de retorno es que con él podemos retornar un valor o un puntero nulo, lo que nos permite manejar más información en una sola llamada:

```cpp
std::optional<int> indice_numero(int numeros[], const size_t &contador, const int &numero)
{
    for (size_t i{}; i < contador; i++)
    {
        if (numeros[i] == numero)
        {
            return i;
        }
    }
    return {}; // std::nullopt
}
 
int arreglo[]{11, 22, 33, 44, 55};
std::optional<int> indice = indice_numero(arreglo, 5, 44);
if (indice.has_value())
    std::cout << "Numero encontrado en indice: "
              << indice.value() << std::endl;
else
    std::cout << "Numero no encontrado" << std::endl;
```

## Funciones como entidades

Una función es una instrucción que puede tomar entradas, realizar una operación específica y producir un resultado, pero eso ya lo sabemos. La parte interesante es que una función se puede pasar como un argumento en otra función y eso es algo muy interesante.

Supongamos que partimos de tres funciones básicas para realizar algunas operaciones aritméticas:

```cpp
#include <iostream>
 
double sumar(double x, double y) { return x + y; }
double restar(double x, double y) { return x - y; }
double producto(double x, double y) { return x * y; }
double dividir(double x, double y) { return x / y; }
```

Ahora queremos crear una **función wrapper** que ejecute nuestras funciones aritméticas pero a su vez muestre algún tipo de información.

La forma esencial de enviar la función como parámetro es **mediante su referencia**, por lo que la trataremos como un puntero, el espacio en la memoria que contiene sus instrucciones:

```cpp
// Paso de función utilizando puntero
double invocar(double (*func)(double, double), double x, double y)
{
    return func(x, y);
}
 
int main()
{
    std::cout << invocar(&sumar, 3.45, 5.3) << std::endl;
    std::cout << invocar(&restar, 3.45, 5.3) << std::endl;
    std::cout << invocar(&producto, 3.45, 5.3) << std::endl;
    std::cout << invocar(&dividir, 3.45, 5.3) << std::endl;
}
```

Desde C++11, otra forma de hacerlo es mediante el uso del template `std::function<>` que permite pasar funciones como objetos. Este objeto se puede crear de la siguiente forma:

```cpp
std::function<return_type(arg1, .., argn)> obj;
return_type var = obj(arg1, ..., argn);
```

En nuestro ejemplo cambiaremos el código de la función invoca de esta forma:

```cpp
#include <functional>
 
// Paso de función utilizando std::function
double invocar(std::function<double(double, double)> func, double x, double y)
{
    return func(x, y);
}
```

También es posible **enviar funciones lambda** (anónimas) a la función `invocar`, el resultado será el mismo:

```cpp
// Paso de una función lambda a una función
std::cout << invocar(
    [](double x, double y) -> double { return x + y; }, // f lambda
    3.45, 5.3) << std::endl;
```

Debemos tener en cuenta que una función anónima está bien si se define pocas veces pero definirla múltiples veces aumentará el tamaño del ejecutable. 

Hablaré en profundidad de las funciones anónimas más adelante.

___
<small class="edited"><i>Última edición: 09 de Mayo de 2022</i></small>