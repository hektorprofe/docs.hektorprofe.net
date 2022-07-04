title: Objetos, recursos y prefabs | Curso Unity desde cero | Hektor Profe

# Objetos, recursos y prefabs

Antes hemos interactuado con algunos objetos como la cámara y las luces, pero esos no son los únicos objetos de la escena, la realidad es que todo lo que existe en la escena SON objetos.

Fijémonos en la jeraquía, ¿véis el cubo a la izquierda de cada elemento? Eso nos indica que es un objeto de juego, en inglés `GameObject`:

![]({{cdn}}/unity/Screenshot_10.png)

¿Y véis que hay objetos que tienen varios niveles? Eso significa que son objetos compuestos de otros objetos, como un padre con muchos hijos enlazados a él:

![]({{cdn}}/unity/Screenshot_37.png)

Muy bien, pues para que estos objetos existan, debemos añadirlos de alguna forma y de algún sitio, ¿no? Pues ese sitio son los recursos del proyecto:

![]({{cdn}}/unity/Screenshot_11.png)

Los recursos, o assets en inglés, contienen todo tipo de información. Desde los modelos 3D de los objetos, los materiales, las texturas, los sonidos, los ficheros de configuración, las bases de datos y un larguísimo etcétera, que incluye incluso, la información de las propias escenas.

Y es que en un proyecto poemos tener múltiples escenas. La escena actual se llama `SampleScene` y podemos guardarla con `Control+S`. El recurso de esta escena se encuentra en la carpeta `Assets/Scenes`. Otros recursos se encuentran en otras carpetas bien organizadas, como `ExampleAssets`, `Materials`, `Presets`, `Scripts`, etc.

Vamos a acercarnos un poco a la mesa de trabajo de la escena, y utilizando la herramienta de movimiento (W), vamos a seleccionar ese casco amarillo. Si os aparecen unas bolas enormes es debido a los iconos de ayuda de la interfaz de Unity conocidos como Gizmos. Podemos hacerlos más pequeños:

![]({{cdn}}/unity/Screenshot_12.png)

Y desactivar esas líneas amarillos que tienen que ver con las luces desactivando los Gizmos de `LightProbeGroup`:

![]({{cdn}}/unity/Screenshot_13.png)

Así veremos simplemente el casco seleccionado con un borde naranja:

![]({{cdn}}/unity/Screenshot_14.png)

Este casco es, como os comenté al princpio, un `GameObject`, concretamente uno llamado `Safety Hat`, y también podemos moverlo mediante las flechas y el cuadrado (W) y rotarlo (E):

![]({{cdn}}/unity/Screenshot_15.png)

Vamos a crear otro casco a partir de su recurso. Para hacerlo buscaremos en la ventana de recursos, en `Models` el modelo `safetyhat` y lo arrastraremos al suelo de la escena:

![]({{cdn}}/unity/Screenshot_16.png)

Como véis por defecto este casco es gris, eso es porque no tiene una textura. En el directorio `Textures\Props\HardHat` encontramos tres texturas para nuestro casco, vamos a arrastrar la azul al casco:

![]({{cdn}}/unity/Screenshot_17.png)

Como véis, en el momento en que arrastramos un recurso a la escena se crea un objeto para representarlo.

Si quisiéramos crear otro casco azul, podríamos repetir el proceso o duplicarlo, seleccionando el objeto `safetyhat` en la jeraquía y presionando `Control+D`:

![]({{cdn}}/unity/Screenshot_18.png)

Pero quiero que tengáis presente una cosa, estos dos cascos son objetos independientes entre ellos. Si arrastramos la textura rosa a uno de ellos, los cambios no afectan al otro:

![]({{cdn}}/unity/Screenshot_19.png)

Sin embargo ese no es el caso de los `Prefabs`. ¿Véis en la jerarquía que hay algunos objetos cuyo cubo es de color azul? Eso significa que son `Prefabs`, plantillas para generar objetos iguales.

Si navegamos al directorio `Assets/Prefabs` veremos algunos. Por ejemplo los botes de pintura. Vamos a arrastrar algunos a la escena:

![]({{cdn}}/unity/Screenshot_20.png)

La diferencia entre tener objetos independientes y prefabs, es que éstos últimos están enlazados a una plantilla común, o dicho de otra forma, a un objeto original.

Si hacemos doble clic en el prefab de los botes de colores, se abrirá de forma independiente:

![]({{cdn}}/unity/Screenshot_21.png)

Si modificamos algún elemento de este Prefab, por ejemplo modificando el tamaño de los botes y la brocha (R), rotándolos un poco y moviéndolos de sitio...

![]({{cdn}}/unity/Screenshot_22.png)

Si ahora volvemos a la escena haciendo clic en `Screnes > Paint Supplies` de la parte superior, veremos que se han modificado todos los botes de pintura al modificar nosotros el original.

![]({{cdn}}/unity/Screenshot_23.png)

Después de este experimento queda clara la idea de que los `objetos` se crean a partir de `recursos` y pueden ser independientes o estar vinculados a un `prefab`.

Poco a poco ahondaremos en estos temas e incluso crearemos nuestros propios prefabs.

___
<small class="edited"><i>Última edición: 11 de Abril de 2021</i></small>