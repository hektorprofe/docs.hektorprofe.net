title: Vectores y puntos | Programación de gráficos 3D | Hektor Profe
description: 

# Vectores y puntos


Es hora de empezar a pensar en 3D, eso implica añadir una nueva dimensión: la **profundidad**, que se representa en lo que se conoce como el **eje Z**.

Empezaré creando un nuevo método para pintar un único píxel en pantalla:

```cpp
void Window::DrawPixel(int x, int y, unsigned int color)
{
    if (x >= 0 && x < windowWidth && y >= 0 && y < windowHeight)
    {
        colorBuffer[(windowWidth * y) + x] = static_cast<uint32_t>(color);
    }
}
```

Si queremos representar algo en el espacio tridimensional, debemos hacerlo a través de números que indican cantidades.

Las cantidades se dividen en dos tipos:

* **Cantidades escalares**: Representadas con único número: temperatura, área, longitud, presión...
* **Cantidades vectoriales**: Representadas con más de un número: velocidad, aceleración, fuerza, arrastre, desplazamiento, elevación...

Para representar una cantidad vectorial de dos números, por ejemplo **velocidad (m/s)**, se utiliza un eje de coordenadas 2D y un vector formado por los componentes `X`, `Y`.

De la misma forma podemos representar una cantidad vectorial formada por tres números **ancho**, **alto** y **profundidad** en un eje de coordenadas 3D mediante un vector formado por los componentes `X`, `Y`, `Z`. 

Un **vector** es un conjunto de componentes donde el orden importa para representar una cantidad formada por dos o más números, así que vamos a empezar por definir unas clases para manejar nuestros propios vectores 2D y 3D:

```cpp
#ifndef VECTOR_H
#define VECTOR_H

#include <iostream>

class Vector2
{
public:
    double x;
    double y;

    friend std::ostream &operator<<(std::ostream &os, const Vector2 &v);
};

class Vector3
{
public:
    double x;
    double y;
    double z;

    friend std::ostream &operator<<(std::ostream &os, const Vector3 &v);
};

#endif
```

Para la implementación por ahora solo la sobrecarga del `ostream` para imprimir un vector:

```cpp
#include "vector.h"

std::ostream &operator<<(std::ostream &os, const Vector2 &v)
{
    os << "(" << v.x << ", " << v.y << ")";
    return os;
}

std::ostream &operator<<(std::ostream &os, const Vector3 &v)
{
    os << "(" << v.x << ", " << v.y << ", " << v.z << ")";
    return os;
}
```

Vamos a suponer que deseamos representar un cubo 3D de 9 píxeles de ancho, alto y profundidad. Podemos entenderlo como un conjunto de 9*9*9 píxeles, donde cada punto es un vector tridimensional.

Lo que podemos hacer es suponer el centro del cubo como el origen del eje de coordenadas (0,0,0) y a partir de ahí uniformemente (en base de -1 a 1) representarlo a la izquierda, derecha, arriba, abajo, adelante y atrás.

Para ello lo podemos inicializar con tres bucles anidados:

```cpp
// Cubo de 9x9x9 píxeles
int counterPoints;
Vector3 cubePoints[9 * 9 * 9];

// Cargar el array de vectores de -1 a 1 en el cubo 9x9x9
for (double x = -1; x <= 1; x += 0.25)
{
    for (double y = -1; y <= 1; y += 0.25)
    {
        for (double z = -1; z <= 1; z += 0.25)
        {
            cubePoints[counterPoints++] = Vector3{x, y, z};
        }
    }
}
```

Este es el principio y final del arreglo 9*9*9 con 729 puntos:

```
(-1, -1, -1), 
(-1, -1, -0.75), 
..., 
(0, 0, -0.25), 
(0, 0, 0), 
(0, 0, 0.25), 
..., 
(1, 1, 0.75), 
(1, 1, 1)
```

El problema es que nuestro `ColorBuffer` se fundamenta en un eje 2D de ancho y alto. ¿Cómo podemos a representar un arreglo de vectores 3D en un buffer 2D?

___
<small class="edited"><i>Última edición: 05 de Junio de 2022</i></small>