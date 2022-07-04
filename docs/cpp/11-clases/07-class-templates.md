title: Class templates | Apuntes lenguaje C++ | Hektor Profe
description: Class templates | Apuntes lenguaje C++

# Class templates en C++

Como ya sabemos los templates permiten escribir programas genéricos. Una forma de implementarlos es mediante funciones, pero también podemos hacerlo utilizando clases. Con un solo template de clase podemos trabajar con múltiples tipos de datos.

## Declaración de un class template

La estructura básica es la siguiente:

```cpp
template <typename T>
class className
{
private:
    T var;
 
public:
    T functionName(T arg);
};
```

En esta cabecera, `T` es un argumento que substituirá al tipo de dato utilizado. Dentro del cuerpo de la clase, tenemos una variable miembro `var` y una función miembro `functionName`, ambas del tipo `T`.

## Creación de una instancia de class template

Con la anterior estructura podemos crear objetos de diferente tipo utilizando la sintaxis:

```cpp
className<dataType> classObject;
```

Por ejemplo:

```cpp
className<int> classObject;
className<float> classObject;
className<string> classObject;
```

En el siguiente ejemplo vamos a crear una plantilla de clase con un **getter** que nos permitirá mostrar diferentes tipos de datos:

```cpp
#include <iostream>
 
template <typename T>
class Numero
{
private:
    // Variable de tipo T
    T num;
 
public:
    Numero(T n) : num(n) {} // Constructor
 
    T getNum() const
    {
        return num;
    }
};
 
int main()
{
 
    // Creamos un objeto de tipo entero
    Numero<int> numeroInt(4);
 
    // Creamos un objeto de tipo double
    Numero<double> numeroDouble(3.14);
 
    std::cout << "int Numero = " << numeroInt.getNum() << std::endl;
    std::cout << "double Numero = " << numeroDouble.getNum() << std::endl;
 
    return 0;
}
```

## Definición de miembros fuera del template

Si necesitamos separar la declaración y la definición de una función (cabecera y fuente) podemos hacerlo fácilmente:

```cpp
// Declaración de la clase
template <typename T>
class Numero{
    // Prototipo de la función
    T getnum() const;
};
 
// Definición de la función
template <typename T>
T Numero<T>::getNum() const {
    return num;
}
```

En el siguiente ejemplo implementaremos una clase `Calculadora` separando la declaración y la definición, pero esta vez en el mismo fichero de cabeceras `calculadora.h`:

```cpp
#ifndef CALCULADORA_H
#define CALCULADORA_H
 
#include <iostream>
 
// Declaración
template <typename T>
class Calculadora
{
private:
    T num1, num2;
 
public:
    Calculadora(T n1, T n2) : num1(n1), num2(n2){};
    void operaciones();
    T suma();
    T resta();
    T producto();
    T division();
};
 
// Definición
template <typename T>
void Calculadora<T>::operaciones()
{
    std::cout << "Numeros: " << num1 << " y " << num2 << std::endl;
    std::cout << num1 << " + " << num2 << " = " << suma() << std::endl;
    std::cout << num1 << " - " << num2 << " = " << resta() << std::endl;
    std::cout << num1 << " * " << num2 << " = " << producto() << std::endl;
    std::cout << num1 << " / " << num2 << " = " << division() << std::endl;
}
 
template <typename T>
T Calculadora<T>::suma() { return num1 + num2; }
 
template <typename T>
T Calculadora<T>::resta() { return num1 - num2; }
 
template <typename T>
T Calculadora<T>::producto() { return num1 * num2; }
 
template <typename T>
T Calculadora<T>::division() { return num1 / num2; }
 
#endif
```

Para utilizarlo:

```cpp
#include <iostream>
#include "calculadora.h"
 
int main()
{
    Calculadora<int> intCalc(3, 2);
    Calculadora<float> floatCalc(1.6, 2.6);
 
    std::cout << "Operaciones enteras" << std::endl;
    intCalc.operaciones();
 
    std::cout << std::endl
              << "Operaciones flotantes" << std::endl;
    floatCalc.operaciones();
 
    return 0;
}
```

```
Operaciones enteras
Numeros: 3 y 2
3 + 2 = 5
3 - 2 = 1
3 * 2 = 6
3 / 2 = 1
 
Operaciones flotantes
Numeros: 1.6 y 2.6
1.6 + 2.6 = 4.2
1.6 - 2.6 = -1
1.6 * 2.6 = 4.16
1.6 / 2.6 = 0.615385
```

## Templates de clase con múltiples parámetros

En algunas ocasiones quizá necesitamos jugar con tipos distintos de parámetros, en esos casos definiremos diferentes `typename` donde estaría cada tipo distinto de dato. Incluso podemos establecer tipos de datos por defecto:

```cpp
template <typename T, typename U, typename V = int>
class ClassName {
  private:
    T member1;
    U member2;
    V member3;
};
```

En el siguiente ejemplo podemos ver cómo construir objetos con miembros de distintos tipos:

```cpp
#include <iostream>
 
// Template de clase con parámetros múltiples y por defecto
template <typename T, typename U, typename V = char>
class ClassTemplate
{
private:
    T var1;
    U var2;
    V var3;
 
public:
    ClassTemplate(T v1, U v2, V v3) : var1(v1), var2(v2), var3(v3) {}
 
    void print()
    {
        std::cout << "var1 = " << var1 << std::endl;
        std::cout << "var2 = " << var2 << std::endl;
        std::cout << "var3 = " << var3 << std::endl;
    }
};

int main()
{
    // Objeto con int, double y char
    ClassTemplate<int, double> obj1(5, 5.5, 'H');
    std::cout << "Valores obj1" << std::endl;
    obj1.print();
 
    // Objeto con float, char y bool
    ClassTemplate<float, char, bool> obj2(6.3f, 'm', false);
    std::cout << std::boolalpha << "\nValores obj2" << std::endl;
    obj2.print();
    return 0;
}
```

```
Valores obj1
var1 = 5
var2 = 5.5
var3 = H
 
Valores obj2
var1 = 6.3
var2 = m
var3 = false
```

___
<small class="edited"><i>Última edición: 09 de Mayo de 2022</i></small>