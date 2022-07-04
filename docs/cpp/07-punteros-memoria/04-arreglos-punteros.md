title: Arreglos y punteros | Apuntes lenguaje C++ | Hektor Profe
description: Arreglos y punteros | Apuntes lenguaje C++

# Arreglos y punteros en C++

El nombre de un arreglo puede tratarse como un puntero a la primera posición del arreglo:

```cpp
int numeros[5] = {11, 22, 33, 44, 55};
int *p_numeros{numeros};
 
// Misma direccion de memoria: 0x87405ff6e0 == 0x87405ff6e0
std::cout << numeros << " == " << p_numeros << std::endl;
 
// Mismo contenido del puntero: 11 == 11
std::cout << *numeros << " == " << *p_numeros << std::endl;
 
// Mismo contenido en las posiciones: 33 == 33
std::cout << numeros[2] << " == " << p_numeros[2] << std::endl;
```

Así mismo una diferencia importante es que no es posible conocer la longitud de un puntero a un arreglo, básicamente porque el compilador no sabe donde apunta hasta que no se pone en marcha el programa:

```cpp
std::cout << std::size(numeros) << std::endl;   // Funciona
std::cout << std::size(p_numeros) << std::endl; // No funciona
```

Por último comentar que, si bien es posible, aunque no recomendable; asignar una dirección de memoria a un puntero a un arreglo

```cpp
int numero = 66;
p_numeros = numero; // Funciona pero no es recomendable hacerlo...
```

Esto no es posible con un arreglo en sí mismo, pues aunque también sea un puntero, es un tipo de puntero especial capaz de identificar su longitud (entre otras cosas), razón por la cuál podemos utilizar std::size y conseguir su tamaño:

```cpp
int numero = 66;
numeros = &numeros; // Esto no es posible porque es un puntero 
```

## Intercambio de arreglos con punteros

Un requisito común es el de intercambiar un valor entre dos variables `a` y `b`, donde `a` valga `b` y `b` valga `a`.

Para solucionarlo es muy común definir una variable temporal para «aguantar» una de las variables mientras asignamos el valor a la otra y no perder su valor:

```cpp
int a = 10, b = 5, tmp = 0;
tmp = a;  // aguantamos el dato de "a" temporalmente
a = b;    // asignamos en "a" el valor de "b"
b = tmp;  // asignamos en "b" el valor de "a"
std::cout << a << " " << b << std::endl;
```

Ahora, si en lugar de intercambiar dos variables queremos intercambiar todos los elementos entre dos arreglos, utilizando este sistema, necesitaremos un arreglo temporal con el mismo número de elementos que los arreglos a intercambiar, realizando una escritura secuencial de sus valores para «aguantar» uno de los dos arreglos, luego una segunda escritura secuencial para modificar los valores del primer arreglo y una tercera escritura secuencial para asignar los valores del segundo arreglo:

```cpp
int pares[5] = {1, 3, 5, 7, 9};
int impares[5] = {0, 2, 4, 6, 8};
 
int temporal[5];
 
// Primera pasada para "aguantar" el primer arreglo en temporal
for (size_t i = 0; i < 5; i++)
    temporal[i] = pares[i];
// Segunda pasada para copiar el segundo arreglo en el primero
for (size_t i = 0; i < 5; i++)
    pares[i] = impares[i];
// Tercera pasada para copiar el arreglo temporal en el segundo
for (size_t i = 0; i < 5; i++)
    impares[i] = temporal[i];
```

Si solo son 5 elementos pues tampoco pasa nada, pero si tenemos que realizar esto para miles de números, la cosa se pone fea porque son un montón de instrucciones.

Este problema sería trivial en el caso de utilizar punteros a arreglos

```cpp
int pares[5] = {1, 3, 5, 7, 9};
int impares[5] = {0, 2, 4, 6, 8};
 
// Definimos y guardamos los punteros
int *p_pares = pares;
int *p_impares = impares;
int *p_temporal;
 
// Intercambiamos los punteros y listo
p_temporal = p_pares;
p_pares = p_impares;
p_impares = p_temporal;
```

Sabiendo el número de elementos en los arreglos podemos recorrer sus respectivos punteros intercambiados y trabajar con ellos:

```cpp
std::cout << "Pares: ";
// Pares intercambiados con punteros
for (size_t i = 0; i < 5; i++)
    std::cout << p_pares[i];  // Pares: 02468
std::cout << "\nImpares: ";
// Impares intercambiados con punteros
for (size_t i = 0; i < 5; i++)
    std::cout << p_impares[i];  // Impares: 13579
```

Este ejemplo es ilustrativo de cómo los punteros tienen aplicaciones que los arreglos en sí mismos no ofrecen.

___
<small class="edited"><i>Última edición: 8 de Mayo de 2022</i></small>