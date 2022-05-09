title: Espacio de nombres | Apuntes lenguaje C++ | Hektor Profe
description: Espacio de nombres | Apuntes lenguaje C++

# Espacio de nombres en C++

Los espacios de nombres son una facilidad de C++ para evitar conflictos de nombres en las declaraciones/deficiniones.

Como es lógico no podemos definir dos veces la misma función:

```cpp
#include <iostream>
 
void mensaje()
{
    std::cout << "Hola bonito mundo" << std::endl;
}
 
// Error, previously defined
void mensaje()
{
    std::cout << "Adios mundo cruel" << std::endl;
}
 
int main()
{
    mensaje();
    return 0;
}
```

Lo que podemos hacer, si realmente necesitamos el mismo nombre para realizar una tarea distinta, es definir las funciones en espacios de nombres diferentes:

```cpp
#include <iostream>
 
void mensaje()
{
    std::cout << "Hola mundo generico" << std::endl;
}
 
namespace hola
{
    void mensaje()
    {
        std::cout << "Hola bonito mundo" << std::endl;
    }
 
}
 
namespace adios
{
    void mensaje()
    {
        std::cout << "Adios mundo cruel" << std::endl;
    }
}
 
int main()
{
    mensaje();        // Hola mundo generico
    hola::mensaje();  // Hola bonito mundo
    adios::mensaje(); // Adios mundo cruel
    return 0;
}
```

Podemos incluir los nombres de espacio antes de los usos, pero debemos tener en cuenta que no se pueden desactivar una vez están en uso, por ejemplo `std`, aunque este no se recomienda por la gran cantidad de funciones que incluye:

```cpp
#include <iostream>
 
using namespace std;
 
int main()
{
    cout << "Hola mundo!" << endl; // Hola mundo!
    return 0;
}
```

Otra forma de conseguir lo anterior es incluir las declaraciones en lugar del `namespace`:

```cpp
#include <iostream>
 
using std::cout;
using std::endl;
 
int main()
{
    cout << "Hola mundo!" << endl; // Hola mundo!
    return 0;
}
```

Cabe comentar que podemos definir el mismo `namespace` en distintos ficheros, pero no es buena práctica hacer importarlos en ficheros de cabeceras debido a que pueden generar recursividad en las importaciones.

Otra posibilidad, aunque a priori no se me ocurre alguna utilidad, es anidar espacios de nombres:

```cpp
#include <iostream>
 
namespace Hola
{
    namespace Mundo
    {
        void saludar()
        {
            std::cout << "Hola mundo!" << std::endl;
        }
    }
}
 
int main()
{
    Hola::Mundo::saludar(); // Hola mundo!
    return 0;
}
```

Como esto sería algo tedioso es posible definir un alias para facilitar la llamada:

```cpp
int main()
{
    namespace HM = Hola::Mundo;
    HM::saludar(); // Hola mundo!
    return 0;
}
```

Una lista completa de lo que incluye el `namespace` de la biblioteca estándar se puede encontrar en [https://en.cppreference.com/w/cpp/header](https://en.cppreference.com/w/cpp/header).

___
<small class="edited"><i>Última edición: 09 de Mayo de 2022</i></small>