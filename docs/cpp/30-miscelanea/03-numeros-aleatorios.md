title: Números aleatorios | Apuntes lenguaje C++ | Hektor Profe
description: Números aleatorios | Apuntes lenguaje C++

# Números aleatorios en C++

Un tema interesante es el de la generación de números aleatorios, o mejor dicho pseudoaleatorios.

Para generar números pseudoaleatorios, la computadora usará una **semilla** (seed) y le aplicará transformaciones matemáticas, convirtiéndola en otro número. Este nuevo número se convierte en la próxima semilla para el generador de números aleatorios. Mientras el programa seleccione una semilla diferente en cada ejecución, (a todos los efectos prácticos) nunca obtendrá la misma secuencia de números aleatorios. Lo que significa que si se utiliza la misma semilla, la secuencia aleatoria se repetirá.

Las transformaciones matemáticas utilizadas se seleccionan cuidadosamente para que todos los números generados aparezcan con la misma frecuencia y no muestren patrones obvios.

```cpp
#include <cstdlib>  // biblioteca de propósito general de C
#include <ctime>    // biblioteca de tiempo de C
#include <iostream>
 
int main ()
{ 
    std::srand( std::time(nullptr));  // usamos de semilla la hora
    std::cout << std::rand() << std::endl;  // generamos un número aleatorio
} 
```

La función `time` devuelve la cantidad de segundos desde el 1 de enero de 1970. Esta convención proviene del sistema operativo Unix y, a veces, se denomina tiempo Unix. En la mayoría de los casos, la hora se almacena en un entero de 32 bits con signo.

Podemos conseguir un número aleatorio en un rango mediante el siguiente algoritmo:

```cpp
std::srand( std::time(nullptr));  // generamos una semilla
 
int min = 0, max = 10;  // definimos un mínimo y un máximo
int num = rand() % (max - min) + min;  // aplicamos este módulo
std::cout << num  << std::endl;
```

Establecer **la misma semilla generará siempre el mismo resultado**:

```cpp
int min = 0, max = 10;
 
std::srand(9999);
std::cout << rand() % (max - min) + min << std::endl;
 
std::srand(9999);
std::cout << rand() % (max - min) + min << std::endl;
 
std::srand(9999);
std::cout << rand() % (max - min) + min << std::endl;
```

Documentación: [https://es.cppreference.com/w/cpp/numeric/random/rand](https://es.cppreference.com/w/cpp/numeric/random/rand)

___
<small class="edited"><i>Última edición: 09 de Mayo de 2022</i></small>