title: Manejo de excepciones y errores | Apuntes lenguaje C++ | Hektor Profe
description: Manejo de excepciones y errores | Apuntes lenguaje C++ 

# Manejo de excepciones y errores en C++

En este punto ya conocemos diferentes formas para manejar potenciales problemas:

* `assert`: para hacer aserciones en tiempo de ejecución.
* `static_assert`: para hacer aserciones en tiempo de compilación.
* `std::cout`: para debugear información en momentos concretos.

Sin embargo las excepciones son un mecanismo incorporado en C++ para traer los problemas a la superficie y poder manejarlos para prevenir que un programa finalice por un fallo.

El siguiente código muestra como provocar una excepción y capturarla dentro de un bloque `try-catch`:

```cpp
try {
    throw 0;
}
catch(int ex) 
{
    std::cout << "Excepcion: " << ex << std::endl;
}
```

Cuando se lanza una excepción, el controlador finaliza inmediatamente el bloque `try` y las variables locales son liberadas, sin embargo los punteros se pierden de la memoria:

```cpp
#include <iostream>
 
class Test
{
public:
    Test() = default;
    ~Test() { std::cout << "Destructor" << std::endl; }
};
 
main()
{
    try
    {
        Test *t_ptr = new Test(); // memoria dinámica
        throw 0;
    }
    catch (int ex)
    {
        // El objeto t_ptr se ha perdido y ya no se puede liberar
        std::cout << "Excepcion: " << ex << std::endl;
    }
}
```

El uso de punteros inteligentes solucionará este problema:

```cpp
#include <iostream>
#include <memory>
 
class Test
{
public:
    Test() = default;
    ~Test() { std::cout << "Destructor" << std::endl; }
};
 
main()
{
    try
    {
        std::shared_ptr<Test> t_ptr = std::make_shared<Test>();
        throw 0;
    }
    catch (int ex)
    {
        // El objeto t_ptr se liberara automáticamente
        std::cout << "Excepcion: " << ex << std::endl;
    }
}
```

Las excepciones son necesarias en determinadas circunstancias para prevenir la finalización del código. El ejemplo clásico es una potencial división entre 0, eso siempre provoca que el programa se rompa:

```cpp
#include <iostream>

double division(double a, double b)
{
    return a / b;
}
 
main()
{
    division(10, 0); // Programa finalizado sin previo aviso
}
```

Lanzando una excepción en la función podemos envolverla en un `try-catch` para solucionar el problema:

```cpp
#include <iostream>

double division(double a, double b)
{
    if (b == 0)
        throw 0;
    return a / b;
}
 
main()
{
    try
    {
        division(10, 0); // Excepcion: 0
    }
    catch (int ex)
    {
        std::cout << "Excepcion: " << ex << std::endl;
    }
}
```

Por desgracia la división entre cero es uno de esos casos de excepción no estándar en C++ y no hay manera de capturarlo de forma genérica.

## Bloque catch ellipsis

Las excepciones se pueden encadenar para comprobar diferentes casos, pero también es posible que ocurran errores que no conocemos, para eso podemos encadenar al final del todo un bloque ellipsis `...`:

```cpp
try {
   ...
} catch (const SomeCustomException& e) {
   ...
} catch (const std::bad_alloc& e) {
   ...
} catch (const std::runtime_error& e) {
   // Mostrar diagnóstico de errores genéricos
} catch (const std::exception& e) {
   // Mostrar diagnóstico de alguna excepción genérca
} catch (...) {
   // Respaldo para errores desconocidos, posible relanzamiento
   // u omisión por si el SO puede manejarlo  
}
```

## Finalización y aborto del programa

En C++, si una excepción no se ha capturado en ningún lugar, se llamará la función `std::terminate()` de la biblioteca `<exception>`. Esta función llamará a la función `std:abort()` de `<cstdlib>` y matará el programa.

Podemos configurar esta función a nuestro gusto en caso de necesitarlo por alguna razón:

```cpp
#include <iostream>
#include <exception>
#include <cstdlib>
#include <thread>
#include <chrono>
 
void terminar_programa()
{
    for (int i{3}; i > 0; i--)
    {
        std::cout << "Finalizando programa en " << i << std::endl;
        std::this_thread::sleep_for(std::chrono::seconds(1));
    }
    std::cout << "Programa abortado";
    std::abort();
}
 
main()
{
    // Configuramos la función terminal
    std::set_terminate(&terminar_programa);
 
    // Provocamos una excepción no manejada
    throw;
}
```

## Especificador de método noexcept

Si tenemos una clase y en un método queremos no queremos permitir que ocurra una excepción no capturada, podemos terminar el programa estableciendo el método como `noexcept`:

```cpp
#include <iostream>
#include <exception>
#include <cstdlib>
#include <thread>
#include <chrono>
 
void terminar_programa()
{
    for (int i{3}; i > 0; i--)
    {
        std::cout << "Finalizando programa en " << i << std::endl;
        std::this_thread::sleep_for(std::chrono::seconds(1));
    }
    std::cout << "Programa abortado";
    std::abort();
}
 
class Test
{
public:
    Test() = default;
    void provocar_error() noexcept
    {
        // Un throw en un noexcept finalizará el programa
        throw;
    }
};
 
main()
{
    std::set_terminate(&terminar_programa);
 
    Test t;
    t.provocar_error();
}
```

Por cierto, los destructores de clase tienen un especificador `noexcept` por defecto, eso significa que si intentamos propagar una excepción no controlada en ellos, el programa terminará.

## Excepciones estándar

El módulo `<exceptions>` de la biblioteca estándar incluye una serie de excepciones ya implementadas para su uso, algunas de las más interesante son las siguientes:

* logic_error:
    * `invalid_argument`
    * `length_error`
    * `out_of_range`
* runtime_error:
    * `overflow_error`
    * `underflow_error`
* others:
    * `bad_alloc`
    * `bad_cast`

Una lista mucho más extensa podemos encontrarla en la documentación [https://en.cppreference.com/w/cpp/error/exception](https://en.cppreference.com/w/cpp/error/exception).

Para capturar una excepción estándar lo haremos almacenando la referencia de la `std::exception`, luego podemos sacar información mediante su método `what()`:

```cpp
try {
    // código con un error de excepciones estándar
} catch (std::exception &ex)
    std::cout << "Algo ha fallado: " << ex.what() << std::endl;
}
```

También podemos invocar una excepción estándar mediante su código de referencia:

```cpp
#include <iostream>
 
main()
{
    int index = -1, max_length = 10;
 
    try
    {
        // invocación de una excepción estándar
        if (index < 0 || index > max_length)
        {
            std::string mensaje = "Indice fuera de rango!";
            throw std::out_of_range(mensaje);
        }
    }
    catch (std::exception &ex)
    {
        std::cout << "Error: " << ex.what() << std::endl;
    }
}
```

## Subclase personalizada de excepción estándar

Por último veamos como implementar nuestra propia excepción estándar completa para el error de división entre cero mediante la herencia a partir de la clase base `std::exception`:

```cpp
#include <iostream>
#include <exception>
#include <string>
 
class DivisionEntreCeroException : public std::exception
{
public:
    DivisionEntreCeroException(int a, int b) noexcept : std::exception(), a{a}, b{b} {}
 
    virtual const char *what() const noexcept override
    {
        // return "Division entre cero detectada";
        return (
                std::string("Division entre cero detectada -> ") +
                std::to_string(a).c_str() + 
                std::string("/") +
                std::to_string(b).c_str()
            ).c_str();
 
        // #include <format> en C++20
        // return (std::format("Division entre cero detectada -> {}/{}\n", a, b)).c_str();
    }
 
private:
    int a{}, b{};
};
 
double division(double a, double b)
{
    if (b == 0)
        throw DivisionEntreCeroException(a, b);
    return a / b;
}
 
main()
{
    try
    {
        division(10, 0);
    }
    catch (std::exception &ex)
    {
        std::cout << ex.what() << std::endl;
        // Division entre cero detectada -> 10/0
    }
}
```

___
<small class="edited"><i>Última edición: 09 de Mayo de 2022</i></small>