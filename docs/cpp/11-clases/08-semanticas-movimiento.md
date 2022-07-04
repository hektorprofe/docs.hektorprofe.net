title: Semánticas de movimiento | Apuntes lenguaje C++ | Hektor Profe
description: Semánticas de movimiento | Apuntes lenguaje C++

# Semánticas de movimiento en C++

A pesar de que C++ moderno puede desarrollar aplicaciones muy rápidas y eficientes, durante muchos años, una de sus debilidades fue la creación de objetos temporales. 

El estándar C++98 definió algunas técnicas de optimización del compilador, como **Copy Elision** y **Return Value Optimization**, que resolvieron parcialmente este problema, pero el verdadero cambio fue la semántica de movimiento introducida en C++11.

## Semánticas de movimiento

Para entender las semánticas de movimiento primero echemos un vistazo a la semántica de copia. En general todas las clases de C++ pueden copiarse mediante uno de estos tres métodos:

**Copia de constructor**

```cpp
T t1;
T t2(t1);
```

**Copia con operador de asignación**

```cpp
T t1, t2;
t2 = t1;
```

**Movimiento de constructor (C++11)**

```cpp
T t1;
T t2(std::move(t1));
```

**Movimiento con operador de asignación (C++11)**

```cpp
T t1, t2;
t2 = std::move(t1);
```

En general las semánticas nos permiten tomar un objeto del contexto actual y pasarlo a otro, evitando la copia del original cuando éste no sigue siendo necesario. Si queremos mover objetos, necesitamos utilizar la función `std::move`.

Cabe mencionar dos cuestiones relacionadas con los anteriores ejemplos:

* ¿Qué ocurre con la variable `t1` después del movimiento? De acuerdo con el funcionamiento estándar de una variable en C++, después de moverla será válida pero no tendrá un estado específico. Eso significa que solo puede ejecutar operaciones que no necesiten precondiciones (como asignarle un `new object`).
* ¿Cómo funciona `std::move`? Pues la verdad es que esta función no mueve nada. Para saber qué sucede realmente debemos aprender qué son los `l` (left) y `r` (right) `values`.

## Lvalues y rvalues

En C++, a diferencia de C, una variable puede declararse como una referencia. Antes de C++11 una referencia podía apuntar únicamente a un `lvalue` (algo cuya dirección se puede tomar).

```cpp
int counter = 10;
int &counterRef = counter;
```

Desde C++11 la referencia puede apuntar al `lvalue` o al `rvalue`. La referencia `rvalue` es básicamente una referencia a un objeto temporal (el lado derecho de una expresión de asignación):

```cpp
int &&counterRef = 10;
```

## Referencia rvalue en las semánticas de movimiento

Como he mencionado anteriormente, hay 4 formas de copiar/mover. Sus declaraciones son las siguientes:

```cpp
Class Punto
{
    //Copia de constructor
    Punto(const Punto &punto);
 
    // Copia con operador de asignación
    Punto &operator=(const Punto &punto);
 
    // Movimiento de constructor 
    Punto(Punto &&punto);
 
    // Movimiento con operador de asignación
    Punto &operator=(Punto &&punto);
}
```

Como podemos observar, las operaciones de copia toman la referencia `lvalue` mientras que las operaciones de movimiento toman la referencia `rvalue`, por lo que el objeto se copia o se mueve dependiendo del tipo de referencia. Esto es precisamente lo que hace `std::move`, convertir la referencia `lvalue` en la referencia `rvalue`.

## Cuando utilizar semánticas de movimiento

Cuando un método toma un `rvalue` como parámetro, podemos pasar la referencia `rvalue` (la referencia temporal del objeto) y también el objeto temporal en sí: `100`, `temp`, `Punto()`.

Es una buena práctica crear sobrecargas de los métodos tomando `lvalues` y `rvalues`, como por ejemplo implementan algunos de los contenedores STL en el método `push_back()`:

```cpp
void push_back(const T &obj);
void push_back(T &&obj);
```

Nos permite crear copias (si el objeto todavía se necesita en ese contexto) o moverlo (si ya no se necesita):

```cpp
std::vector<Punto> puntos;
Punto p1, p2;
 
puntos.push_back(punto1);            // lvalue
puntos.push_back(std::move(punto2)); // rvalue
```

Este es el uso típico de las semánticas de movimiento.

## Cuando no utilizar semánticas de movimiento

Un error común es utilizar `std::move` cuando la variable local es retornada por una función:

```cpp
std::vector<int> getNumeros()
{
    std::vector<int> numeros = {1,2,3};
    return std::move(numeros);
}
 
auto numeros = getNumeros();
```

En este caso se crean 2 objetos:

1. La variable local `numeros` dentro de la función `getNumeros` (objeto temporal).
2. El objeto del lado izquierdo donde se llama `getNumeros`, este objeto el cual se crea mediante el constructor `std::move`.

El problema aquí es que el compilador por defecto utiliza una técnica de optimización llamada **RVO** (Optimización del Valor de Retorno), con el objetivo de evitar copias en objetos temporales.

Si borramos `std::move` del código, sin **RVO** se crean en su lugar 3 objetos:

```cpp
std::vector<int> getNumeros()
{
    std::vector<int> numeros = {1,2,3};
    return numeros;
}
 
auto numeros = getNumeros();
```

1. La variable local `numeros` dentro de la función `getNumeros` (objeto temporal).
2. El objeto del lado derecho donde se llama `getNumeros` (objeto temporal).
3. El objeto del lado izquierdo donde se llama `getNumeros`.

Con **RVO** solo se creará 1 objeto:

```cpp
std::vector<int> getNumeros()
{
    return std::vector<int>{1, 2, 3};
}
 
auto numeros = getNumeros();
```

## En conclusión

!!! hint ""
    Las semánticas de movimiento son una poderosa técnica para ayudarnos a evitar copias innecesarias, pero para sacar el máximo provecho debemos recordar que los compiladores modernos optimizan el código en algunos casos y pueden hacerlo mejor que utilizar `std::move`.

___
<small class="edited"><i>Última edición: 09 de Mayo de 2022</i></small>