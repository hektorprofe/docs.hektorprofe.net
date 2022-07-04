title: Comprensión del distribuible con 7-Zip | Curso Qt/PySide | Hektor Profe

# Comprensión del distribuible con 7-Zip

Los ejecutables son bastante pesados porque incluyen el intérprete de `Python` y todas las dependencias de `Qt`.

El directorio de un programa básico ocupa unos 80MB, pero tranquilos, podemos reducir mucho el tamaño a la hora de compartir nuestro programa utilizando un compresor como [7-Zip](https://www.7-zip.org/) y el formato `7z`.

Este compresor es software libre y por lo tanto gratuito, a diferencia de Winzip o Winrar así que os lo recomiendo encarecidamente. Además el formato `7z` es de los que comprimen mejor, si establecemos el nivel de comprensión de la carpeta en `Ultra` podemos reducir el tamaño del distribuible hasta cuatro veces.

<img src="{{cdn}}/pyside/10-docs/02.png">

Otros modos de compresión como el clásico `zip` o `tar.gz` no reducen tanto el tamaño:

<img src="{{cdn}}/pyside/10-docs/03.png">


___
<small class="edited"><i>Última edición: 22 de Marzo de 2021</i></small>