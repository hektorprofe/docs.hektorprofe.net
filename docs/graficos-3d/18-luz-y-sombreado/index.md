title: Luz y sombreado | Programación de gráficos 3D | Hektor Profe
description: 

# Luz y sombreado

Los objetos en la realidad no se perciben simplemente como entidades de colores sólidos sino que les afectan la iluminación y las sombras del entorno:

![]({{cdn}}/graficos3d/image-73.png)

Por una parte tenemos la incedencia de la propia luz en el objeto y por otro la sombra proyectada por éste sobre una superficie. Voy a enfocarme en una posible implementación de la primera.

Podemos entender la luz como un vector con una dirección:

```cpp
#ifndef LIGHT_H
#define LIGHT_H

#include "vector.h"

class Light
{
public:
    Vector3 direction;
};

#endif
```

Dependiendo de cómo se proyecta la luz encontramos distintos tipos:

![]({{cdn}}/graficos3d/image-74.png)

Lo que voy a implementar es el tipo más simple, una **fuente global de luz direccional** que afectará a todos los objetos por igual. Esta luz no tiene una posición específica, sino que es más bien como un sol gigantesco que ilumina todo en una dirección.

Lo siguiente que debemos plantearnos es cómo afectará esta fuente de luz a los objetos y cómo cambiará el rasterizado de sus caras. Para ello haremos uso de diferentes algoritmos de iluminación.

## Sombreado plano

Uno los algoritmos más sencillos de implementar se conoce como **sombreado plano** (*flat shading*). Éste dice que dependiendo de la alineación que hay entre el rayo proyectado por la luz y la cara de la malla, más o menos brillante u oscuro será el color de esa cara. En otras palabras, si la `normal` de la cara está completamente alineada con la dirección de la luz estará completamente iluminada.

![]({{cdn}}/graficos3d/image-75.png) 

El siguiente método `ApplyIntensity` nos permitirá graduar un color en un porcentaje para determinar el color de la cara iluminada:

```cpp
class Light
{
public:
    Vector3 direction;

    static uint32_t ApplyIntensity(uint32_t color, float percentageFactor)
    {
        uint32_t a = (color & 0xFF000000);
        uint32_t r = (color & 0x00FF0000) * percentageFactor;
        uint32_t g = (color & 0x0000FF00) * percentageFactor;
        uint32_t b = (color & 0x000000FF) * percentageFactor;

        uint32_t newColor = a | (r & 0x00FF0000) | (g & 0x0000FF00) | (b & 0x000000FF);
        return newColor;
    }
};
```

Haciendo uso de operadores bit a bit y máscaras extraemos la porción de cada color `ARGB` y aplicamos el factor de porcentaje (en tanto por uno). Luego generamos el nuevo color extrayendo, nuevamente con máscaras, cada porción y sumándolas.

Vamos a crear una fuente de luz en `window.h` que por proyecte desde un poco por delante de la profundidad de la pantalla `{0,0,1}`:

```cpp
#include "light.h"

/* Light settings */
Light light{.direction{0, 0, 1}};
```

![]({{cdn}}/graficos3d/image-76.png) 

Ahora, para visualizar mejor la iluminación cambiaremos los colores de las caras del `mock` cube a blanco:

```cpp
uint32_t meshColors[]
{
    0xFFFFFFFF, 0xFFFFFFFF, 
    0xFFFFFFFF, 0xFFFFFFFF, 
    0xFFFFFFFF, 0xFFFFFFFF, 
    0xFFFFFFFF, 0xFFFFFFFF, 
    0xFFFFFFFF, 0xFFFFFFFF, 
    0xFFFFFFFF, 0xFFFFFFFF
};
```

Justo después de proyectar el color vamos a llamar a un nueo método de `Triangle` llamado `ApplyFlatShading()` para recalcular el color del triángulo en función del ángulo de la luz:

```cpp
/*** Apply projections and lighting for all face vertices ***/
for (size_t j = 0; j < 3; j++) {}

/** Apply flat shading ***/
triangles[i].ApplyFlatShading(window->light);
```

Este método hará uso de la `normal`, algo que estamos calculando dentro del método `ApplyCulling` que no siempre se ejecutará, recodemos que podemos desactivarlo. 

Tendremos que externalizar la parte del cálculo de la normal y almacenarla como miembro del triángulo:

```cpp
Vector3 normal;

void CalculateNormal()
{
    // Get the vector substracion B-A and C - A and normalize 'em
    Vector3 vectorAB = this->vertices[1] - this->vertices[0];
    Vector3 vectorAC = this->vertices[2] - this->vertices[0];
    vectorAB.Normalize();
    vectorAC.Normalize();
    // Compute the face normal (corss product) and normalize it
    // Using our left-handed system (z grows inside the monitor)
    // So we apply have to appky the order: AB x AC
    normal = vectorAB.CrossProduct(vectorAC);
    normal.Normalize();
}

void ApplyCulling(float *cameraPosition)
{
    // Find the vector betweenn a triangle point and camera origin
    Vector3 cameraRay = Vector3(cameraPosition[0], cameraPosition[1], cameraPosition[2]) - this->vertices[0];
    // Calculate how aligned the camera ray is with the face normal
    float dotNormalCamera = normal.DotProduct(cameraRay);
    // Test the dotNormalCamera and render the triangle if is >0
    this->culling = (dotNormalCamera < 0);
}
```

Lo llamaremos antes de ejecutar el culling:

```cpp
/*** Calculate the normal ***/
triangles[i].CalculateNormal();

/*** Back Face Culling Algorithm ***/
if (window->enableBackfaceCulling)
{}
```

El método para recalcular el color, con una copia de seguridad del color inicial para poder realizar los subsiguientes cambios de iluminación quedará:

```cpp
uint32_t color = 0xFFFFFFFF;
uint32_t originalColor = color;  // original color backup

// Constructor con copia de seguridad del color
Triangle(uint32_t color) : color(color), shadedColor(color){};  

#include "light.h"

class Triangle
{
public:
    void ApplyFlatShading(Light light)
    {
        // Calculate shading intensity based in how aligned is
        // the normal vector and the vector of the light ray
        float lightIntensityFactor = normal.DotProduct(light.direction);
        color = Light::ApplyIntensity(originalColor, lightIntensityFactor);
    }
} 
```

Si probamos el resultado observaremos algo interesante:

![]({{cdn}}/graficos3d/anim-24.gif)

Si bien estamos aplicando correctamente el sombreado, parece que lo tenemos negado y en lugar de proyectar luz está proyectando oscuridad, de ahí que si la alineación entre el vector de la luz y la normal de la cara es total se vea completamente oscuro.

Esto es debido a que el ángulo hay que calcularlo al revés, de la normal hacia el vector de la luz. ¿La razón? La luz se refleja en dirección contraria, así que vamos a negar el producto escalar:

![]({{cdn}}/graficos3d/image-77.png) 

```cpp
float lightIntensityFactor = -normal.DotProduct(light.direction);
```

Ahora sí, aquí tenemos el sombreado funcionando:

![]({{cdn}}/graficos3d/anim-25.gif)

Sin embargo debemos asegurarnos de que el valor del producto escalar se encuentra entre `0` y `1`, por lo que tendremos que recortarlo, lo que en inglés se denomina `clamp` o restricción. 

Si el factor es menor que `0`, será `0`. Si es mayor que `1`, será `1`. Así nos aseguraremos de que el recoloreado es el correcto:

```cpp
// Clamp percentageFactor between 0 and 1
if (percentageFactor < 0) percentageFactor = 0;
if (percentageFactor > 1) percentageFactor = 1;
```

## Sombreado suavizado

Hemos visto como el sombreado plano se programa sobre los triángulos en base a su normal, de manera que una cara tendrá un color.

Existen otros algoritmos de sombreado más avanzados, como los de sombreado suavizado. Uno de los más famosos es el [**Sombreado Gouraud**](https://es.wikipedia.org/wiki/Sombreado_Gouraud).

Esta técnica se basa en la interpolación de la luz no para la normal de la cara, sino para cada píxel de la cara en función de los colores en las las normales de los vértices:

![]({{cdn}}/graficos3d/anim-26.gif)

Cuantos más polígonos tenga el modelo, mayor será el suavizado de la sombra:

![]({{cdn}}/graficos3d/anim-27.gif)

Comparado con el algoritmo de sombreado plano es mucho más trabajoso para la CPU así que no lo vamos a implementar, pero vale la pena comentarlo.

## Valores verticales invertidos

En este punto, si cambiamos nuestro *mock* cube por el modelo **cube.obj** debería funcionarnos todo correctamente:

```cpp
mesh = Mesh(this, "assets/cube.obj");
```

![]({{cdn}}/graficos3d/image-78.png)

Pero si cargamos el cono, aunque se rasterice bien, veremos que está volteado verticalmente:

```cpp
mesh = Mesh(this, "assets/cone.obj");
```

![]({{cdn}}/graficos3d/image-79.png)

El problema radica en que, en nuestro sistema hemos considerado que la `Y` crece hacia abajo, en el color buffer, siendo `(0,0)` la esquina superior izquierda. Sin embargo, en los modelos de blender la `Y` crece hacia arriba.

Así que tendremos que invertir los valores de `Y` proyectados en la pantalla, antes de trasladarlos:

```cpp
// Invert the y values to account the flipped screen y coord
triangles[i].projectedVertices[j].y *= -1;
```

![]({{cdn}}/graficos3d/image-80.png)

Esta era también la razón por la que la luz superior del cubo no funcionaba bien, pero ahora si se renderizará correctamente.

___
<small class="edited"><i>Última edición: 05 de Junio de 2022</i></small>