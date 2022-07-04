title: Cadenas de caracteres | Apuntes lenguaje C++ | Hektor Profe
description: Cadenas de caracteres | Apuntes lenguaje C++

# Cadenas de caracteres en C++

## Manipulación de caracteres y C-Strings

La biblioteca estándar incluye una serie de funcionalidades para trabajar con caracteres, aquí la tabla con ellas: [https://en.cppreference.com/w/cpp/string/byte](https://en.cppreference.com/w/cpp/string/byte)

Por citar algunas funciones muy sencillas, tenemos `std::isdigit` para saber si un carácter es numérico o std::toupper para devolverlo en su forma mayúscula:

```cpp
char letra{'h'};
 
if (std::isdigit(letra))
    std::cout << letra << " es un digito" << std::endl;
else
    std::cout << letra << " no es un digito" << std::endl;
 
std::cout << letra << " en mayuscula "
            << (char)std::toupper(letra) << std::endl;
```

Así mismo también ofrece un apartado `<cstring>` para manejar cadenas de texto en el formato clásico heredado de C, aquí la tabla de funcionalidades: [https://en.cppreference.com/w/cpp/header/cstring](https://en.cppreference.com/w/cpp/header/cstring)

Las **C-Strings** son arreglos de caracteres con un carácter nulo `\0` al final que indica el final una cadena. Cuando las definimos mediante un arreglo podemos inicializarlas automáticamente en la definición, el sistema añadirá manualmente el carácter de fin de cadena:

```cpp
#include <cstring>
 
char cadena[]{"Hola mundo"}; 
std::cout << cadena << std::endl;
std::cout << "Longitud cadena: " << std::strlen(cadena) << std::endl;
```

También podemos definirlas mediante punteros constantes de caracteres:

```cpp
#include <cstring>
 
const char *p_cadena{"Hola mundo"};
std::cout << p_cadena << std::endl;
std::cout << "Longitud cadena: " << std::strlen(p_cadena) << std::endl;
```

Inclusive se pueden definir a partir de los caracteres para almacenarlas en el montón (con new), pero debemos añadir manualmente el carácter fin de cadena:

```cpp
#include <cstring>
 
char *p_cadena2 = new char[]{'H','o','l','a',' ','m','u','n','d','o','\0'};
std::cout << p_cadena2 << std::endl;
std::cout << "Longitud cadena: " << std::strlen(p_cadena2) << std::endl;
```

Algunas funcionalidades interesantes, a parte de la longitud `std::strlen`, son la concatenación `std::strcat` y la copia `std::strcpy`:

```cpp
char cadena1[]{"Hola "};
char cadena2[]{"mundo"};
char cadena3[10]{};
 
// Concatenación de cadenas
std::strncat(cadena3, cadena1, std::size(cadena1));
std::strncat(cadena3, cadena2, std::size(cadena2));
std::cout << cadena3 << std::endl; // Hola mundo
 
// Copia de cadenas
char cadena4[10]{};
std::strcpy(cadena4, cadena3);
std::cout << cadena4 << std::endl; // Hola mundo
```

## Cadenas std::string y sus métodos

Las cadenas son objetos que representan secuencias de caracteres. La biblioteca estándar incluye la clase `std::string` que proporciona una alternativa sencilla, segura y versátil para la utilización de matrices explícitas de caracteres.

Hay muchas formas de definir una cadena de esta clase:

```cpp
// Cadena vacía
std::string cadena;
 
// Desde const char * (c-string)
std::string cadena ("Hola mundo");
std::string cadena {"Hola mundo"};
std::string cadena = "Hola mundo";
 
// Usando el constructor de copia
std::string cadena1 ("Hola mundo");
std::string cadena2 (cadena1);
 
// A partir de subcadenas y/o buffers
std::string cadena1 ("Hola mundo");
std::string cadena2 (cadena1, 0, 4); // "Hola"
 
// Usando relleno (solo char)
std::string cadena (6, 'a'); // "aaaaaa"
 
// Usando el constructor de iteración
std::string cadena1 ("Hola mundo");
std::string cadena2 (cadena1.begin(), cadena1.begin() + 4); // "Hola"
```

Podemos concatenar `std::string` utilizando los operadores sobrecargados `+`:

```cpp
std::string cadena1 = "Hola";
std::string cadena2 = "mundo";
std::string cadena3 = cadena1 + " " + cadena2; // "Hola mundo"
```

También mediante el operador de suma en asignación en la propia cadena `+=`:

```cpp
std::string cadena = "Hola";
cadena += " mundo"; // "Hola mundo"
```

Podemos agregar cadenas **C-string**, incluidos los literales de cadena:

```cpp
std::string cadena1 = "Hola";
std::string cadena2 = "mundo";
const char *coma = ", ";
std::string cadena3 = cadena1 + coma + cadena2; // "Hola mundo"
```

O utilizar el método `push_back()` para insertar un carácter al final del arreglo:

```cpp
std::string cadena = "ab";
cadena.push_back('c'); // abc
```

De forma similar podemos utilizar el método `append()` para añadir una cadena al final de otra:

```cpp
std::string cadena = "Hola";
cadena.append(" mundo"); // Hola mundo
```

Podemos consultar y modificar los caracteres de una `std::string` mediante índices o el método `.at()`:

```cpp
std::string cadena = "Hola mundo";
cadena[0] = 'M';
cadena.at(7) = 'c';
cadena.at(8) = 'h';
std::cout << cadena << std::endl; // Mola mucho
```

De forma similar podemos utilizar los métodos `front()` y `back()` para consultar y modificar los caracteres del principio y del final de la cadena:

```cpp
std::string cadena = "Hola mundo";
cadena.front() = 'M';
cadena.back() = 'a';
std::cout << cadena << std::endl; // Mola munda
```

Además disponemos del método `c_str()`, que devuelve la cadena en formato **C-string** que podemos almacenar en un `const char*`:

```cpp
std::string cadena1 = "Hola mundo";
const char *cadena2 = cadena1.c_str(); // C-string no modificable
```

Desde C++17 podemos utilizar el método `data()` para modificar el arreglo `char*` subyacente, lo que modificará la cadena `std:string` original:

```cpp
std::string cadena1 = "Hola mundo";
char *cadena2 = cadena1.data();
cadena2[0] = 'M';
std::cout << cadena1 << " = " << cadena2
          << std::endl; // Mola mundo = Mola mundo
```

Podemos determinar si una `std:string` está vacía mediante le método `empty()`:

```cpp
std::string cadena;
if (cadena.empty()) std::cout << "Cadena vacia" << std::endl;
```

Y su longitud o tamaño (es lo mismo) mediante `length()` y `size()`:

```cpp
std::string cadena = "Hola mundo";
std::cout << "Longitud: " << cadena.length() << std::endl;
std::cout << "Tamano: " << cadena.size() << std::endl;
```

El método `max_size()` nos dirá el número máximo de caracteres que puede almacenar una cadena en nuestro sistema:

```cpp
std::string cadena;
std::cout << "Tamano maximo: " << cadena.max_size() << std::endl;
// Tamano maximo: 9223372036854775807
```

Así mismo podemos consultar la capacidad de una cadena con el método `capacity()`, el tamaño del espacio de almacenamiento asignado actualmente para la cadena, expresado en bytes.

```cpp
std::string cadena;
std::cout << "Capacidad: " << cadena.capacity() << std::endl;
// Capacidad: 15
```

La capacidad se almacena por defecto, de manera que al intentar almacenar más caracteres de los que se pueden almacenar en el bloque actual, el objeto `std::string` reclama más espacio en la memoria:

```cpp
std::string cadena;
std::cout << "Capacidad actual: " << cadena.capacity() << "\n"; // 15
cadena = "Hola hola hola hola hola";
std::cout << "Capacidad actual: " << cadena.capacity() << "\n"; // 30
```

Podemos reservar de antemano una cantidad de espacio mediante `reserve()` y luego ajustarlo al tamaño de la cadena actual mediante `shrink_to_fit()`:

```cpp
std::string cadena;
cadena.reserve(100);
cadena = "Hola hola hola hola hola";
std::cout << "Capacidad actual: " << cadena.capacity() << "\n"; // 100
cadena.shrink_to_fit();
std::cout << "Capacidad actual: " << cadena.capacity() << "\n"; // 24
```

Por último comentar que es posible comparar fácilmente `std::string`, incluso con **C-strings** y cadenas literales, son iguales mediante los operadores `==` y `!=`:

```cpp
std::string cadena{"Hola"};
std::cout << std::boolalpha;
std::cout << (cadena == "Hola") << std::endl; // true
std::cout << (cadena != "Hola") << std::endl; // false
```

También se pueden comparar lexicográficamente (en el orden como aparecerían en el diccionario) usando el método `compare()` que devolverá:

* Valor cero 0: cuando las cadenas que se comparan son lexicográficamente iguales.
* Valor negativo <0: cuando la primera cadena es lexicográficamente menor que la segunda.
* Valor positivo >0: cuando la primera cadena es lexicográficamente mayor que la segunda.

```cpp
std::string cadena{"Hola"};
std::cout << cadena.compare("Hola") << std::endl;  //  0
std::cout << cadena.compare("Holas") << std::endl; // -1 (después)
std::cout << cadena.compare("Hey") << std::endl;   //  1 (antes)
```

Sin duda C++ pone a nuestra disposición un montón de utilidades para manejar y optimizar el uso de la memoria.

## Buscar, substituir, intercambiar y convertir std::string

Repasemos ahora algunas utilidades de la clase `std::string`, las cuales se pueden encontrar descritas en la documentación: [https://en.cppreference.com/w/cpp/string/basic_string](https://en.cppreference.com/w/cpp/string/basic_string)

**Búsqueda**

```cpp
std::string cad{"Hola mundo"};
std::cout << cad.find("mundo") << std::endl; // 5
std::cout << cad.find("adios") << std::endl; // npos (no encontrado)
 
// Debemos comprobar siempre que no se devuelve un npos
if (cad.find("adios") == std::string::npos)
    std::cout << "No encontrado" << std::endl;
```

**Substitución**

```cpp
std::string cadena{"Hola buenos dias"}; // cadena original
std::string objetivo{"buenos dias"};    // porcion substituible
std::string porcion{"buenas noches"};   // porcion substituta
int size = porcion.size();              // nº de caracteres a substituir
int pos = cadena.find("buenos dias");   // buscar el indice encontrado
if (pos != std::string::npos)
    cadena.replace(pos, size, porcion.substr(0, size));
std::cout << cadena << std::endl; // Hola buenas noches
```

**Intercambio**

```cpp
std::string cad1{"Hola"};
std::string cad2{"Adios"};
 
cad1.swap(cad2);
std::cout << cad1 << ", " << cad2 << std::endl; // Adios, Hola
```

**Conversión de número a cadena**

```cpp
std::cout << std::to_string(101) << std::endl;   // "101"
std::cout << std::to_string(3.14f) << std::endl; // "3.140000"
std::cout << std::to_string(45.32) << std::endl; // "45.320000"
```

**Conversión de cadena a número**

```cpp
std::cout << std::stoi("101") << std::endl;   // 101
std::cout << std::stof("3.14") << std::endl;  // 3.14
std::cout << std::stod("45.32") << std::endl; // 45.32
```

## Cadenas en crudo (raw string literals)

El carácter de escapa `\` en las cadenas nos sirve para establecer caracteres especiales que indican saltos de línea `\n`, tabulaciones `\t`, caracteres nulos `\0`, etc. Por esa razón definir una cadena como la siguiente no es posible:

```cpp
std::string ruta{"C:\Usuario\Documentos\Escritorio"};  // error
```

Una forma de definir estas cadenas con caracteres de escape es utilizar el propio carácter de escape `\` para escapar el escape:

```cpp
std::string ruta{"C:\\Usuario\\Documentos\\Escritorio"};
std::cout << ruta << std::endl; 
// C:\Usuario\Documentos\Escritorio
```

O también podemos definir una cadena en crudo (raw) con el modificador `R` de esta forma:

```cpp
std::string ruta{R"(C:\Usuario\Documentos\Escritorio)"};
std::cout << ruta << std::endl; 
// C:\Usuario\Documentos\Escritorio
```

En caso de que encontremos comillas con paréntesis, podemos evitar que la interprete delimitando la cadena entre tres guiones `---`:

```cpp
std::string cadena{R"---(C:\("U")suario\("D")ocumentos)---"};
std::cout << cadena << std::endl; 
// C:\("U")suario\("D")ocumentos
```

## Vistas de cadenas (std::string_view)

Desde C++17 encontramos un tipo de dato algo extraño llamado `std::string_view` o vista de cadena: [https://en.cppreference.com/w/cpp/string/basic_string_view](https://en.cppreference.com/w/cpp/string/basic_string_view)

Podemos suponer una vista como una ventana a través de la cuál podemos observar un texto, pero no tenemos acceso a él ni a su modificación.

Esto puede resolver un problema de copias múltiples en la memoria, tal como ilustra el siguiente código:

```cpp
char texto[]{"Hola mundo"};   // Primera definición
std::string cadena1{texto};   // Segunda de definición
std::string cadena2{cadena1}; // Tercera definición
 
std::cout << sizeof(std::string) << "\n";                // 32 bytes
std::cout << &texto << " " << sizeof(texto) << "\n";     // 0x9d457ff870 11
std::cout << &cadena1 << " " << sizeof(cadena1) << "\n"; // 0x9d457ff860 32
std::cout << &cadena2 << " " << sizeof(cadena2) << "\n"; //  0x9d457ff850 32
```

En esta pieza de código definimos una **C-string** y a partir de ella una `std::string` que utilizamos a su vez como origen para otra `std::string`. ¿Cuántas copias de `Hola mundo` existen en la memoria del programa?

En primer lugar tenemos la cadena literal `Hola mundo` reconocida en tiempo de compilación y almacenada de forma binaria en la memoria. A partir de ella se crea la copia almacenada en el puntero para la **C-string** y luego las dos copias por valor para las `std::string`, lo que hacen 4 `Hola mundo` almacenados paralelamente en el programa.

Si aplicamos la misma lógica pero utilizando vistas de cadena reduciremos el tamaño en la memoria a 1 solo`Hola mundo`:

```cpp
std::string_view texto{"Hola mundo"}; // Primera definición
std::string_view cadena1{texto};      // Segunda de definición
std::string_view cadena2{cadena1};    // Tercera definición
 
std::cout << sizeof(texto) << "\n";                      // 16 bytes
std::cout << &texto << " " << sizeof(texto) << "\n";     // 0x9d457ff870 16
std::cout << &cadena1 << " " << sizeof(cadena1) << "\n"; // 0x9d457ff860 16
std::cout << &cadena2 << " " << sizeof(cadena2) << "\n"; // 0x9d457ff850 16
```

Las `std::string_view` nativas no son modificables, pero si las creamos a partir de una `std::string` o **C-string** y modificamos la original, las vistas también cambiarán, pues apuntan al fin y al cabo a la original:

```cpp
std::string original{"Hola mundo"};
std::string_view texto{original};
std::string_view cadena1{texto};
std::string_view cadena2{cadena1};
 
original[0] = 'M';
 
std::cout << original << "\n"; // Mola mundo
std::cout << texto << "\n";    // Mola mundo
std::cout << cadena1 << "\n";  // Mola mundo
std::cout << cadena2 << "\n";  // Mola mundo
```

Se recomienda utilizar siempre `std::string_view` antes que **C-strings** o cualquier tipo de cadena solo de lectura como sería una `const std::string`, no solo para optimizar memoria sino también para incrementar la seguridad.

___
<small class="edited"><i>Última edición: 08 de Mayo de 2022</i></small>