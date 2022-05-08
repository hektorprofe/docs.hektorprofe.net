title: Referencias y manipulación de arreglos | Apuntes lenguaje C++ | Hektor Profe
description: Referencias y manipulación de arreglos | Apuntes lenguaje C++

# Referencias y manipulación de arreglos en C++

Ya sabemos que un **puntero** en C++ es una variable que contiene la dirección de memoria de otra variable. ¿Pero qué es una referencia?

Una **referencia** es un alias o acceso para una variable ya existente, que una vez inicializada no se puede cambiar para hacer referencia a otra. Son en cierto modo similares a los punteros constantes:

```cpp
int numero{44};
int &ref_numero{numero};
std::cout << ref_numero << std::endl;
```

Esta tabla resume las diferencias más notables:

| Puntero | Referencia |
|---|---|
| Un puntero se puede inicializar en cualquier momento después de la definición. | Una referencia debe inicializarse en el momento de la definición. |
| Un puntero puede apuntar al valor NULL. | Una referencia no puede apuntar al valor NULL. |
| Los punteros deben ser desreferenciados con el asterisco *. | Las referencias se utilizan por su nombre. |
| Un puntero se puede cambiar para que apunte a cualquier variable del mismo tipo. | Una vez inicializada en una variable, no se puede modificar para que apunte a otra variable. |

Así mismo, aunque la referencia no permite cambiar a donde apunta, permite modificar el valor original de la variable referenciada:

```cpp
ref_numero += 33;  // Modificamos el valor referenciado
std::cout << numero<< std::endl;  // 77
```

Para evitar eso podemos definir la referencia como constante:

```cpp
int numero{44};
const int &ref_numero{numero};  // referencia constante
ref_numero += 33;               // error al modificar el valor
```

Como decía al principio una referencia es en esencia un puntero constante, así que podríamos decir que ambas definiciones tiene un uso parecido:

```cpp
int numero{44};
const int* const p_numero {&numero};  // puntero constante a valor constante
p_numero += 33;                       // error al modificar el valor
```

Sin embargo gracias a su capacidad mutable las referencias **pueden ser muy útiles para trabajar con arreglos**, especialmente para modificarlos secuencialmente.

Por ejemplo, pese a que mediante variables no podemos modificar los elementos en un `for` por valores:

```cpp
int numeros[5]{11, 22, 33, 44, 55};
 
// El for por valor copia los elementos y no son modificables
for (auto numero : numeros)
    numero *= 10;
 
for (auto numero : numeros)
    std::cout << numero << " ";  // 11 22 33 44 55
```

Si en lugar de copiar los elementos los almacenamos en referencias, sí podremos modificarlos secuencialmente sin necesidad de índices:

¿Cuándo utilizar unos y otros?

* Se recomienda utilizar **referencias** en parámetros de funciones y para retornar tipos de datos.
* Se recomienda utilizar **punteros** cuando:
    * Si se necesita aritmética de punteros o punteros de paso `NULL`. Por ejemplo para matrices, pues esto acceso se implementa mediante aritmética de punteros.
    * Para implementar estructuras de datos como listas enlazadas, árboles, etc. y sus algoritmos, pues para apuntar a diferentes celdas tenemos que usar el concepto de punteros.

___
<small class="edited"><i>Última edición: 08 de Mayo de 2022</i></small>