title: Tipos de datos | Curso Unity desde cero | Hektor Profe

# Tipos de datos

En esta lección vamos a introducir el uso de datos, otro de esos conceptos súmamente importantes, tanto en el desarrollo de videojuegos como en cualquier programa.

Vivimos en la era de la información, y esa información se representa digitalmente en forma de datos de diferentes tipos. Los tipos básicos que encontramos en Unity son:

* Los números enteros, llamados `integers`, no tienen parte decimal y pueden ser negativos.
* Los números decimales, llamados `floats`, tienen parte decimal y pueden ser negativos.
* Los valores lógicos, llamados `booleans`, representan la verdad/falsedad de una sentencia.
* Las cadenas de texto, llamadas `strings`, son para los caracteres y símbolos de escritura.

Luego tenemos tipos de datos estructurados como los `vectores`, que son conjuntos de varios decimales, o los `GameObjects`, que representan estructuras complejas formadas por multitud de información de todo tipo.

Por tanto, dependiendo de la información, deberemos utilizar unos tipos de datos u otros. Si queremos gestionar un número utilizaremos `integers` o `floats`, mientras que si necesitamos manipular un texto, utilizaremos `strings` y para almacenar el resultado de una sentencia lógica cuyo resultado sea verdadero o falso, haremos uso de los `booleans`.

Vamos a realizar algunos experimentos visuales para entender mejor cómo trabajar con los datos.

Cuando nuestro cubo se pone a dar vueltas y a flotar, lo hace porque hay un flujo desde el evento `Update` hasta las unidades de transformación.

¿Qué ocurriría si condicionamos el flujo dependiendo de un valor lógico verdadeo o falso? Vamos a hacerlo:

![]({{cdn}}/unity/Screenshot_85.png)

Lo que hemos conseguido aquí es un controlador que nos permite activar o desactivar el flujo de las transformaciones mediante una condición lógica llamada `if`, esn español `si`:

![]({{cdn}}/unity/Record_14.gif)

Vamos a mostrar en la consola un mensaje que nos diga si el cubo se mueve o no. Como un mensaje es una cadena de texto haremos uso del tipo `string` y lo pasaremos a una unidad que ejecute el método `Debug.Log`:

![]({{cdn}}/unity/Screenshot_86.png)

Dependiendo del valor lógico ahora se muestra un mensaje u otro por la consola:

![]({{cdn}}/unity/Screenshot_87.png)

Como véis con los datos podemos añadir dinamismo y mostrar información, pero hay un problema... Los datos que estamos manejando en nuestro ejemplo son valores literales, y si bien podemos modificarlos desde el `Script Graph` mientras desarrollamos el juego, en el juego final no vamos a contar con esta herramienta.

Si queremos manipular los datos de un videojuego necesitamos almacenarlos y ahí es donde entran en juego las variables, de las cuales hablaremos en la próxima lección.

___
<small class="edited"><i>Última edición: 14 de Abril de 2021</i></small>