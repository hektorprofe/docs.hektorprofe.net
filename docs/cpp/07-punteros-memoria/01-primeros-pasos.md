title: Primeros pasos con punteros | Apuntes lenguaje C++ | Hektor Profe
description: Primeros pasos con punteros | Apuntes lenguaje C++

# Primeros pasos con punteros en C++

Siempre que definimos una variable, ésta ocupa un lugar de la memoria en base al tamaño del tipo de dato almacenado. Un puntero es un tipo de variable que almacena la dirección de la memoria de una variable y no el valor en sí mismo.

Por defecto los punteros implícitamente reciben el valor de puntero nulo `nullptr`:

```cpp
int *p_entero{};               // direccion de memoria de un int
double *p_fraccional{nullptr}; // direccion de memoria de un double
```

En sistemas de 32 bits los punteros ocupan 4 bytes, que en los de 64 bits ocupan 8 bytes.

No podemos asignar un valor a un puntero, ni literal ni tampoco variable:

```cpp
p_entero = 10; // Error: No es una dirección en la memoria
double pi{3.1415};
p_fraccional = pi; // Error: No es una dirección en la memoria
```

Sin embargo, podemos asignar la dirección de memoria de una variable estableciendo el signo & delante de la variable.

```cpp
double pi{3.1415};
p_fraccional = pi; // Esto sí funcionará
```

Si mostramos el valor del puntero podremos observar una dirección de memoria:

```cpp
std::cout << p_fraccional << std::endl;  // 0x9c70fff6a8
```

Pero si indicamos que esa variable es un puntero mediante `*`, podremos acceder al valor que contiene:

```cpp
std::cout << *p_fraccional << std::endl; // 3.1415
```

Si intentamos almacenar un tipo de dato que no concuerda con el tipo del puntero, la compilación fallará:

```cpp
p_entero = pi;  // cannot convert 'double*' to 'int*' in assignment
```

Algo interesante es que un puntero a un carácter constante se puede inicializar como una cadena:

```cpp
const char *p_texto{"Hola mundo"};  // se expande a un arreglo de char
```

Si intentamos mostrar el puntero, automáticamente imprimiremos el texto completo:

```cpp
std::cout << p_texto << std::endl;  // Hola mundo
```

¿Por qué sucede esto? Cuando la función `std::cout` detecta un puntero a un carácter lo interpreta como una **C-String** e intenta mostrar todos los caracteres que contiene. Dereferenciar el puntero devolverá el primer carácter del arreglo:

```cpp
std::cout << *p_texto << std::endl; // H
```

Como estos punteros a caracteres no requieren reservar una cantidad de espacio de antemano, son muy cómodos por ejemplo para almacenar un arreglo de cadenas, donde cada cadena es un puntero de caracteres:

```cpp
const char *p_lineas[]{
    "Esto es una linea",
    "Segunda linea de un texto",
    "Aqui la tercera linea",
    "La ultima linea es la cuarta"};
```

Dos formas de recorrer y mostrar estas líneas fácilmente mediante un for serían:

```cpp
// Mediante el acceso a los elementos del rango
for (const char *linea : p_lineas)
    std::cout << linea << std::endl;
 
// Mediante un for clásico con indices
for (size_t i = 0; i < std::size(p_lineas); i++)
    std::cout << p_lineas[i] << std::endl;
```

___
<small class="edited"><i>Última edición: 08 de Mayo de 2022</i></small>