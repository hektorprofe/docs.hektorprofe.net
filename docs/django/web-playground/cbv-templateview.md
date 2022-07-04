title: Class Based Views y TemplateView | Curso de Django | Hektor Profe

# Class Based Views y TemplateView

Desde el principio del curso todas las vistas que hemos creado en
nuestros proyectos han sido vistas basadas en funciones, FBV. Su nombre
está claro, pues se definen en simples funciones que luego llamamos en
el respectivo fichero urls.py. Estas eran las únicas vistas que se
podían crear hasta que llegaron las vistas basadas en clases.

¿Qué diferencia hay? Bueno, si lo pensáis detenidamente una clase es una
estructura mucho más completa que una simple función. Permite usarla de
molde y puede contener comportamientos predefinidos que se pueden
heredar en otras clases, así que tienen un objetivo muy claro:
ahorrarnos tiempos a la hora de implementar funcionalidades comunes.

En otras palabras, tenemos a nuestra disposición un amplio catálogo de
Vistas Basadas en Clases a modo de plantillas que podemos utilizar y
extender a voluntad.

Hay una web increíble llamada
[https://ccbv.co.uk/](https://www.google.com/url?q=https://ccbv.co.uk/&sa=D&source=editors&ust=1616715294446000&usg=AOvVaw2cOWk0e6YNkZrfsadNU9Wh) donde
podemos encontrar un resumen y documentación de todas ellas (entrar y
comentarlas):

![]({{cdn}}/django/images/image406.png)

A lo largo de esta web playground haremos uso de un montón de ellas, ya
veréis.

Vamos a empezar con la app Core, ¿cómo se traduciría lo que tenemos
ahora a CBV? Bueno, lo primero es elegir qué tipo de CBV se adaptaría
mejor a nuestras necesidades.

Como las vistas de Blog no tienen nada de especial y simplemente cargan
un Template, deberíamos buscar una CBV genérica, concretamente la de
TemplateView.

Entramos a la documentación:
[https://ccbv.co.uk/projects/Django/2.0/django.views.generic.base/TemplateView/](https://www.google.com/url?q=https://ccbv.co.uk/projects/Django/2.0/django.views.generic.base/TemplateView/&sa=D&source=editors&ust=1616715294448000&usg=AOvVaw2a3dnMj8hyhptbt7lRwfUi) \
Y de ahí a la documentación de Django:
[https://docs.djangoproject.com/en/dev/ref/class-based-views/...](https://www.google.com/url?q=https://docs.djangoproject.com/en/dev/ref/class-based-views/base/%23django.views.generic.base.TemplateView&sa=D&source=editors&ust=1616715294448000&usg=AOvVaw38UanB32DO3CBOMrosHuJF) 

En la documentación encontraremos cómo manejar las TemplateView:

![]({{cdn}}/django/images/image69.png)

En este ejemplo nos muestran como crear una CBV TemplateView, pasar
valores al diccionario de contexto y cómo llamarla en urls. Nosotros no
tenemos que enviar nada, así que nos será más fácil:

![]({{cdn}}/django/images/image308.png)\
![]({{cdn}}/django/images/image189.png)

Como véis ya no estamos creando funciones que devuelven el template con
la lógica, sino clases que heredan de TemplateView y que por defecto
tienen un atributo llamado template\_name. Luego a la hora de llamarlas
en el urls tienen un método llamado as\_view() que las devuelve como una
vista. Vamos a probar:

![]({{cdn}}/django/images/image335.png)

Cómo veis está todo igual. ¿Por qué no probamos a enviar algún dato al
diccionario de contexto? Para ello sobreescribiremos el método
get\_context\_data que debe devolver un diccionario de contexto después
de recuperarlo de la superclase:

![]({{cdn}}/django/images/image207.png)\
![]({{cdn}}/django/images/image851.png)\
![]({{cdn}}/django/images/image55.png)

Pero como esto es un poco complejo, en lugar de modificar el contexto es
posible sobreescribir el método get que es el encargado de devolver la
respuesta:

![]({{cdn}}/django/images/image228.png)\
![]({{cdn}}/django/images/image55.png)

¿Esto ya se parece más a una FBV no?

Por cierto, ¿se os ocurre alguna razón por la que este método se llame
get? Pues sí, se llama GET ni más ni menos porque se encarga de
responder las peticiones GET, así que podéis suponer que también existe
un método POST, algo muy conveniente para separar la lógica al procesar
formularios, pero eso lo veremos más adelante.

Por ahora es posible que muchos os preguntéis para qué utilizar las CBV
y complicarnos la vida. Es verdad que cambiar la forma de pensar es
difícil, pero creedme que vale la pena y os lo demostraré en las
siguientes lecciones.

___
<small class="edited"><i>Última edición: 25 de Marzo de 2021</i></small>