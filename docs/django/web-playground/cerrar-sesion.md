title: Cerrando la sesión | Curso de Django | Hektor Profe

# Cerrando la sesión 

En este punto sería interesante modificar el diseño del menú superior
para mostrar estas opciones en lugar de las del administrador. Vamos a
volver a base.html:

![]({{cdn}}/django/images/image345.png)

Al estar identificados debería aparecernos la opción de Salir:

![]({{cdn}}/django/images/image821.png)

Si salimos nos llevará a la pantalla por defecto como si saliéramos
desde el administrador.

![]({{cdn}}/django/images/image651.png)

Obviamente no queremos esto y como podéis suponer podemos cambiar la
página de redirección de la misma forma que hicimos con el Login:

![]({{cdn}}/django/images/image492.png)

Con esto acabamos la autenticación ¿Ha sido bastante fácil no? En las
siguientes lecciones estaremos trabajando el registro y la recuperación
de contraseñas.


___
<small class="edited"><i>Última edición: 25 de Marzo de 2021</i></small>