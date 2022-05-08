title: Arreglos de datos clásicos | Apuntes lenguaje C++ | Hektor Profe
description: Resumen sobre el manejo de arrays en C++.

# Arreglos de datos clásicos en C++

## Definición y acceso sencuencial de arreglos

Un arreglo o array es una estructura que sirve para almacenar una sucesión de datos del mismo tipo, siendo por tanto homogénea y finita:

```cpp
int numeros[]{2, 5, 8, 2, 5, 6, 9, 10, 1, 3};
```

La lectura secuencial se puede realizar fácilmente mediante bucles `for`, ya sea con índices:

```cpp
for (size_t i{0}; i < 10; i++)
{
    std::cout << numeros[i] << std::endl;
}
```

También podemos utilizar `std::size` para detectar el número de elementos automáticamente:

```cpp
for (size_t i = 0; i < std::size(numeros); i++)
{
    std::cout << numeros[i] << std::endl;
}
```

Rizando el rizo podemos sacar este número dividiendo el tamaño en bytes del arreglo entre el tamaño en bytes del tipo de dato de la primera posición:

```cpp
size_t size{sizeof(numeros) / sizeof(numeros[0])};
for (size_t i = 0; i < size ; i++)
{
    std::cout << numeros[i] << std::endl;
}
```

Otra forma de recorrer el arreglo es mediante el acceso a los elementos del rango:

```cpp
for (int numero : numeros)
{
    std::cout << numero << std::endl;
}
```

Por cierto, nunca debemos asignar valores fuera del arreglo. Esto es curioso porque C++ nos permitirá hacerlo y lo que ocurrirá es que estaremos accediendo a una posición de memoria cualquiera, lo que conllevaría en el peor de los casos, si almacenamos una información, a destruir lo que haya y hacer que el programa deje de funcionar debido a la corrupción de datos:

```cpp
numeros[100] = 999;  // NO ESCRIBIR FUERA DE LOS LÍMITES
```

## Arreglos multidimensionales y acceso secuencial

Un arreglo multidimensional es un arreglo con otros arreglos anidados, de manera que se crea una estructura con múltiples dimensiones.

La forma de trabajar con N dimensiones es mediante N índices para representar el acceso a cada nivel, como en este ejemplo sencillo:

```cpp
// tabla de números 3x3 con 9 elementos
int tabla[3][3]{
    {0, 0, 0}, // primera fila
    {1, 1, 1}, // segunda fila
    {2, 2, 2}  // tercera fila
};
```

La lectura podemos realizar cómodamente con diferentes índices y detectando la longitud de cada dimensión con `std::size`:

```cpp
for (size_t i = 0; i < std::size(tabla); i++)
{
    for (size_t j = 0; j < std::size(tabla[j]); j++)
    {
        std::cout << tabla[i][j] << " ";
    }
    std::cout << std::endl;
}
```

```
0 0 0
1 1 1
2 2 2
```

Como curiosidad, podemos almacenar múltiples caracteres en un arreglo multidimensional de caracteres de manera que podamos almacenar cadenas de caracteres, pues no son más que arreglos de caracteres:

```cpp
// Arreglo de caracteres con 10 posibles caracteres por elemento
char textos[][10]{
    {"Hola"},   // primera cadena
    {"Adios"},  // segunda cadena
    {"Que tal"} // tercera cadena
};
```

Como `std::cout` imprime todos los elementos de un arreglo de caracteres como un único elemento podemos imprimir los textos fácilmente:

```cpp
for (size_t i = 0; i < std::size(frases); i++)
{
    std::cout << frases[i] << std::endl;
}
```

```
Hola
Adios
Que tal
```

___
<small class="edited"><i>Última edición: 08 de Mayo de 2022</i></small>