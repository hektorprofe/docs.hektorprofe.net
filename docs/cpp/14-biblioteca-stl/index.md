title: Biblioteca STL | Apuntes lenguaje C++ | Hektor Profe
description: iblioteca STL | Apuntes lenguaje C++

# Biblioteca STL en C++

La **Standard Template Library** contiene un conjunto de contenedores, algoritmos e iteradores ya implementados listos para utilizarlos. Por ejemplo:

* **Contenedores**: vector, array, lista, deque, queue, stack.
* **Algoritmos**: sorting, finding, copying, filling, generating, transforming.
* **Iteratores**: input, output, forward, bidirectional, random access, contiguous.

A continuación repasaremos algunas de las definiciones más comunes.

## Primeros contenedores

### std::vector

Este contenedor permite almacenar datos de forma contigua en la memoria y provee distintas funciones parea manipular la información:

```cpp
#include <iostream>
#include <vector>
 
// Función para imprimir un vector por referencia
template <typename T>
void print_vec( const std::vector<T>& vec){
    for(size_t i{}; i < vec.size();++i){
        std::cout << vec[i] << " ";
    }
    std::cout << std::endl;    
}
 
// Función para imprimir un arreglo por puntero
template <typename T>
void print_raw_array(const T* p, std::size_t size)
{
    std::cout << "data = ";
    for (std::size_t i = 0; i < size; ++i)
        std::cout << p[i] << ' ';
    std::cout << std::endl;
}
 
 
int main(){
 
    // Construcción de vectores
    std::vector<std::string> vec_str {"The","sky","is","blue","my","friend"};
    std::cout << "vec1[1]  : " << vec_str[1] << std::endl;
    print_vec(vec_str);
 
    std::cout << "------" << std::endl;
 
    // Un vector vacío no tiene contenido
    std::vector<int> ints1;
    std::cout << "ints1 : ";
    print_vec(ints1); 
 
    std::vector<int> ints2 = { 1,2,3,4 };
    std::vector<int> ints3{ 11,22,33,44 };
     
    std::cout << "ints2 : ";
    print_vec(ints2);
 
    std::cout << "ints3 : ";
    print_vec(ints3);
 
    // Vector de 22 items inicializados a 55
    std::vector<int> ints4(20, 55);
    std::cout << "ints4 : ";
    print_vec(ints4);
     
    // La inicialización uniforme no funcionará
    std::vector<int> ints5{20, 55};
    std::cout << "ints5 : ";
    print_vec(ints5);
 
    // Acceso a los elementos
    std::cout << std::endl;
    std::cout << "Accessing elements in a vector: " << std::endl;
    std::cout << "vec_str[2] : " << vec_str[2] << std::endl;
    std::cout << "vec_str.at(3) : " << vec_str.at(3) << std::endl;
    std::cout << "vec_str.front() : " << vec_str.front() << std::endl;
    std::cout << "vec_str.back() : " << vec_str.back() << std::endl;
 
    // Uso del método data()
    std::cout << "using raw array : " << std::endl;
    print_raw_array(vec_str.data(), vec_str.size());
 
    // Añadir y borrar items
    std::cout << std::endl;
    std::cout << "Adding and removing stuff : " << std::endl;
     
    std::cout << "ints1 : " ;
    print_vec(ints1);
     
    // Inserción de item al final
    ints1.push_back(100);
    ints1.push_back(200);
    ints1.push_back(300);
    ints1.push_back(500);
    std::cout << "ints1 : " ;
    print_vec(ints1);
     
    // Borrado de item al final
    ints1.pop_back();
    std::cout << "ints1 : " ;
    print_vec(ints1);
    
    return 0;
}
```

```
int_array4 : 500 500 
vec1[1]  : sky
The sky is blue my friend 
------
ints1 : 
ints2 : 1 2 3 4 
ints3 : 11 22 33 44 
ints4 : 55 55 55 55 55 55 55 55 55 55 55 55 55 55 55 55 55 55 55 55 
ints5 : 20 55 
 
Accessing elements in a vector: 
vec_str[2] : is
vec_str.at(3) : blue
vec_str.front() : The
vec_str.back() : friend
using raw array :
data = The sky is blue my friend
 
Adding and removing stuff :
ints1 :
ints1 : 100 200 300 500
ints1 : 100 200 300
```

### std::array

Esta estructura permite almacenar datos en un contenedor de tamaño fijo. Algunas funciones son parecidas a las del tipo vector:

```cpp
#include <iostream>
#include <experimental/array>
#include <array>
 
// El segundo argumento debe ser el tamaño
template <typename T,size_t Size> 
void print_array( const std::array<T,Size>& arr){
    for(size_t i{}; i < arr.size();++i){
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;    
}
 
template <typename T>
void print_raw_array(const T* p, std::size_t size)
{
    std::cout << "data = ";
    for (std::size_t i = 0; i < size; ++i)
        std::cout << p[i] << ' ';
    std::cout << std::endl;
}
 
 
int main(){
 
    // Por defecto se inicializan con basura
    std::array<int, 3> int_array1; 
 
    // Contendrá 1,2,0
    std::array<int, 3> int_array2{ 1,2 }; 
 
    // Contendrá 0 0 0
    std::array<int, 3> int_array3{}; 
 
    // El compilador deduce el tipo std::array<int,2>
    std::array int_array4{ 1,2 }; 
 
    // Error de compilación si se inicializan demasiados ítems
    // std::array<int, 3> int_array5{1,2,3,4,5}; 
 
    // Deducción automática mediante auto (experimental)
    auto int_array6 = std::experimental::make_array(1, 2, 3, 4, 5);
 
    std::cout << "int_array1 : " ;
    print_array(int_array1);
     
    std::cout << "int_array2 : " ;
    print_array(int_array2);
     
    std::cout << "int_array3 : " ;
    print_array(int_array3);
     
    std::cout << "int_array4 : " ;
    print_array(int_array4);
     
    std::cout << "int_array6 : " ;
    print_array(int_array6);
 
    // Añadir y borrar ítems
    // No se pueden añadir ítems, solo en la inicialización
    // Se puede rellenar todo el array con el mismo ítem
    std::cout << std::endl;
    std::cout << "Filling the array : " << std::endl;
    int_array1.fill(321);
    int_array4.fill(500);
    std::cout << "int_array1 : " ;
    print_array(int_array1);
    std::cout << "int_array4 : " ;
    print_array(int_array4);
 
    // Acceso a los elementos
    std::cout << std::endl;
    std::cout << "Accessing elements in an array: " << std::endl;
    std::cout << "int_array2[0] : " << int_array2[0] << std::endl;
    std::cout << "int_array2.at(1) : " << int_array2.at(1) << std::endl;
    std::cout << "int_array2.front() : " << int_array2.front() << std::endl;
    std::cout << "int_array2.back() : " << int_array2.back() << std::endl;
 
    //Método data()
    print_raw_array(int_array2.data(),int_array2.size());
    
    return 0;
}
```

```
int_array1 : 32758 -1558290560 433 
int_array2 : 1 2 0 
int_array3 : 0 0 0 
int_array4 : 1 2 
int_array6 : 1 2 3 4 5 
 
Filling the array : 
int_array1 : 321 321 321 
int_array4 : 500 500 
 
Accessing elements in an array:
int_array2[0] : 1
int_array2.at(1) : 2
int_array2.front() : 1
int_array2.back() : 0
data = 1 2 0
```

## Iteradores

Un iterador es una forma de atravesar secuencialmente un contenedor de una forma unificada, independientemente de la estructura interna del contenedor. Cada contenedor en C++ normalmente define una estructura genérica para trabajar con iteradores.

```cpp
#include <iostream>
#include <vector>
#include <array>
 
// Función para imprimir una colección mediante iteradores
template <typename T>
void print_collection(const T& collection){
    auto it = collection.begin();
     
    std::cout << " [";
    while(it != collection.end()){
        std::cout << " " << *it ;
        ++it;
    }
    std::cout << "]" << std::endl;
}
 
int main(){
 
    // Creamos un par de contenedores
    std::vector<int> ints1{ 11,22,33,44 };
    std::array<int,4> ints2 {100,200,300,400};
 
    // Iniciamos unos iteradores para los contenedores
    std::vector<int>::iterator it_begin = ints1.begin();
    std::vector<int>::iterator it_end = ints1.end();
 
    // Realizamos algunas comparaciones entre ellos
    std::cout << std::boolalpha;
    std::cout << "first elt : " << *it_begin << std::endl;
    std::cout << "it == end_it : " << (it_begin == it_end) << std::endl;
    
    // Vamos incrementando el iterador inicial
    ++it_begin;
    std::cout << "second elt : " << *it_begin << std::endl;
    std::cout << "it == end_it : " << (it_begin == it_end) << std::endl;
 
    ++it_begin;
    std::cout << "third elt : " << *it_begin << std::endl;
    std::cout << "it == end_it : " << (it_begin == it_end) << std::endl;
 
    ++it_begin;
    std::cout << "fourth elt : " << *it_begin << std::endl;
    std::cout << "it == end_it : " << (it_begin == it_end) << std::endl;
 
    // Eventualmente el iterador inicial y final serán iguales
    ++it_begin;
    std::cout << "junk elt : " << *it_begin << std::endl;
    std::cout << "it == end_it : " << (it_begin == it_end) << std::endl;
 
    // Impresión de los ítems mediante iteradores
    std::cout << "--------" << std::endl;
 
    std::cout << "ints1 : " ;
    print_collection(ints1);
 
    std::cout << "ints2 :";
    print_collection(ints2);
 
    return 0;
}
```

```
first elt : 11
it == end_it : false
second elt : 22
it == end_it : false
third elt : 33
it == end_it : false
fourth elt : 44
it == end_it : false
junk elt : 0
it == end_it : true
--------
ints1 :  [ 11 22 33 44]
ints2 : [ 100 200 300 400]
```

Los iteradores dan bastante juego, ya que podemos utilizar un iterador invertido para recorrer los elementos desde el final hasta le principio:

```cpp
#include <iostream>
#include <vector>
 
int main()
{
    // Definimos un contenedor vector con 10 numeros
    std::vector<int> numbers{1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
 
    // Creamos un iterador invertido
    std::vector<int>::reverse_iterator it = numbers.rbegin();
 
    // Probamos a modificar el iterador inverso (último elemento)
    *it = 34;
 
    // Recorremos todos los elementos hasta el último
    std::cout << "Numbers : [";
    while (it != numbers.rend())
    {
        std::cout << " " << *it;
        ++it;
    }
    std::cout << " ] " << std::endl;
    std::cout << "--------" << std::endl;
 
    return 0;
}    
```

```
Numbers : [ 34 9 8 7 6 5 4 3 2 1 ] 
```

Como vemos un iterador por defecto es mutable, podemos modificar los elementos. Podemos crear iteradores constantes:

```cpp
#include <iostream>
#include <vector>
 
// Función para imprimir un contenedor con iteradores
template <typename T>
void print_collection(const T &collection)
{
    auto it = collection.begin();
 
    std::cout << " [";
    while (it != collection.end())
    {
        std::cout << " " << *it;
        ++it;
    }
    std::cout << "]" << std::endl;
}
 
int main()
{
 
    std::vector<int> numbers{11, 22, 33, 44, 55, 66, 77};
 
    // Iterador no constante modidicable
    std::vector<int>::iterator it = numbers.begin();
    while (it != numbers.end())
    {
        *it = 100;
        ++it;
    }
 
    std::cout << "numbers : ";
    print_collection(numbers);
 
    std::cout << "-------" << std::endl;
 
    // Iterador constante
    std::vector<int>::const_iterator c_it = numbers.cbegin();
    auto c_it = numbers.cbegin();
    while (c_it != numbers.end())
    {
        *c_it = 100; // Error, iterador no modidicable
        ++c_it;
    }
 
    // Iterador constante invertido
    auto it1 = numbers.crbegin();
    std::vector<int>::const_reverse_iterator it1 = numbers.crbegin();
 
    while (it1 != numbers.crend())
    {
        *it1 = 200; // Error, iterador no modidicable
        ++it1;
    }
 
    return 0;
}
```

Para más información sobre los iteradores y sus categorías aquí está la documentación:

* [https://en.cppreference.com/w/cpp/iterator/iterator](https://en.cppreference.com/w/cpp/iterator/iterator)
* [https://en.cppreference.com/w/cpp/iterator/iterator_tags](https://en.cppreference.com/w/cpp/iterator/iterator_tags)

### std::begin y std::end

Estas dos definiciones son template functions que retornan el iterador inicial y final respectivamente para un contenedor pasado como parámetro.

Son funciones útiles cuando quieres que un iterador codificado funcione también con arrays de C clásicos. Los arrays de C soportan punteros y los punteros cumplen los requisitos para los iteradores de acceso aleatorio.

El requisito para el argumento del template es que la colección pasado debe permitir estos iteradores de inicio y fin:

```cpp
#include <iostream>
#include <vector>
 
int main()
{
 
    // Begin y end en un contenedor de tipo vector
    std::vector<int> vic{1, 2, 3, 4, 5, 6, 7, 8, 9};
    std::cout << "\nVector container: ";
    for (auto it = vic.begin(); it != vic.end(); ++it)
    {
        std::cout << *it << " ";
    }
 
    // Begin y end en un arreglo de C
    int vi[]{1, 2, 3, 4, 5, 6, 7, 8, 9};
    std::cout << "Array de C: ";
    for (auto it = std::begin(vi); it != std::end(vi); ++it)
    {
        std::cout << *it << " ";
    }
 
    return 0;
}
``` 

```
Vector container: 1 2 3 4 5 6 7 8 9
Array de C: 1 2 3 4 5 6 7 8 9
```

## Clasificación de contenedores

Los contenedores nos permiten almacenar elementos de distintas formas.

* **Contenedores secuenciales** donde los elementos se almacenan secuencialmente:
    * `std::deque`
    * `std::forward_list`
    * `std::list`
    * `std::vector` (muy rápido para búsquedas por índice `[]`)
    * `std::array`
* **Contenedores asociativos** donde los elementos se almacenan por clave:
    * `std::pair`
    * `std::set` (muy rápido para buscar elementos)
    * `std::map`
    * `std::multiset` y `std::multimap`
* **Contenedores adaptadores** especializados en diferentes propósitos:
    * `std::stack`
    * `std::queue`
    * `std::priority_queue`

En la documentación se puede encontrar la lista completa de contenedores: [https://en.cppreference.com/w/cpp/container](https://en.cppreference.com/w/cpp/container)

## Contenedores secuenciales

### std::deque (double ended queue)

Esta estructura, al igual que los vectores y listas, soporta el acceso de operadores aleatorios como `[]`. Sin embargo, los elementos no se almacenan de forma contigua en la memoria, sino que se organizan alrededor de las inserciones y borrados a ambos lados de la estructura:

* Son muy rápidas.
* No requieren copia de elementos ni movimientos.
* Nunca invalidan punteros ni referencias a otros elementos de la colección.
* En definitiva, si se necesitan inserciones y borrados a ambos lados de un contenedor (principio y fin), esta estructura es una buena elección.

### std::forward_list

Este contenedor se implementa como una única lista enlazada en la memoria:

```
item1 --> item2 --> item3 --> item4 
```

Donde cada nodo apunta al siguiente elemento:

* Los elementos pueden almacenarse de forma no contigua en la memoria, esto hace que la localización en la memoria no sea muy buena y pone las cosas difíciles a la optimización de la CPU, por ejemplo para realizar inversiones.
* No provee acceso aleatorio a los elementos `[]`.
* Solo tiene iteradores hacia adelante (no invertidos), así que no se puede recorrer a la inversa.

### std::list

Este contenedor se implementa como una doble lista enlazada en la memoria.

```
item1 --> item2 --> item3 --> item4 
      <--       <--       <--
```

Donde cada nodo apunta al elemento anterior y elemento siguiente:

* Los elementos pueden no almacenarse contiguamente en la memoria, por lo que la localización de memoria es bastante mala y como pasaba con la forward list, no es demasiado óptima para recorrerse de forma inversa.
* Tampoco provee operadores de acceso aleatorio como `[]`.
* Al tener dos punteros (anterior y siguiente elemento) provee iteradores adelante y hacia atrás.

### std::array

Este contenedor es de tamaño fijo y los elementos se almacenan de forma contigua en la memoria:

* El tamaño se especifica durante la creación del objeto como un parámetro de template.
* Es bueno para reforzar colecciones de tamaño fijo.
* Es bueno para reemplazar el uso de los arrays crudos dadas sus limitaciones, como la de no poder recorrerlos.

## Contenedores asociativos

### std::pair

Este contenedor se utiliza para almacenar dos componentes de una única entidad y provee facilidades para manipularlos a través de su primer y segundo miembro. Es muy simple y se utiliza en conjunto con otros contenedores, por ejemplo un vector de pares.

### std::set

Este contenedor que ordena los elementos en su interior sin importar como se inserten:

* Impone una condición en os elementos que se pueden almacenar: deben proveer alguna forma de compararse a otros elementos.
* Internamente se utiliza el `operator<` para ordenar los elementos, por lo que sus tipos deben implementar ese operador.
* Al ser elementos ordenados, encontrarlos en el conjunto es muy rápido, similar a como buscamos las palabras de un diccionario.
* Es posible personalizar como se ordenan los elementos implementando el operator< en los tipos almacenados o especificando un callback que le explique como debe compararlos.
* El `callback` puede ser un puntero a una función, un funtor o una función lambda.
* Este tipo no permite la duplicidad de elementos, si se intenta añadir un elemento duplicado se ignorará.
* Para decidir si dos elementos son duplicados, este contenedor no utiliza el `operator==`, en su lugar se utiliza `operator<`. Dos elementos `x` e `y` son equivalentes si `!(x < y) && !(y < x)`.

### std::map

Este contenedor sirve para almacenar valores pares (clave-valor):

* Los elementos se almacenan en claves que van incrementando por defecto.
* No permite la duplicidad de claves, pero si de valores.
* Las búsquedas por clave son muy rápidas debido a que automáticamente ordena los elementos cuando los añades al contenedor.
* `std::set` y `std:map` comparten la propiedad de no almacenar duplicados y que los elementos se ordenen automáticamente.

### std::multiset y std::multimap

Estos dos contenedores son variantes de `std::set` y `std::map` respectivamente cuyo propósito es poder almacenar duplicidades:

* Siguen siendo ordenados, por lo que el `operator<` en las entidades almacenadas importa.
* El resto de métodos son similares a sus estructuras básicas.

### std::unordered_set y std::unordered_map

Tal como su nombre indica, son otras dos variantes de `std::set` y `std::map` que se especialización en no ordenar los elementos de ninguna forma útil como contenedores:

* *sí mismo internamente utilizan lo que conoce como un **hash map** para ordenar los elementos, lo que hace algunas operaciones mucho más rápidas que sus estructuras básicas.
* Es posible proveerlos de un hash map personalizado para controlar cómo ordenar los elementos.
* Independientemente de cual de los dos se utilice son contenedores extremadamente rápidos.

## Contenedores adaptadores

### std::stack

La estructura stack (pila) no es propiamente un contenedor, es una interfaz construida sobre diferentes contenedores (`vector`, `list`, `deque`…) que permite una serie de operaciones determinadas:

* Un stack funcina como una estructura **LIFO** (Last In First Out).
* Para implementar la semántica LIFO, un stack requiere que el contenedor subyacente soporte los métodos `back()`, `push_back()` y `pop_back()`. De ahí que `std::vector`, `std::list` y `std::deque` sean candidatos.
* Podemos acceder a los elementos de la parte superior de la pila con `top()` y podemos sacarlos mediante `pop()`. Hay que tener en cuenta que `pop()` no devuelve el valor sino que remueve el elemento y deja al siguiente encima. Algo que puede suceder hasta que la pila se vacía.
* Disponen del método `size()` para consultar cuantos elementos hay en la colección.

### std::queue

La estructura queue (cola) es otra interfaz para contenedores que implementa la semántica **FIFO** (First In First Out), donde el primer elemento en entrar es el primer elemento en salir:

* Es una adaptación por encima de los contenedores secuenciales que soportan las siguientes métodos:
    * `back()`: para recuperar el último elemento.
    * `front()`: para recuperar el primer elemento.
    * `push_back()`: para añadir elementos al final del contenedor.
    * `pop_front()`: para remover el primer elemento.
* Los contenedores `std::deque` y `std::list` son candidatos para su uso. Por otro lado `std::vector` no es compatible al no implementar el método `pop_front()`.

### std::priority_queue

Esta interfaz de contenedor adaptador funciona como una cola, pero el primer elemento en salir es siempre el que tiene una mayor prioridad. La prioridad se decide mediante el método de comparación de los tipos almacenados, por defecto `std::less<>`.

* La adaptación del contenedor secuencial requiere que soporte los métodos:
    * `front()`: para recuperar el primer elemento.
    * `push_back()`: para añadir elementos al final del contenedor.
    * `pop_front()`: para remover el primer elemento.
* Los contenedores `std::deque` y `std::vector` son candidatos para su uso. Por otro lado `std::list` no es compatible al no implementar un iterador de acceso aleatorio.
* Algunos de los métodos más útiles implementados por la cola de prioridad son:
    * `top()`: para recuperar el elemento con mayor prioridad (lectura).
    * `push()`: para añadir elementos.
    * `pop()`: para remover elementos (el de mayor prioridad).
* Podemos controlar la forma de ordenación cambiando el método comparador por defecto `std::less<>` a través de la sobrecarga del operator< en los tipos almacenados o especificando un comprador personalizado al crear la `std::priority_queue`.

## Clasificación de algoritmos

La biblioteca de algoritmos define funciones para una variedad de propósitos (por ejemplo, buscar, clasificar, contar, manipular) que operan en rangos de elementos. Un rango se define como [first, last), donde last se refiere al elemento después del último elemento a inspeccionar o modificar y está excluido del rango. Tenemos dos categorías:

* **Algoritmos de legado**: para trabajar con pares de iteradores.
* **Algoritmos de rangos**: para trabajar directamente con contenedores (C++20).

La lista completa de algoritmos podemos encontrarla en la documentación: [https://en.cppreference.com/w/cpp/algorithm](https://en.cppreference.com/w/cpp/algorithm)

## Algoritmos de legado

### std::all_of, std::any_of y std::none_of

Estos algoritmos comprueban si un predicado es true para todos, alguno o ninguno de de los elementos en un rango:

```cpp
#include <vector>
#include <numeric>
#include <algorithm>
#include <iterator>
#include <iostream>
#include <functional>
  
int main()
{
    std::vector<int> v(10, 2);
    std::partial_sum(v.cbegin(), v.cend(), v.begin());
    std::cout << "Among the numbers: ";
    std::copy(v.cbegin(), v.cend(), std::ostream_iterator<int>(std::cout, " "));
    std::cout << '\n';
  
    if (std::all_of(v.cbegin(), v.cend(), [](int i){ return i % 2 == 0; })) {
        std::cout << "All numbers are even\n";
    }
    if (std::none_of(v.cbegin(), v.cend(), std::bind(std::modulus<int>(), 
                                                     std::placeholders::_1, 2))) {
        std::cout << "None of them are odd\n";
    }
    struct DivisibleBy
    {
        const int d;
        DivisibleBy(int n) : d(n) {}
        bool operator()(int n) const { return n % d == 0; }
    };
  
    if (std::any_of(v.cbegin(), v.cend(), DivisibleBy(7))) {
        std::cout << "At least one number is divisible by 7\n";
    }
}
```

```
Among the numbers: 2 4 6 8 10 12 14 16 18 20 
All numbers are even
None of them are odd
At least one number is divisible by 7
```

### std::for_each

Aplica una función a un rango de elementos:

```cpp
#include <vector>
#include <algorithm>
#include <iostream>
  
struct Suma
{
    void operator()(int n) { sum += n; }
    int suma{0};
};
  
int main()
{
    std::vector<int> nums{3, 4, 2, 8, 15, 267};
  
    auto print = [](const int& n) { std::cout << " " << n; };
  
    std::cout << "antes:";
    std::for_each(nums.cbegin(), nums.cend(), print);
    std::cout << '\n';
  
    std::for_each(nums.begin(), nums.end(), [](int &n){ n++; });
  
    // llama a Suma::operator() para cada miembro
    Suma s = std::for_each(nums.begin(), nums.end(), Suma());
  
    std::cout << "despues: ";
    std::for_each(nums.cbegin(), nums.cend(), print);
    std::cout << '\n';
    std::cout << "suma: " << s.suma << '\n';
}
```

```
antes: 3 4 2 8 15 267
despues:  4 5 3 9 16 268
suma: 305
```

### std::max_element y std::min_element

Devuelven el elemento más grande y más pequeño de un rango:

```cpp
#include <algorithm>
#include <iostream>
#include <vector>
#include <cmath>
 
static bool abs_compare(int a, int b)
{
    return (std::abs(a) < std::abs(b));
}
 
int main()
{
    std::vector<int> v{3, 1, -14, 1, 5, 9};
    std::vector<int>::iterator result1;
 
    result1 = std::max_element(v.begin(), v.end());
    std::cout << "max element at: " << std::distance(v.begin(), result1) << '\n';
 
    result1 = std::max_element(v.begin(), v.end(), abs_compare);
    std::cout << "max element (absolute) at: " << std::distance(v.begin(), result1) << '\n';
 
    std::vector<int>::iterator result2 = std::min_element(v.begin(), v.end());
    std::cout << "min element at: " << std::distance(v.begin(), result2);
}
```

```
max element at: 5
max element (absolute) at: 2
min element at: 2
```

### std::find y std::find_if

Encuentra el primer elemento que satisfaga los criterios específicos:

```cpp
#include <iostream>
#include <algorithm>
#include <vector>
#include <iterator>
 
int main()
{
    int n1 = 3;
    int n2 = 5;
 
    std::vector<int> v{0, 1, 2, 3, 4};
 
    auto resultado1 = std::find(std::begin(v), std::end(v), n1);
    auto resultado2 = std::find(std::begin(v), std::end(v), n2);
 
    if (resultado1 != std::end(v))
    {
        std::cout << "v contiene: " << n1 << '\n';
    }
    else
    {
        std::cout << "v no contiene: " << n1 << '\n';
    }
 
    if (resultado2 != std::end(v))
    {
        std::cout << "v contiene: " << n2 << '\n';
    }
    else
    {
        std::cout << "v no contiene: " << n2 << '\n';
    }
 
    // búsqueda con función lambda condicional
    auto impar = [](int x)
    {
        if ((x % 2) != 0)
        {
            return true;
        }
        return false;
    };
 
    auto impar_n_posicion = std::find_if(std::begin(v), std::end(v), impar);
    if (impar_n_posicion != std::end(v))
    {
        std::cout << "v contiene por lo menos un impar: "
                  << *impar_n_posicion << '\n';
    }
    else
    {
        std::cout << "v no contiene ningun impar" << '\n';
    }
}
```

```
v contiene: 3
v no contiene: 5
v contiene por lo menos un impar: 1
```

### std::copy y std::copy_if

Copia un rango de elementos a una nueva ubicación:

```cpp
#include <algorithm>
#include <iostream>
#include <vector>
#include <iterator>
#include <numeric>
  
int main()
{
    std::vector<int> from_vector(10);
    std::iota(from_vector.begin(), from_vector.end(), 0);
    // Nota: iota rellena el rango [first, last) con valores
    // crecientes de forma secuencial, comenzando con value 
    // y repetitivamente evaluando ++value.
  
    std::vector<int> to_vector;
    std::copy(from_vector.begin(), from_vector.end(),
              std::back_inserter(to_vector));
    // o de manera alterna,
    // std::vector<int> to_vector(from_vector.size());
    // std::copy(from_vector.begin(), from_vector.end(), to_vector.begin());
    // cualquier manera es equivalente a
    // std::vector<int> to_vector = from_vector;
  
    std::cout << "to_vector contiene: ";
  
    std::copy(to_vector.begin(), to_vector.end(),
              std::ostream_iterator<int>(std::cout, " "));
    std::cout << '\n';
  
    std::cout << "los nones en to_vector son: ";
  
    std::copy_if(to_vector.begin(), to_vector.end(),
                 std::ostream_iterator<int>(std::cout, " "),
                 [](int x) { return (x % 2) == 1; });
    std::cout << '\n';
}
```

```
to_vector contiene: 0 1 2 3 4 5 6 7 8 9 
los nones en to_vector son: 1 3 5 7 9
```

### std::sort

Ordena un intervalo en orden ascendente:

```cpp
#include <algorithm>
#include <functional>
#include <array>
#include <iostream>
  
int main()
{
    std::array<int, 10> s{5, 7, 4, 2, 8, 6, 1, 9, 0, 3};
  
    std::sort(s.begin(), s.end());
    for (int a : s) {
        std::cout << a << " ";
    } 
    std::cout << '\n';
  
    std::sort(s.begin(), s.end(), std::greater<int>());
    for (int a : s) {
        std::cout << a << " ";
    } 
    std::cout << '\n';
}
```

```
0 1 2 3 4 5 6 7 8 9
9 8 7 6 5 4 3 2 1 0
```

### std::transform

Aplica una función a un rango de elementos:

```cpp
#include <algorithm>
#include <cctype>
#include <iostream>
#include <string>
#include <vector>
  
int main()
{
    std::string s("hola");
 
    // Primera transformación de minúsculas a minúsculas
    std::transform(s.begin(), s.end(), s.begin(),
                   [](unsigned char c) -> unsigned char { return std::toupper(c); });
      
    std::vector<std::size_t> ordinals;
 
    // Segunda transformación de caracteres a números ordinales
    std::transform(s.begin(), s.end(), std::back_inserter(ordinals),
                   [](unsigned char c) -> std::size_t { return c; });
  
    std::cout << s << ':';
    for (auto ord : ordinals) {
       std::cout << ' ' << ord;
    }
  
    // Tercera transformación de adición (suma valor + valor)
    std::transform(ordinals.cbegin(), ordinals.cend(), ordinals.cbegin(),
                   ordinals.begin(), std::plus<>{});
  
    std::cout << '\n';
    for (auto ord : ordinals) {
       std::cout << ord << ' ';
    }
    std::cout << '\n';
}
```

```
HOLA: 72 79 76 65
144 158 152 130
```

## Algoritmos de rangos

Estos son exclusivos de C++20, la lista completa se puede encontrar en [https://es.cppreference.com/w/cpp/ranges](https://es.cppreference.com/w/cpp/ranges).

___
<small class="edited"><i>Última edición: 09 de Mayo de 2022</i></small>