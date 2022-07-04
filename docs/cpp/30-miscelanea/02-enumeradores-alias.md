title: Enumeradores y alias | Apuntes lenguaje C++ | Hektor Profe
description: Enumeradores y alias | Apuntes lenguaje C++

# Enumeradores y alias en C++

## Clases enumeradoras

En ocasiones quizá necesitaremos identificar una serie de valores estáticos utilizando nombres. Para esas ocasiones podemos utilizar una clase enumeradora, un tipo de dato que otorgará un valor entero de fondo a los valores nombrados que necesitemos manejar y que podemos consultar mediante un casting:

```cpp
enum class Mes
{
    Enero,      // 0
    Febrero,    // 1
    Marzo,      // 2
    Abril,      // 3
    Mayo,       // 4
    Junio,      // 5
    Julio,      // 6
    Agosto,     // 7
    Septiembre, // 8
    Octubre,    // 9
    Noviembre,  // 10
    Diciembre   // 11
};
 
Mes mes{Mes::Mayo};
std::cout << "Mayo -> " << static_cast<int>(mes) << std::endl;
```

Son especialmente útiles para utilizar en conjunto con condiciones `switch-case`, de hecho una práctica común es crear una función para devolver la representación textual en caso de necesitarlo:

```cpp
std::string_view mes_a_cadena(Mes mes)
{
    using enum Mes;
    switch (mes)
    {
    case Enero:
        return "Enero";
    case Febrero:
        return "Febrero";
    case Marzo:
        return "Marzo";
    case Abril:
        return "Abril";
    case Mayo:
        return "Mayo";
    case Junio:
        return "Junio";
    case Julio:
        return "Julio";
    case Agosto:
        return "Agosto";
    case Septiembre:
        return "Septiembre";
    case Octubre:
        return "Octubre";
    case Noviembre:
        return "Noviembre";
    case Diciembre:
        return "Diciembre";
    default:
        return "None";
    }
}
 
Mes mes{Mes::Mayo};
std::cout << mes_a_cadena(mes) << std::endl; // Mayo
```

!!! hint "Enumeradores clásicos"
    Antes de C++11 se utilizaban enumeradores clásicos (sin clases), pero no se recomiendan porque implican una transformación implícita a entero. Si bien ésta puede ser útil en algunos casos, introduce problemas para poder comparar diferentes enumeradores entre ellos.

## Alias de tipo

Dejando de banda los enumeradores, otra utilidad de C++ son los **alias de tipo** (type alias), una especie de accesos rápidos que podemos crear para ahorrarnos escribir algo de código.

Por ejemplo, si deseamos definir un tipo de dato tedioso como `unsigned long long int`, podemos definir un alias para este tipo y ahorrarnos escribirlo todo el rato para definir nuevas variables:

```cpp
using SuperEntero = unsigned long long int;
SuperEntero numero{99999999999999999};
 
std::cout << sizeof(unsigned long long int) << std::endl; // 8
std::cout << sizeof(SuperEntero) << std::endl;            // 8
std::cout << sizeof(numero) << std::endl;                 // 8
```

___
<small class="edited"><i>Última edición: 09 de Mayo de 2022</i></small>