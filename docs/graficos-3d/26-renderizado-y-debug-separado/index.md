title: Renderizado y debug por separado | Programación de gráficos 3D | Hektor Profe
description: 

# Renderizado y debug por separado

En este bloque mi objetivo es separar el renderizado y el debug para que los eventos como hacer clic no se molesten mútuamente. Con esto podré mejorar la funcionalidad de `mouseClicked` y conseguir un resultado más óptimo.

Para separar espacios voy a crear diferentes espacios de `Dear ImGuI` y ya que estoy también un menú:

```cpp
// Iniciamos un Frame de Imgui
ImGui_ImplSDLRenderer_NewFrame();
ImGui_ImplSDL2_NewFrame(window);
ImGui::NewFrame();

// Top menú bar
if (ImGui::BeginMainMenuBar())
{
    if (ImGui::BeginMenu("Archivo"))
    {
        if (ImGui::MenuItem("Salir")) { running = false; }
        ImGui::EndMenu();
    }
    ImGui::EndMainMenuBar();
}

// Rendering window
ImGui::Begin("Rendering");
ImGui::Image(colorBufferTexture, ImVec2(900, 600));
ImGui::End();

// Debug window
ImGui::Begin("Debugging");
ImGui::Checkbox("Limitar FPS", &this->enableCap);
//...
ImGui::End();

// End Frame
ImGui::EndFrame();
```

El punto interesante es que en la ventana de rendering lo que hacemos es dibujar una imagen con precisamente el `colorBufferTexture`. Para que no lo dibuje dos veces lo único que debemos hacer es durante el `RenderColorBuffer` no copiar la textura al renderer principal:

```cpp
void Window::RenderColorBuffer()
{
    SDL_UpdateTexture(colorBufferTexture, NULL, colorBuffer, windowWidth * sizeof(uint32_t));
    //SDL_RenderCopy(renderer, colorBufferTexture, NULL, NULL);
}
```

En este punto me interesa que los buffers de color y profundidad tengan un tamaño más pequeño, o que en última instancia quizá en el futuro, se adapten al tamaño de la ventana interior. Por eso voy a crear dos variables para controlar ese tamaño:

```cpp
class Window
{
public:
    int rendererWidth;
    int rendererHeight;
};
```

Por ahora las estableceré en el constructor de la ventana, también aprovecharé para establecer el `aspectRatio` con la proporción de la ventana raíz y recalcuilar la matriz de proyección:

```cpp
Window() : windowWidth(1280), windowHeight(720), rendererWidth(960), rendererHeight(640) 
{
    aspectRatio = rendererHeight / static_cast<float>(rendererWidth);
    projectionMatrix = Matrix4::PerspectiveMatrix(fovFactor, aspectRatio, zNear, zFar);
};
```

Estos nuevos tamaños serán los que utilizaré en lugar de `windowWidth` y `windowHeight` en todo el fichero `window.cpp`, así que **refactorizaré ambos campos para cambiarles el nombre** excepto al momento de crear la ventana que conservaremos los tamaños iniciales:

```cpp
// Creamos la ventana SDL
SDL_WindowFlags window_flags = (SDL_WindowFlags)(SDL_WINDOW_RESIZABLE | SDL_WINDOW_ALLOW_HIGHDPI); // SDL_WINDOW_BORDERLESS
window = SDL_CreateWindow( "3D Renderer", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, windowWidth, windowHeight, window_flags);
```

Por supuesto no olvidemos cambiar el tamaño harcodeado de la imagen en la subventana del rendering:

```cpp
ImGui::Image(colorBufferTexture, ImVec2(rendererWidth, rendererHeight));
```

Ni tampoco las rectificaciones de posición una vez proyectados los vértices y las normales en el `mesh.cpp`:

```cpp
/*** Apply projections and lighting for all face vertices ***/
for (size_t j = 0; j < 3; j++)
{
    // Project the current vertex using matrices
    triangles[i].ProjectWorldVertex(j, window->projectionMatrix);
    // First scale the projected vertex by screen sizes
    triangles[i].projectedVertices[j].x *= (window->rendererWidth / 2.0);
    triangles[i].projectedVertices[j].y *= (window->rendererHeight / 2.0);
    // Invert the y values to account the flipped screen y coord
    triangles[i].projectedVertices[j].y *= -1;
    // Then translate the projected vertex to the middle screen
    triangles[i].projectedVertices[j].x += (window->rendererWidth / 2.0);
    triangles[i].projectedVertices[j].y += (window->rendererHeight / 2.0);
}

// Project the normal vectors if we want to draw it
if (window->drawTriangleNormals)
{
    // Project the current normal to create an origin and a destiny vectors
    triangles[i].ProjectWorldNormal(window->projectionMatrix);
    for (size_t j = 0; j < 2; j++)
    {
        // First scale the projected vertex by screen sizes
        triangles[i].projectedNormal[j].x *= (window->rendererWidth / 2.0);
        triangles[i].projectedNormal[j].y *= (window->rendererHeight / 2.0);
        // Invert the y values to account the flipped screen y coord
        triangles[i].projectedNormal[j].y *= -1;
        // Then translate the projected vertex to the middle screen
        triangles[i].projectedNormal[j].x += (window->rendererWidth / 2.0);
        triangles[i].projectedNormal[j].y += (window->rendererHeight / 2.0);
    }
}
```

Por último, y es muy importante, desactivaremos el movimiento de las ventanas haciendo clic, sólo lo permitiremos arrastrando la barra de título:

```cpp
// Setup Dear ImGui context
IMGUI_CHECKVERSION();
ImGui::CreateContext();
ImGuiIO& io = ImGui::GetIO(); (void)io;
io.ConfigWindowsMoveFromTitleBarOnly = true;
```

Con esto en principio tendremos las dos partes por separado:

![]({{cdn}}/graficos3d/image-137.png)

Por desgracia si hacemos clic en cualquier parte seguiremos modificando la cámara, pero ahora podemos hacer algo muy interesante. Podemos definir una variable para detectar si nuestra subventana se encuentra activa con el ratón encima:

```cpp
class Window
{
public:
    bool rendererActive;
};
```

Y durante la definición de la ventana con `ImGui` establecer su estado:

```cpp
// Rendering window
ImGui::Begin("Rendering");
ImGui::Image(colorBufferTexture, ImVec2(rendererWidth, rendererHeight));
rendererActive = ImGui::IsWindowFocused() && ImGui::IsWindowHovered();
ImGui::End();
```

Ahora podemos utilizar esto como condición para poder rotar la vista:

```cpp
case SDL_MOUSEMOTION:
    // Process rotation only if...
    if (mouseClicked and rendererActive)
    {
```

Y para moverla:

```cpp
// Process the WASD movement with a keyState map only if...
if (rendererActive)
{
    const uint8_t* keystate = SDL_GetKeyboardState(NULL);
```

Todavía quedan algunos bugs y se puede pulir más pero creo que empieza a dar el pego:

![]({{cdn}}/graficos3d/anim-43.gif) 

Algo que podemos hacer es que mientras se arrastra la subventana de `Rendering` tampoco se pueda interactuar con la cámara. Para ello podemos definir:

```cpp
class Window
{
public:
    bool rendererDragged;
};
```

Mientras establecemos la subventana, justo después del `ImGui::Begin` almacenaremos si el ratón se encuentra sobre la franja del título (el contextualizador funciona de esa forma):

```cpp
// Rendering window
ImGui::Begin("Rendering");
rendererDragged = ImGui::IsItemHovered();
```

Luego lo utilizamos de condición como ya hicimos antes:

```cpp
case SDL_MOUSEMOTION:
    // Process rotation only if...
    if (mouseClicked and rendererActive and !rendererDragged)
    {
```

```cpp
// Process the WASD movement with a keyState map only if...
if (rendererActive and !rendererDragged)
{
    const uint8_t* keystate = SDL_GetKeyboardState(NULL);
```

Un último detalle que me gustaría implementar es la posibilidad de que la rueda de ratón pueda hacer zoom como pasa en editores como Unity. Tengo la costumbre de hacerlo y me sale de forma natural así que la voy a añadir a modo de incremento y decremento en el eje `z` de la cámara:

```cpp
case SDL_MOUSEWHEEL:
    if (rendererActive and !rendererDragged) {
        // Scroll up
        if (event.wheel.y > 0)
        {
            camera.forwardVelocity = camera.direction * 30.0 * deltaTime;
            camera.position += camera.forwardVelocity;
        }
        // Scroll down
        else if (event.wheel.y < 0)
        {
            camera.forwardVelocity = camera.direction * 30.0 * deltaTime;
            camera.position -= camera.forwardVelocity;
        }
        // Set the result moving positions into the camera interface
        cameraPosition[0] = camera.position.x;
        cameraPosition[1] = camera.position.y;
        cameraPosition[2] = camera.position.z;
    }
    break;
```

El resultado final es todo lo que podía esperar:

![]({{cdn}}/graficos3d/anim-44.gif) 

___
<small class="edited"><i>Última edición: 05 de Junio de 2022</i></small>