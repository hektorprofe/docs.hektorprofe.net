title: Interpolación de perspectiva corregida | Programación de gráficos 3D | Hektor Profe
description: 

# Interpolación de perspectiva corregida

Actualmente tenemos un problema con la texturización, los texels se renderizan siempre con un tamaño constante generando un efecto extraño en los triángulos:

![]({{cdn}}/graficos3d/image-94.png)

Para corregir la distorsión de las texturas debemos incorporar la profundidad en la interpolación de los valores:

![]({{cdn}}/graficos3d/image-93.png)

Tenemos que aplicar la brecha de perspectiva sobre la posición del texel pero la perspectiva no es una transformación lineal, es decir, una vez aplicada la proyección de perspectiva no podemos devolver `Z` a su valor inicial con una ecuación lineal.

Entonces, estamos de acuerdo que para arreglar la distorsión creada por la perspectiva necesitamos encontrar la profundidad del punto `P` en el triángulo, pero desafortunadamente no podemos interpolar `z` directamente porque `z` no es lineal para todo el triángulo:

![]({{cdn}}/graficos3d/image-95.png)

Sin embargo, su recíproco `1/z` sí que es lineal y podemos utilizarlo para encontrar el punto `z` interpolado de `P`:

![]({{cdn}}/graficos3d/image-96.png)

Teniendo en cuenta que contamos con una matriz `4x4` donde almacenamos en `W` el valor original de `Z` antes de proyectarlo, podemos hacer uso de él para nuestro cálculo:

![]({{cdn}}/graficos3d/image-97.png)

Ordenando todas estas ideas, el algoritmo para conseguir la interpolación de perspectiva corregida es:

1. Utilizar el recíproco de todos los atributos `1/w` (ahora lineales en el espacio de pantalla).
2. Interpolar los valores de la cara  utilizando pesos baricéntricos mediante el factor `1/w`.
3. Finalmente, dividir todos los atributos entre `1/w` para deshacer la transformación de perspectiva.

El primer cambio en el código que realizaremos será enviar a la función `DrawTexturedTriangle` los componentes `z` y `w` de cada vector:

```cpp
void Window::DrawTexturedTriangle(int x0, int y0, float z0, float w0, Texture2 uv0, int x1, int y1, float z1, float w1, Texture2 uv1, int x2, int y2, float z2, float w2, Texture2 uv2, uint32_t* texture)
```

Deberemos intercambiar los correspondientes valores durante el ordenamiento de los vértices:

```cpp
// Reordenamiento de los vértices y las UV coords: y0 < y1 < y2
if (y0 > y1) // Primer intercambio
{
    SwapIntegers(&y0, &y1);
    SwapIntegers(&x0, &x1);
    SwapFloats(&z0, &z1);
    SwapFloats(&w0, &w1);
    SwapTextures(&uv0, &uv1);
}
if (y1 > y2) // Segundo intercambio
{
    SwapIntegers(&y1, &y2);
    SwapIntegers(&x1, &x2);
    SwapFloats(&z1, &z2);
    SwapFloats(&w1, &w2);
    SwapTextures(&uv1, &uv2);
}
if (y0 > y1) // Tercer intercambio
{
    SwapIntegers(&y0, &y1);
    SwapIntegers(&x0, &x1);
    SwapFloats(&z0, &z1);
    SwapFloats(&w0, &w1);
    SwapTextures(&uv0, &uv1);
}
```

Adaptaremos los vectores de texturizado de `Vector2` a `Vector4` con los correspondientes valores:

```cpp
// Create vector points for texturing after sorting the vertices
Vector4 pA{ (double)x0, (double)y0, (double)z0, (double)w0 };
Vector4 pB{ (double)x1, (double)y1, (double)z1, (double)w1 };
Vector4 pC{ (double)x2, (double)y2, (double)z2, (double)w2 };
```

Para ello necesitaremos un constructor nuevo para `Vector4`:

```cpp
Vector4(double x, double y, double z, double w) : x(x), y(y), z(z), w(w) {};
```

Hacer este cambio entre vectores implicará modificar la definición del método `DrawTexel` para poder recibir `Vector4`:

```cpp
void Window::DrawTexel(int x, int y, Vector4 a, Vector4 b, Vector4 c, Texture2 t0, Texture2 t1, Texture2 t2, uint32_t *texture, Window *window)
```

Dentro de `DrawTexel` el método para calcular los pesos baricéntricos espera los vectores en formato `Vector2`, podemos añadir un método `ToVector2()` a la clase `Vector4` para cambiarlos al vuelo:

```cpp
Vector2 Vector4::ToVector2()
{
    return Vector2(x, y);
}
``` 

Y utilizarlo:

```cpp
// Calculate the weights using the vectors A,B,C and P
Vector3 weights = Vector3::BarycentricWeights(a.ToVector2(), b.ToVector2(), c.ToVector2(), p);
```

En este punto deberemos enviar los campos correctos a `window->DrawTextureTriangle`:

```cpp
// Triángulos texturizados
if (window->drawTexturedTriangles)
{
    window->DrawTexturedTriangle(
        sortedTriangles[i].projectedVertices[0].x, sortedTriangles[i].projectedVertices[0].y, sortedTriangles[i].projectedVertices[0].z, sortedTriangles[i].projectedVertices[0].w, sortedTriangles[i].textureUVCoords[0],
        sortedTriangles[i].projectedVertices[1].x, sortedTriangles[i].projectedVertices[1].y, sortedTriangles[i].projectedVertices[1].z, sortedTriangles[i].projectedVertices[1].w, sortedTriangles[i].textureUVCoords[1],
        sortedTriangles[i].projectedVertices[2].x, sortedTriangles[i].projectedVertices[2].y, sortedTriangles[i].projectedVertices[2].z, sortedTriangles[i].projectedVertices[2].w, sortedTriangles[i].textureUVCoords[2],
        window->meshTexture);
}
```

Ya tenemos los preparativos realizados, ahora hay que implementar el algoritmo de corrección de la perspectiva.

Primero vamos a prepararnos para realizar la interpolación de `U`, `V` y la recíproca de `w` (que es lineal):

```cpp
// Variables to store the interpolated values of U, V and also the reciprocal 1/w for the current pixel
float interpolatedU;
float interpolatedV;
float interpolatedReciprocalW;
```

Luego calcularemos las interpolaciones `UV` dividiendo entre `w`:

```cpp
// Calculate the interpolations multipling every U/w and V/w coord per its weight factor per 1/w
interpolatedU = (t0.u/a.w) * alpha + (t1.u/b.w) * beta + (t2.u/c.w) * gamma;
interpolatedV = (t0.v/a.w) * alpha + (t1.v/b.w) * beta + (t2.v/c.w) * gamma;
```

Calcularemos la interpolación recíproca `1/w`:

```cpp
// Find the interpolate value of 1/w for the current pixel
interpolatedReciprocalW = (1/a.w) * alpha + (1/b.w) * beta + (1/c.w) * gamma;
```

Y dividimos los valores interpolados `UV` por ella:

```cpp
// Now we can divide back both interpolated values by 1/w
interpolatedU /= interpolatedReciprocalW;
interpolatedV /= interpolatedReciprocalW;
```

En este punto deberíamos estar realizando correctamente la interpolación corregida con perspectiva:

![]({{cdn}}/graficos3d/anim-33.gif)


## Optimizar divisiones comunes

El caso es que realizar para cada píxel estas divisiones le añade mucho estrés a la CPU:

```cpp
// Calculate the interpolations multipling every U/w and V/w coord per its weight factor per 1/w
interpolatedU = (t0.u/a.w) * alpha + (t1.u/b.w) * beta + (t2.u/c.w) * gamma;
interpolatedV = (t0.v/a.w) * alpha + (t1.v/b.w) * beta + (t2.v/c.w) * gamma;

// Find the interpolate value of 1/w for the current pixel
interpolatedReciprocalW = (1/a.w) * alpha + (1/b.w) * beta + (1/c.w) * gamma;
```

Si nos lo paramos a pensar muchas de estas divisiones las podemos realizar de forma común para todos los texels del mismo triángulo, así que vamos a sacarlas fuera para reutilizarlas:

```cpp
void Window::DrawTexturedTriangle(int x0, int y0, float z0, float w0, Texture2 uv0, int x1, int y1, float z1, float w1, Texture2 uv1, int x2, int y2, float z2, float w2, Texture2 uv2, uint32_t* texture)
{
    // ...

    // Create vector points for texturing after sorting the vertices
    Vector4 pA{ (double)x0, (double)y0, (double)z0, (double)w0 };
    Vector4 pB{ (double)x1, (double)y1, (double)z1, (double)w1 };
    Vector4 pC{ (double)x2, (double)y2, (double)z2, (double)w2 };

    // Common divisions for texel drawing in all the triangle face
    float uDivW[3] = { uv0.u / pA.w , uv1.u / pB.w, uv2.u / pC.w };
    float vDivW[3] = { uv0.v / pA.w , uv1.v / pB.w, uv2.v / pC.w };
    float oneDivW[3] = { 1 / pA.w , 1 / pB.w, 1 / pC.w };

    // REPLACE ALL DRAWTEXEL PASSING COMMON DIVISIONS
    DrawTexel(x, y, pA, pB, pC, uv0, uv1, uv2, uDivW, vDivW, oneDivW, texture, this);
}
```

Deberemos modificar el método `DrawTexel` para recibir estas divisiones comunes en sus respectivos arrays y utilizarlas:

```cpp
void Window::DrawTexel(int x, int y, Vector4 a, Vector4 b, Vector4 c, Texture2 t0, Texture2 t1, Texture2 t2, float *uDivW, float* vDivW, float* oneDivW, uint32_t *texture, Window *window)
{
    // ...
    interpolatedU = uDivW[0] * alpha + uDivW[1] * beta + uDivW[2] * gamma;
    interpolatedV = vDivW[0] * alpha + vDivW[1] * beta + vDivW[2] * gamma;
    interpolatedReciprocalW = oneDivW[0] * alpha + oneDivW[1] * beta + oneDivW[2] * gamma;
}
```

Con esto nos ahorremos bastantes divisiones y el código quedará mucho más optimizado.

## Coordenadas UV incorrectas

Para finalizar el tema, un pequeño experimento que podemos realizar es cambiar los primeros texels de la textura por un color sólido, por ejemplo blanco:

```cpp
REDBRICK_TEXTURE = new (std::nothrow) uint8_t[16400]{
    0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, // ...
}
```

Si comprobamos donde se han modificado estos colores es posible que nos encontremos un resultado distinto al esperado:

![]({{cdn}}/graficos3d/image-99.png)

En lugar de lo que presumiblemente era esperable y aparecer en la esquina superior izquierda, quizá aparecen en otro sitio.

La verdad es que he codificado manualmente las coordenadas UV de las caras sin prestar mucha atención a la disposición y por eso no aparece correctamente. 

Solucionar esta cara sería tan simple como cambiar las coordenadas UV por las correctas:

```cpp
Texture2 meshTextureUVs[]{ {1,0},{0,0},{0,1},{1,0},{0,1},{1,1}, //...
```

![]({{cdn}}/graficos3d/image-100.png)

Evidentemente este problema no lo tendremos con modelos generados en programas como **Blender** porque las coordenadas UV deberían ser siempre las correctas.

___
<small class="edited"><i>Última edición: 05 de Junio de 2022</i></small>