title: Manejo de ficheros | Curso de Python | Hektor Profe
description: Tradicionalmente existen dos tipos de persistencia básica: con ficheros o con bases de datos y en esta unidad vamos a centrarnos en la primera.

# Manejo de ficheros

Tradicionalmente existen dos tipos de persistencia básica: con ficheros o con bases de datos. En esta sección vamos a centrarnos en la primera.

<div class='embed-container'><iframe src='https://player.vimeo.com/video/292161550' frameborder='0' webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe></div>

Antes de comenzar con los ficheros necesitamos contar con unos conocimientos básicos. Debéis tener en cuenta que escribir en el disco duro puede resultar peligroso si se hace mal, así que aseguraros de entender todo bien.

## ¿Qué es un fichero?

Primeramente, ¿qué es un fichero? Un fichero es un conjunto de bits almacenados en un dispositivo de memoria persistente, normalmente un disco duro. Este conjunto de información se identifica con un nombre  (el nombre del fichero) y la dirección de la carpeta o directorio que lo contiene. Todos, absolutamente todos los ficheros se localizan en un directorio determinado que se conoce como la ruta del fichero.

Por cierto, los ficheros se conocen también como archivos informáticos porque son equivalentes digitales de los archivos escritos por ejemplo en expedientes, tarjetas o libretas que encontraríamos en una oficina tradicional.

Otra cosa importante es que los ficheros se suelen identificar también con una extensión. Una extensión es un código que se escribe después del nombre, con un punto y varios caracteres y que nos permite identificar varios ficheros de un mismo tipo. En realidad ésto no deja de ser una formalidad, ya que a nuestros programas no les importa la extensión, sino cómo deben interpretar los datos que hay escritos dentro. 

## Operaciones básicas

Segundo, las cuatro operaciones que nos permiten los ficheros son:

* **Creación**: Proceso por el cual creamos un fichero en el disco.
* **Apertura**: Proceso por el cual abrimos un fichero del disco para comenzar a trabajar.
* **Cierre**: Proceso por el cual cerramos un fichero para dejar de trabajar con él.
* **Extensión**: Proceso por el cual añadimos información al fichero.

Es posible realizar varias operaciones a la vez, como creación y apertura en la misma instrucción. Sin embargo es necesario abrir un fichero para poder extenderlo o cerrarlo.

## Puntero del fichero

Tercero, el puntero es un concepto por el cual podemos entender como el ordenador accede y escribe en el fichero correctamente. Imaginaros el puntero como si fuera el dedo del ordenador mientras recorre el fichero, igual que nosotros seguimos con el dedo un texto mientras lo leemos y así sabemos por dónde vamos. 

El puntero es muy importante, ya que por ejemplo, si se encuentra al principio del fichero y le decimos que guarde datos ahí, si no hay nada perfecto, pero si ya hay datos ¿que ocurrirá? Que los guardaremos encima de otros datos y quizá haremos que el fichero quede inservible. Entonces, ¿si queremos añadir datos al fichero, dónde debería estar el puntero? Pues al final del todo, justo donde no hay nada más.

## Ficheros de texto y binarios

Ésta es la última diferencia que debemos entender. Si probáis a crear un fichero con un editor de texto, luego lo podemos abrir cómodamente para seguir trabajando, como cuando creamos un script de Python. Ésto es porque los editores guardan la información en ficheros de texto plano, tal como nosotros lo escribimos.

Pero ¿qué ocurre si intentamos abrir una imagen o sonido con el editor? Pues que aparecen muchos códigos extraños. 

La causa es que estos ficheros no almacenan texto plano, sino datos binarios.
Los datos binarios son la forma básica de datos que un ordenador maneja, y por tanto también la forma más rápida de escribir y leer información de un fichero. Por éso sirven para guardar de todo, desde imágenes, sonidos, ficheros que a su vez han sido comprimidos, texto enriquecido (como el de un documento de word) o incluso el ejecutable de un programa. Lo malo es que para nosotros son más difíciles de manejar que los ficheros porque requieren conocimientos informáticos sobre el funcionamiento de los bits, bytes y las conversiones entre tipos, así que no los veremos. 

En su lugar echaremos un vistazo al módulo pickle y cómo nos puede ayudar a gestionar colecciones.

___
<small class="edited"><i>Última edición: 3 de Octubre de 2018</i></small>