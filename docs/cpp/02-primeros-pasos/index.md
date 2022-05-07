title: Primeros pasos | Apuntes lenguaje C++ | Hektor Profe
description: Repaso de algunos conceptos clave sobre el uso del lenguaje C++.

# Primeros pasos en C++

Breve repaso de algunos conceptos clave sobre el uso de este lenguaje de programación.

## Comentarios en C++

Con el objetivo de que los programadores podamos explicar nuestro propio código existen los comentarios.

En C++ podemos crear bloques de comentarios:

```cpp
/* Bloque 
      de
       comentarios */
```

Y comentarios en línea:

```cpp
// Comentario en una línea
```

No tiene mucho más misterio, solo tener en cuenta que no se debe abusar de ellos y que siempre que se pueda el código debe ser auto explicativo, dejando los comentarios para explicar detalles del funcionamiento.

## Errores y advertencias en C++

Sin entrar todavía en profundidad en el lenguaje, debemos comentar los diferentes tipos de fallos que puede arrojar un código en C++:

* Errores de compilación.
* Errores en tiempo de ejecución.
* Advertencias.

Un `error de compilación` es un fallo en el código que impide que éste se pueda compilar, por ejemplo olvidarnos una instrucción o escribir mal la sintaxis. Estos errores normalmente los detectan los propios editores de código antes de intentar la compilación:

![]({{cdn}}/cpp/image-17.png)

Si intentamos compilar con un error de compilación no nos dejará:

![]({{cdn}}/cpp/image-18.png)

Por otro lado los `errores en tiempo de ejecución` solo se pueden prevenir con experiencia. Como el editor y el compilador no pueden identificarlos, generalmente el programa compilará sin problemas pero ocurrirá algún tipo de malfuncionamiento durante la ejecución.

Por ejemplo cuando tenemos una variable con un cero almacenada en la memoria y la dividimos de otro número (ya veremos lo que es una variable):

![]({{cdn}}/cpp/image-20.png)

En este ejemplo se compila sin ningún error pero al ejecutar el programa éste finaliza súbitamente, algo que podemos deducir pues nunca llega a ejecutarse la línea 8.

Por último las `advertencias` tampoco impiden la compilación pero el compilador sí es capaz de entender que puede ocurrir algo inconsistente. Por ejemplo, si intentamos una división entre cero de forma literal (sin usar una variable) el compilador puede analizar el código fuente, identificar esa situación y lanzarnos un aviso:

![]({{cdn}}/cpp/image-21.png)

## Sentencias y funciones en C++

Seguimos repasando los conceptos básicos del lenguaje C++ antes de entrar de lleno en él.

Como todos los lenguajes de programación, C++ se fundamenta en sentencias que suponen las unidades básicas de computación ejecutables por el procesador. Así mismo un `programa` es una colección de sentencias organizadas de tal manera que permiten lograr un objetivo.

En C++ las sentencias finalizan con un punto coma `;` y se ejecutan por orden de arriba hacia abajo hasta llegar a la última o hasta que una sentencia indica la terminación del programa.

Por otro lado también encontramos `funciones` que son conjuntos o bloques de sentencias identificados con un nombre único y que permiten la reutilización del código, con la excepción de la función `main()` que es el bloque principal del programa y define dónde empieza a ejecutarse.

```cpp
#include <iostream>
 
// void indica que la función devolverá un valor vacío
void saludar()  
{
    std::cout << "Hola!" << std::endl;
}
 
// main es la función principal y se ejecuta automáticamente
int main()  
{
    saludar();
    saludar();
    saludar();
    return 0;
}
```

En este ejemplo podemos observar que para ejecutar una función ésta debe estar definida antes de su llamada.

Las funciones dan mucho juego, profundizaré en ellas más adelante.

## Entradas y salidas en C++

Volvamos a repasar brevemente las funciones de la librería `<iostream>` (Input/Output Stream) que importamos en todos nuestros ejemplos:

* `cin`: Flujo de entrada
* `cout`: Flujo de salida
* `cerr`: Flujo de error no almacenado.
* `clog`: Flujo de error almacenado.
* `endl`: Fin de línea.

Como ya comentamos necesitamos esta librería para controlar el flujo de datos de la terminal, un flujo que no limita solo a la salida sino también a la entrada. En otras palabras, igual que podemos mostrar información por la terminal también podemos leerla.

Para leer un dato por la terminal debemos redirigirlo hacia una variable donde almacenarlo. Profundizaremos en las variables más adelante así que por ahora entendámoslas como un espacio en la memoria identificado con un nombre y que almacena información.

```cpp
#include <iostream>
 
int main()
{
  int numero;  // Variable para un número entero
  std::cout << "Escribe un numero: ";
  std::cin >> numero;
  std::cout << "El numero es " << numero;
  return 0;
}
```

En este código debemos notar varias cosas. En primer lugar la definición de una variable debe ser antes del uso, como es lógico. Luego notamos que el operador de inserción está al revés `>>`, esto indica que la entrada (o lectura) se inserta hacia la variable, mientras que en la salida `<<` se inserta el valor a mostrar en el flujo de salida:

![]({{cdn}}/cpp/image-24.png)

Por cierto, si escribimos en la terminal algo que no sea un número entero fijaros en el resultado:

![]({{cdn}}/cpp/image-25.png)

Este `0` es el valor por defecto que tiene una variable de tipo número entero, por lo que podemos entender que realmente no se ha almacenado nada en ella.

Si quisiéramos leer un texto podemos utilizar el tipo de dato `std::string` (cadena) mediante la función `std::getline` (conseguir línea) que debemos importar de la librería `<string>` de la siguiente forma:

```cpp
#include <iostream>
#include <string>
 
int main()
{
  std::string texto; // variable para una cadena de texto
  std::cout << "Escribe un texto: ";
  std::getline(std::cin, texto);
  std::cout << "El texto es " << texto;
  return 0;
}
```

Cuyo resultado sería el siguiente:

![]({{cdn}}/cpp/image-26.png)

Debemos tener en cuenta que en este punto lo que estamos leyendo es un texto y eso significa que no podemos operarlo matemáticamente, aunque de eso hablaremos cuando profundicemos en las variables y tipos de datos.

## Biblioteca estándar y STL en C++

El lenguaje C++ cuenta con una serie de funcionalidades por defecto conocidas como `características del núcleo` o en inglés `core features`.

Estas características definen lo que podemos realizar con el lenguaje pero pronto nos percataremos de que la mayoría no se encuentran disponibles por defecto, necesitamos cargarlas de la `biblioteca estándar`, una colección de clases y funciones declaradas en el espacio de nombres `std`. En [https://es.cppreference.com/w/cpp/header](https://es.cppreference.com/w/cpp/header) encontraréis una lista de los encabezados disponibles.

A su vez dentro de esta biblioteca encontramos un subconjunto de definiciones muy utilizado conocido como `STL (Standard Template Library)` que contiene diferentes tipos de datos, algoritmos, iteradores, funciones, etc. En [https://es.cppreference.com/w/cpp/container](https://es.cppreference.com/w/cpp/container) encontraréis una lista de los contenedores disponibles.
___
<small class="edited"><i>Última edición: 07 de Mayo de 2022</i></small>