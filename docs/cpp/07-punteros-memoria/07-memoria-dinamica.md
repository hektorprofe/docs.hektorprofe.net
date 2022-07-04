title: Memoria dinámica (Heap) | Apuntes lenguaje C++ | Hektor Profe
description: Memoria dinámica (Heap) | Apuntes lenguaje C++ 

# Memoria dinámica (Heap) en C++

## Reservar y liberar memoria dinámica

La asignación dinámica de la memoria hace referencia a reservar un espacio en el montón (heap) para almacenar una información. Esta forma requiere el uso de la palabra reservada new para establecer el tamaño deseado del puntero:

```cpp
int *p_numero = new int;  // Espacio reservado dinámicamente
*p_numero = 55;  // Asignación en el espacio dinámico
std::cout << *p_numero << std::endl;  // 55
```

La vida de los datos en el montón (heap) existe mientras el programador no los elimine manualmente de la memoria, por ello cuando no necesitemos más la información deberemos vaciar el espacio utilizando la palabra reservada `delete`, haciendo que el programa devuelva la memoria al sistema operativo:

```cpp
delete p_numero;  // Vaciamos el espacio reservado
```

También se sugiere que una vez vaciado el espacio le asignamos el puntero `nullptr` para indicar en el propio código un reseteo, eso nos indicará visualmente que debemos volver a reservar la memoria antes de utilizar el puntero:

```cpp
p_numero = nullptr;  // Reiniciamos el puntero
```

Por defecto el espacio reservado dinámicamente contiene información aleatoria, pero podemos asignar el valor directamente en la definición:

```cpp
// Reserva con asignación directa
int *p_numero{int(55)};      
int *p_numero = new int(55);
 
// Reserva con asignación uniforme
int *p_numero = new int{55};
int *p_numero{new int{55}};
```

Por cierto, no debemos eliminar un puntero ya vaciado, podría pasar cualquier cosa en la memoria y dejar nuestro programa inservible:

```cpp
// ¡CUIDADO AQUÍ!
delete p_numero;
delete p_numero;
```

En resumen:

```cpp
// Variable en la pila (stack) gestionada automáticamente
int numero = 10;
 
// Puntero reservado dinámicamente en el montón (heap)
int *p_numero = new int(55);
// Debemos vaciar la memoria manualmente
delete p_numero;
// Y recomendablemente asignarle nullptr para dejar un aviso
p_numero = nullptr;
```

## Punteros colgantes (dangling pointers)

Un puntero colgante es un puntero que no apunta a una dirección de memoria válida, por lo que al intentar dereferenciarlo y utilizarlo, resultará en un comportamiento indefinido.

Esto es algo muy malo, pues se pueden generar situaciones imprevistas en el código y posiblemente un error de ejecución que termine con el programa bloqueado.

Hay tres tipos de punteros colgantes:

* Punteros no inicializados.
* Punteros eliminados.
* Múltiples punteros apuntando a la misma dirección de memoria.

```cpp
// Puntero colgante por no inicialización
int *p_numero;  
 
// Puntero colgante por eliminación
delete p_numero;  
 
// Dos punteros con la misma dirección de memoria
int *ptr1 {new int{10}};  
int *ptr2 {ptr1};
// Vaciamos la memoria del primer puntero
delete ptr1; 
 
ptr1; // Puntero colgante por eliminación
ptr2; // Puntero colgante por referencia a un puntero eliminado
```

Para prevenir los punteros colgantes podemos podemos aplicar estas directrices:

* Inicializar siempre los punteros.
* Reiniciar los punteros después de eliminarlos con el valor `nullptr`.
* Comprar que un puntero no es `nullptr` antes de utilizarlo.
* En múltiples punteros con la misma dirección, asegurarnos de que la propiedad esté clara.

```cpp
// Inicialización para evitar un puntero colgante
int *p_numero{new int{55}};  
 
// Reinicio de un puntero eliminado para evitar un puntero colgante
delete p_numero;  
p_numero = nullptr;
 
// Comprobación de un puntero nulo antes de utilizarlo
if (p_numero != nullptr) std::cout << *p_numero << std::endl;
 
// Establecer la jerarquía de punteros maestro-esclavo
int *p_maestro{new int{77}};
int *p_esclavo{p_maestro};
p_maestro = nullptr;
// Solo acceder al valor del esclavo si el maestro es válido
if (p_maestro != nullptr) std::cout << *p_esclavo << std::endl;
```

## Error al reservar la memoria dinámica

De vez en cuando, en raras ocasiones, la reserva de memoria dinámica puede fallar, por ejemplo cuando no hay suficiente memoria disponible.

De forma predeterminada, cuando se utiliza el operador `new` para intentar asignar memoria y la función no puede hacerlo, se produce una excepción `bad_alloc`. Utilizando un bloque `try catch` podemos capturar la excepción y actuar en consecuencia:

```cpp
try {
    int* numeros {new int[100000000000000]};
} catch(std::exception& ex){
    std::cout << "Error al reservar la memoria: " << ex.what() << "\n";
}
```

También es posible utilizar un modificador `nothrow` como argumento para que en lugar de fallar se devuelva un puntero nulo. Esta constante `nothrow` es un valor de tipo `nothrow_t` con el único propósito de no lanzar la excepción `bad_alloc`:

```cpp
int *numeros{new (std::nothrow) int[100000000000000]};
if (numeros != nullptr) 
    std::cout << "Memoria reservada correctamente" << "\n";
else
    std::cout << "Error al reservar la memoria" << "\n";
```

## Pérdidas de memoria (memory leaks)

Un **memory leak** es una situación que puede ocasionar la pérdida del acceso a la memoria que hemos almacenado dinámicamente en el montón (heap).

Por ejemplo, si almacenamos una información en el montón y luego redireccionamos ese puntero a otra variable. En ese caso perderemos el acceso a la información original que seguirá almacenada en la memoria, es decir, habrá ocurrido un memory leak:

```cpp
int *p_numero{new int{66}}; // Reservamos memoria dinámica con un numero
int numero{99};             // Definimos otro número
p_numero = &numero ;        // Si redireccionamos el puntero al número
                            // la dirección con el 66 en el heap sigue
                            // existiendo pero hemos perdido su referencia,
                            // por lo que ha ocurrido un memory leak
```

Esto no ocurre solo al sobreescribir la dirección de una variable en la pila (stack), pasará lo mismo al definir una nueva variable en el montón (heap):

```cpp
int *p_numero{new int{66}}; // Reservamos memoria dinámica
p_numero = new int{99};     // Si redireccionamos el puntero
                            // perderemos la dirección original de 66,
                            // habrá ocurrido un memory leak
```

Debemos prestar mucha atención a esto, sobretodo con las definiciones en bloques, pues fuera de ellos perderemos el acceso al puntero pero el valor seguirá existiendo en la memoria:

```cpp
#include <iostream>

int main()
{
    {
        int *p_numero{new int{66}};  // Reservamos memoria en un bloque
    }
 
    // En este punto fuera del bloque ya no podemos acceder al puntero,
    // si no lo hemos eliminamos antes ocurrirá un memory leak
}
```

Recordad siempre eliminar y reiniciar la memoria para garantizar espacio al sistema:

```cpp
#include <iostream>

int main()
{
    {
        int *p_numero{new int{66}};
 
        delete p_numero;     // Borrado
        p_numero = nullptr;  // Y reinicio
    }
}
```

## Arreglos almacenados dinámicamente

Se trata de arreglos que se reservan en el montón (heap) mediante el operador `new`. Permiten el uso de la constante `std::nothrow` para evitar el error en caso de no disponer de la memoria requerida.

Podemos definir estos arreglos de distintas formas:

```cpp
// Definimos un tamaño para el arreglo
size_t size{10};
 
// Inicialización con sobrecarga creciente (los valores son basura)
int *p_numeros = new (std::nothrow) int[size];
 
// Inicialización con sobrecarga no arrojadiza (los valores son 0)
int *p_numeros = new (std::nothrow) int[size]{};
 
// Inicialización con asignación parcial (los demás valores son 0)
int *p_numeros = new (std::nothrow) int[size]{11, 22, 33, 44, 55};
```

Recordemos que mediante `std::nothrow` el puntero será `nullptr` en caso de no haber reservado la memoria correctamente, podemos comprobarlo directamente sin la igualdad, ya que se tomará como `0`:

```cpp
if (p_numeros) {
    // Si no es un puntero nulo podemos utilizarlo sin problema
}
```

Para liberar la memoria de un arreglo dinámico debemos especificar los corchetes:

```cpp
delete[] p_numeros;
p_numeros = nullptr;
```

Por último recordemos que estos arreglos al ser punteros no permiten la sintaxis del `for` con elementos porque no almacenan propiedades internas como su longitud:

```cpp
for(int numero : p_numeros) { }  // esto no funcionará
```

En su lugar deberemos recorrerlos mediante índices o con la aritmética de punteros mediante la suma de posición con un clásico `for` a partir de la longitud almacenada anteriormente:

```cpp
for (int i = 0; i < size; i++)
{
    std::cout << p_numeros[i] << std::endl;      // índices
    std::cout << *(p_numeros + i) << std::endl;  // aritmética
}
```

___
<small class="edited"><i>Última edición: 08 de Mayo de 2022</i></small>