title: Variables de objeto | Curso Unity desde cero | Hektor Profe

# Variables de objeto

En esta lección vamos a aborar el problema de trabajar con variables a nivel de gráfico y es que en un desarrollo óptimo un gráfico debería encargarse de una tarea y no mezclar acciones. Como decía Julio César, divida y vencerás.

En nuestro caso hemos realizado diferentes acciones en el mismo gráfico así que vamos a dividir su contenido en tres:

* `Controlador`: para activar o desactivar el movimiento.
* `Rotacion`: para añadir la rotación al objeto.
* `Traslacion`: para añadir la traslación al objeto.

Podemos clonar `Assets/Graphs/Experimento` un par de veces y cambiar sus nombres:

![]({{cdn}}/unity/Screenshot_97.png)

Ahora configuraremos tres máquinas de guiones, una para cada gráfico. Podemos simplemente copiar el componente y pegarlo como nuevo dos veces y configurarlos así:

![]({{cdn}}/unity/Screenshot_98.png)

Ahora vamos a establecer el código de cada gráfico para hacerlos independientes entre ellos.

**Controlador**:

![]({{cdn}}/unity/Screenshot_99.png)

**Rotación**:

![]({{cdn}}/unity/Screenshot_101.png)

**Traslación**:

![]({{cdn}}/unity/Screenshot_100.png)


Si probamos el videojuego notaremos que ya no funciona, pese a que el `Controlador` está funcionando y alterna correctamente la variable `Booleana`:

![]({{cdn}}/unity/Record_15.gif)

¿Qué está sucediendo? ¿Por qué no funciona? ¿Recordáis que al principio de la lección os he dicho que íbamos a abordar un problema? Pues aquí tenemos el problema.

La variable que tenemos en los gráficos, llamada `activarMovimiento`, en realidad no es una variable, sino tres variables diferentes con el mismo nombre. Cada una existiendo dentro del gráfico y de forma independiente de las demás.

Por suerte para nosotros, si lo que necesitamos es que las gráficos manipulen una variable común, podemos crearla a nivel del objeto. 

Así que vamos a borrar las tres variables `activarMovimiento` y luego la vamos a añadir de nuevo pero esta vez a nivel de `Objeto` desde el componente `Variables`:

![]({{cdn}}/unity/Screenshot_102.png)

Substituimos la variable a nivel de objeto en los tres gráficos, <u>teniendo en cuenta que ahora en el controlador debemos establecer el valor también a nivel de objeto</u>:

**Controlador**:

![]({{cdn}}/unity/Screenshot_106.png)

**Rotación**:

![]({{cdn}}/unity/Screenshot_104.png)

**Traslación**:

![]({{cdn}}/unity/Screenshot_105.png)

Y si ahora probamos el juego, al utilizar una variable común del objeto, ya funcionará perfectamente:

![]({{cdn}}/unity/Record_16.gif)

De la misma forma que una variable de gráfico no es común entre objetos, una de objetos no es común en la escena, ni una de escena en la aplicación.

Así que como véis el ámbito de las variables es un concepto muy importante y no podéis descuidarlo porque sino, dependiendo de lo que intentéis hacer, no podréis acceder a su información.

___
<small class="edited"><i>Última edición: 14 de Abril de 2021</i></small>