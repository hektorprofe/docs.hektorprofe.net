title: Opción de editar la contraseña | Curso de Django | Hektor Profe

# Opción de editar la contraseña

Bien, como os comenté al final de la anterior lección vamos a dar al
usuario la posibilidad de editar su contraseña. Por suerte no tenemos
que hacerlo todo nosotros, la mayor parte del trabajo está hecho.

Vamos a empezar añadiendo un enlace en nuestro formulario de perfil:

![]({{cdn}}/django/images/image450.png)\
![]({{cdn}}/django/images/image919.png)\
        ![]({{cdn}}/django/images/image509.png)

Si accedemos al enlace nos aparecerá el formulario del administrador:

![]({{cdn}}/django/images/image74.png)

Sólo tenemos que cambiar estos templates por los nuestros. Os los voy
adjuntar en los recursos, como siempre sólo tenéis que copiarlos en el
directorio templates de la app registration:

![]({{cdn}}/django/images/image606.png)

Vamos a probar:

![]({{cdn}}/django/images/image830.png)

![]({{cdn}}/django/images/image921.png)

Para crearlos he tomado como referencia los originales, os vuelvo a
dejar el enlace al repositorio por si queréis ojearlos:
[https://github.com/django/django/tree/master/django/contrib/admin/templates/registration](https://www.google.com/url?q=https://github.com/django/django/tree/master/django/contrib/admin/templates/registration&sa=D&source=editors&ust=1616715294566000&usg=AOvVaw2BOBVCl_FeqmDARUZ2vQRD)

Con esto nuestro formulario está oficialmente acabado, hay un par de
detalles que vamos a mejorar en la siguientes dos lecciones y que
utilizaré como excusa para introduciros un nuevo concepto como son las
señales y también las pruebas unitarias.

___
<small class="edited"><i>Última edición: 25 de Marzo de 2021</i></small>