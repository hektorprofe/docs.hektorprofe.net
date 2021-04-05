title: Email obligatorio al registrarse | Curso de Django | Hektor Profe

# PEmail obligatorio al registrarse

Nuestro registro está muy bien, pero hay un problema, y es que por
defecto Django no requiere el email para dar de alta una cuenta. Esto
podría parecer una nimiedad, pero sin un email no os puedo enseñar cómo
configurar la restauración de contraseña, y es un tema importante porque
le añade un plus de calidad a nuestras páginas.

Podríamos crear el formulario desde cero o extender UserCreationForm. Mi
pereza me impide trabajar más de la cuenta así que haremos lo segundo.

![]({{cdn}}/django/images/image493.png)

Tened en cuenta que el campo email no es adrede, sino que es el nombre
del campo en el modelo User aunque no se haga uso de él por defecto.

Ahora tenemos que adaptar la vista:

![]({{cdn}}/django/images/image562.png)

Y sólo nos faltará extender el método get\_form con el nuevo campo
email:

![]({{cdn}}/django/images/image402.png)\
![]({{cdn}}/django/images/image402.png)

Un apunte importante: Tened en cuenta que estamos extendiendo el
formulario UserCreationForm y éste contiene sus propias validaciones. La
única forma de sustituir los widgets sin afectar al resto del formulario
es modificarlos en tiempo de ejecución desde el método get\_form.

En todo caso nuestro formulario se ve bastante bien… ¿Funcionará? Vamos
a probarlo:

![]({{cdn}}/django/images/image377.png)

Parece que sí, vamos a verificar su email a través del panel de
administrador:

![]({{cdn}}/django/images/image234.png)

Y sí, se ha guardado el correo:

![]({{cdn}}/django/images/image587.png)

Sin embargo todavía tenemos un último problema por solucionar… Lo
veremos en la próxima lección.

___
<small class="edited"><i>Última edición: 25 de Marzo de 2021</i></small>