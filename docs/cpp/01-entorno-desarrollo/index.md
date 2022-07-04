title: Entorno de desarrollo | Apuntes lenguaje C++ | Hektor Profe
description: Instalación y configuración del entorno Visual Studio Code para programar en C++.

# Entorno de desarrollo en C++

## Compiladores C++ en Windows

Empezamos la aventura instalando en Windows diferentes compiladores para código C++.

En primer lugar MinGW (Minimalist GNU for Windows) y Clang LLVM los podemos encontrar en [https://winlibs.com/](https://winlibs.com/), concretamente en el ZIP para 64 bits [GCC 11.2.0 + LLVM/Clang/LLD/LLDB 13.0.0 + MinGW-w64 9.0.0 (MSVCRT)](https://github.com/brechtsanders/winlibs_mingw/releases/download/11.2.0-13.0.0-9.0.0-msvcrt-r3/winlibs-x86_64-posix-seh-gcc-11.2.0-llvm-13.0.0-mingw-w64-9.0.0-r3.zip).

Después de descomprimirlo en el disco C:\mingw64 y añadir el directorio C:\mingw64\bin al PATH de sistema puedo comprobar que dispongo tanto del compilador g++ como clang++ en una terminal:

![]({{cdn}}/cpp/image.png)

Así mismo he instalado el compilador MSVC de [Visual Studio Community 2019](https://visualstudio.microsoft.com/es/vs/older-downloads/), que podemos comprobar mediante cl.exe en la Developer PowerShell:

![]({{cdn}}/cpp/image-2.png)

Las diferentes funcionalidades soportadas por cada compilador pueden encontrarse en las tablas comparativas en la web [https://en.cppreference.com/w/cpp/compiler_support](https://en.cppreference.com/w/cpp/compiler_support).

Sin más, lo próximo será configurar algún editor para empezar a programar código.

## Ejecutar código C++ con VSC

Una vez configurados los compiladores deseados, la forma más sencillo de compilar y ejecutar un fichero en VSC es instalar la extensión [Code Runner](https://marketplace.visualstudio.com/items?itemName=formulahendry.code-runner).

Una vez instalada, para compilar y ejecutar el típico `Hola Mundo`, podemos crear un main.cpp en un directorio, presionar F1 y buscar la opción `Run Code`:

```cpp
#include <iostream>
 
int main()
{
    std::cout << "Hola Mundo!";
    return 0;
}
```

El resultado será la salida por pantalla:

![]({{cdn}}/cpp/image-3.png)

Debemos tener en cuenta que esta extensión probará un compilador automáticamente.

Si queremos extender la configuración de compilación deberemos crear un directorio `.vscode` en el proyecto y un fichero `settings.json` establecer la configuración deseada.

Por ejemplo para utilizar `GCC++20`:

```json
{
    "code-runner.executorMap": {
        "cpp": "cd $dir && g++ -std=c++20 *.cpp -o $fileNameWithoutExt && ./$fileNameWithoutExt.exe"
    }
}
```

![]({{cdn}}/cpp/image-6.png)

Para utilizar `Clang++20`:

```json
{
    "code-runner.executorMap": {
        "cpp": "cd $dir && clang++ -std=c++20 *.cpp -o $fileNameWithoutExt && ./$fileNameWithoutExt.exe"
    }
}
```

![]({{cdn}}/cpp/image-5.png)

Para utilizar `Cl++latest`:

```json
{
    "code-runner.executorMap": {
        "cpp": "cd $dir && cl.exe /Zi /std:c++latest /EHsc /Fe: $fileNameWithoutExt.exe $fileName && $dir$fileNameWithoutExt.exe",
    }
}
```

*Nota*: Para hacer funcionar la configuración de `CL` se debe abrir `Visual Studio Code` desde la `Developer Powershell` estando situado en el directorio del proyecto:

```bash
cd /directorio/proyecto
code .
```

![]({{cdn}}/cpp/image-4.png)

Por mi parte estaré utilizando generalmente la configuración de GCC+20, por lo que configuraré por defecto el editor de esa forma desde `Archivo > Preferencias > Configuración`. Buscando la opción `code-runner.executorMap`:

![]({{cdn}}/cpp/image-7.png)

Y ahí estableciendo una configuración por defecto para ahorrarme el `settings.json` en cada proyecto:

![]({{cdn}}/cpp/image-8.png)

*Consejo*: Podemos añadir un `cls &&` justo después de `cd $dir` para limpiar la terminal (o `clear` en Linux/Mac):

![]({{cdn}}/cpp/image-11.png)

En cuanto al intelliSense (remarcador de sintaxis), para que sea compatible con la versión 20 se hace desde `Ver > Paleta de comandos > C/C++: Editar configuraciones (UI)`:

![]({{cdn}}/cpp/image-9.png)

En la nueva ventana cambiaremos esta opción:

![]({{cdn}}/cpp/image-10.png)

Sin más, con esto deberíamos tenerlo todo listo.

## Primer programa en C++

Como es costumbre se puede empezar a aprender creando un programa `Hola Mundo`:

```cpp
#include <iostream>
 
int main()
{
    std::cout << "Hello World!" << std::endl;
    return 0;
}
```

En la primera línea encontramos la importación de un componente de la biblioteca estándar (STL) de C++ para manejar operaciones de entrada/salida.

Si no lo importamos el editor se quejará haciendo referencia a que los miembros `cout` y `endl` no se encuentran definidos:

![]({{cdn}}/cpp/image-12.png)

El nombre `iostream` es un acrónimo de `Input/Output Stream` y es que el flujo de entrada y salida de datos en C++ (y su predecesor C) no se encuentra definida dentro de la sintaxis básica y se provee por medio de librerías de funciones especializadas como ésta, que define los siguientes objetos:

* `cin`: Flujo de entrada
* `cout`: Flujo de salida
* `cerr`: Flujo de error no almacenado.
* `clog`: Flujo de error almacenado.
* `endl`: Fin de línea.

En cualquier caso, lo que encontramos en nuestro programa es un primer bloque de código:

```cpp
int main()
{
}
```

Este bloque es una función cuyo nombre es main y este nombre es muy especial pues le indica al programa que esta es la función principal y se debe empezar a ejecutar desde aquí. Además como es lógico solo puede existir una única función main en el programa.

En cuanto al texto impreso en la terminal, corresponde a la porción:

```cpp
std::cout << "Hello World!" << std::endl;
```

Aquí tenemos la instrucción `std::cout` para iniciar un flujo de salida y el operador de inserción `<<` que permite insertar en el flujo caracteres entre comillas dobles, acabando con la inserción de un fin de línea `std::endl` y el respectivo punto y coma `;` que finaliza la instrucción.

Esta instrucción podemos escribirla varias veces para imprimir tantas líneas como deseemos:

```cpp
std::cout << "Primera linea" << std::endl;
std::cout << "Segunda linea" << std::endl;
std::cout << "Tercera linea" << std::endl;
```

Finalmente, la función principal main espera algún tipo de retorno para saber que el programa ha finalizado, generalmente se indica un return 0 para devolver un número 0:

```cpp
return 0;
```

Como punto interesante comentar que, por defecto este código fuente se ejecuta en la terminal de Windows sin codificación, incapaz de entender los símbolos especiales latinos:

![]({{cdn}}/cpp/image-15.png)

Podemos importar la librería `Windows.h` y justo antes de mostrar por pantalla el texto establecer la codificación UTF-8 para que la terminal decodifique correctamente los símbolos:

![]({{cdn}}/cpp/image-14.png)

Con esto hemos revisado las instrucciones básicas de un programa con C++.

___
<small class="edited"><i>Última edición: 07 de Mayo de 2022</i></small>