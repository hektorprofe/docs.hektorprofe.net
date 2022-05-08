title: Aritmética de punteros | Apuntes lenguaje C++ | Hektor Profe
description: Aritmética de punteros | Apuntes lenguaje C++

# Aritmética de punteros en C++

Se trata de un conjunto de operaciones que podemos realizar en los punteros que representan un arreglo para manipularlos. Estas operaciones incluyen navegación de los elementos, cómputo de la distancia entre elementos y comparación de las direcciones de los elementos.

## Navegación con punteros

Si incrementamos o decrementamos un puntero, éste moverá su dirección en base al tamaño del tipo de dato del puntero. Esto es útil siempre y cuando no salgamos del espacio en la memoria que ocupan los datos.

```cpp
int numeros[5]{11, 22, 33, 44, 55}; // arreglo de numeros
int *p_numeros = numeros;           // puntero al arreglo
 
std::cout << *(p_numeros + 0) << std::endl; // primer numero
std::cout << *(p_numeros + 1) << std::endl; // segundo numero
std::cout << *(p_numeros + 2) << std::endl; // tercer numero
std::cout << *(p_numeros + 3) << std::endl; // cuarto numero
std::cout << *(p_numeros + 4) << std::endl; // quinto numero
```

Si nos salimos del espacio en la memoria obtendremos resultados inestables y por tanto un mal funcionamiento del programa:

```cpp
std::cout << *(p_numeros + 10) << std::endl; // fuera de rango
```

Esta lógica la podemos usar con el nombre del arreglo refiriéndonos a él como un puntero:

```cpp
std::cout << *(numeros + 0) << std::endl; // primer numero
std::cout << *(numeros + 1) << std::endl; // segundo numero
std::cout << *(numeros + 2) << std::endl; // tercer numero
std::cout << *(numeros + 3) << std::endl; // cuarto numero
std::cout << *(numeros + 4) << std::endl; // quinto numero
```

## Distancia entre punteros

Para conseguir la distancia entre dos punteros podemos restarlos, el resultado será un número entero que representará el número de elementos entre dos punteros:

```cpp
int numeros[8]{11, 22, 33, 44, 55, 66, 77, 88};
int *ptr1 = numeros + 0; // 11
int *ptr2 = numeros + 7; // 88
 
std::cout << "ptr2 - ptr1: " << ptr2 - ptr1 << std::endl; //  7
std::cout << "ptr1 - ptr2: " << ptr1 - ptr2 << std::endl; // -7
```

Si por alguna razón necesitamos almacenar esta distancia podemos utilizar un tipo de dato `std::ptrdiff_t`:

```cpp
std::ptrdiff_t distancia = ptr2 - ptr1;
std::cout << "distancia: " << distancia << "\n"; // distancia: 7
```

## Comparación de direcciones

Los punteros permiten, como otros datos, el uso de operaciones relacionales. Lo que estaremos comparando son en realidad las direcciones de memoria. El primer dato de un arreglo siempre tendrá un puntero menor en la memoria que el segundo, el segundo menor que el tercero, etc:

```cpp
int numeros[8]{11, 22, 33, 44, 55, 66, 77, 88};
int *ptr1 = numeros + 0; // 11
int *ptr2 = numeros + 7; // 88
 
std::cout << std::boolalpha << std::endl;
 
std::cout << "ptr1 > ptr2: " << (ptr1 > ptr2) << std::endl;   // false
std::cout << "ptr1 < ptr2: " << (ptr1 < ptr2) << std::endl;   // true
std::cout << "ptr1 >= ptr2: " << (ptr1 >= ptr2) << std::endl; // false
std::cout << "ptr1 <= ptr2: " << (ptr1 <= ptr2) << std::endl; // true
std::cout << "ptr1 == ptr2: " << (ptr1 == ptr2) << std::endl; // false
std::cout << "ptr1 != ptr2: " << (ptr1 != ptr2) << std::endl; // true
```

___
<small class="edited"><i>Última edición: 08 de Mayo de 2022</i></small>