title: Ordenar caras por profundidad | Programación de gráficos 3D | Hektor Profe
description: 

# Ordenar caras por profundidad

Por ahora el sistema rasteriza los colores de los triángulos por el orden como le llegan pero eso no es lo óptimo, debemos rasterizar teniendo presente la profundidad de las caras.

Para ilustrar este problema voy a modificar el programa para que las caras tengan colores distintos, así que vamos a almacenar un color que inicialmente será blanco y a utilizarlo:

```cpp
class Triangle
{
public:
    uint32_t color = 0xFFFFFFFF;
}

// Triángulos
if (window->drawFilledTriangles)
{
    window->DrawFilledTriangle(
        triangles[i].projectedVertices[0].x, triangles[i].projectedVertices[0].y,
        triangles[i].projectedVertices[1].x, triangles[i].projectedVertices[1].y,
        triangles[i].projectedVertices[2].x, triangles[i].projectedVertices[2].y,
        triangles[i].color);
}
```

Como el modelo de blender no aporta el color de una cara vamos a crear el cubo manualmente y aportaremos los colores de las caras a mano, **eso sí, debemos añadir 1 a los índices porque es el cambio que hicimos respecto a los modelos de blender**:

```cpp
Vector3 meshVertices[]{
    {-1, -1, -1},
    {1, -1, -1},
    {-1, 1, -1},
    {1, 1, -1},
    {-1, -1, 1},
    {1, -1, 1},
    {-1, 1, 1},
    {1, 1, 1}
};

Vector3 meshFaces[]{
    {2, 1, 3},
    {2, 3, 4},
    {5, 6, 8},
    {5, 8, 7},
    {2, 8, 6},
    {2, 4, 8},
    {5, 3, 1},
    {5, 7, 3},
    {3, 8, 4},
    {3, 7, 8},
    {2, 6, 5},
    {2, 5, 1}
};

uint32_t meshColors[]{
    0xFFFF0000, 
    0xFFFF0000, 
    0xFF00FF00, 
    0xFF00FF00, 
    0xFF0000FF, 
    0xFF0000FF, 
    0xFFFFA500, 
    0xFFFFA500, 
    0xFFFFFF00, 
    0xFFFFFF00, 
    0xFF00FFFF, 
    0xFF00FFFF
};

mesh = Mesh(this, meshVertices, 8, meshFaces, 12, meshColors);
//mesh = Mesh(this, "assets/cube.obj");
```

El color de los triángulos los inicializaremos con un constructor que que recibirá el color al crearlo:

```cpp
Triangle() = default;
Triangle(uint32_t color) : color(color){};
```

Simplemente lo estableceremos al generar los triángulos:

```cpp
Mesh::Mesh(Window *window, Vector3 *vertices, int verticesLength, Vector3 *faces, int facesLength, uint32_t *colors)
{
    // ...
    this->triangles.push_back(Triangle(colors[i])); // con color
};
```

Como demuestra la siguiente animación, los colores de las caras se mezclan cuando el **back face culling* está desactivado, no nos es posible apreciar correctamente la profundidad de las caras traseras del cubo:

![]({{cdn}}/graficos3d/anim-15.gif)

## Algoritmo del pintor

Hay varias formas de resolver nuestro problema, más adelante trataré un sistema llamado `Z-Buffer` pero por ahora introduciré un mecanismo llamado **algoritmo del pintor**.

Este algoritmo explica que el dibujado se debe realizar por capas, empezando por las más profundas y luego las más cercanas. Esto implica que deberemos encontrar un valor para la profundidad de cada cara, ordenarlas a partir de ese número y finalmente dibujarlas de atrás hacia adelante.

Aplicando esto al código, al renderizar el `mesh`, las caras serán préviamente ordenadas en profundidad `z`:

```cpp
void Mesh::Render()
{
    // !!! Antes de renderizar triángulos ordenarlos por media de profundidad

    for (size_t i = 0; i < triangles.size(); i++) { }
}
```

¿Cómo sacamos esa profundidad de la cara? ¿Cómo computa si cada vértice puede tener una profundidad `z` diferente?

![]({{cdn}}/graficos3d/image-64.png)

Pues lo que haremos es una asunción muy sencilla, la **profundidad de la cara** será la **media de profundidad de los tres vértices**. Si bien no será la profundidad real sino una aproximación, pero por ahora nos servirá:

```cpp
class Triangle
{
public:
    float averageDepth;

    void AverageDepth() 
    {
        averageDepth = (vertices[0].z + vertices[1].z + vertices[2].z) / 3;
    }
}
```

Ahora, antes de renderizar los triángulos deberemos ordenarlos a partir de esa profundidad media.

Como he implementado un contenedor de tipo `std::deque` puede utilizar la función `std::sort` para ordenarlo fácilmente, pero debo sobrecargar el `operador <` necesario en la comparación:

```cpp
class Triangle
{
public:
    bool operator<(const Triangle &t) const
    {
        return averageDepth < t.averageDepth;
    }
}
```

```cpp
#include <algorithm>

void Mesh::Render()
{
    // Antes de renderizar triángulos ordenarlos por media de profundidad
    std::deque sortedTriangles(triangles);
    std::sort(sortedTriangles.begin(), sortedTriangles.end());

    // Loop projected triangles array and render them
    for (size_t i = 0; i < sortedTriangles.size(); i++)
    {
        // If culling is true and enabled globally bypass the current triangle
        if (window->enableBackfaceCulling && sortedTriangles[i].culling)
            continue;

        // Triángulos
        if (window->drawFilledTriangles)
        {
            window->DrawFilledTriangle(
                sortedTriangles[i].projectedVertices[0].x, sortedTriangles[i].projectedVertices[0].y,
                sortedTriangles[i].projectedVertices[1].x, sortedTriangles[i].projectedVertices[1].y,
                sortedTriangles[i].projectedVertices[2].x, sortedTriangles[i].projectedVertices[2].y,
                sortedTriangles[i].color);
        }

        // Wireframe
        if (window->drawWireframe)
        {
            window->DrawTriangle(
                sortedTriangles[i].projectedVertices[0].x, sortedTriangles[i].projectedVertices[0].y,
                sortedTriangles[i].projectedVertices[1].x, sortedTriangles[i].projectedVertices[1].y,
                sortedTriangles[i].projectedVertices[2].x, sortedTriangles[i].projectedVertices[2].y,
                0xFF0095FF);
        }

        // Vértices
        if (window->drawWireframeDots)
        {
            window->DrawRect(sortedTriangles[i].projectedVertices[0].x - 2, sortedTriangles[i].projectedVertices[0].y - 2, 5, 5, 0xFFFF0000);
            window->DrawRect(sortedTriangles[i].projectedVertices[1].x - 2, sortedTriangles[i].projectedVertices[1].y - 2, 5, 5, 0xFFFF0000);
            window->DrawRect(sortedTriangles[i].projectedVertices[2].x - 2, sortedTriangles[i].projectedVertices[2].y - 2, 5, 5, 0xFFFF0000);
        }
    }
}
```

A diferencia de antes, ahora las caras sin **back face culling** se pintan algo mejor:

![]({{cdn}}/graficos3d/anim-16.gif)

Sin embargo todavía dista de ser perfecto, pues este algoritmo no puede representar algunas composiciones como la de la siguiente figura:

![]({{cdn}}/graficos3d/image-65.png)

Además nuestra asunción de hacer la media de profundidad entre los puntos quizá no es la mejor de todas.

En todo caso retomaré el tema más adelante, una vez repasado  lo referente a las matrices, sus operaciones y transformaciones básicas.

___
<small class="edited"><i>Última edición: 05 de Junio de 2022</i></small>