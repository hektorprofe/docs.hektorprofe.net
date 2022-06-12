title: Mallas en memoria dinámica | Programación de gráficos 3D | Hektor Profe
description: 

# Mallas en memoria dinámica

Hasta ahora todo lo que hemos hecho tenía como propósito dibujar triángulos para recrear un cubo.

En esta sección la idea es desarrollar una clase `Mesh` que nos permita almacenar de forma dinámica múltiples vértices y las caras de los triángulos:

```cpp
#ifndef MESH_H
#define MESH_H

#include <iostream>
#include <deque>
#include "vector.h"
#include "triangle.h"

// Para prevenir dependencias cíclicas
class Window;

class Mesh
{
private:
    Window *window;
    Vector3 rotation;
    Vector3 rotationAmount;
    std::deque<Vector3> faces;
    std::deque<Vector3> vertices;
    std::deque<Triangle> triangles;

public:
    Mesh() = default;
    Mesh(Window *window, Vector3 *vertices, int verticesLength, Vector3 *faces, int facesLength);
    void SetRotationAmount(float x, float y, float z);
    void Update();
    void Render();
};

#endif
```

La diferencia respecto al cubo es que ahora tenemos `faces`, `vertices` y `triangles` como contenedores dinámicos (colas), que permiten almacenar información dinámicamente.

En la implementación recorreremos los arreglos de vértices y caras para almacenarlos en la malla durante la inicialización, así como inicializamos el mismo número de triángulos que de caras. Por ello es necesario un contructor pode fecto en `Triangle`:

```cpp
class Triangle
{
public:
    Triangle() = default;
};
```

En cada fotograma generaremos los triángulos, los guardaremos en la cola `triangles` y los  transformarlos, para finalmente renderizadores una vez ya están proyectados:

```cpp
#include "mesh.h"
#include "window.h" // Importamos la fuente de la ventana

Mesh::Mesh(Window *window, Vector3 *vertices, int verticesLength, Vector3 *faces, int facesLength)
{
    this->window = window;
    // Initialize the dinamic vertices
    for (size_t i = 0; i < verticesLength; i++)
        this->vertices.push_back(vertices[i]);
    // Initialize the dinamic faces and empty triangles (same number)
    for (size_t i = 0; i < facesLength; i++)
    {
        this->faces.push_back(faces[i]);
        this->triangles.push_back(Triangle());
    }
};

void Mesh::SetRotationAmount(float x, float y, float z)
{
    rotationAmount = {x, y, z};
}

void Mesh::Update()
{
    // Set new framr rotation amounts
    rotation.x += rotationAmount.x;
    rotation.y += rotationAmount.y;
    rotation.z += rotationAmount.x;

    // Loop all triangle faces of the mesh
    for (size_t i = 0; i < triangles.size(); i++)
    {
        // Create a new triangle to store data and render it later
        triangles[i].vertices[0] = vertices[static_cast<int>(faces[i].x)];
        triangles[i].vertices[1] = vertices[static_cast<int>(faces[i].y)];
        triangles[i].vertices[2] = vertices[static_cast<int>(faces[i].z)];

        // Loop all vertice for the face and apply transformations
        for (size_t j = 0; j < 3; j++)
        {
            // Rotation
            triangles[i].RotateVertex(j, rotation);
            // Translation (away from camera)
            triangles[i].TranslateVertex(j, window->cameraPosition);
            // project the vertex and scale it from 3D to 2D
            triangles[i].ProjectVertex(j, window->fovFactor);
            // Translate the projected vertex to the middle screen
            triangles[i].projectedVertices[j].x += (window->windowWidth / 2);
            triangles[i].projectedVertices[j].y += (window->windowHeight / 2);
        }
    }
}

void Mesh::Render()
{
    // Loop projected triangles array and render them
    for (size_t i = 0; i < triangles.size(); i++)
    {
        window->DrawTriangle(
            triangles[i].projectedVertices[0].x,
            triangles[i].projectedVertices[0].y,
            triangles[i].projectedVertices[1].x,
            triangles[i].projectedVertices[1].y,
            triangles[i].projectedVertices[2].x,
            triangles[i].projectedVertices[2].y,
            0xFF00FFFF);
    }
}
```

La generación de la malla implica enviarle los vertices, caras y sus respectivas longitudes durante su creación:

```cpp
class Window
{
private:
    Mesh mesh;
};

void Window::Setup()
{
    // Custom objects
    Vector3 meshVertices[]{
        {-1, -1, -1},
        { 1, -1, -1},
        {-1,  1, -1},
        { 1,  1, -1},
        {-1, -1,  1},
        { 1, -1,  1},
        {-1,  1,  1},
        { 1,  1,  1}
    };

    Vector3 meshFaces[]{
        {1, 0, 2}, 
        {1, 2, 3}, 
        {4, 5, 7}, 
        {4, 7, 6}, 
        {1, 7, 5}, 
        {1, 3, 7}, 
        {4, 2, 0}, 
        {4, 6, 2}, 
        {2, 7, 3}, 
        {2, 6, 7}, 
        {1, 5, 4}, 
        {1, 4, 0}
    };
    
    mesh = Mesh(this, meshVertices, 8, meshFaces, 12);
    mesh.SetRotationAmount(0.01, 0.01, 0.01);
}

void Window::Update()
{
    // Custom objects update
    mesh.Update();
}

void Window::Render()
{
    // Custom objects render
    mesh.Render();
}
```

El resultado es el mismo que antes pero con este sistema, próximamente podremos cargar la información dinámicamente desde ficheros con modelos.

___
<small class="edited"><i>Última edición: 05 de Junio de 2022</i></small>