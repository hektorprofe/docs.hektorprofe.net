title: Validando un email único | Curso de Django | Hektor Profe

# Validando un email único

Pues sí, el problema es que pueden haber dos usuarios con el mismo
email. Carece de toda lógica, pero el registro por defecto de Django no
sólo considera que el email es un campo optativo, sino que tampoco es
único. Menudo despropósito...

Probad a crear otro usuario con el mismo email, ya veréis:

![]({{cdn}}/django/images/image840.png)

Hay innumerables formas de solucionar este problema, cada una más
compleja que las demás, por eso vamos a utilizar la más sencilla de
todas: añadir una validación específica de campo. Sólo tenemos que ir al
formulario y añadir un método para validar, o mejor dicho “limpiar” el
campo email:

![]({{cdn}}/django/images/image3.png)

La lógica es sobreescribir el método clean\_\<nombre\_del\_campo\>, de
manera que a través de self podemos acceder a los campos después de que
Django los valide y añadir una validación extra.  Si no hay ningún
Usuario con ese email devolveremos el email validado, pero si existe
alguno invocaremos un error de tipo ValidationError con el mensaje que
queremos mostrar en el formulario:

![]({{cdn}}/django/images/image458.png)

Y con esto acabamos el formulario de registro.

___
<small class="edited"><i>Última edición: 25 de Marzo de 2021</i></small>