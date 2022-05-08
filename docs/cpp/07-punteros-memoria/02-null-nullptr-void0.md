title: NULL, nullptr, void* y ((void*)0) | Apuntes lenguaje C++ | Hektor Profe
description: NULL, nullptr, void* y ((void*)0) | Apuntes lenguaje C++

# NULL, nullptr, void* y ((void*)0) en C++

Una vez comienzas a profundizar en el lenguaje C++ empiezas a observar todo tipo de prácticas de lo más extrañas, especialmente cuando tiene que ver con valores nulos, punteros nulos, ceros, etc. Esto tiene que ver con las diferencias entre C y C++.

En C cuando queremos establecer un puntero a un lugar sin datos, es decir, que el puntero existe pero no está inicializado, se le asigna la palabra reservada `NULL`.

El caso es que esta palabra reservada en C es en realidad una macro de `((void*)0)`:

```cpp
#define NULL ((void*)0)
```

Esta pequeña pieza de código es un casting entre un **puntero vacío** `void*` y un número 0 que en la práctica se trata como una especie de constante para un puntero nulo. Un puntero vacío es un puntero que no tiene ningún tipo de dato asociado pero puede contener la dirección a cualquier tipo de dato, además de permitir el casteos entre tipos.

Teniendo esto en cuenta, el puntero nulo `NULL` en C no sería realmente un puntero a la nada (además de que eso no puede existir, ya que la nada no existe no se puede representar formalmente) sino un puntero vacío hacia un 0, algo que se considera un estándar del lenguaje.

Sin embargo en C++ la palabra `NULL` no es un puntero, sino una macro con el número 0:

```cpp
#define NULL 0
```

Esa es la razón por la cuál se puede operar aritméticamente:

```cpp
int n = NULL + 10;
std::cout << n << std::endl;  // 10
```

Esto funcionará aunque el compilador nos dará un warning: `NULL used in arithmetic`.

¿Entonces en C++ como se hace referencia a un puntero a la nada? Pues mediante la palabra reservada `nullptr`, introducida en C++11:

```cpp
int n = nullptr + 10; // error, invalid operands of types
```

Dejando de banda toda esta explicación, la parte que me sigue llamando la atención es la del casteo del puntero `void*` a otros tipos. ¿Qué utilidad puede tener esto?

En C++ no podemos asignar la dirección de una variable de un tipo de dato a un puntero de otro tipo

```cpp
int *ptr;  // puntero entero
double d = 9.0;  // variable double
 
ptr = &d;  // Error, no se puede asignar double* a int*
```

Pues utilizando un puntero vacío podemos hacer el truco:

```cpp
void *ptr;  // puntero vacío
int i = 5;  // int
double d = 9.0;  // double
ptr = &i;  // funciona al asignar un int
ptr = &d;  // funciona al asignar un double
```

Lo malo es que no podemos dereferenciar el puntero para conseguir el valor:

```cpp
std::cout << &ptr << std::endl; // error, undereferenced
```

En su lugar lo que podemos hacer es un cast de puntero nulo `void*` al tipo de puntero del dato que queremos mostrar:

```cpp
ptr = &d;  // asignamos un double
std::cout << *(double *)ptr << std::endl; // cast de void* a double*
```

Utilizando la sintaxis segura con `static_cast` podemos hacer lo mismo así:

```cpp
using namespace std;
std::cout << *(static_cast<double *>(ptr)) << std::endl;
```

Las posibilidades de este lenguaje son enormes.

___
<small class="edited"><i>Última edición: 08 de Mayo de 2022</i></small>