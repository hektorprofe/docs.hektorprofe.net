title: Funciones Inline (en línea) | Apuntes lenguaje C++ | Hektor Profe
description: Funciones Inline (en línea) | Apuntes lenguaje C++

# Funciones Inline (en línea) en C++

Las funciones en línea son funciones que se expanden en el código en lugar de sobrecalentar la llamada, es decir, se copian directamente en la ejecución del código en lugar de llamarse desde un lugar de la memoria.

En algunas ocasiones, cuando una función es muy sencilla, el proceso de llamarla de la memoria es más costoso que tenerla simplemente definida en el propio código.

Por ejemplo esta función `inline` y su llamada:

```cpp
inline int sumar(int a, int b){ return a+b; }
std::cout << sumar(10, 5) << std::endl;
```

A efectos prácticos sería equivalente a insertar directamente la función en el código y llamarla, esta sería una interpretación equivalente:

```cpp
std::cout << [](int a, int b) { return (a + b); }(10, 5) << std::endl;
```

Esto tiene sus pros y sus contras, pues al final se está generando una copia de la función ejecutada y cuando se llama múltiples veces el tamaño del binario aumentará equitativamente.

En resumen, debemos tener en cuenta los siguientes puntos:

* Las funciones en línea pueden incrementar el tamaño del programa compilado.
* Se recomiendan únicamente para funciones pequeñas de uso frecuente.
* El programador debe valorar los beneficios e inconvenientes de su uso.
* Marcar una función en línea es una sugerencia para el compilador, pero él puede ignorar esa sugerencia en función de sus propias consideraciones.

___
<small class="edited"><i>Última edición: 09 de Mayo de 2022</i></small>