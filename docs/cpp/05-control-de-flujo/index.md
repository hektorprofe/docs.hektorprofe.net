title: Control de flujo | Apuntes lenguaje C++ | Hektor Profe
description: Resumen de algunas características del control de flujo en C++.

# Control de flujo en C++

## Cortocircuitado de evaluaciones

Cuando tenemos múltiples condiciones unidades mediante operadores lógicos como `&&` (and) y `||` (or), podemos cortocircuitarlas para ahorrarnos la ejecución de las subsiguientes evaluaciones:

```cpp
// Cortocircuitado de and
if (false && true && true)
{
    // el primer false ya no ejecuta las siguientes comprobaciones
}
 
// Cortocircuitado de or
if (true || false || false)
{
    // el primer true ya no ejecuta las siguientes comprobaciones
}
```

## Inicializadores en if, switch y for

Una funcionalidad que me ha llamado la atención de C++ es que un bloque como `if` en la propia definición permite definir variables locales:

```cpp
if (int num{10}; false) 
```

La condición `switch` también acepta un inicializador:

```cpp
int opcion{5};
switch (int num{10}; opcion)
```

Finalmente, un bucle `for` mediante rangos también permite esta funcionalidad:

```cpp
for (int multiplicador{5}; auto valor : {10, -5, 0, 5, 25})
{
    std::cout << valor * multiplicador << std::endl;
}
```

## Bucles for utilizando arreglos

Un bucle `for` clásico se basa en una definición, una condición y una instrucción de paso para ejecutar un bloque de instrucciones un número determinado de veces:

```cpp
for (unsigned int n = 0; n < 10; n++)
{
    std::cout << n << std::endl;
}
```

Desde C++11 es posible emular un típico `foreach` (de otros lenguajes) para recorrer los elementos de un arreglo, en cuyo caso no necesitamos una condición ni una instrucción de paso:

```cpp
int valores[] = {10, -5, 0, 5, 25};
for (int valor : valores)
{
    std::cout << valor << std::endl;
}
```

Podemos dejar al compilador deducir el tipo de dato del arreglo para que sea más cómodo:

```cpp
for (auto valor : {10, -5, 0, 5, 25})
{
    std::cout << valor << std::endl;
}
```

___
<small class="edited"><i>Última edición: 08 de Mayo de 2022</i></small>