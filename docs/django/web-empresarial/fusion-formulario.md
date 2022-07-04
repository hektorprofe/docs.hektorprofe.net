title: Fusionando el formulario | Curso de Django | Hektor Profe 

# Fusionando el formulario

Lo que vamos a hacer es reutilizar nuestra maqueta y cambiar sólo las
partes dinámicas. Para ello dibujaremos los campos manualmente en lugar
de hacer que Django lo muestre todo de golpe. Este proceso viene
detallado en la documentación, como siempre os comparto el enlace en los
recursos.

[https://docs.djangoproject.com/en/dev/topics/forms/\#rendering-fields-manually](https://docs.djangoproject.com/en/dev/topics/forms/\#rendering-fields-manually) 

Vamos a sustituir la parte del renderizado por nuestro código:

![]({{cdn}}/django/images/image489.png)

Ahora vamos a sustituir los campos Nombre, Email y Mensaje por lo
siguiente:

![]({{cdn}}/django/images/image256.png)

Obviamente hacerlo de esta forma es más trabajoso pero también más
elegante, ya que podemos añadir estilos a la validación de errores.
Justo después de cada campo podemos mostrar sus errores específicos con
{%raw%}{{ form.campo.errors }}{%endraw%}. Si existen errores Django genera una lista con
la clase ‘errorList’ (ver código fuente). Como yo ya he maquetado de
antemano los estilos de esa clase nos saldrá bien:

![]({{cdn}}/django/images/image397.png)

Vamos a ver como queda:

![]({{cdn}}/django/images/image303.png)

Va tomando forma, pero todavía nos faltan unos pequeños detalles: los
atributos internos de los inputs y el textarea.

Estas configuraciones nos permitirán modificar las longitudes mínimas y
máximas, o cualquier atributo del campo sobreescribiendo el diccionario
attrs a partir del widget, lo cual es útil para añadir una clase css al
campo y darle la apariencia que tenía en nuestra maqueta, entre otras
muchas cosas:

![]({{cdn}}/django/images/image783.png)

Y con esto ahora sí tenemos el formulario perfecto, sólo nos faltará
implementar el envío de emails:

![]({{cdn}}/django/images/image278.png)


___
<small class="edited"><i>Última edición: 25 de Marzo de 2021</i></small>