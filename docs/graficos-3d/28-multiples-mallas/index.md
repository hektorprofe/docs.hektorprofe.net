title: Múltiples mallas | Programación de gráficos 3D | Hektor Profe
description: 

# Múltiples mallas

Mi sistema cumple con todos los pasos importantes del *rendering pipeline*, pero antes de darlo por finalizado me gustaría añadir la funcionalidad de controlar múltiples `meshes`.

Esto incluye una serie de problemáticas respecto al funcionamiento actual y es que cada `mesh` se renderizada de forma independiente en su propio código, además la interfaz no está preparada para manejar múltiples modelos.

Voy a crear una clase llamada `RenderEngine` que tomará un vector de diferentes `mesh` y ejecutará sus métodos `Update` y `Render`:

```cpp
#ifndef ENGINE_H
#define ENGINE_H

#include <vector>
#include "mesh.h"

class RenderEngine
{
public:

	void SetMeshes(std::vector<Mesh> meshes)
	{
		this->meshes = meshes;
	}

	void Update()
	{
		for (size_t i = 0; i < meshes.size(); i++)
		{
			meshes[i].Update();
		}
	}

	void Render()
	{
		for (size_t i = 0; i < meshes.size(); i++)
		{
			
			meshes[i].Render();
		}
	}

private:
	std::vector<Mesh> meshes;
};

#endif
```

Luego puedo crear un vector de `mesh` en la ventana:

```cpp
#include "engine.h"

class Window
{
public:
    RenderEngine renderEngine;
private:
    std::vector<Mesh> meshes;
};
```

Cargar unos cuantos cubos y pasárselos al `RenderEngine`:

```cpp
/* Mesh loading */
meshes.push_back(
    Mesh(this, "res/cube.obj", "res/cube.png", Vector3(1, 1, 1), Vector3(0, 0, 0), Vector3(-3, 0, 8)));
meshes.push_back(
    Mesh(this, "res/cube.obj", "res/cube.png", Vector3(1, 1, 1), Vector3(0, 0, 0), Vector3(0, 0, 8)));
meshes.push_back(
    Mesh(this, "res/cube.obj", "res/cube.png", Vector3(1, 1, 1), Vector3(0, 0, 0), Vector3(3, 0, 8)));
meshes.push_back(
    Mesh(this, "res/cube.obj", "res/cube.png", Vector3(1, 1, 1), Vector3(0, 0, 0), Vector3(-1.5, 3, 8)));
meshes.push_back(
    Mesh(this, "res/cube.obj", "res/cube.png", Vector3(1, 1, 1), Vector3(0, 0, 0), Vector3(1.5, 3, 8)));
meshes.push_back(
    Mesh(this, "res/cube.obj", "res/cube.png", Vector3(1, 1, 1), Vector3(0, 0, 0), Vector3(0, 6, 8)));

// Send the loaded meshes to the render engine
renderEngine.SetMeshes(meshes);
```

En lugar de actualizar y dibujar una sola malla ejecuto `renderEngine.Update` y `renderEngine.Render` para procesar todos mis modelos de golpe:

![]({{cdn}}/graficos3d/anim-50.gif) 

Evidentemente lo óptimo sería unificar todo el *rendering pipeline* pero tengo otros proyectos en mente (como aprender `OpenGL`) y será en ese momento cuando aproveche para rehacer este experimento de una forma mucho más óptima.

Por cierto, ¿por qué un `<vector>` y no una `deque`? Porque hoy me ha dado por realizar algunos experimentos para determinar qué contenedor es más rápido y este es el resultado:

* `<deque>`:
    * Inicialización de 50'000'000 `Vector3`: 2782ms
    * Iteración y modificación de 50'000'000 `Vector3`: 377ms

* `<vector>`:
    * Inicialización de 50'000'000 `Vector3`: 1143ms
    * Iteración y modificación de 50'000'000 `Vector3`: 111ms

* `<vector>` con reserva:
    * Inicialización de 50'000'000 `Vector3`: 303ms
    * Iteración y modificación de 50'000'000 `Vector3`: 109ms

Por eso he cambiado todas mis `deque` por `vector`.

En cualquier caso con esto termino el desarrollo de mi renderizador de modelos 3D. He aprendido muchísimo y estoy muy ilusionado con aprender más tecnologías gráficas para complementar éste y futuros proyectos.

Sin más agradecer hasta el infinito el gran trabajo del profesor [Gustavo Pezzi](https://pikuma.com/) y su curso de gráficos 3D por haberme enseñado tanto, servirme como guía y fuente de inspiración.

___
<small class="edited"><i>Última edición: 05 de Junio de 2022</i></small>