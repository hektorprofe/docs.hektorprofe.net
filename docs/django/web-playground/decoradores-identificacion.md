title: Usando decoradores de identificación | Curso de Django | Hektor Profe

# Usando decoradores de identificación

¿Entonces cada vez que queramos comprobar si un usuario está
identificado tenemos que crear un Mixin? Pues no, eso os lo he enseñado
con la excusa de que aprendáis a crear Mixins y ver el potencial que
tienen, pero por suerte para nosotros Django incluye varias funciones
decoradoras para requerir identificación antes de devolver una vista.

Por ejemplo, dentro de nuestro StaffRequiredMixin podríamos ahorrarnos
la parte de comprobar al usuario haciendo uso de la función decoradora
staff\_member\_required a través del decorador de métodos
method\_decorator:

![]({{cdn}}/django/images/image828.png)\
![]({{cdn}}/django/images/image162.png)

Lo bueno que tiene este decorador es que redirecciona de nuevo a la
página donde teníamos que identificarnos para seguir trabajando:

![]({{cdn}}/django/images/image389.png)

Pero en el fondo esto de la redirección es lo de menos, lo bueno que
tiene el uso de decoradores es que no estamos obligados a utilizarlos en
Mixins, sino que se pueden enviar a las CBV directamente, sólo debemos
definir el method\_decorator antes de la CBV e indicarle el decorador y
el nombre del método donde queremos añadirlo, en nuestro caso el
dispatch (podemos borrar el mixin porque ya no lo necesitamos):

![]({{cdn}}/django/images/image42.png)

Cómo véis ni siquiera necesitábamos un Mixin, pero en el proceso hemos
aprendido un montón de cosas.

Existen dos funciones decoradoras más:

-   login\_required para comprobar que un usuario esté identificado
-   permission\_required para comprobar que un usuario esté identificado
    y a la vez tenga algún permiso

Os voy a dejar documentación de todas en los recursos, así como la forma
de decorar directamente en el URLPatterns:\
\
[https://docs.djangoproject.com/en/dev/topics/auth/default/\#the-login-required-decorator](https://docs.djangoproject.com/en/dev/topics/auth/default/\#the-login-required-decorator)\
[https://docs.djangoproject.com/en/dev/topics/auth/default/\#the-permission-required-decorator](https://docs.djangoproject.com/en/dev/topics/auth/default/\#the-permission-required-decorator) \
[https://docs.djangoproject.com/en/dev/topics/class-based-views/intro/\#decorating-class-based-views](https://docs.djangoproject.com/en/dev/topics/class-based-views/intro/\#decorating-class-based-views) \
[https://docs.djangoproject.com/en/dev/\_modules/django/contrib/admin/views/decorators/](https://docs.djangoproject.com/en/dev/\_modules/django/contrib/admin/views/decorators/) 

Y con esto acabamos la introducción a las CBV y las vistas CRUD.

Ahora ya contáis con los fundamentos necesarios para empezar a trabajar
la autenticación, el registro y el manejo de usuarios, así que si no os
perdáis las próximas lecciones. 

Refactorizando CBV en las URLs - NO SE EXPLICARÁ, DEMASIADOS PROBLEMAS

Estoy seguro de que con todo lo que hemos hecho hasta ahora sobre CBV ya
os ha quedado claro su potencial, ¿pero os imagináis que pudiéramos
ahorrarnos incluso más trabajo? Pues váis a flipar, porque ¿y si os digo
que podemos trasladar casi todo lo que tenemos sólo a nuestras urls y
ahorrarnos las vistas os lo creeríais?

Mirad, vamos a core/urls y haremos la magia ahí:

![]({{cdn}}/django/images/image695.png)\
![]({{cdn}}/django/images/image37.png)

¿Habéis visto? Podemos generar nuestras CBV ahí mismo e incluso enviar
un diccionario de contexto. ¿Pero podremos hacer lo mismo con las CBV de
la app Pages? Vamos a probar:

![]({{cdn}}/django/images/image90.png)

Para las tres primeras no tendremos ningún problema, podemos generarlas
sin problemas. Lo malo es la UpdateView porque contiene un método. Los
métodos no podemos redefinirlos aquí, por lo que lo más sensato es
dejarnos de historias y dejarla como la teníamos:

![]({{cdn}}/django/images/image400.png)\
![]({{cdn}}/django/images/image99.png)

Finalmente la DeleteView si podemos generarla sin problemas:

![]({{cdn}}/django/images/image800.png)

Así que podemos volver a views.py y borrar todo lo que no necesitamos,
aunque a vosotros mejor os recomiendo comentarlo por si en un futuro
queréis analizarlo:

![]({{cdn}}/django/images/image635.png)

Hemos pasado de tener más de 30 líneas a apenas unas 13 definiendo
nuestras CBV en el propio urls.py. ¿Qué os parece?

___
<small class="edited"><i>Última edición: 25 de Marzo de 2021</i></small>