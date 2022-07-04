title: Gestión de la memoria (Stack y Heap) | Apuntes lenguaje C++ | Hektor Profe
description: Gestión de la memoria (Stack y Heap) | Apuntes lenguaje C++

# Gestión de la memoria (Stack y Heap) en C++

Cuando ejecutamos un programa, nuestro sistema operativo le asigna un proceso con algo de memoria, llamada la **memoria virtual**, donde ejecutarse. Esa memoria virtual se divide en segmentos:

![]({{cdn}}/cpp/image-50.png)

* El **segmento de texto**, conocido como segmento de código, contiene las instrucciones ejecutables y es solo de lectura: [https://en.wikipedia.org/wiki/Code_segment](https://en.wikipedia.org/wiki/Code_segment).
* El **segmento de datos** contiene la inicialización de las variables estáticas, globales y estáticas locales: [https://en.wikipedia.org/wiki/Data_segment](https://en.wikipedia.org/wiki/Data_segment).
* El **segmento heap** (montón) contiene memoria reservada dinámicamente por el programador para almacenar variables temporales, se gestiona con las instrucciones `malloc`, `calloc`, `realloc` y `free`. Es un segmento compartido por todos los subprocesos, bibliotecas compartidas y módulos cargados dinámicamente en un proceso: [https://en.wikipedia.org/wiki/Manual_memory_management](https://en.wikipedia.org/wiki/Manual_memory_management).
* El **segmento stack** (pila), ubicado en la parte superior de la memoria, contiene la pila de llamadas (call stack). Se trata de una estructura **LIFO** (último en llegar primero en salir) donde se almacenan los argumentos pasados al programa, las cadenas del entorno, argumentos de las funciones, variables locales no inicializadas, además de almacenar el registro de llamada de funciones y el retorno: [https://en.wikipedia.org/wiki/Stack-based_memory_allocation](https://en.wikipedia.org/wiki/Stack-based_memory_allocation).

## Diferencias entre stack y heap

Los segmentos más interesantes para nosotros son el **montón (heap)** y la **pila (stack)**, así que voy a resumir sus diferencias clave en una tabla:

| Parámetro | Stack (pila) | Heap (montón) |
|----|---|---|
| Estructura de datos | Estructura de datos lineal. | Estructura de datos jerárquica. |
| Velocidad de acceso | Acceso de alta velocidad. | Más lento en comparación con la pila. |
| Gestión del espacio | Es un espacio administrado eficientemente por el sistema operativo para que la memoria nunca se fragmente. | El espacio de pila no se usa de manera tan eficiente. La memoria puede fragmentarse como bloques de memoria asignados y liberados. |
| Acceso | Solo variables locales. | Permite acceder a variables de forma global. |
| Límite de tamaño | El límite depende del sistema operativo. | No tiene un límite específico. |
| Redimensión | Las variables no pueden cambiar de tamaño. | Las variables pueden cambiar de tamaño. |
| Asignación de memoria | La memoria se asigna en un bloque contiguo. | La memoria se asigna en cualquier orden aleatorio. |
| Asignación y desasignación | Se realiza automáticamente mediante instrucciones del compilador. | Lo hace manualmente el programador. |
| Desasignación | No requiere desasignar variables. | Se necesita una desasignación explícita. |
| Coste | Menor. | Mayor. |
| Implementación | Matrices simples, memoria dinámica y basada en listas vinculadas. | Matrices y árboles. |
| Mayor problema | Escasez de memoria. | Fragmentación de la memoria. |
| Localidad de referencia | Instrucciones automáticas en tiempo de compilación. | Adecuado. |
| Flexibilidad | Tamaño fijo. | Redimensionable. |
| Tiempo de acceso | Más rápido. | Más lento. |

## ¿Cuándo utilizar el montón y la pila?

* El **montón (heap)** debe utilizarse cuando se necesita asignar un gran bloque de memoria. Por ejemplo crear una matriz de gran tamaño o una estructura demasiado grande para mantener una variable durante mucho tiempo.

* La **pila (stack)** es mejor utilizarla cuando se trabaja con variables relativamente pequeñas que solo se requieren mientras una función está viva, debido a que provee un acceso más fácil y rápido.

___
<small class="edited"><i>Última edición: 08 de Mayo de 2022</i></small>