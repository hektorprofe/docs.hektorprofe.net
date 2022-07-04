title: Módulos estándar | Curso de Python | Hektor Profe
description: Los módulos son ficheros que contienen definiciones que se pueden importar en otros scripts para reutilizar sus funcionalidades.

# Módulos estándar

A continuación os resumo los que son para mí algunos de los módulos esenciales de Python, luego profundizaremos en algunos de ellos:

* <u>_**copy**_</u>: Ya conocemos el módulo copy, lo hemos utilizado para crear copias de variables referenciadas en memoria, como colecciones y objetos.
* <u>_**collections**_</u>: También hicimos una pequeña visita al módulo de colecciones cuando vimos las colas, una mejora de las listas que añadía funcionalidades específicas de estas estructuras. Este es uno de los cuatro módulos que veremos más a fondo en esta unidad.
* <u>_**datetime**_</u>: Hemos hablado largo y tendido de tipos de datos y colecciones, pero hemos pasado por alto un tipo esencial utilizado para manejar las fechas y las horas. Sin él sería muy difícil manejar el tiempo, así que he considerado que este módulo es otro de los esenciales y también lo trabajaremos en esta unidad.
* <u>_**doctest**_</u> y <u>_**unittest**_</u>: Estos dos módulos son importantísimos a la hora de crear pruebas, o tests. El testing, en inglés, es un aspecto esencial de la programación, y en la comunidad Python se dice que si un código no tiene tests que validen su funcionamiento, entonces no vale la pena ni echarle una ojeada. Los trabajaremos específicamente en una unidad entera.
* **html, xml y json**: También quiero comentar estos tres módulos, que aunque no los vamos a trabajar, permiten manejar cómodamente estructuras de datos html, xml y json. Son muy utilizados en el desarrollo web.
* <u>_**pickle**_</u>: Es un módulo que abarca las funciones necesarias para trabajar con ficheros y objetos. Lo  trabajaremos en la próxima unidad del curso junto al manejo de ficheros de texto.
* <u>_**math**_</u>: Posiblemente uno de los módulos más importantes de cualquier lenguaje, ya que incluye un montón de funciones para trabajar matemáticamente. Lo veremos más a fondo en esta misma unidad.
* <u>_**re**_</u>: Otro módulo de visita obligatoria, aunque más avanzado es el de las expresiones regulares (Regular Expressions). Utilizando una sintaxis especial, sirven para hacer comprobaciones y búsquedas. Son especialmente útiles trabajando con cadenas de caracteres, pero incluye muchos métodos alternativos. Hablaremos de ellas en una unidad sobre funcionalidades avanzadas.
* <u>_**random**_</u>: Este es el cuarto y último módulo que veremos en esta unidad, y sirve para generar contenidos aleatorios, escoger aleatoriamente valores y este tipo de cosas que hacen que un programa tenga comportamientos al azar. Es muy útil en el desarrollo de videojuegos y en la creación de pruebas.
* **socket**: El módulo avanzado socket está enfocado en la comunicación entre distintas máquinas utilizando protocolos. permitiendo crear sistemas cliente-servidor. No lo trabajaremos en este curso pero he considerado interesante comentarlo.
* <u>_**sqlite3**_</u>: Sqlite es un sistema de gestión de bases de datos relacional con la peculiaridad que no requiere un proceso independiente, sino que se gestiona a partir de ficheros que hacen de bases de datos. Python trae un módulo para trabajar con este sistema, y lo trabajaremos específicamente en una unidad posterior.
* **sys**: Nos permite conseguir información del entorno del sistema operativo o manejarlo en algunas ocasiones, se considera un módulo avanzado e incluso puede ser peligroso utilizarlo sin conocimiento. Lo expongo porque hemos utilizado alguna función, pero no hablaremos de él.
* **threading**: Se trata de otro módulo avanzado que sirve para dividir procesos en subprocesos gracias a distintos hilos de ejecución paralelos. La programación de hilos es compleja y he considerado que es demasiado para un curso básico-medio como éste.
* <u>_**tkinter**_</u>: Finalmente, y posiblemente el que me hace más ilusión de todos. Tkinter es el módulo de interfaz gráfica de facto en Python. Le dedicaré una unidad entera bastante extensa en la que aprenderemos a crear formularios con botones, campos de texto y otros componentes.

___
<small class="edited"><i>Última edición: 2 de Octubre de 2018</i></small>