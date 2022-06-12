title: Migrando a Visual Studio | Programación de gráficos 3D | Hektor Profe
description: 

# Migrando a Visual Studio

Desde que estoy utilizando **Dear ImGui** notado que el proceso de compilación manual empiez a alargarse y he decidido probar qué tal con **Visual Studio 2019**. El resultado ha sido satisfactorio, la compilación es más rápida y se puede debugear fácilmente, así que he decidido migrar el proyecto.

Era mi primera vez utilizando este IDE y ha sido un poco confuso por la forma de disponer los ficheros, pero cuando aprendes como funciona es de hecho bastante simple.

He decidido reorganizar el código del proyecto en la carpeta `src` y los recursos en la carpeta `res`. Luego simplemente los arrastras a los filtros de explorador y ya lo tienes preparados:

![]({{cdn}}/graficos3d/image-85.png)

Como **Dear ImGui** hay que compilarlo, he movido su código al directorio `src/vendor/imgui` y con un par de filtros lo puedo visualizar cómodamente en el árbol de archivos del proyecto.

Para hacer funcionar `SDL` he descargado el fichero [SDL2-devel-2.0.22-VC.zip (Visual C++ 32/64-bit)](http://sdl2-devel-2.0.22-vc.zip/), lo he descomprimido en mi disco `C:/vclibs` y he añadido la carpeta `C:\vclibs\SDL2-2.0.22\lib\x64` con la biblioteca `SDL2.dll` al PATH de mi sistema para no tener que ir copíandolo todo el rato en el directorio de los ejecutables. 

A continuación, ya en el proyecto, he necesitado añadir los directorios `include` y `lib` de la librería `SDL`, haciendo clic derecho `Propiedades` en el proyecto. Ahí con la plataforma `x64` en `Directorios de VC++` en las secciones `Directorios de archivos de inclusión` y `Directorios de archivos de bibliotecas`:

![]({{cdn}}/graficos3d/image-86.png)

Luego en el apartado `Vinculador` he añadido las dependencias adicionales de compilación `SDL2.lib;SDL2main.lib;`:

![]({{cdn}}/graficos3d/image-87.png)

Finalmente hay que decirle donde debe ir a buscar `ImGui` para compilarlo en el apartado `C/C++ > General > Directorios de inclusión adicionales`:

![]({{cdn}}/graficos3d/image-88.png)

He tenido que cambiar algunas cosillas donde el compilador de Visual Studio se quejaba, pero poca cosa:

![]({{cdn}}/graficos3d/image-89.png)

___
<small class="edited"><i>Última edición: 05 de Junio de 2022</i></small>