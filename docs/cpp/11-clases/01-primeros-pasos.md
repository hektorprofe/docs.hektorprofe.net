title: Primeros pasos con las clases | Apuntes lenguaje C++ | Hektor Profe
description: Primeros pasos con las clases | Apuntes lenguaje C++

# Primeros pasos con las clases en C++

## Definición de clases y objetos

Las clases nos ofrecen un paradigma distinto para desarrollar soluciones, en ellas nos enfocamos en replicar problemas del mundo real en la programación mediante los objetos, las instancias de nuestras propias estructuras:

```cpp
#include <iostream>
 
const double PI {3.14159265358979323846264338};
 
class Cilindro {
    public: 
        //Funciones (métodos)
        double volumen(){
            return PI * radio * radio * altura;
        }
 
    public: 
        // Variables miembro
        double radio{1};
        double altura{1};
};
```

Para trabajar con nuestra clase crearemos instancias, ya sea en el **stack**:

```cpp
// Objecto en el stack
Cilindro cilindro1; 
std::cout << "volumen: " << cilindro1.volumen() << std::endl;
 
// Cambiamos las variables miembro
cilindro1.radio = 10;
cilindro1.altura = 3;
 
std::cout << "volumen: " << cilindro1.volumen() << std::endl;
```

O en el **heap** mediante punteros, sin olvidar liberar la memoria tras el uso, teniendo en cuenta que el acceso a los métodos y miembros es mediante la notación con flecha:

```cpp
// Objecto en el heap
Cilindro *cilindro2 = new Cilindro();
std::cout << "volumen: " << (*cilindro2).volumen() << std::endl;
std::cout << "volumen: " << cilindro2->volumen() << std::endl;
 
// Cambiamos las variables miembro
cilindro2->radio = 10;
cilindro2->altura = 3;
 
std::cout << "volumen: " << cilindro2->volumen() << std::endl;
 
// Liberamos la memoria
delete cilindro2;
```

## Método constructor en clases

El método **constructor** es un método especial que se llama al crear una instancia, no retorna nada, tiene el mismo nombre que la clase, puede recibir parámetros y usualmente inicializada las variables miembro de la clase, además se puede sobrecargar y mediante el puntero `this` se puede hacer referencia a un puntero que apunta a la propia instancia, útil para comunicarse entre las variables miembro entre métodos:

```cpp
#include <iostream>
 
const double PI{3.14159265358979323846264338};
 
class Cilindro
{
public:
    // Constructor sin parámetros
    Cilindro()
    {
        radio = 2.0;
        altura = 2.0;
    };
 
    // Constructor con parámetros
    Cilindro(double radio, double altura)
    {
        this->radio = radio;
        this->altura = altura;
    };
 
    // Funciones (métodos)
    double volumen()
    {
        return PI * radio * radio * altura;
    }
 
private:
    // Variables miembro
    double radio{1};
    double altura{1};
};
 
Cilindro cilindro = Cilindro(4.5, 8);
std::cout << "volumen: " << cilindro.volumen() << std::endl;
```

También existen los **constructores por defecto**, que pueden ser llamados sin argumentos:

```cpp
#include <iostream>
 
const double PI{3.14159265358979323846264338};
 
class Cilindro
{
public:
    // Constructor por defecto
    Cilindro() = default;
 
    // Constructor con parámetros
    Cilindro(double radio, double altura)
    {
        this->radio = radio;
        this->altura = altura;
    };
 
    // Funciones (métodos)
    double volumen()
    {
        return PI * radio * radio * altura;
    }
 
private:
    // Variables miembro
    double radio{1};
    double altura{1};
};
 
Cilindro cilindro = Cilindro();
std::cout << "volumen: " << cilindro.volumen() << std::endl;
```

## Método destructor en clases

El método especial **destructor** se llama cuanto un objeto se borra de la memoria, es decir, muere. Son necesarios para definir las tareas de liberación de la memoria dinámica o limpiezas asociadas.

Por ejemplo, supongamos una clase `Perro` con una variable edad que hemos decidido almacenar dinámicamente, pues recae en nuestra mano como programadores liberar correctamente esa memoria en el destructor:

```cpp
#include <iostream>
 
class Perro
{
public:
    // Constructores
    Perro()
    {
        this->nombre = "Nada";
 
        // Memoria dinámica
        this->edad = new int;
        *this->edad = 0;
    }
 
    Perro(std::string nombre, int edad)
    {
        this->nombre = nombre;
 
        // Memoria dinámica
        this->edad = new int;
        *this->edad = edad;
    }
 
    // Destructor con tareas de limpieza
    ~Perro()
    {
        delete this->edad;
        std::cout << "Perro liberado de la memoria" << std::endl;
    }
 
private:
    std::string nombre;
    int *edad;
};
 
// Perro liberado de la memoria al finalizar la función
int main()
{
    Perro perro("Maxi", 3);
    return 0;
}
```

Debemos prestar atención porque si bien el momento de la destrucción a veces es obvio, como un objeto local sale de su ámbito o cuando liberamos un objeto del `heap`, en otros casos no lo es tanto, como cuando pasamos un objeto a una función o lo devolvemos un objeto desde una función:

```cpp
// Perro creado en memoria dinámica en la función
void funcion()
{
    Perro *perro = new Perro("Maxi", 3);
}
 
// Perro nunca liberado de la memoria
int main()
{
    funcion();
    return 0;
}
```

¡Recordemos siempre limpiar la memoria dinámica!

```cpp
// Perro creado en memoria dinámica en la función
void funcion()
{
    Perro *perro = new Perro("Maxi", 3);
    // Liberar la memoria
    delete perro;
}
 
// Perro liberado de la memoria dentro de la propia función
int main()
{
    funcion();
    return 0;
}
```

## Getters y Setters en clases

Los **getters** y **setters** son métodos de acceso para exponer los miembros privados de la clase, de manera que podamos controlar la forma de establecer y consultar los valores almacenados en ellos:

```cpp
#include <iostream>
 
const double PI{3.14159265358979323846264338};
 
class Cilindro
{
public:
    // Constructor por defecto
    Cilindro() = default;
 
    // Constructor con parámetros
    Cilindro(double radio, double altura)
    {
        this->radio = radio;
        this->altura = altura;
    };
 
    // Métodos getter
    double get_radio() const 
    {
        return this->radio;
    }

    double get_altura() const 
    {
        return this->altura;
    }
 
    // Métodos setter
    void set_radio(double radio)
    {
        this->radio = radio;
    }
 
    void set_altura(double altura)
    {
        this->altura = altura;
    }
 
    // Funciones (métodos)
    double volumen()
    {
        return PI * radio * radio * altura;
    }
 
private:
    // Variables miembro
    double radio{1};
    double altura{1};
};
 
Cilindro cilindro = Cilindro(3.1, 5.6);
std::cout << "volumen: " << cilindro.volumen() << std::endl;
cilindro.set_radio(4.5);
cilindro.set_altura(9.5);
std::cout << "volumen: " << cilindro.volumen() << std::endl;
std::cout << "altura: " << cilindro.get_altura() << std::endl;
```

## Organización de clases en ficheros

Para ejecutar y organizar de forma eficiente el código las clases suelen separar en **ficheros de cabeceras** (header files) con las declaraciones y **ficheros de fuentes** (source files) con las definiciones.

Además, para evitar dependencias cruzadas se utilizan guardas de inclusión `ifndef` que generan *wrappers*, espacios contenidos dentro de una cláusula para evitar la redefinición múltiple.

Adaptando el ejemplo del cilindro tendremos:

**cilindro.h**

Declaración o cabecera de la clase `Cilindro`:

```cpp
#ifndef CYLINDER_H
#define CYLINDER_H
 
#include "constantes.h"
class Cilindro
{
public:
    // Constructores
    Cilindro() = default;
    Cilindro(double radio, double altura);
 
    // métodos
    double volumen();
 
    // Métodos setter y getter
    double get_radio() const ;
    double get_altura() const ;
    void set_radio(double radio);
    void set_altura(double altura);
 
private:
    // Variables miembro
    double radio{1};
    double altura{1};
};
 
#endif
```

**cilindro.cpp**

Definición o fuente de la clase `Cilindro`:

```cpp
#include "cilindro.h"
 
// Constructor con parámetros
Cilindro::Cilindro(double radio, double altura)
{
    this->radio = radio;
    this->altura = altura;
};
 
// Métodos getter
double Cilindro::get_radio() const
{
    return this->radio;
}

double Cilindro::get_altura() const
{
    return this->altura;
}
 
// Métodos setter
void Cilindro::set_radio(double radio)
{
    this->radio = radio;
}
 
void Cilindro::set_altura(double altura)
{
    this->altura = altura;
}
 
// Funciones (métodos)
double Cilindro::volumen()
{
    return PI * radio * radio * altura;
}
```

**constantes.h**

Cabeceras con constantes potencialmente incluidas de forma cruzada:

```cpp
#ifndef CONSTANTS_H
#define CONSTANTS_H
 
const double PI {3.14159265358979323846264338327};
 
#endif
```

**main.cpp**

Fichero que incluirá las declaraciones y la función principal:

```cpp
#include <iostream>
#include "cilindro.h"
 
int main(){
    Cilindro cilindro(10,5);
    std::cout << "volumen: " << cilindro.volumen() << std::endl;
     
    return 0;
}
```

## Compilación y vinculación

Cuando trabajamos con múltiples ficheros, a la hora de compilar debemos tener en cuenta dos procesos distintos: la compilación (compiling) y la vinculación (linking).

* La **compilación** es la fase que traduce el programa a un código de nivel de ensamblaje de bajo nivel. El compilador toma el archivo preprocesado (sin ninguna directiva) y genera un archivo de objeto que contiene código de nivel de ensamblaje. Ahora, el archivo de objeto creado está en forma binaria. En el archivo de objeto creado, cada línea describe una instrucción de nivel de máquina de bajo nivel. La conversión a lenguaje ensamblador es importante ya que es un lenguaje de salida común para muchos compiladores de diferentes lenguajes de alto nivel.

* La **vinculación**, como sugiere el nombre, se refiere a la creación de un solo archivo ejecutable a partir de múltiples archivos de objetos. El archivo creado después de la vinculación está listo para ser cargado en la memoria y ejecutado por el sistema.

Los comandos para compilar y vincular son, por ejemplo a partir de un fichero principal **main.cpp** y unas utilidades con su cabecera **utilities.h** y fuente **utilities.cpp**:

* Compilación y vinculación: `g++ -o output.exe main.cpp utilities.cpp`
* Compilación: g++ `-c main.cpp utilities.cpp`
* Vinculación: g++ `-o output.exe main.o utilities.o`

Por otro lado, acerca de la **declaración** y la **definición** debemos tener en cuenta:

* Si el nombre no se utiliza nunca (no se llama la función o variable) en la función principal `main`, la definición no será necesaria.
* Si se compila sin una declaración, y el nombre es utilizado, se obtendrá un error de compilación de tipo `unknown name`.
* Si se compila una declaración sin una definición pero ésta no se llama en el código, la compilación funcionará.
* Si se compila una declaración sin una definición y ésta se llama en el código, la compilación dará un error de vinculación.

En este punto empezaremos a hablar de **unidades de traducción** (TU) una unidad básica de compilación en C++, consistente en el contenido de un solo archivo de fuente, más el contenido de cualquier archivo de encabezado incluido directa o indirectamente en él, exceptuando aquellas líneas que se ignoraron mediante instrucciones de preprocesamiento condicional.

Es importante tenerlo en cuenta porque la vinculación es una propiedad asociada a un nombre que controla su ámbito la visibilidad entre las **TU**.

Una **constante** tiene una vinculación interna, eso significa que es únicamente visible en la TU donde se ha declarado. Si se declara la variable de mismo nombre en otra **TU**, la variable creada será una definición separada de la anterior. Una variable definida mediante la cláusula extern implicará que tiene una vinculación externa, por lo que si es utilizada en otra **TU** vinculada, será la misma variable y esto también afectará a una **constante**. Así mismo, una función puede importarse como externa con la misma palabra `extern`:

```cpp
// main.cpp
#include <iostream>
 
double PI{3.14};           // Vinculación interna
extern const double E;     // Vinculación externa
int hola{6};               // Vinculación externa
 
extern void print();       // Vinculación externa
 
int main()
{
    std::cout << "&PI en main: " << &PI << std::endl;
    std::cout << "&hola en main: " << &hola << std::endl;
    print();
    return 0;
}
```

```cpp
// prueba.cpp
#include <iostream>
 
const double PI{3.14};        // vinculación interna
extern const double E{2.71};  // vinculación externa
extern int hola;              // vinculación externa
 
void print() // vinculación externa
{
    std::cout << "&PI en prueba: " << &PI << std::endl;
    std::cout << "&hola en prueba: " << &hola << std::endl;
}
```

```
$ g++ -o main.exe main.cpp utilities.cpp
$ ./main.exe
 
&PI en main: 0x7ff60c924020      <---- son diferentes
&E en main: 0x7ff7369a5088       <---- es la misma
&hola en main: 0x7ff60c924028    <---- es la misma
 
&PI en prueba: 0x7ff60c925070
&E en prueba: 0x7ff7369a5088
&hola en prueba: 0x7ff60c924028
```

Por último comentar que es posible realizar una **declaración adelantada** (forward declaration) de una clase para poder utilizarla en una cabecera, pero no podremos utilizar ninguno de sus miembros, solo la referencia del nombre:

```cpp
class Punto;
 
class Linea
{
public:
    Linea();
    ~Linea();
 
    // Funcionará sin que el compilador conozca los miembros
    void imprimir_punto(const Punto &p); 
 
    // No funcionará, el compilador no conoce los miembros
    void imprimir_punto(const Punto &p) {
        std::cout << p.x << ", " << p.y << std::endl;  
    }
}
```

## Métodos encadenados con puntero this

Ya comentamos que el puntero `this` es un realidad la dirección en la memoria donde se encuentra la instancia de la clase. Esto nos permite trabajar con la instancia de formas interesantes, por ejemplo consultar su dirección:

```cpp
#include <iostream>
 
class Perro
{
public:
    Perro(std::string nombre, int edad)
    {
        this->nombre = nombre;
        this->edad = new int;
        *this->edad = edad;
 
        std::cout << "Perro " << this->nombre
                  << " construido en " << this << std::endl;
    }
 
    ~Perro()
    {
        delete this->edad;
        std::cout << "Perro liberado de la memoria" << std::endl;
    }
 
private:
    std::string nombre;
    int *edad;
};

int main()
{
    Perro perro("Maxi", 3);
    return 0;
}
```
 
```
Perro Maxi construido en 0xc68c1ffa00
Perro liberado de la memoria
```

Pues algo muy interesante es que si devolvemos el puntero `this` en nuestros métodos, podemos encadenar la llamada de diferentes métodos, pues estamos devolviendo la propia instancia, aunque para ello necesitaremos contar desde el principio con la dirección de la instancia, algo que podemos solucionar creando el objeto dinámicamente en el **heap**:

```cpp
// Método que devuelve  el puntero this para encadenarlos
Perro *set_nombre(std::string nombre)
{
    this->nombre = nombre;
    return this;
}

// Método que devuelve  el puntero this para encadenarlos
Perro *set_edad(int edad)
{
    *this->edad = edad;
    return this;
}
 
void info()
{
    std::cout << "Perro " << this->nombre
              << " con edad " << *this->edad << std::endl;
}

int main()
{
    Perro *perro = new Perro("Maxi", 3);
    perro->set_nombre("Fox")->set_edad(5)->info();
    delete perro;
 
    return 0;
}
```

```
Perro Maxi construido en 0x19dc22b6f90
Perro Fox con edad 5
Perro liberado de la memoria
```

Si preferimos trabajar en el **stack** y no almacenar la memoria dinámicamente, podemos obtener el mismo resultado mediante el retorno de las referencias del punteros `this` con `&`:

```cpp
// Método que devuelve la referencia de this para encadenarlos
Perro &set_nombre(std::string nombre)
{
    this->nombre = nombre;
    return *this;
}
// Método que devuelve la referencia de this para encadenarlos
Perro &set_edad(int edad)
{
    *this->edad = edad;
    return *this;
}

int main()
{
    Perro perro = Perro("Maxi", 3);
    perro.set_nombre("Fox").set_edad(5).info();
 
    return 0;
}
```

```
Perro Maxi construido en 0xeaa71ffa80
Perro Fox con edad 5
Perro liberado de la memoria
```

## Diferencias entre Class y Struct

A parte de las clases `class`, también encontramos el tipo estructura `struct`, cuya diferencia clave es que sus miembros son públicos por defecto.

Por ejemplo, en esta clase `Perro` no podemos acceder directamente a los miembros:

```cpp
class Perro
{
    std::string nombre;
};
 
int main()
{
    Perro perro;
    perro.nombre = "Maxi"; // Error, miembro privado
 
    return 0;
}
```

Pero sí podemos hacerlo en su versión con `struct`:

```cpp
struct Perro
{
    std::string nombre;
};
 
int main()
{
    Perro perro;
    perro.nombre = "Maxi"; // Funciona, miembro público
    std::cout << perro.nombre << std::endl;
 
    return 0;
}
```

```
Maxi
```

Esta capacidad hace a las estructuras perfectas para almacenar datos simples sin tener que desarrollar la lógica de las clases.

De hecho, existe una forma de extraer la información de una estructura muy rápidamente mediante **bindings**:

```cpp
struct Perro
{
    std::string nombre;  // indice 0
    int edad;            // indice 1
};
 
int main()
{
    Perro perro {"Maxi", 5}; 
    auto [nombre, edad] = perro;  // 0, 1
    std::cout << "Nombre: " << nombre << std::endl;
    std::cout << "Edad: " << edad << std::endl;
 
    return 0;
}
```

```
Nombre: Maxi
Edad: 5
```

## Acerca de los objetos constantes

Un objeto puede declararse constante, como cualquier otra variable en C++:

```cpp
const double PI{3.14159265358979323846264338};
 
class Cilindro
{
public:
    // Constructor con parámetros
    Cilindro(double radio, double altura)
    {
        this->radio = radio;
        this->altura = altura;
    };
 
    // Métodos getter
    double get_radio() const
    {
        return this->radio;
    }

    double get_altura() const
    {
        return this->altura;
    }
 
    // Métodos setter 
    void set_radio(double radio)
    {
        this->radio = radio;
    }
 
    void set_altura(double altura)
    {
        this->altura = altura;
    }
 
    // Funciones (métodos)
    double volumen()
    {
        return PI * radio * radio * altura;
    }
 
private:
    // Variables miembro
    double radio{1};
    double altura{1};
};

const Cilindro cilindro = Cilindro(3.1, 5.6);
```

La propiedad `const` afecta después de la construcción y finaliza antes de la destrucción de la instancia, en otras palabras, el constructor y destructor pueden modificar los miembros del objeto pero todos los demás métodos no pueden:

```cpp
std::cout << cilindro.volumen() << std::endl;  // Error
```

Sin embargo, si definimos una función miembro como constante, tendremos acceso a ella:

```cpp
double volumen() const  // <-----
{
    return PI * radio * radio * altura;
}
```

Y ahora la llamada funcionará:

```cpp
std::cout << cilindro.volumen() << std::endl;  // 169.06
```

El puntero `this` que se envía a las funciones miembro constantes es un puntero constante, eso significa que el puntero no se puede utilizar para modificar los objetos de los miembros, cualquier intento de cambiar la información desde esas funciones dará error:

```cpp
double volumen() const
{
    this->radio = 10; // Error
    return PI * radio * radio * altura;
}
```

Los objetos constantes solo pueden llamar funciones miembro constantes, los objetos no constantes tienen acceso tanto a las funciones mimbro constantes como no constantes.

Una función miembro constante puede sobrecargarse con una versión no constante de la misma, la elección de la versión la hará el compilador en función de que el objeto que la llama sea o no constante.

Así mismo, los constructores y destructores jamás deben declararse como constantes, pues ellos siempre deben tener acceso a modificar el objeto aunque éste sea constante (son el principio y fin de su ciclo de vida).

Como curiosidad, las funciones miembro estáticas no pueden definirse como constantes, la palabra `const` modifica el puntero `this` pasado a la función, pero las funciones miembro estáticas `static` no envían el puntero `this` al poder ser llamadas sin instanciar un objeto.

!!! tip "Buenas prácticas"
    Cualquier función miembro **no estática que no modifique** los datos miembro del objeto, debería declararse como `const` para poder trabajar con objetos constantes.

## Getters actuando como setters

Puede ser que en algún momento nos interese devolver una referencia en un método de una clase, en ese caso debemos tener en cuenta que el objeto miembro devuelto será modificable a través del método:

```cpp 
#include <iostream>
 
const double PI{3.14159265358979323846264338};
 
class Cilindro
{
public:
    // Constructor con parámetros
    Cilindro(double radio, double altura)
    {
        this->radio = radio;
        this->altura = altura;
    };
 
    // La referencia es modificable!
    double &get_radio()
    {
        return this->radio;
    }
    // La referencia es modificable!
    double &get_altura() 
    {
        return this->altura;  
    }
 
    double volumen() const
    {
        return PI * radio * radio * altura;
    }
 
private:
    // Variables miembro
    double radio{1};
    double altura{1};
};

Cilindro cilindro = Cilindro(3.1, 5.6);
std::cout << cilindro.volumen() << std::endl;
cilindro.get_radio() = 10.6; // Es modificable!
std::cout << cilindro.volumen() << std::endl;
```

Definir la referencia como constante solucionará el problema, e idealmente definir la función como miembro constante añadiría otra capa de seguridad:

```cpp
const double &get_radio() const
{
    return this->radio;
}

const double &get_altura() const
{
    return this->altura;
}

cilindro.get_radio() = 10.6; // Error, no es modificable!
```

## Inicialización listada en constructor

Esta es una técnica que consiste en indicar de forma listada los miembros a inicializar en el constructor, tiene algunas ventajas como evitar copias innecesarias de los datos e incluso en algunos casos son la única forma de inicializar un objeto.

En la **inicialización por copia**:

```cpp
// Constructor clásico con inicialización de valores copiados
Cilindro(double radio, double altura)
{
    this->radio = radio;
    this->altura = altura;
};
```

* El objeto se crea y los miembros se asignan a partir de las variables.
* Se generan copias innecesarias de los datos.
* El orden de las variables miembro no importa.

En la **inicialización listada**:

```cpp
// Constructor listado con inicialización directa en miembros
Cilindro(double radio, double altura) : radio(radio), altura(altura){ };
```

* La inicialización ocurre en la creación real del objeto.
* Se evitan copias innecesarias.
* El orden de las variables miembro importa.

## Constructores explícitos y delegados

Hablemos de algunas características de los constructores, empezando por la cláusula `explicit`, que indica al constructor que utilice conversiones explícitas en los tipos de datos:

```cpp
class Punto
{
public:
    // Conversión explícita a enteros
    explicit Punto(int x, int y) : x(x), y(y){};
    void print()
    {
        std::cout << "(" << x << ", " << y << ")\n";
    }
 
private:
    double x{}, y{};
};

Punto p(14.76, 84.25);
p.print(); // (14, 84) <-- ¡Son enteros!
```

También podemos **delegar un constructor** a otro, por ejemplo, con una inicialización vacía:

```cpp
// Constructor delegado
Punto() : Punto(5, 5) {}
 
// Se llamará a este constructor en caso de no enviar argumentos
explicit Punto(int x, int y) : x(x), y(y){};

Punto p;
p.print(); // (5, 5)
```

## Copia de objetos (shallow/deep) en constructores

En C++ un constructor puede recibir una instancia para realizar una copia de los valores uno a uno:

```cpp
class Punto
{
public:
    Punto(double x, double y) : x(x), y(y){};
    void print()
    {
        std::cout << "(" << x << ", " << y << ") "
                  << "[" << this << "]" << std::endl;
    }
    void set(double x, double y)
    {
        this->x = x;
        this->y = y;
    }
 
private:
    double x{}, y{};
};

Punto p1(5, 5);
Punto p2(p1);
p1.print(); // (5, 5) [0x952e7ffd20]
p2.print(); // (5, 5) [0x952e7ffd10]
 
// Si editamos el primer punto solo cambiará ese
p1.set(10, 10);
p1.print(); // (10, 10) [0x952e7ffd20]
p2.print(); // (5, 5) [0x952e7ffd10]
```

Hasta aquí todo es correcto, el problema aparece cuando nuestras clases contienen miembros que son punteros o en otras palabras, están almacenados en el **heap**, pues en esa situación no se copiarán los valores sino que se copiara la dirección en la memoria, implicando que en ambos objetos el miembro apunte al mismo lugar:

```cpp
class Punto
{
public:
    ~Punto()
    {
        delete this->x;
        delete this->y;
    }
 
    // Al trabajar con punteros crearemos los datos dinámicamente
    Punto(double x, double y) : x(new double(x)), y(new double(y)){};
 
    void set(double x, double y)
    {
        *(this->x) = x;
        *(this->y) = y;
    }
 
    void print()
    {
        std::cout << "(" << *x << ", " << *y << ") "
                  << "[" << this << "]" << std::endl;
    }
 
private:
    double *x{}, *y{};  // Ahora trabajamos con punteros
};

Punto p1(5, 5);
Punto p2(p1);
p1.print(); // (5, 5) [0xca45fffba0]
p2.print(); // (5, 5) [0xca45fffb90]
 
// Si editamos el primer punto cambiarán ambos
p1.set(10, 10);
p1.print(); // (10, 10) [0xca45fffba0]
p2.print(); // (10, 10) [0xca45fffb90]
```

Para solucionar esto podemos crear unos **getters** que devuelvan el valor de los miembros privados y sobrecargar un constructor para que copie directamente los valores consultando estos getters a partir de la referencia del objeto:

```cpp
class Punto
{
public:
    ~Punto()
    {
        delete this->x;
        delete this->y;
    }
 
    Punto(double x, double y) : x(new double(x)), y(new double(y)){};
 
    // Creamos unos getters
    double *get_x() const { return this->x; }
    double *get_y() const { return this->y; }
 
    // Sobrecargamos un constructor que tome los datos de un Punto
    Punto(Punto &p) : Punto(*(p.get_x()), *(p.get_y())){};
 
    void set(double x, double y)
    {
        *(this->x) = x;
        *(this->y) = y;
    }
 
    void print()
    {
        std::cout << "(" << *x << ", " << *y << ") "
                  << "[" << this << "]" << std::endl;
    }
 
private:
    double *x{}, *y{};
};

Punto p1(5, 5);
Punto p2(p1);
p1.print(); // (5, 5) [0xca45fffba0]
p2.print(); // (5, 5) [0xca45fffb90]
 
// Si editamos el primer punto solo cambiará ese
p1.set(10, 10);
p1.print(); // (10, 10) [0xca45fffba0]
p2.print(); // (5, 5) [0xca45fffb90]
```

**Shallow Copy (copia superficial)**

La forma de copiar directamente los valores se conoce como **Shallow Copy** (copia superficial) y funcione bien mientras no haya ningún miembro almacenado en el **heap**. 

En el momento en que realizamos una copia con valores en el **heap** (memoria dinámica), entonces debemos ser conscientes que copiarlos directamente afectará a la dirección de memoria y no tendremos una copia, sino un acceso entre a la misma información.

**Deep Copy (copia profunda)**

Si implementamos una copia por valores real para los datos del **heap** almacenando nueva memoria, tal como hemos hecho en el segundo ejemplo, ésta se denomina **Deep Copy** (copia profunda).

## Manejo secuencial de objetos en arreglos

Manejar objetos en arreglos es muy sencillo, tenemos distintas formas dependiendo de si queremos contar con copias o referencias a los mismos para poder modificarlos:

```cpp
#include <iostream>
 
class Punto
{
public:
    ~Punto()
    {
        delete this->x;
        delete this->y;
    }
 
    Punto(double x, double y) : x(new double(x)), y(new double(y)){};
 
    // Creamos unos getters y setters
    double *get_x() const { return this->x; }
    double *get_y() const { return this->y; }
 
    // Sobrecargamos un constructor que tome los datos de un Punto
    Punto(Punto &p) : Punto(*(p.get_x()), *(p.get_y())){};
 
    void set(double x, double y)
    {
        *(this->x) = x;
        *(this->y) = y;
    }
 
    void print()
    {
        std::cout << "(" << *x << ", " << *y << ") "
                  << "[" << this << "]" << std::endl;
    }
 
private:
    double *x{}, *y{};
};
 
Punto p1(5, 4), p2(3, 4), p3(1, 2);
Punto puntos[]{p1, p2, p3, Punto(p3), Punto(7, 5)};
```

Por ejemplo podemos recorrer con copias, aunque eso utilizará más memoria de la necesaria:

```cpp
// Cuando recorremos los objetos generamos copias
for (Punto p : puntos)
{
    p.set(*(p.get_x()) * 2, *(p.get_y()) * 2);
    p.print();
}
```

```
(10, 8) [0xe03d7ff6a0]
(6, 8) [0xe03d7ff6a0]
(2, 4) [0xe03d7ff6a0]
(2, 4) [0xe03d7ff6a0]
(14, 10) [0xe03d7ff6a0]
```

Mediante las referencias podemos modificar los objetos originales y ahorrar memoria:

```cpp
// Con referencia podemos modificar los objetos
for (Punto &p : puntos)
{
    p.set(*(p.get_x()) * 2, *(p.get_y()) * 2);
    p.print();
}
```

```
(10, 8) [0x38197ff5e0]
(6, 8) [0x38197ff5f0]
(2, 4) [0x38197ff600]
(2, 4) [0x38197ff610]
(14, 10) [0x38197ff620]
```

Si queremos referencias a objetos constantes, deberemos recordar marcar los métodos necesarios como constantes:

```cpp
// Método llamable por objetos constantes
void print() const
{
    std::cout << "(" << *x << ", " << *y << ") "
              << "[" << this << "]" << std::endl;
}
```

```cpp
// Con referencia a objetos prevenimos la modificación
for (const Punto &p : puntos)
{
    p.set(*(p.get_x()) * 2, *(p.get_y()) * 2); // Error
    p.print();
}
```

```
(5, 4) [0x5ab5bffb20]
(3, 4) [0x5ab5bffb30]
(1, 2) [0x5ab5bffb40]
(1, 2) [0x5ab5bffb50]
(7, 5) [0x5ab5bffb60]
```

Y no podemos olvidar la gestión secuencial clásica mediante índices, pues accediendo directamente al arreglo tampoco realizaremos copias, aunque **aquí los objetos sí serán modificables**:

```cpp
// Un loop normal tampoco generará copias
for (size_t i{}; i < std::size(puntos); i++)
{
    puntos[i].set(0, 0);
    puntos[i].print();
    // (puntos + i)->print();
    // (*(puntos + i)).print();
}
```

```
(0, 0) [0xc71cbff930]
(0, 0) [0xc71cbff940]
(0, 0) [0xc71cbff950]
(0, 0) [0xc71cbff960]
(0, 0) [0xc71cbff970]
```

___
<small class="edited"><i>Última edición: 09 de Mayo de 2022</i></small>