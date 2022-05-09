title: Tiempo de ejecución | Apuntes lenguaje C++ | Hektor Profe
description: Tiempo de ejecución | Apuntes lenguaje C++

# Tiempo de ejecución en C++

Mediante la biblioteca `<chrono>` podemos generar dos timestamps, uno de inicio y otro de fin para restar ambos y conseguir el tiempo que ha pasado entre los dos momentos. Esto es muy útil para realizar mediciones de tiempo de ejecución:

```cpp
#include <iostream>
#include <chrono>
 
int main()
{
    // timestamp de inicio
    std::chrono::steady_clock::time_point begin = std::chrono::steady_clock::now();
 
    // 10 millones de iteraciones
    for (int i{0}; i < 10000000; i++);
 
    // timestamp de final
    std::chrono::steady_clock::time_point end = std::chrono::steady_clock::now();
 
    // mostramos el tiempo (milisegundos, nanosegundos, microsegundos...)
    std::cout << "Tiempo: " << std::chrono::duration_cast<std::chrono::milliseconds>(end - begin).count() << "ms" << std::endl;
}
```

___
<small class="edited"><i>Última edición: 09 de Mayo de 2022</i></small>