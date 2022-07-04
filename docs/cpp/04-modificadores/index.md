title: Modificadores y especificadores | Apuntes lenguaje C++ | Hektor Profe
description: Repaso a los modificadores y especificadores basicos de C++. 

# Modificadores y especificadores en C++

## Formateo de salida

En estas tablas se encuentra un resumen de las funciones que modifican la salida del buffer de texto para realizar diferentes tareas en la información:

![]({{cdn}}/cpp/image-45.png)

![]({{cdn}}/cpp/image-46.png)

Referencia de las funciones: [https://es.cppreference.com/w/cpp/io/manip](https://es.cppreference.com/w/cpp/io/manip)

## Límites numéricos

Nos permiten saber el mínimo y máximo representado en un tipo numérico:

```cpp
#include <iostream>
#include <limits>
 
int main()
{
    std::cout << "Short is from "
              << std::numeric_limits<short>::min() << " to "
              << std::numeric_limits<short>::max() << std::endl;
 
    std::cout << "Unsigned short is from "
              << std::numeric_limits<unsigned short>::min() << " to "
              << std::numeric_limits<unsigned short>::max() << std::endl;
 
    std::cout << "Int is from "
              << std::numeric_limits<int>::min() << " to "
              << std::numeric_limits<int>::max() << std::endl;
 
    std::cout << "Unsigned int is from "
              << std::numeric_limits<unsigned int>::min() << " to "
              << std::numeric_limits<unsigned int>::max() << std::endl;
 
    std::cout << "Long is from "
              << std::numeric_limits<long>::min() << " to "
              << std::numeric_limits<long>::max() << std::endl;
 
    std::cout << "Float is from "
              << std::numeric_limits<float>::min() << " to "
              << std::numeric_limits<float>::max() << std::endl;
 
    std::cout << "Lowest float is from "
              << std::numeric_limits<float>::lowest() << " to "
              << std::numeric_limits<float>::max() << std::endl;
 
    std::cout << "Lowest double is from "
              << std::numeric_limits<double>::lowest() << " to "
              << std::numeric_limits<double>::max() << std::endl;
 
    std::cout << "Lowest for long double is from "
              << std::numeric_limits<long double>::lowest() << " to "
              << std::numeric_limits<long double>::max() << std::endl;
 
    return 0;
}
```

```
Short is from -32768 to 32767
Unsigned short is from 0 to 65535
Int is from -2147483648 to 2147483647
Unsigned int is from 0 to 4294967295
Long is from -2147483648 to 2147483647
Float is from 1.17549e-38 to 3.40282e+38
Lowest for float is from -3.40282e+38 to 3.40282e+38
Lowest for double is from -1.79769e+308 to 1.79769e+308
Lowest for long double is from -1.18973e+4932 to 1.18973e+4932
```

Más información: [https://es.cppreference.com/w/cpp/types/numeric_limits](https://es.cppreference.com/w/cpp/types/numeric_limits)

## Operaciones aritméticas en tipos integrales menores de 4 bytes

Quiero documentar este caso porque me ha llamado la atención.

En C++ los tipos menores de 4 bytes como `char` y `short int` no soportan operaciones aritméticas, sus tamaños son 1 y 2 bytes respectivamente:

```cpp
short int num1{10}, num2{20};
short int res{num1 + num2}; // Error
```

Pero si intentamos mostrar directamente la suma de ambos sí funcionará:

```cpp
short int num1{10}, num2{20};
std::cout << num1 + num2 << std::endl;
```

¿Por qué funciona? Debido a la deducción automática del sistema al encontrar el tipo literal de salida:

```cpp
short int num1{10}, num2{20};
auto res{num1 + num2};  // se deduce un tipo int
std::cout << res << std::endl;
```

¿Pero por qué no podemos operar tipos menores de 4 bytes?

Esto no es una característica del lenguaje sino una limitación de las arquitecturas de los procesadores que ejecutan el código. El tipo entero en C suele tener el tamaño estándar del registro de la CPU. Más silicio ocupa más espacio y más potencia, por lo que en muchos casos la aritmética solo se puede hacer en los tipos de datos de «tamaño natural». Aunque esto no es cierto en todos los casos, muchas arquitecturas todavía tienen esta limitación.

Para una discusión completa sobre el tema: [https://stackoverflow.com/a/24372323](https://stackoverflow.com/a/24372323)

## Literales, constantes, expresiones e inicializaciones constantes

Hablemos un poco de sobre los datos y su representación.

En primer lugar se conoce como un valor **literal** a un dato que no se encuentra almacenado en una variable pero se utiliza en el código:

```cpp
std::cout << 1000 << std::endl;  // literal entero 1000
```

Un valor literal ocupa la memoria en tiempo de ejecución del programa.

Por otro lado una **constante** `const` es una variable con un valor fijo definido antes o durante la ejecución del programa. Se trata como una variable regular con la única excepción de que su valor no se puede cambiar:


```cpp
const int x{5};
x = 10;  // error de compilación
```

Una constante puede ser definida tanto en tiempo de compilación como ejecución:

```cpp
/* constante en tiempo de compilación*/
const double mase_base { 10.5 };
 
/* constante en tiempo de ejecución */
double masa;
std::cin >> masa;  // lectura del valor constante
const double mase_base { masa };
```

Una constante en tiempo de compilación siempre será más rápida de gestionar que en tiempo de ejecución, pero a su vez es menos flexible.

En cualquier caso también encontramos dos especificadores que extienden las definiciones constantes.

Una **expresión constante** `constexpr` sirve para declarar que es posible evaluar una función o variable en tiempo de compilación. Obviamente estamos hablando de valores constantes evaluados en compilación cuyo valor no se puede modificar:

```cpp
const int alto{5}, ancho{10};
constexpr int area{alto * ancho};  // esto funcionará
 
int alto{5}, ancho{10};
constexpr int area{alto * ancho};  // esto no funcionará
```

El segundo ejemplo no funcionará porque una variable no constante puede cambiar su valor, implicando que el valor de la expresión constante cambiase con ello, así que no dejará compilarlo.

Por último desde C++20 también es posible declarar **inicializaciones constantes** `constinit` cuyas variables sí pueden modificarse:


```cpp
#include <iostream>
 
constinit int num{100};  // definición en tiempo de ejecución
 
int main()
{
    std::cout << num << std::endl;  // inicialmente siempre vale 100
 
    num = 200;  // podemos modificar la variable
    std::cout << num << std::endl;
 
    return 0;
}
```

También podemos inicializar a partir de una constante o una expresión constante:


```cpp
const int CIEN{100};
constinit int num{CIEN}; // funcionará
 
constexpr int CIEN{100};
constinit int num{CIEN}; // funcionará
 
int CIEN{100};
constinit int num{CIEN}; // no funcionará
```

Para más información aquí dejo la respectiva documentación:

* `const` [https://en.cppreference.com/book/intro/constants](https://en.cppreference.com/book/intro/constants)
* `constexpr` [https://es.cppreference.com/w/cpp/language/constexpr](https://es.cppreference.com/w/cpp/language/constexpr)
* `constinit` [https://es.cppreference.com/w/cpp/language/constinit](https://es.cppreference.com/w/cpp/language/constinit)

___
<small class="edited"><i>Última edición: 08 de Mayo de 2022</i></small>