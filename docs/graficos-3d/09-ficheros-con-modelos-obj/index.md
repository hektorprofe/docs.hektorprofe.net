title: Ficheros con modelos OBJ | Programación de gráficos 3D | Hektor Profe
description: 

# Ficheros con modelos OBJ

Es el momento de ir un paso más allá y cargar la información de un modelo desde un fichero generado en algún modelador 3D como Blender.

El formato de fichero elegido para importar los modelos es [Wavefront OBJ](https://en.wikipedia.org/wiki/Wavefront_.obj_file). Es el más simple y contiene la información necesaria para que nuestro programa pueda dibujar los objetos.

Sinceramente no tengo ni idea de utilizat [Blender](https://www.blender.org/) pero quiero crear algunos modelos y guardarlos para poder trabajar con ellos, así que lo he descargado e instalado.

Este programa es complejo pero por suerte para mí un proyecto empieza con un cubo:

![]({{cdn}}/graficos3d/image-34.png)

Así que simplemente voy a seleccionarlo y exportarlo como `obj` en `File > Export > Wavefront .obj`, lo llamaré `Cube.obj` y lo guardaré en el diretorio `assets` de mi proyecto, pero atención, debemos asegurarnos de que exporte el modelo con caras triangulares ya que por defecto lo hace en caras cuadradas y nuestro sistema no es compatible:

![]({{cdn}}/graficos3d/image-35.png)

El contenido de este fichero es el siguiente:

```
# Blender v3.1.2 OBJ File: ''
# www.blender.org
mtllib cube.mtl
o Cube
v 1.000000 1.000000 -1.000000
v 1.000000 -1.000000 -1.000000
v 1.000000 1.000000 1.000000
v 1.000000 -1.000000 1.000000
v -1.000000 1.000000 -1.000000
v -1.000000 -1.000000 -1.000000
v -1.000000 1.000000 1.000000
v -1.000000 -1.000000 1.000000
vt 0.875000 0.500000
vt 0.625000 0.750000
vt 0.625000 0.500000
vt 0.375000 1.000000
vt 0.375000 0.750000
vt 0.625000 0.000000
vt 0.375000 0.250000
vt 0.375000 0.000000
vt 0.375000 0.500000
vt 0.125000 0.750000
vt 0.125000 0.500000
vt 0.625000 0.250000
vt 0.875000 0.750000
vt 0.625000 1.000000
vn 0.0000 1.0000 0.0000
vn 0.0000 0.0000 1.0000
vn -1.0000 0.0000 0.0000
vn 0.0000 -1.0000 0.0000
vn 1.0000 0.0000 0.0000
vn 0.0000 0.0000 -1.0000
usemtl Material
s off
f 5/1/1 3/2/1 1/3/1
f 3/2/2 8/4/2 4/5/2
f 7/6/3 6/7/3 8/8/3
f 2/9/4 8/10/4 6/11/4
f 1/3/5 4/5/5 2/9/5
f 5/12/6 2/9/6 6/7/6
f 5/1/1 7/13/1 3/2/1
f 3/2/2 7/14/2 8/4/2
f 7/6/3 5/12/3 6/7/3
f 2/9/4 4/5/4 8/10/4
f 1/3/5 3/2/5 4/5/5
f 5/12/6 1/3/6 2/9/6
```

En la [Wikipedia](https://en.wikipedia.org/wiki/Wavefront_.obj_file) podemos encontrar una explicación sobre los contenidos:

```
# List of geometric vertices, with (x, y, z, [w]) 
# coordinates w is optional and defaults to 1.0.
v 0.123 0.234 0.345 1.0

# List of texture coordinates, in (u, [v, w]) 
# coordinates, these will vary between 0 and 1. 
# v, w are optional and default to 0.
vt 0.500 1 [0]

# List of vertex normals in (x,y,z) form;  
# normals might not be unit vectors.
vn 0.707 0.000 0.707

# Parameter space vertices in (u, [v, w]) form; 
# free form geometry statement ( see below )
vp 0.310000 3.210000 2.100000

# Polygonal face element (see below)
f 6/4/1 3/5/3 7/6/5

# Line element (see below)
l 5 8 1 2 4 9
```

Por ahora lo que a nosotros nos interesa son las líneas que empiezan con `v` (*vertices*) y `f` (*faces*) donde se definen la lista de vértices y caras poligonales respectivamente, justamente lo que hemos estado codificando a mano hasta ahora.

Si nos fijamos en las caras veremos que no hay ningún `0`, deberemos tenerlo en cuenta ya que nuestro sistema toma los índices empezando por 0.

Los valores de los vértices y caras se encuentran separados por espacios:

```
v 1.000000 1.000000 -1.000000
f 5/1/1 3/2/1 1/3/1
```

Pero como según la documentación, una cara puede contener a parte de sus vértices, la información de la textura del vértice (*vertex texture coordinate index*) y el vértice normalizado (*vertex normal index*), estos valores se encuentran separados por barras:

```
f v1/vt1/vn3 v1/vt3/vn3 v3/vt3/vn3
```

A nosotros nos interesa esencialmente el primer valor que es el que contiene el **índice del vértice**, ya más adelante haremos uso de otros de estos valores.

Recapitulando, nuestra tarea será desarrollar una funcionalidad que lea todas las líneas del fichero, identifique el código de la línea (v, vn, f...) y en función de ello genere la estructura necesaria para crear la malla en la memoria.

## Carga de OBJ en la memoria

Mi idea es añadir otro constructor a nuestro `Mesh` de manera que puedas enviar manualmente los vectores o alternativamente una cadena de texto con un PATH a un fichero para tomar los datos de ahí:

```cpp
Mesh(Window *window, std::string fileName);
```

Así crear nuestro cubo debería ser tan fácil como hacer:

```cpp
mesh = Mesh(this, "assets/cube.obj");
```

Así que manos a la obra:

```cpp
#include <fstream>

Mesh::Mesh(Window *window, std::string fileName)
{
    this->window = window;

    // Open the file
    std::ifstream file(fileName);
    if (!file.is_open())
    {
        std::cerr << "Error reading the file " << fileName << std::endl;
        return;
    }
    // If file is loaded in memory read each line
    std::string line;
    while (std::getline(file, line))
    {
        // if starts with v it's a vertex
        if (line.rfind("v ", 0) == 0)
        {
            Vector3 vertex; // %lf -> double (large float)
            sscanf(line.c_str(), "v %lf %lf %lf", &vertex.x, &vertex.y, &vertex.z);
            this->vertices.push_back(vertex);
        }
        // if starts with f it's a face
        else if (line.rfind("f ", 0) == 0)
        {
            int vertexIndices[3];
            int textureIndices[3];
            int normalIndices[3];
            sscanf(line.c_str(), "f %d/%d/%d %d/%d/%d %d/%d/%d",
                   &vertexIndices[0], &textureIndices[0], &normalIndices[0],
                   &vertexIndices[1], &textureIndices[1], &normalIndices[1],
                   &vertexIndices[2], &textureIndices[2], &normalIndices[2]);
            Vector3 face;
            face.x = vertexIndices[0];
            face.y = vertexIndices[1];
            face.z = vertexIndices[2];
            this->faces.push_back(face);
            this->triangles.push_back(Triangle());
        }
    }
}
```

Si funciona, el resultado pues será el aburrido cubo de siempre...

![]({{cdn}}/graficos3d/image-37.png)

Pero ahora podemos hacer algo más divertido, podemos crear alguna forma interesante en blender y exportarla.

Simplemente podemos crear un proyecto vacío, borrar el cubo y en `Add > Mesh` añadir alguna forma que nos guste, como un cono:

![]({{cdn}}/graficos3d/image-38.png)

O el mono de blender:

![]({{cdn}}/graficos3d/image-39.png)

Ahora si todo va bien, solo cambiando el nombre del fichero deberíamos ser capaces de cargar los distintos modelos.

Por ejemplo el cono de `cone.obj`:

![]({{cdn}}/graficos3d/anim-06.gif)

Y el mono de `monkey.obj`:

![]({{cdn}}/graficos3d/anim-07.gif)

En esta sección hemos dado un paso adelante enorme y ya no estamos limitados a trabajar simplemente con cubos.

___
<small class="edited"><i>Última edición: 05 de Junio de 2022</i></small>