title: Paquete Cinemachine | Curso Unity desde cero | Hektor Profe

## Paquete Cinemachine

En esta lección vamos a introducir un paquete muy potente de Unity que utilizaremos bastante de ahora en adelante, se trata de `Cinemachine`, una colección de scripts automatizados para controlar cámaras.

Vamos a ir a `Window > Package Manager`, desplegaremos el menú y seleccionaremos `Unity Registry`, buscaremos el paquete `Cinemachine` y lo instalaremos:

![]({{cdn}}/unity/Screenshot_60.png)

Una vez instalado, vamos a crear una cámara muy sencilla desde `GameObject > Cinemachine > Virtual Camera`. La configuraremos con la propiedad `Follow` siguiendo a nuestra esfera, y el `body` será de tipo `Framing Transposer`, un encuadre de trasposición:

![]({{cdn}}/unity/Screenshot_61.png)

Solo habiendo hecho esto tendremos un sistema de seguimiento para la esfera que nos mostrará en todo momento y de forma suavizada una vista en tercera persona.

Si desactivamos la propiedad de la cámara virtual `Game Window Guides` este es el resultado:

![]({{cdn}}/unity/Record_09.gif)

Como véis en poco tiempo se puede empezar a conseguir resultados muy interesantes, pero la verdad es que solo estamos rascando la superfície.

___
<small class="edited"><i>Última edición: 12 de Abril de 2021</i></small>