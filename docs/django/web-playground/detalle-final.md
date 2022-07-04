title: El detalle final | Curso de Django | Hektor Profe

# El detalle final

Si habéis experimentado un poco os habréis dado cuenta de un
detalle muy importante que falta, y ese es que los hilos salgan
ordenados de más recientes a más antiguos.

¿Se os ocurre alguna forma de hacerlo? Haber si sois capaces de en muy
pocos pasos arreglar este problema, os aseguro que sólo hay que añadir 4
líneas en nuestro fichero models.py.

Para solucionar este problema debemos crear un campo updated en
nuestro modelo Thread. Este detectará cuando se modificó por última vez
y nos permitirá añadir un ordenamiento automático en la pertinente clase
Meta.

![]({{cdn}}/django/images/image270.png)\
![]({{cdn}}/django/images/image290.png)

Sin embargo cuando añadimos modificamos un campo many2many updated no se
actualiza, y aquí el mayor truco de este ejercicio, simular un guardado
para actualizar el campo updated. ¿Dónde? ¡Pues en la señal que valida
los mensajes!

![]({{cdn}}/django/images/image661.png)

Habiendo hecho esto, migramos:

![]({{cdn}}/django/images/image885.png)\
![]({{cdn}}/django/images/image25.png)

Y a partir de este momento, cuando se añada un mensaje a un Hilo, este
aparecerá arriba del todo al recargar la página.

![]({{cdn}}/django/images/image823.png)

Como siempre Django haciendo fácil lo más difícil.

Con esto estimados alumnos, acabamos el proyecto, espero que hayáis
aprendido muchísimo y podáis aplicar muchas de las funcionalidades
vistas en vuestros futuros proyectos.

___
<small class="edited"><i>Última edición: 25 de Marzo de 2021</i></small>