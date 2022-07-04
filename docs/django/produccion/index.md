title: Entornos de producción | Curso de Django | Hektor Profe

# Entornos de producción

Llevo todo el curso repitiendo entornos de producción por aquí, entornos
de producción por allá, así que ha llegado la hora de aprender un poco
más sobre ellos.

Cuando hablamos de entornos normalmente hacemos referencia a un “lugar”
donde se ejecuta el código, aunque quizá sería más acertado entenderlo
como una configuración que envuelve la ejecución del propio software.

Los entornos más comunes son el de desarrollo y el de producción, aunque
también existen otros como los de pruebas.

A grandes rasgos, el entorno de desarrollo es donde los programadores
crean las aplicaciones, y suele contener configuraciones que les ayudan
en el proceso. En Django eso se refleja muy bien, por ejemplo, cuando
tenemos el DEBUG en True, pues cualquier error que surja se nos mostrará
en el frontend para facilitarnos la depuración.

En cambio el entorno de producción es el que está dirigido al usuario
final, el lugar donde correrá el código una vez está funcionando
públicamente. Aquí no tendría mucho sentido activar el DEBUG y de hecho
sería una completa falla de seguridad, pues cualquiera podría provocar
un fallo y analizar el registro para recopilar información privada.

Otro cambio importante podría ser a la hora de servir ficheros
estáticos, pues si bien durante el desarrollo se puede configurar Django
para servirlos y facilitarnos la vida, esta funcionalidad no está
pensada para un entorno de producción con multitud de usuarios. De esa
tarea se encargarían servidores preparados para ello como Nginx o
Apache.

Incluso podríamos hablar de bases de datos, pues JAMÁS deberíamos
trabajar con la misma en ambos entornos, y de hecho sería uno de los
errores más desafortunadas que podéis cometer como desarrolladores de
software. Sólo imaginaros que haciendo pruebas borrais un montón de
registros… pues como no tengáis una copia de seguridad os puede caer una
buena demanda por parte del cliente eh.

Por tanto queda claro que no se puede utilizar la misma configuración
mientras desarrollamos nuestra aplicación que cuando la tenemos colgada
en Internet, y se requieren realizar una serie de cambios para que todo
funcione.

Bueno, pues este proceso de adaptar el código de un entorno a otro se
conoce como la fase de despliegue, y contiene la instalación,
configuración y unas pruebas básicas de funcionamiento.

En definitiva “Desplegar Django” es el nombre que recibe el proceso de
copiar y adaptar el proyecto desde un entorno de desarrollo a un entorno
de producción. Sin embargo como copiar los datos literalmente de un
sitio a otro sería muy tedioso y poco seguro, existen los repositorios,
hablaremos de ellos en la siguiente lección.

Por ahora, os dejo un enlace con la lista de cosas que desde la
documentación oficial Django nos recomiendan modificar de cara a un buen
despliegue:
[https://docs.djangoproject.com/en/dev/howto/deployment/checklist/](https://docs.djangoproject.com/en/dev/howto/deployment/checklist/)

___
<small class="edited"><i>Última edición: 25 de Marzo de 2021</i></small>