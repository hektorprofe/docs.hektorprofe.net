title: Reutilización de scripts | Curso Unity desde cero | Hektor Profe

# Reutilización de scripts

El objetivo de esta lección es reutilizar nuestros scripts gráficos en diferentes cubos pero logrando un comportamiento ligeramente distinto entre ellos mediante el uso de variables para controlar la velocidad de rotación y traslación.

Así que vamos a crear un par de variables `Vector3` en el objeto llamadas `vectorRotacion` y `vectorTraslacion`, a las que asignaremos unos valores por defecto como los que estamos usando actualmente:

![]({{cdn}}/unity/Screenshot_107.png)

Y utilizaremos estas variables como origen de los datos para transformar el cubo. 

Por eso en lugar de la versión que establece de forma independiente los ejes, cambiaremos a `transform rotate eulers`, que toma como entrada un vector 3D, asignando su entrada al vector como la salida de nuestra variable `velocidadRotacion`:

![]({{cdn}}/unity/Screenshot_109.png)

Y haremos exactamente lo mismo para la traslación, cambiando la unidad de transformación a una versión que tome un vector3 como entrada:

![]({{cdn}}/unity/Screenshot_111.png)

Ahora viene la parte divertida, vamos a clonar el cubo con diferentes colores y tamaños. En mi ejemplo he hecho uno naranja 3*3*3, uno azul 2*2*2 y uno rojo 1*1*1:

![]({{cdn}}/unity/Screenshot_112.png)

Si presionamos espacio los tres cubos empezarán a flotar, pero lo interesante es que podemos controla de forma independencia la velocidad de rotación y traslación de cada uno ajustando las variables que hemos creado:

![]({{cdn}}/unity/Record_17.gif)

Como véis reutilizar scripts es la clave a la hora de impementar funcionalidades comunes en los objetos.

Pero, ¿y si quisiéramos añadir una pequeña variación a uno de los tres cubos? Por ejemplo, que en lugar de mover el cubo rojo al presionar espacio, tengamos que presionar la tecla R?

Para conseguir esta variación debemos crear una copia `embebida` del script `Controlador` en el cubo rojo y modificarla.

Esto se consigue presionando el botón `Convert`:

![]({{cdn}}/unity/Screenshot_113.png)

Al hacerlo el gráfico de los recursos `Assets/Graphs/Controlador` se copiará como un recurso embebido dentro del propio objeto y podremos editarlo a nuestro gusto, siendo éste independiente de los demás cubos:

![]({{cdn}}/unity/Screenshot_114.png)

Simplemente editaremos el gráfico y cambiaremos la tecla `Space` por la letra `R`:

![]({{cdn}}/unity/Screenshot_115.png)

Sin más complicación ahora podremos controlar cuando se mueven los cubos naranja y azul con el espacio, y el rojo con la R:

![]({{cdn}}/unity/Record_18.gif)

Con esto ya sabemos lo básico sobre reutilizar scripts gráficos y cómo sobreescribir comportamientos específicos.


___
<small class="edited"><i>Última edición: 14 de Abril de 2021</i></small>