title: Introducción | Python | Academia | Hektor Profe
description: Aprende lo más básico para empezar con el lenguaje de moda en ciencia de datos, desarrollo web, hacking...

# Introducción a Python

<div class="contenedor_youtube">
  <iframe id="odysee-iframe" width="560" height="315" src="https://odysee.com/$/embed/-Curso--Python-para-principiantes/39606867b1618070fb050b2680b055eac089d396?r=3icueB68NV3UEFHyqs2QRfzRUeABmHDU" allowfullscreen></iframe>
</div>

Si te interesa aprender este lenguaje pero no sabes muy bien por dónde empezar, en este pequeño curso comparto contigo los primeros pasos que debes seguir para configurar tu entorno de desarrollo, crear tus primeros scripts y los tipos de datos básicos del lenguaje.

Independientemente del uso que quieras darle al lenguaje estos son los fundamentos que deben quedarte claros desde el principio, ya que estarás utilizándolos durante todo el tiempo.

Además haremos un breve repaso del uso que se le da profesionalmente para que no te quede ninguna duda antes de lanzarte a la piscina.

## ¿Qué es Python?

Sin entrar en demasiados detalles, Python es el lenguaje de programación que ha sufrido el mayor crecimiento durante los últimos años, en gran parte gracias a su filosofía de la simplicidad y la rápida curva de aprendizaje que ofrece. 

### ¿Quién lo utiliza?

* Ingenieros de software
* Matemáticos
* Analistas de datos
* Científicos
* Contables
* Ingenieros de red
* Incluso niños (es el más popular para empezar a programar)

### ¿Por qué es tan especial?

* Permite resolver problemas en menos tiempo y con menos código. Esta es precisamente una de las razones por las que empresas como Google, Spotify, Dropbox o Facebook lo utilizan. Un ejemplo para ilustrar su poder es, cómo haríamos en diferentes lenguajes para extraer la palabra “Hola” de una cadena de texto “Hola mundo”:
    * **C#**: str.Substring(0,4)
    * **JavaScript**: str.substr(0,4)
    * **Python**: str[0:4]
* Es un lenguaje multipropósito utilizado para resolver todo tipo de tareas:
    * Análisis de datos
    * Inteligencia artificial y aprendizaje automático
    * Desarrollo de aplicaciones web, móvil y de escritorio
    * Scripts de automatización
    * Pruebas de código
    * Hacking
* Es de alto nivel, de manera que no tienes que preocuparte de tareas complejas como el manejo de memoria.
* Es multiplataforma, por lo que se puede ejecutar tanto en Windows, MAC y Linux.
* Tiene una gran comunidad, literalmente puedes encontrar la solución a casi cualquier duda sólo buscando preguntas ya respondidas en Stack Overflow o mirando repositorios públicos de Github.
* Su ecosistema es enorme, abarcando todo tipo de librerías, frameworks y herramientas. Algo debido en gran parte a que es un lenguaje bastante maduro con más de 20 años de edad.

### ¿Qué versiones encontramos?

* **Python 2**: la versión antigua y que tendrá soporte oficial hasta 2020.
* **Python 3**: la versión actual en constante mejora y que se tratará en el curso.

## Instalación

Existen varias formas de instalar Python 3 y de hecho los usuarios de Linux y MAC ya lo tenéis instalado por defecto así que no tenéis que hacer nada. Si estáis en Windows os recomiendo descargar la versión que encontraréis en [la web oficial](https://www.python.org/downloads/). Seguís los pasos añadiendo Python al PATH en la primera ventana del instalador y listo. Eso sí, desinstalad cualquier otra versión que tengáis porque si os detecta que tenéis más de una a la vez no os va a funcionar.

Una vez lo tengáis podéis abrir una terminal en Windows y escribir:

```bash
python
```

Lo mismo podéis hacer en Linux y MAC, sólo que para usar la versión 3 en lugar de la 2, deberéis especificar:

```bash
python3
```

Esto nos entrará al intérprete de Python, una terminal interactiva útil para experimentar. Por ejemplo podemos escribir una suma o cualquier expresión válida en Python, es parecida a la consola interactiva de JavaScript que tenemos en el navegador:

```bash
print("Hola mundo")
```

```bash
2 + 2
```

Sin embargo nosotros vamos a estar aprendiendo en un entorno más cómodo, así que vamos a salir del intérprete llamando a la función:

```bash
exit()
```

## Configurando el entorno

Para crear programas en Python tenemos dos tipos de herramienta:

* Editores de código
* Entornos integrales de desarrollo (IDE)

Por regla general los IDEs tienen más funcionalidades, como autocompletado, depuración, pruebas... pero la línea que los separa se ha ido estrechando con los nuevos editores que permiten instalar extensiones creadas por la comunidad, haciéndolos mucho más poderosos y transformándolos prácticamente en pseudo-IDEs.

Los editores más famosos actualmente son:

* Visual Studio Code
* SublimeText
* Atom

Y los IDE que se suelen utilizar para Python:

* PyCharm
* Eclipse con PyDev

Como ya comento en el curso de JavaScript para principìantes, mi editor de cabecera actualmente es Visual Studio Code. Tiene algunas extensiones muy útiles para Python y además es gratuito, así que utilizaré ese en el curso. Podéis descargarlo desde [su web oficial](https://code.visualstudio.com/).

Una vez lo tengáis instalado necesitaréis añadir la extensión Python que aparece en la portada del propio editor, eso añadirá el soporte y varias funcionalidades.

Si VSCode no os sale automáticamente en español, buscad una extensión llamada **Spanish Language Pack** y la instaláis, al reiniciar deberíais tenerlo listo.

## Primer programa

Ahora con VScode abierto, vamos a ir Fichero > Abrir carpeta y crearemos una  para ir trabajando dentro, podéis llamarla **curso-python** o lo que gustéis, luego la abrís.

Veréis que os aparece un navegador de ficheros a la izquierda con el directorio,  ahí podemos añadir un nuevo fichero llamado por ejemplo **hola.py**.

Nuestro primero programa simplemente nos saludará por pantalla con el típico mensaje "Hola mundo", eso en Python como ya vimos se hace así:

```python
print("Hola mundo")
```

Pero vamos a dejarlo más bonito subrayando esta frase, para hacerlo poned lo siguiente justo debajo:

```python
print("Hola mundo")
print("=" * 10)
```

Ahora guardad el fichero, al hacerlo quizá os aparecen unos mensajes de aviso en VSCode, instalad las dos extensiones, tanto **pylint** como **autopep8**, luego hablaremos de ellas y para qué sirven.

Desplegad la terminal (Terminal -> Nueva terminal) y escribid el comando para ejecutar este script:

```bash
python hola.py
```

Sacad vuestras propias conclusiones.

## Ejecución rápida

Antes de meternos de lleno con la sintaxis del lenguaje, debería mostraros como configurar Python correctamente en VSCode para ejecutar cómodamente nuestros programas pulsando una combinación de teclas.

Lo primero es tener en cuenta que cuando tenemos un directorio con al menos un fichero python, VSCode añade una configuración de ejecución específica. En nuestro caso aparece en la parte inferior izquierda la versión de Python que estamos utilizando para ejecutar el script.

Si estáis en Windows seguramente ya tendréis Python 3 por defecto, pero los usuarios de MAC y Linux posiblemente no, así que os explicaré como cambiar la configuración.

Para ejecutar el código vamos a instalar una extensión llamada “Code runner”, cuando la tengáis los usuarios de MAC y Linux tendréis que configurarla para usar **python3**:

* Archivo > Preferencias > Configuración
* Buscad **code-runner.executorMap** y haced clic en **Editar en settings.json**.
* Justo después de la última configuración escribid **code-runner** y buscad la opción **executorMap** para autocompletarla. Se os añadirán muchas líneas, buscad la que pone "python -u" y cambiad el valor por "python3" para que utilice esa versión.
* También os recomiendo, sobretodo si tenéis Windows, añadir en la configuración de **code-runner** la opción **runInTerminal** en true para mostrar el resultado de la ejecución en la terminal y no en la pestaña por defecto, ya que puede dar problemas con la codificación de caracteres.

Una vez guardada la configuración cread un script llamado **version.py** con el siguiente contenido:

```python
import sys
print(sys.version)
```

Podréis ejecutarlo automáticamente con la combinación **Control+Alt+N** (en Mac la tecla Alt creo que equivale a la de Opción), veréis que os aparece el resultado en la terminal si configurásteis la opción **runInTerminal** de **code-runner** en `True`.

## Linting y formateo

¿Recordáis aquellas dos extensiones que hemos instalado? Vamos a ver qué hacen.

Por su parte **pylint** añade soporte de linting para los ficheros Python. El *linting*, desconozco si hay una palabra en español para referirse a ello, es un depurador de sintaxis y otros fallos menores, nos mostrará errores mientras escribimos el código.

Por ejemplo, si nos descuidamos de cerrar un paréntesis:

```python
print("Hola mundo"
```

Por otro lado, **autopep8** es una extensión que formatea el código para añadir las buenas prácticas descritas en la [guía de estilos PEP-8](https://www.python.org/dev/peps/pep-0008/), que describe las convenciones que siguen los propios desarrolladores del lenguaje para escribir el código de forma ordenada y legible.

Os sugiero hacer lo siguiente para que VSCode formatee automáticamente el código al guardar el fichero:

* Archivo > Preferencias > Configuración
* Buscad **formatOnSave** y activad la casilla si no lo está.

Al guardar un script veréis que se añade una línea al final, eso es una de las convenciones, así que podéis dar hecho que ya os funciona.

## Variables

Programar sirve esencialmente para manipular datos o información, y para hacerlo necesitamos almacenarlos.

Las variables hacen referencia al hecho de dar un nombre a un espacio en la memoria donde almacenaremos los datos temporalmente. La clave está en que mientras tengamos el nombre de la variable siempre podremos acceder a la información que contiene.

Definir una variable en Python es extremadamente sencillo, cread un fichero **variables.py**:

```python
nombre = 'Héctor'
print(nombre)
```

Lo que tenemos aquí es una variable de tipo cadena, un tipo de dato usado para almacenar texto. Pueden declararse de varias formas, normalmente limitando el texto entre comillas simples o dobles.

Así que hemos declarado una variable llamada nombre que contiene información de tipo texto.

Igual que en JavaScript y otros lenguajes, no se debe establecer cualquier nombre para una variable, hay que seguir las reglas y a poder ser también las buenas prácticas:

* No usar de nombre una palabra reservada. Éstas forman parte de la sintaxis del lenguaje. El propio editor os indicará un fallo si da la casualidad que habéis puesto un nombre reservado.
* No pueden comenzar con un número.
* No pueden contener espacios ni guiones, aunque sí barras bajas. De hecho por convención es recomendable usar la notación snake case que utiliza barras bajas para separar palabras y todo en minúscula:

```python
primer_apellido = 'Costa'
segundo_apellido = 'Guzmán'
```

* Deberían tener nombres descriptivos que den información contextual. Por ejemplo, nombres como a, b, x… no nos dan ninguna información y eso puede llevarnos a confusiones.
* Son case sensitive, es decir, las mayúsculas y minúsculas afectan directamente a la singularidad de las variables. Por ejemplo, no es lo mismo **apellido** que **Apellido**, son dos variables diferentes.

Otra cosa que se puede hacer en Python es utilizar la declaración múltiple, y la notación es bastante curiosa:

```python
nombre, apellido = 'Héctor', 'Costa'
print(nombre, apellido)
```

Y por último un truco, si quisíeramos varias variables con el mismo valor, podemos asignarlas así:

```python
x = y = z = 1
print(x, y, z)
```

Por cierto fijaros que hemos usado un número, otro tipo de dato diferente a las cadenas de texto. 

En la siguiente lección hablaremos de los tipos de datos primitivos.

## Tipos primitivos

¿Qué tipos de valores podemos asignar a una variable en Python? Igual que en JavaScript se organizan en dos tipos:

* Los tipos por valor o primitivos
* Los tipos estructurados o no primitivos

Veamos los primeros, de los otros hay muchos y veremos un par luego.

En la categoría de los tipos primitivos encontramos esencialmente estos:

* Integer (número entero)
* Long (número entero muy grande)
* Float (número decimal)
* String (cadena)
* Boolean (booleano)
* None (nulo)

Como siempre, las cadenas y los números tienen un sentido implícito porque sirven para almacenar información de ese tipo:

```python
nombre = 'Héctor'  # literal cadena
edad = 29          # literal entero
pi = 3.1416        # literal decimal
```

Luego el tipo booleano o lógico podemos entenderlo como el sentido afirmativo o negativo de una sentencia. Únicamente puede tener dos valores **True** o **False** (verdadero o falso), que por cierto son palabras reservadas y a diferencia de JavaScript tienen la primera letra en mayúscula:

```python
llevoGafas = True  # literal booleano
```

Por último el tipo **None** se utiliza para establecer un valor vacío o nulo en una variable, también es una palabra reservada con la primera letra en mayúscula:

```python
nombre = None
print(type(nombre))
```

## Tipado dinámico

Python, al igual que JavaScript, es un lenguaje de tipado dinámico. Hay dos formas de tipado:

* Estático
* Dinámico

En los lenguajes estáticos, cuando declaramos una variable es necesario especificar el tipo que tiene y ese tipo es inalterable:

```javascript
String nombre = 'Héctor'; // java
```

En cambio en lenguajes como Python no es necesario establecer un tipo y además puede cambiar en cualquier momento, eso es porque viene determinado en tiempo de ejecución por el valor asignado a la variable:

```python
nombre = 'Héctor' # python
```

Pasando la variable o literal a la función **type()** de Python podremos consultar el tipo de una variable, eso sí, tendremos que pasarlo a un print() porque sino no veremos el resultado:

```python
nombre = 'Héctor'
print(type(nombre))
```

Inicialmente la variable es de tipo string, pero si le asignamos un número cambiará automáticamente:

```python
nombre = 10
print(type(nombre))
```

## Listas

Veamos ahora un tipo de dato no primitivo como es la estructura lista.

Como su nombre indica, una lista sirve para almacenar varios valores, y en Python esos valores pueden ser de cualquier tipo, eso es posible gracias al tipado dinámico.

Vamos a hacer unas pruebas en un fichero **listas.py**:

```python
letras = ["a", "b", "c"]
print(letras)
```

Como véis una lista se declara entre corchetes y sus elementos hay que separarlos usando comas.

Para acceder a los elementos de una lista podemos usar los índices. El índice es el número de la posición que queremos consultar, simplemente tenemos que hacer referencia a esa posición entre corchetes:

```python
letras = ["a", "b", "c"]
print(letras[0])  # Primera letra	
print(letras[1])  # Segunda letra
```

Un truco para mostrar una posición en concreto es simplemente restar uno a la posición que queremos mostrar. 

Por ejemplo, para mostrar el tercer elemento con la "c", haríamos 3 - 1 = 2:

```python
print(letras[2])  # Tercera letra	
```

También podemos hacer uso del índice -1 para devolver el último elemento de la lista:

```python
print(letras[-1])  # Última letra
```

## Listas anidadas

Algo interesante que vale la pena comentar es la posibilidad de poner listas dentro de listas, sublistas que se dicen. Esto genera estructuras multidimensionales conocidas como matrices.

Por ejemplo, una tabla con filas y columnas se podría representar así:

```python
personas = [
  ["Héctor", "Costa", "30"],
  ["Juan", "García", "35"],		
  ["Diego", "Pérez", "27"],
]
```

Para acceder a los elementos anidados de las filas y columnas usaríamos dos índices en lugar de uno, el primero haciendo referencia a la fila y el segundo a la columna. 

Aplicando esa lógica, si queremos saber la edad de Diego, sabiendo que se encuentra en la última columna de la última fila, podríamos hacer:

```python
print(personas[-1][-1])  # Edad de Diego
```

O el apellido de Juan, estando éste en la segunda fila y segunda columna:

```python
print(personas[1][1])  # Apellido de Juan
```

Para acabar este mini repaso, en Python es posible usar la función **len()** para saber la longitud de una lista, algo que nos devolverá ni más ni menos que un entero con el número de elementos que la forman:

```python
print(len(personas))
```

Como veis, aún siendo una lista multidimensional, nos dice que su longitud es 3, pues está formada por tres sublistas.

## Diccionarios

El segundo y último tipo no primitivo que os quiero comentar en este pequeño curso son los diccionarios, pues son junto con las listas los que más suelo utilizar.

Estas estructuras también permiten almacenar varios elementos, pero con la peculiaridad de que en lugar de estar referenciados a partir de la posición, lo están a partir de una clave, de ahí que se conozcan también como estructuras en clave-valor.

Para verlos en acción siempre suelo enseñar el ejemplo más fácil, un diccionario para traducir colores del español al inglés:

```python
colores = {
  "rojo": "red",
  "azul": "blue",
  "negro": "black"
}
print(colores)
```

El diccionario se declara entre llaves y contiene elementos con la sintaxis **clave:valor** separados por comas. La clave puede ser un número o una cadena de texto, sin embargo la peculiaridad es que no puede haber dos claves iguales, algo que de hecho es bastante lógico.

Sea como sea, para consultar la traducción de un color bastaría con hacer referencia a la clave entre corchetes:

```python
print(colores["negro"])
```

Lo bueno que tienen es que podemos añadir claves y valores muy fácilmente:

```python
colores["gris"] = "gray"
print(colores["gris"])
```

Evidentemente podríamos cambiar un valor ya existente haciendo referencia al mismo, como si fuera una variable cualquiera:

```python
colores["gris"] = "white"
print(colores["gris"])
```

Por último comentar que también se puede usar la función **len()** para saber el número de elementos que contienen:

```python
print(len(colores))
```

## Funciones

Lo último que vamos a ver son las funciones, bloques de código reutilizable que forman parte de casi todos los lenguajes de programación actuales.

Son esencialmente una serie de instrucciones identificadas con un nombre que sirven para realizar una determinada tarea o cálculo sobre unos valores.

Vamos a crear una para estudiar su funcionamiento:

```python
def saludar():
  print('Hola mundo')
```

Todo el contenido del bloque a partir del punto y con un nivel de tabulación formará parte de la función.

Una vez la tenemos definida podemos ejecutarla haciendo referencia a su nombre:

```python
saludar()
```

Los paréntesis es lo que indica que queremos ejecutar la función, sino los ponemos simplemente haríamos referencia a ella. 

Podemos ejecutarla tantas veces como queramos:

```python
saludar()
saludar()
saludar()
```

Por ahora nuestra función no es muy útil, sólo imprime un mensaje, vamos a transformarla en algo más interesante.

Las funciones pueden recibir datos que pueden manipularse dentro para realizar diferentes tareas. Es precisamente el hecho de que una función puede recibir datos lo que las hace tan versátiles y uno de los conceptos claves de la programación.

Por ejemplo podríamos recibir un nombre y saludarlo. Para hacerlo es muy sencillo, sólo tenemos que definir un parámetro de la siguiente forma:

```python
def saludar(nombre):
  print('Hola mundo')
```

El parámetro nombre se comportará como una variable que únicamente existirá dentro de la función, así que podemos hacer uso de ella:

```python
def saludar(nombre):
  print('Hola', nombre)
```

Para enviar el nombre, deberemos pasar el valor durante la llamada de la función como si fuera una variable o literal:

```python
saludar('Héctor')
```

Con este cambio hemos transformado la función en algo dinámico que tiene comportamientos distintos dependiendo del nombre que le pasemos:

```python
saludar('Daniel')
saludar('Javier')
```

En este punto es importante hacer una aclaración. Los valores que enviamos a una función se llaman argumentos, pero durante la definición nos referimos a ellos como parámetros.

¿Pero y si quisiéramos enviar un segundo argumento con el apellido? Pues deberíamos añadir un segundo parámetro en la definición:

```python
def saludar(nombre, apellido):
  print('Hola', nombre, apellido) 
```

Y al ejecutarlo enviar ese segundo argumento:

```python
saludar('Héctor', 'Costa')
```

Ahora bien, a diferencia de JavaScript, si intentamos llamar a la función y no pasamos uno de los parámetros, en Python dará error:

```python
saludar('Héctor')
```

Para solucionarlo podemos indicar valores por defecto a los parámetros de la siguiente forma:

```python
def saludar(nombre=None, apellido=None):
  print('Hola', nombre, apellido) 
```

De esa forma sí podríamos llamarla sin enviar uno de los parámetros y simplemente se mostraría **None** en su lugar.

## Funciones con retorno

Como os expliqué, las funciones pueden recibir argumentos y manejar sus valores como parámetros:

```python
def doblar(numero):
  print(numero*2)

doblar(5)
```

El problema es que sólo existen dentro de su propio bloque, por lo que no podemos acceder a esa información desde el exterior:

```python
print(numero)
```

Si en lugar de mostrar el doble del número quisiéramos devolver ese valor al exterior para seguir trabajando con él, entonces necesitaremos usar el retorno de valores:

```python
def doblar(numero):
  return numero*2

doblar(5)
```

En este momento veremos que no se muestra nada, tendríamos que ponerlo en un **print()**:

```python
print(doblar(5))
```

Sin embargo la utilidad más común es almacenar el valor en una variable para poder seguir trabajando con ella:

```python
numero = doblar(5)

print(numero)
```

De esta forma habremos devuelto un cálculo interno de la función al exterior.

Por cierto, imaginaros que queremos el doble del doble del doble de un número. ¿Cómo podríamos hacerlo? Pues fácil, llamando de forma anidada la función 3 veces:

```python
numero = doblar(doblar(doblar(5)))  # 5 -> 10 -> 20 -> 40

print(numero)
```

Este es el mismo ejemplo que he puesto en el curso de JavaScript y es sólo para liaros un poco, así que no pasa nada si no acabáis de entenderlo 

Sea como sea recordad que las funciones son un conjunto de instrucciones reutilizables identificadas con un nombre, que tienen como objetivo realizar una tarea o un cálculo y que pueden comunicarse con el exterior recibiendo y retornando datos.

___
<small class="edited"><i>Última edición: 16 de Marzo de 2021</i></small>