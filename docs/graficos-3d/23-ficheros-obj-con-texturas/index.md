title: Ficheros OBJ con texturas | Programación de gráficos 3D | Hektor Profe
description: 

# Ficheros OBJ con texturas

Tenemos nuestro cubo y la textura cargada pero nos falta las coordenadas UV. 

Según la [wikipedia](https://en.wikipedia.org/wiki/Wavefront_.obj_file) en el fichero **obj** encontramos las coordenadas de texturas con el siguiente formato:

```python
# List of texture coordinates, in (u, [v, w]) coordinates, 
# these will vary between 0 and 1. v, w are optional and default to 0.
vt 0.500 1 [0]
vt ...
```

Si una cara tiene las coordenadas de texturas se reciben en la segunda posición separadas con una barra (`vt1, vt2, vt3`):

```python
f v1/vt1 v2/vt2 v3/vt3 ...
```

Los índices de las coordenadas para cada triángulo ya las estamos guardando:

```cpp
int textureIndices[3];
```

Lo que no tenemos todavía es la lista con la información de esas coordenadas, así que vamos a guardarlas en una nueva cola en la `mesh`:

```cpp
class Mesh
{
private:
    std::deque<Texture2> coordinates;
};
```

Las vamos añadiendo a la cola a medida que las encontremos:

```cpp
// if starts with vt it's a texture coordinate
else if (line.rfind("vt ", 0) == 0)
{
    Texture2 textureCoords;
    sscanf_s(line.c_str(), "vt %f %f", &textureCoords.u, &textureCoords.v);
    this->coordinates.push_back(textureCoords);
}
```

El constructor del triángulo tiene previsto que le enviemos las coordenadas de las texturas, las podemos recuperar y enviárselas:

```cpp
// recover the triangle coords using the textureIndeces
Texture2 triangleCoords[]{ 
    this->coordinates[textureIndices[0]], 
    this->coordinates[textureIndices[1]], 
    this->coordinates[textureIndices[2]]};
this->triangles.push_back(Triangle(0xFFFFFFFF, triangleCoords));
```

Si ponemos en marcha el programa para probar si funciona...

![]({{cdn}}/graficos3d/image-105.png)

Nos dice que estamos intentando acceder a un luar de la cola fuera del rango, eso es porque en el fichero **obj** los índices empiezan con `1` y no con `0`, debemos restarles `1`:

```cpp
Texture2 triangleCoords[]{ 
    this->coordinates[textureIndices[0] - 1], 
    this->coordinates[textureIndices[1] - 1], 
    this->coordinates[textureIndices[2] - 1]};
```

Si probamos ahora...

![]({{cdn}}/graficos3d/image-106.png)

¡Parece que nos estamos acercando! El problema es que las coordenadas y la textura no concuerdan. Podemos abrir **Blender** y aplicar nuestra textura a un nuevo cubo.

Soy un completo novato con Blender pero he encontrado un tutorial donde explican como hacerlo rápido.

Primero cambiamos al modo `Viewport Shading`:

![]({{cdn}}/graficos3d/image-107.png)

A continuación seleccionamos el cubo, vamos a `Material Properties` y cambiamos el `Base Color` por una `Image Texture` y buscamos la que queremos aplicar:

![]({{cdn}}/graficos3d/image-108.png)

Al hacerlo veremos que efectivamente las coordenadas UV por defecto del cubo no pintan nuestra textura como nosotros queremos, tenemos que cambiarlas manualmente.

Abriremos el modo `UV Editor`:

![]({{cdn}}/graficos3d/image-109.png)

Y cambiaremos a la imagen de nuestro cubo:

![]({{cdn}}/graficos3d/image-110.png)

Si arrastramos desde la esquina superior derecha del editor (aparece una cruz en el puntero) podemos activar dos vistas, nos será útil:

![]({{cdn}}/graficos3d/image-111.png)

Si activamos el modo de selección de caras y seleccionamos una veremos qué parte de la textura se está aplicando:

![]({{cdn}}/graficos3d/image-112.png)

Como se puede apreciar está mal mapeado, nosotros queremos que el cuadrado sea la cara completa.

Buscaremos la opción `UV > Smart UV Project` y le daremos a OK:

![]({{cdn}}/graficos3d/image-113.png)

Automáticamente el tamaño de la cara se establecerá al completo, esto debería corregir las coordenadas UV de esa cara:

![]({{cdn}}/graficos3d/image-114.png)

Seguramente hay alguna opción para repetir esto en todos las caras, pero no tengo ni idea(algún día seguro que lo aprenderé), así que repetiré el proceso para cada cara:

![]({{cdn}}/graficos3d/image-115.png)

Una vez las tenga todas corregidas exportaré el cubo en `obj` con `Y` creciente hacia abajo, caras triangulares y las nuevas coordenadas UV:

![]({{cdn}}/graficos3d/image-116.png)

El programa debería renderizarlo correctamente:

![]({{cdn}}/graficos3d/image-118.png)

Efectivamente, ya se renderiza, pero todavía tenemos un último problema pendiente... ¿Lo hace de forma volteada?

El caso es que Blender nos da los valores de las coordenadas V invertidas, deberemos voltearlas. Es muy fácil, simplemente hacemos lo siguiente justo después de ordenar los vértices en el `DrawTexturedTriangle`:

```cpp
// Flip the V component to account for inverted UV-coordinates
uv0.v = 1 - uv0.v;
uv1.v = 1 - uv1.v;
uv2.v = 1 - uv2.v;
```

Por fin tendremos nuestra recompensa, un cubo modelado y texturizado en **Blender** cargado perfectamente en nuestro visualizador 3D:

![]({{cdn}}/graficos3d/anim-35.gif)

## Prevenir overflow del buffer de textura

Tenemos que tener en cuenta algo importante a la hora de renderizar los pixels relativos al texel.

Si por casualidad el cálculo de `alpha`, `beta` o `gamma` es muy pequeño, por ejemplo `0.00001`, acabaremos con un número negativo muy pequeño implicando que el punto está fuera del triángulo.

Las coordenadas baricéntricas son puras matemáticas para definir un punto en un triángulo, pero en la realidad tenemos una pantalla con un número limitado de píxels y esa "proyección" que hacemos no concuerda con la realidad, saliéndose del espacio de dibujado y causando potenciales fallos:

![]({{cdn}}/graficos3d/image-117.png)

Esto nos lleva a la conocida como *fill convention*, la convención de relleno para determinar si un píxel se encuentra dentro o fuera del triángulo para realizar un redondeo al alza (*ceil*) o a la baja (*floor*).

Este tema llevó de calle a los ingenieros del paso pero en mi caso no voy a complicarme demasiado. Pemitiré que un valor se encuentre fuera del triángulo, pero si eso sucede simplemente truncaremos el valor haciendo el módulo del `textureWidth` y el `textureHeight` para que el valor no se salga de los límites:

```cpp
// Calculate the texelX and texelY based on the interpolated UV and the texture sizes
int texelX = abs(static_cast<int>(interpolatedU * textureWidth)) % textureWidth;
int texelY = abs(static_cast<int>(interpolatedV * textureHeight)) % textureHeight;
```

Este pequeño *hack* debería prevenir que ocurra un overflow.

Así queda este modelo de un [cangrejo](https://sketchfab.com/3d-models/dancing-crab-uca-mjoebergi-280863886fee409ab3c8168f07caa89f):

![]({{cdn}}/graficos3d/anim-36.gif)

Aquí se puede observar cómo todavía tenemos un problema al renderizar la profundidad de los vértices, dibujándose la pinza del cangrejo por detrás del cuerpo.

En la próxima sección vamos a arreglarlo.

___
<small class="edited"><i>Última edición: 05 de Junio de 2022</i></small>