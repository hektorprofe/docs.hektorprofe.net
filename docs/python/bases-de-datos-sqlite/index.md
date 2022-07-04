title: Bases de datos SQLite | Curso de Python | Hektor Profe
description: ¿Qué es una base de datos? También conocidas como bancos de datos son simplemente conjuntos de datos que hacen referencia a información perteneciente a un mismo contexto.

# Bases de datos SQLite

¿Qué es una base de datos? También conocidas como bancos de datos son simplemente conjuntos de información. Ya conocéis algunos tipos de datos, como los números, las cadenas de caracteres, las fechas, etc. 

<div class='embed-container'><iframe src='https://player.vimeo.com/video/293596147' frameborder='0' webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe></div>

A lo largo de esta unidad vamos a aprender con ejemplos a utilizar una bases de datos  conjunto al lenguaje Python. Sin embargo, suponiendo que muchos de vosotros no habéis utilizado nunca una base de datos, hay una serie de conceptos básicos que tenéis que conocer antes de empezar, así que he decidido dedicar esta presentación previa a explicarlos 

## Bases de datos

¿Qué es una base de datos? También conocidas como bancos de datos, son simplemente conjuntos de datos . Ya conocéis algunos tipos de datos, como los números, las cadenas de caracteres, las fechas, etc.

Bueno, pues estos conjuntos de datos hacen referencia a información perteneciente a un mismo contexto. Es decir, si hablamos de los clientes de una empresa, éstos datos comunes de todos los clientes podrían ser sus nombres, apellidos, direcciones, teléfonos… O los productos de una tienda, cada uno con su nombre, precio, descripción, etc.

Por tanto, al ser datos del mismo contexto, las bases de datos permiten almacenarlos sistemáticamente, de forma automatizada, con la finalidad de un posterior uso. Ya sea para realizar consultas, comparativas, análisis, modificaciones o simplemente borrarlos.

Como son programas complejos centrados en la gestión de información, reciben el nombre de **SGBD**: Sistemas Gestores de Bases de Datos. 

La peculiaridad de los **SGBD** es que implementan sus propios lenguajes internos de programación par realizar las consultas, que pueden ser tan simples como consultar el nombre de todos los clientes de la empresa, o tan complejas como conseguir información de los pedidos de una tienda, a la vez que se consultan los clientes y en un conjunto de fechas determinado.

## Modelos

De todas formas, los tipos de datos y la forma de almacenarlos pueden diferir mucho dependiendo exactamente del contexto, y es por eso que con el tiempo se han ido desarrollando una serie de modelos distintos para gestionar las bases de datos.

* **Jerárquicas**: Utilizan un modelo los datos que se organiza en forma de árbol invertido, en donde un nodo padre de información puede tener varios hijos...
* **De red**: Una mejora del modelo jerárquico que permite a un hijo tener varios padres...
* **Transaccionales**: Cuyo único fin es el envío y recepción de datos a grandes velocidades, estas bases son muy poco comunes
* **Relacionales**: Éste es el modelo utilizado en la actualidad para representar problemas reales y administrar datos dinámicamente. Es en el que nos vamos a centrar, pero hay otros...
* **Documentales**: Permiten guardar texto completo, y en líneas generales realizar búsquedas más potentes. Sirven para almacenar grandes volúmenes de información de antecedentes históricos. Junto a las relacionales son de las más utilizadas en el desarrollo web.
* **Orientadas a objetos**: Este modelo es bastante reciente y propio de los modelos informáticos orientados a objetos, donde se trata de almacenar en la base de datos los objetos completos. Es posible que tome más importancia en el futuro.
* **Deductivas**: Son bases de datos que permiten hacer deducciones. Se basan principalmente en reglas y hechos que son almacenados en la base de datos, por lo que son algo complejas.

## Modelo Relacional

Las bases de datos Relacionales son muy utilizadas actualmente gracias a que es fácil representar y gestionar problemas del mundo real.

Se basan en la idea de crear relaciones entre conjuntos de datos, en los que cada relación es también una tabla. Cada tabla consta de registros, formados por filas y columnas, también conocidos como tuplas y campos.

Evidentemente dentro de las bases de datos relacionales, existen muchos **SGBD**. La mayoría también son compatibles con Python. Algunos son de pago, otros gratuitos, los hay sencillos y otros muy avanzados. Hagamos un repaso:

* **SQL Server**: Es un sistema de manejo de bases de datos del modelo relacional, desarrollado por la empresa Microsoft y únicamente disponible para sistemas Windows. Es privativo y competidor directo de Oracle, MySQL y PostgreSQL.
* **Oracle**: Database es un sistema de gestión de base de datos de tipo objeto-relacional privativo, desarrollado por Oracle Corporation, considerado como uno de los sistemas más completos. Su dominio en el mercado de servidores empresariales fue casi total hasta la aparición de la competencia. Es multiplataforma y además las últimas versiones de Oracle han sido certificadas para poder trabajar bajo GNU/Linux.
* **MySQL**: Es un sistema de gestión de bases de datos relacional desarrollado bajo licencia dual GPL/Licencia comercial por Oracle Corporation y está considerada como la base datos open source más popular del mundo, y una de las más populares en general junto a Oracle y Microsoft SQL Server, sobre todo para entornos de desarrollo web.
* **PostgreSQL**: Es un Sistema de gestión de bases de datos relacional orientado a objetos y libre. Como muchos otros proyectos de código abierto, el desarrollo de PostgreSQL no es manejado por una empresa o persona, sino que es dirigido por una comunidad de desarrolladores que trabajan de forma desinteresada, altruista, libre o apoyados por organizaciones comerciales.
* **SQLite**: Es un sistema de gestión de bases de datos relacional contenido en una pequeña biblioteca escrita en C. Es un proyecto de dominio público y a diferencia de los otros sistemas que utilizan la arquitectura cliente-servidor, su motor no es un proceso independiente sino que se enlaza con el programa pasando a ser parte integral del mismo. Sin embargo no os dejéis engañar, porque aunque parezca la solución sencilla, SQLite en su tercera versión permite bases de datos de hasta 2 Terabytes de tamaño y muchas otras funcionalidades. En definitiva su configuración es muy sencilla, tan sencilla que no existe, por lo que no dará problemas y es la mejor solución para este curso.

Así que como véis encontramos multitud de **SGBD** Relacionales. En Python, cada uno de ellos cuenta módulos libres y programas conectores para comunicar las bases de datos y el lenguaje de programación. Sin embargo, pese a que son sistemas distintos, el lenguaje de las consultas no varía mucho, sino sería muy difícil pasar de un sistema a otro y los **SGBD** no podrían competir entre ellos. 

Lo que nos lleva a nuestra última cuestión, ¿qué tienen en común? ¿Qué son esas siglas SQL en sus nombres?

## El lenguaje SQL

A parte de los lenguajes de programación como Python, centrados en la creación de los programas, los **SGBD** implementan su propia sintaxis o lenguaje propio para realizar consultas y modificaciones en sus registros.

El lenguaje más utilizado en las bases de datos relacionales el lenguaje SQL (Lenguaje de Consulta Estructurada), y es necesario aprenderlo si queremos utilizar este tipo de bases de datos en nuestros programas.

Evidentemente este lenguaje abarca muchísimo, por lo que en esta unidad sólo veremos algunas consultas básicas para utilizar en conjunto con SQLite en nuestros scripts de Python.

___
<small class="edited"><i>Última edición: 5 de Octubre de 2018</i></small>