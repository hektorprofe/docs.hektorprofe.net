title: Transformaciones lineales | Programación de gráficos 3D | Hektor Profe
description: 

# Transformaciones lineales


Hemos visto como dividiendo entre el eje `Z` hemos conseguido la **brecha de perspectiva** para la proyección en perspectiva. Sin embargo, esta función es solo uno de los diferentes pasos que necesitamos para conseguir la verdadera proyección en perspectiva.

A parte de dvidir entre `Z` necesitamos considerar por ejemplo, cuál es ángulo del `FOV` (el campo de visión) que estamos utilizando, o también el `AR` (la relación de aspecto) de la pantalla. Para conseguir esto necesitaremos acudir a la **proyección de matrices**, pero es un tema que trataremos más adelante.

Por ahora utilizaremos la **brecha de perspectiva** y nos centraremos en algo más interesante, añadir dinamismo a nuestro cubo mediante la aplicación de transformaciones en sus vectores.

## Transformando vectores

Para transformar los vectores necesitamos acudir al **álgebra lineal**, la rama de la matemática que estudia las ecuaciones y funciones lineales, así cómo su representación como vectores y matrices.

Las tres transformaciones esenciales son:

* **Escalado**: Para hacer más grande o más pequeño el vector.
* **Traslación**: Para mover el vector de sitio a otro.
* **Rotación**: Para rotar el vector una cierta cantidad.

Las transformaciones las llevaremos a cabo antes de la proyección, durante el evento de actualización y antes del renderizado:

1. `ProcessInput()`
2. `Update()`
    1. `TransformPoints()`
        1. `Rotate(x, y, z)`
        2. `Scale(amout)`
        3. `Translate(amout)`
    2. `ProjectPoints()`
3. `Render()`

## Razones trigonométricas

Para realizar las transformaciones de los vectores es necesario utilizar la trigonometría, así que vamos a repasar los conceptos básicos.

Trigonometría significa **estudio de los trígonos**, polígonos con tres lados y tres ángulos.

Las razones trigonométricas son las relaciones entre los lados de un triángulo rectángulo:

![]({{cdn}}/graficos3d/image-20.png)

![](https://latex.codecogs.com/png.image?\dpi{150}\bg{white}sin(\alpha)&space;=&space;\frac{opuesto}{hipotenusa}&space;\rightarrow&space;s&space;=&space;o&space;/&space;h)

![](https://latex.codecogs.com/png.image?\dpi{150}\bg{white}cos(\alpha)&space;=&space;\frac{adyacente}{hipotenusa}&space;\rightarrow&space;c&space;=&space;a&space;/&space;h)

![](https://latex.codecogs.com/png.image?\dpi{150}\bg{white}tan(\alpha)&space;=&space;\frac{opuesto}{adyacente}&space;\rightarrow&space;t&space;=&space;o&space;/&space;a)

Estas relaciones nos permitirán realizar distintos cálculos esenciales para las transformaciones lineales como por ejemplo la rotación. 

Una forma de recordarlas es mediante la palabra **sohcahtoa**.

## Rotación de vectores

Ahora que hemos repasado el tema de las razones trignométricas podemos aplicar esos conceptos para rotar los vectores de nuestro cubo.

Para rotar un vector (x,y) se debe aplicar la fórmula de la rotación de matrices:

<img src="https://latex.codecogs.com/png.image?\dpi{150}\bg{white}\begin{bmatrix}cos&space;(\alpha)&space;&&space;-sin(\alpha)\\sin(\alpha)&space;&&space;cos(\alpha)\\\end{bmatrix}&space;*\begin{bmatrix}x&space;\\y&space;\\\end{bmatrix}"/>

Dado un vector `(x, y)` queremos aplicarle una rotación (ángulo) para conseguir el nuevo vector rotado `(x', y')`.

![]({{cdn}}/graficos3d/image-21.png)

Tomando el triángulo que forma `(x, y)` con ángulo `β` y el triángulo que forma `(x', y')` con ángulo `θ` podemos establecer sus relaciones trigonométricas para encontrar los valores del vector rotado `(x', y')`:

![]({{cdn}}/graficos3d/image-22.png)

<img src="https://latex.codecogs.com/png.image?\dpi{150}\bg{white}\\cos(&space;\theta&space;)&space;=&space;x/r&space;\to&space;x&space;=&space;r&space;*&space;cos(\theta)\\sin(&space;\theta&space;)&space;=&space;y/r&space;\to&space;y&space;=&space;r&space;*&space;sin(\theta)"/>

Para determinar los valores rotados necesitamos asumirlos como la suma de `θ` y `β`: 

<img src="https://latex.codecogs.com/png.image?\dpi{150}\bg{white}\\cos(&space;\theta&space;&space;&plus;&space;\beta&space;)&space;=&space;x'/r&space;\to&space;x'&space;=&space;r'&space;*&space;cos(\theta&space;&plus;&space;\beta)\\sin(&space;\theta&space;&space;&plus;&space;\beta)&space;=&space;y'/r&space;\to&space;y'&space;=&space;r'&space;*&space;sin(\theta&space;&plus;&space;\beta)"/>

No sabemos el ángulo `β` pero en trigonometría existen las conocidas **fórmulas de adición** que explican como expandir el seno y el coseno de una suma o resta de dos ángulos:

![]({{cdn}}/graficos3d/image-24.png)

Aplicando la fórmula de adición del ángulo para el coseno:

<img src="https://latex.codecogs.com/png.image?\dpi{150}\bg{white}\\x'&space;=&space;rcos(\theta&space;&plus;&space;\beta)\\x'&space;=&space;r(cos\theta&space;cos&space;\beta&space;-&space;sin\theta&space;sin\beta)\\x'&space;=&space;rcos\theta&space;cos&space;\beta&space;-&space;rsin\theta&space;sin\beta"/>

Aquí podemos substituir `rcosθ` por `x`y `rsinθ` por `y` para conseguir finalmente el valor de `x'`:

<img src="https://latex.codecogs.com/png.image?\dpi{150}\bg{white}x'&space;=&space;x&space;cos&space;\beta&space;-&space;y&space;sin\beta"/>

Lo mismo podemos formular para conseguir el valor de `y'`:

<img src="https://latex.codecogs.com/png.image?\dpi{150}\bg{white}\\&space;y'&space;=&space;rsin(\theta&space;&plus;&space;\beta)\\&space;y'&space;=&space;r(sin\theta&space;cos&space;\beta&space;&plus;&space;cos&space;\theta&space;sin&space;\beta)\\&space;y'&space;=&space;rsin&space;\theta&space;cos&space;\beta&space;&plus;&space;rcos&space;\theta&space;sin&space;\beta\\&space;"/>

Substituimos `rsinθ` por `y` y `rcosθ` por `x` para conseguir el valor de `y'`:

<img src="https://latex.codecogs.com/png.image?\dpi{150}\bg{white}\\&space;y'&space;=&space;y&space;cos\beta&space;&plus;&space;x&space;sin&space;\beta&space;"/>

Y ya tenemos las ecuaciones que podemos escribir en forma matricial para un ángulo `α`:

<img src="https://latex.codecogs.com/png.image?\dpi{150}\bg{white}\begin{bmatrix}cos&space;(\alpha)&space;&&space;-sin(\alpha)\\sin(\alpha)&space;&&space;cos(\alpha)\\\end{bmatrix}&space;*\begin{bmatrix}x&space;\\y&space;\\\end{bmatrix}"/>

Ahora bien, esto es para rotar un vector 2D, ¿cómo se aplica con un vector 3D?

Pues si nos lo paramos a pensar, podemos rotar un elemento en base a cualquier de los dimensiones. No es lo mismo rotar algo horizontalmente, que verticalmente o en profundidad.

Al tener tres tipos de rotación el eje aldedor del que vamos a rotar quedará congelado, es decir, no se modificará y es precisamente gracias a eso que no necesitamos nada más para manejar las rotaciones.

Para rotar alrededor del eje `z`:

<img src="https://latex.codecogs.com/png.image?\dpi{150}\bg{white}\\&space;x'&space;=&space;xcos&space;\beta&space;-&space;y&space;sin&space;\beta\\&space;y'&space;=&space;xsin\beta&space;&plus;&space;ycos\beta\\&space;z'&space;=&space;inmutable"/>

Para rotar alrededor del eje `y`:

<img src="https://latex.codecogs.com/png.image?\dpi{150}\bg{white}\\&space;x'&space;=&space;xcos&space;\beta&space;-&space;z&space;sin&space;\beta\\&space;y'&space;=&space;inmutable\\&space;z'&space;=&space;xsin\beta&plus;zcos\beta"/>

Para rotar alrededor del eje `x`:

<img src="https://latex.codecogs.com/png.image?\dpi{150}\bg{white}\\&space;x'&space;=&space;inmutable\\&space;y'&space;=&space;ycos&space;\beta&space;-&space;z&space;sin&space;\beta\\&space;z'&space;=&space;ysin\beta&plus;zcos\beta"/>

## Función de rotación

Después de tanta trigonometría es hora de programar un poco y llevar a código todo lo que hemos aprendido.

Empecemos creando unos métodos para rotar los vectores 3D:

```cpp
class Vector3
{
public:
    double x;
    double y;
    double z;

    friend std::ostream &operator<<(std::ostream &os, const Vector3 &v);

    void RotateX(float angle);
    void RotateY(float angle);
    void RotateZ(float angle);
};
```

La implementación siguiendo las fórmulas de la lección anterior:

```cpp
void Vector3::RotateX(float angle)
{
    double newY = y * cos(angle) - z * sin(angle);
    double newZ = y * sin(angle) + z * cos(angle);

    y = newY;
    z = newZ;
}
void Vector3::RotateY(float angle)
{
    double newX = x * cos(angle) - z * sin(angle);
    double newZ = x * sin(angle) + z * cos(angle);

    x = newX;
    z = newZ;
}
void Vector3::RotateZ(float angle)
{
    double newX = x * cos(angle) - y * sin(angle);
    double newY = x * sin(angle) + y * cos(angle);

    x = newX;
    y = newY;
}
```

Ahora, podemos aplicar la rotación a partir de un `Vector3 cubeRotation` declarado fuera del `while`:

```cpp
// Rotación cubo
Vector3 cubeRotation;
```

Justo antes de proyectar el cubo a 2D, le aplicaremos las transformaciones:

```cpp
window.Update();

// Rotation transformations per frame
cubeRotation.x += 0.01;
cubeRotation.y += 0.01;
cubeRotation.z += 0.01;

for (size_t i = 0; i < 9 * 9 * 9; i++)
{
    Vector3 point = cubePoints[i];
    // Rotation transformations
    point.RotateX(cubeRotation.x);
    point.RotateY(cubeRotation.y);
    point.RotateZ(cubeRotation.z);
    // Restamos la distancia de la cámara
    point.z -= cameraPosition.z;
    // Proyeccion del punto
    cubeProjectedPoints[i] = PerspectiveProjection(point);
}

window.Render();
```

Como resultado tendremos el cubo rotando:

![]({{cdn}}/graficos3d/anim-01.gif)

## Refactorización 2

Tenemos mucho que refactorizar en la ventana y nuestros vectores, así que pongámonos manos a la obra.

Empezando por las variables del `fovFactor` y el `cameraPosition` dentro de la ventana como variables públicas, eso nos permitirá luego, a través de un puntero de `window`, acceder desde cualquier lugar a ellos.

```cpp
#include "vector.h"

class Window
{
public:
    float fovFactor = 400;
    Vector3 cameraPosition{0, 0, -5};
```

A continuación los métodos de proyección podemos incluirlos en nuestros vectores de manera que un `Vector3` devuelva ya su versión `Vector2` proyectada a partir de un `fovFactor`:

```cpp
class Vector3
{
public:
    Vector2 OrtoraphicProjection(float fovFactor);
    Vector2 PerspectiveProjection(float fovFactor);
};
```

La implementación quedaría así:

```cpp
Vector2 Vector3::OrtoraphicProjection(float fovFactor)
{
    return Vector2{fovFactor * x, fovFactor * y};
}

Vector2 Vector3::PerspectiveProjection(float fovFactor)
{
    return Vector2{(fovFactor * x) / z, (fovFactor * y) / z};
}
```

Para utilizarlos simplemente cambiaremos:

```cpp
// cubeProjectedPoints[i] = PerspectiveProjection(point);
cubeProjectedPoints[i] = point.PerspectiveProjection(fovFactor);
```

También refactorizaremos los tres métodos de rotar X, Y, Z en un único método que tome un `Vector3` para las cantidades y el ángulo:

```cpp
void Rotate(Vector3 angles);
```

La implementación se ejecutará en función de los valores del Vector de cantidades

```cpp
void Vector3::Rotate(Vector3 angles)
{
    if (angles.x != 0)
        RotateX(angles.x);
    if (angles.y != 0)
        RotateY(angles.y);
    if (angles.z != 0)
        RotateZ(angles.z);
}
```

Llamarlo será tan sencillo como:

```cpp
// Rotation transformations
point.Rotate(cubeRotation);
```

En este punto lo más interesante sería crear nuestra propia clase `cube` para crear y renderizar cubos de forma sencilla, además nos permitirá separar cómodamente la función principal de los objetos tridimensionales:

```cpp
#ifndef CUBE_H
#define CUBE_H

#include <iostream>
#include <memory>
#include "vector.h"

// Para prevenir dependencias cíclicas
class Window;

class Cube
{
public:
    size_t pointsCounter{0};
    std::unique_ptr<Vector2[]> projectedPoints;

private:
    Window *window;
    Vector3 rotation;
    Vector3 rotationAmount;
    std::unique_ptr<Vector3[]> points;

public:
    Cube() = default;
    Cube(Window *window, int length);
    void SetRotationAmount(float x, float y, float z);
    void Update();
    void Render();
};

#endif
```

La implementación factorizada con el puntero de ventana y algunas mejores quedará de esta forma:

```cpp
#include "cube.h"
#include "window.h" // Importamos la fuente de la ventana

Cube::Cube(Window *window, int pointsPerSide)
{
    this->window = window;

    // Si el numero de puntos por lado es par le sumamos 1
    // El centro del cuadrado es el punto intermedio 0,0,0
    // Por eso necesitamos asegurarnos de poder dividirlo
    if (pointsPerSide % 2 == 0)
        pointsPerSide++;

    points = std::make_unique<Vector3[]>(pointsPerSide * pointsPerSide * pointsPerSide);
    projectedPoints = std::make_unique<Vector2[]>(pointsPerSide * pointsPerSide * pointsPerSide);

    // Array de vectores de -1 a 1 (requiere longitud impar)
    float portion = 1.0f / (pointsPerSide / 2);

    for (float x = -1.0; x <= 1; x += portion)
    {
        for (float y = -1.0; y <= 1; y += portion)
        {
            for (float z = -1.0; z <= 1; z += portion)
            {
                // std::cout << x << "," << y << "," << z << std::endl;
                points[pointsCounter++] = Vector3{x, y, z};
            }
        }
    }
}

void Cube::Update()
{
    // Set new framr rotation amounts
    rotation.x += rotationAmount.x;
    rotation.y += rotationAmount.y;
    rotation.z += rotationAmount.x;

    for (size_t i = 0; i < pointsCounter; i++)
    {
        Vector3 point = points[i];
        // Rotation transformation
        point.Rotate(rotation);
        //  Restamos la distancia de la cámara
        point.z -= window->cameraPosition.z;
        // Proyeccion del punto
        projectedPoints[i] = point.PerspectiveProjection(window->fovFactor);
    }
}

void Cube::SetRotationAmount(float x, float y, float z)
{
    rotationAmount = {x, y, z};
}

void Cube::Render()
{
    /* Dibujar proyección reposicionada al centro */
    for (size_t i = 0; i < pointsCounter; i++)
    {
        window->DrawPixel(
            projectedPoints[i].x + window->windowWidth / 2,
            projectedPoints[i].y + window->windowHeight / 2,
            0xFF00FFFF);
    }
}
```

Podemos pasar la referencia de la ventana al cubo, que lo crearemos en una variable privada `cube`:

```cpp
class Window
{
private:
    /* Custom objects */
    Cube cube;
```

Lo inicializaremos en el método `window.Setup()`, así como su rotación:

```cpp
#include "cube.h"

void Window::Setup()
{
    // Custom objects
    cube = Cube(this, 7);
    cube.SetRotationAmount(0.01, 0.01, 0.01);
}
```

Realizamos los cálculos de transformación y proyección mediante en el `window.Update()`:

```cpp
void Window::Update()
{
    // Custom objects updating
    cube.Update();
}
```

Y lo renderizaremos en el `window.Render()`:

```cpp
// Custom objects rendering
cube.Render();
```

En este punto podemos eliminar `window.PostRender()` del bucle `while` y establecer la llamada al final del propio `Render` ya que a partir de ahora los elementos los manejaremos desde la ventana:

```cpp
void Window::Render()
{
    // Clear color buffer
    ClearColorBuffer(static_cast<uint32_t>(0xFF0000000));

    // Render the background grid
    DrawGrid(0xFF616161);

    // Custom objects renderring
    cube.Render();

    // Late rendering actions
    PostRender();
}
```

El resultado final será el mismo de antes:

![]({{cdn}}/graficos3d/anim-02.gif)

Pero al refactorizar el código la función `main` quedará super limpia:

```cpp
#include <iostream>
#include "window.h"

int main(int argc, char *argv[])
{
    Window window(640, 480);

    window.Init();
    window.Setup();

    while (window.running)
    {
        window.ProcessInput();
        window.Update();
        window.Render();
    }

    return 0;
}
```

Además en el futuro, una vez implementemos la transformación de traslación, podremos dibujar múltiples cubos con sus propiedades independientes, tiempo al tiempo.

___
<small class="edited"><i>Última edición: 05 de Junio de 2022</i></small>