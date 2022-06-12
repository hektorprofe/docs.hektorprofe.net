title: Decodificación de ficheros PNG | Programación de gráficos 3D | Hektor Profe
description: 

# Decodificación de ficheros PNG

El siguiente paso es cargar las texturas desde imágenes, para ello utilizaremos una biblioteca ya existente llamada [upng](https://github.com/elanthis/upng).

Simplemente copiamos `upng.h` y `upng.c` al directorio `src`, le cambiamos el nombre a `upng.cpp` para compilarlo y los agregamos al proyecto.

Si intentamos compilar en **Visual Studio** nos pedirá cambiar la función `fopen` por `fopen_s`, la versión segura, básicamente es cambiar esta línea de `upng.cpp`:

```cpp
fopen_s(&file, filename, "rb");
``` 

Tengo esta textura en un png llamado `cube.png` guardado en el directorio `res`:

![]({{cdn}}/graficos3d/image-101.png)

Lo que haré es inicializar el mesh `cube.obj` pasándole también la ruta de la textura, todo lo demás referente a la textura actual puedo borrarlo de la ventana:

```cpp
/* Mesh loading */
mesh = Mesh(this, "res/cube.obj", "res/cube.png");
```

La nueva firma quedará:

```cpp
Mesh(Window *window, std::string modelFileName, std::string textureFileName);
```

A partir de ahora nuestro `mesh` también almacenará la textura y su información:

```cpp
class Mesh
{

private:
    int textureWidth{ 0 };
    int textureHeight{ 0 };
    upng_t *pngTexture{ nullptr };
    uint32_t* meshTexture{ nullptr };
};
```

Para cargar la textura en el constructor, después de cargar el modelo haremos:

```cpp
Mesh::Mesh(Window* window, std::string modelFileName, std::string textureFileName)
{
    // Load the texture after loading the model
    pngTexture = upng_new_from_file(textureFileName.c_str());
    if (pngTexture == NULL)
    {
        std::cerr << "Error reading the file " << textureFileName << std::endl;
        return;
    }

    upng_decode(pngTexture);
    if (upng_get_error(pngTexture) == UPNG_EOK)
    {
        meshTexture = (uint32_t*)upng_get_buffer(pngTexture);
        textureWidth = upng_get_width(pngTexture);
        textureHeight = upng_get_height(pngTexture);
        std::cout << "Texture loaded: " << textureFileName << " " << textureWidth << "x" << textureHeight << std::endl;
    }
}
```

Tendremos que enviar la textura y su tamaño al dibujar el texel:

```cpp
window->DrawTexturedTriangle(
    sortedTriangles[i].projectedVertices[0].x, sortedTriangles[i].projectedVertices[0].y, sortedTriangles[i].projectedVertices[0].z, sortedTriangles[i].projectedVertices[0].w, sortedTriangles[i].textureUVCoords[0],
    sortedTriangles[i].projectedVertices[1].x, sortedTriangles[i].projectedVertices[1].y, sortedTriangles[i].projectedVertices[1].z, sortedTriangles[i].projectedVertices[1].w, sortedTriangles[i].textureUVCoords[1],
    sortedTriangles[i].projectedVertices[2].x, sortedTriangles[i].projectedVertices[2].y, sortedTriangles[i].projectedVertices[2].z, sortedTriangles[i].projectedVertices[2].w, sortedTriangles[i].textureUVCoords[2],
    meshTexture, textureWidth, textureHeight);
```

Esta información la recibiremos en el método y la pasaremos a las dos llamadas de `DrawTexel`:

```cpp
void Window::DrawTexturedTriangle(int x0, int y0, float z0, float w0, Texture2 uv0, int x1, int y1, float z1, float w1, Texture2 uv1, int x2, int y2, float z2, float w2, Texture2 uv2, uint32_t* texture, int textureWidth, int textureHeight)
{
    // ...
    DrawTexel(x, y, pA, pB, pC, uv0, uv1, uv2, uDivW, vDivW, oneDivW, texture, textureWidth, textureHeight);
}
```

Y las utilizaremos en lugar de recibirlas desde el puntero `window` como hasta ahora:

```cpp
void Window::DrawTexel(int x, int y, Vector4 a, Vector4 b, Vector4 c, Texture2 t0, Texture2 t1, Texture2 t2, float *uDivW, float* vDivW, float* oneDivW, uint32_t *texture, int textureWidth, int textureHeight)
{
    // ...
    // Calculate the texelX and texelY based on the interpolated UV and the texture sizes
    int texelX = abs(static_cast<int>(interpolatedU * textureWidth));
    int texelY = abs(static_cast<int>(interpolatedV * textureHeight));

    // Finally draw the pixel with the color stored in our texture harcoded array
    DrawPixel(x, y, texture[(textureWidth * texelY) + texelX]);
}
```

Solo nos falta añadir un método para liberar la textura de la memoria:

```cpp
void Mesh::Free()
{
    upng_free(pngTexture);
}
```

Y lo llamamos en el destructor de la `window`:

```cpp
Window::~Window()
{
    // Liberamos la textura del mesh
    mesh.Free();
}
```

Si ejecutamos el programa notaremos algo extraño:

![]({{cdn}}/graficos3d/image-102.png)

La verdad es que nos falta configurar las coordenadas UV y por eso se rellena todo el cubo con el color del primer píxel.

En la próxima sección voy a implementar la lectura de las coordenadas UV desde ficheros obj, pero antes fijémonos en el color del primer píxel, no concuerda con el de la textura:

![]({{cdn}}/graficos3d/image-103.png)

Esto es debido a que la biblioteca `upng` únicamente soporta colores RGB, RGBA. escala de grises y escala de grises con transparencia alpha. Sin embargo nuestro buffer de color está configurado sobre una textura SDL con formato de píxel `SDL_PIXELFORMAT_RGBA8888`. 

Según la [wiki de SDL](https://wiki.libsdl.org/SDL_PixelFormatEnum) un formato compatible con el que lee `upng` sería `SDL_PIXELFORMAT_RGBA32`, así que vamos a cambiarlo:

```cpp
void Window::Setup()
{
    // Crear la textura SDL utilizada para mostrar el color buffer
    colorBufferTexture = SDL_CreateTexture(renderer, SDL_PIXELFORMAT_RGBA32, SDL_TEXTUREACCESS_STREAMING, windowWidth, windowHeight);
}
```

Con esto ya deberíamos dibujar el color correcto del primer píxel:

![]({{cdn}}/graficos3d/image-104.png)

___
<small class="edited"><i>Última edición: 05 de Junio de 2022</i></small>