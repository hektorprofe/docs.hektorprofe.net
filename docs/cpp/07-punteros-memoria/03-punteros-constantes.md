title: Punteros constantes y a constantes | Apuntes lenguaje C++ | Hektor Profe
description: Punteros constantes y a constantes | Apuntes lenguaje C++

# Punteros constantes y a constantes en C++

Aunque el título parece un juego de palabras, hay una gran diferencia entre estos conceptos así que vamos a explorarlos más a fondo.

Lo primero que debemos recordar es que un  **puntero** permite trabajar tanto su dirección en la memoria como el valor que la posición almacena:

```cpp
int *p_numero{nullptr};
int numero{1000};
 
// cambiamos el valor a partir de la direccion de memoria
p_numero = &numero;
std::cout << *p_numero << std::endl; // 1000
 
// luego podemos asignar un valor a la direccion memoria
*p_numero = 200;
std::cout << *p_numero << std::endl; // 200
```

## Puntero a valor constante

Ahora bien, si es un puntero a un valor constante, no podremos modificar el valor directamente pero sí podremos cambiarlo mediante la dirección de memoria:

```cpp
int numero{1000};
const int *p_numero{&numero};  // puntero a un dato constante
 
*p_numero = 200;  // Error: este puntero es solo de lectura
 
int numero2{2000};
p_numero = &numero2;  // cambiar la memoria sí funcionará
std::cout << *p_numero << std::endl; // 200
```

De la misma forma, si modificamos el valor original de la variable también podremos cambiar el valor al que apunta el puntero:

```cpp
int numero{1000};
const int *p_numero{&numero};  // puntero a un dato constante
 
numero = 3000;  // cambiar el valor original funcionará
std::cout << *p_numero << std::endl; // 3000
```

Podemos entenderlo como que const se aplica al nombre de la variable. De hecho, no podemos crear un puntero no constante a una variable constante:

```cpp
const int numero{1000}; // variable constante
int *p_numero{&numero}; // error, se requiere un puntero a un dato constante
const int *p_numero{&numero};  // si es constante sí funcionará
```

## Puntero constante

Ahora bien, ¿y si queremos que un puntero sea constante? Es decir, que su dirección de memoria no pueda cambiar. Entonces debemos indicar const delante del nombre del puntero y no del tipo de dato:

```cpp
int numero{1000};
int *const p_numero{&numero}; // puntero constante a variable no constante
```

En este caso la dirección de memoria es inalterable pero el valor se puede cambiar:

## Puntero constante a valor constante

Y esto nos lleva a una última posibilidad, un puntero constante a un valor constante, cuya dirección y valor sean inalterables:

```cpp
int numero{1000};
const int *const p_numero{&numero}; // puntero constante a variable no constante
 
int numero2{2000};
p_numero = &numero2; // Error, no se puede cambiar su dirección de memoria
*p_numero = numero2; // Error, tampoco es posible cambiar su valor
```

## Resumen de tipos

* Puntero (dirección modificable y valor modificable): 

    `<tipo> *puntero { &variable }`

* Puntero a constante (dirección modificable y valor no modificable): 
    
    `const <tipo> *puntero { &variable }`

* Puntero constante (dirección no modificable y valor modificable): 
    
    `<tipo> *const puntero { &variable }`

* Puntero constante a constante (dirección no modificable y valor no modificable): 

    `const <tipo> *const puntero { &variable }`

Para ilustrar un ejemplo de utilidad de esto retomemos la colección de líneas vista anteriormente:

```cpp
const char *p_lineas[]{
    "Esto es una linea",
    "Segunda linea de un texto",
    "Aqui la tercera linea",
    "La ultima linea es la cuarta"};
```

Aquí tenemos un puntero a un dato constante que es un array con múltiples líneas de texto. Esto indica que las líneas no son modificables al ser **C-Strings** de solo lectura con caracteres constantes:

```cpp
*p_lineas[0] = 'A';  // error al cambiar la E por una A
```

Sin embargo sí es posible modificar toda una línea a partir del índice cuando se define una nueva **C-String**, tal como se especifica en la definición `const char`:

```cpp
const char *linea{"Esta es mi nueva linea"};  // esta cadena es un puntero en la memoria
p_lineas[0] = linea; // podemos cambiar la línea a partir de la dirección de la linea
 
for (const char *linea : p_lineas)
    std::cout << linea << std::endl;
```

Sabiendo que un puntero también puede ser constante podemos evitar esta situación definiendo nuestro puntero de líneas como un **puntero constante a un arreglo de caracteres constantes**:

```cpp
const char *const p_lineas[]{
    "Esto es una linea",
    "Segunda linea de un texto",
    "Aqui la tercera linea",
    "La ultima linea es la cuarta"};
 
const char *linea{"Esta es mi nueva linea"};
p_lineas[0] = linea; // error, ahora la dirección es inmutable
```

Los punteros son una de las características más potentes de C++, seguiré explorándolos próximamente.

___
<small class="edited"><i>Última edición: 08 de Mayo de 2022</i></small>