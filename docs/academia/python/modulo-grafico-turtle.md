title: Módulo gráfico Turtle | Python | Academia | Hektor Profe
description: Si quieres adentrarte en el maravilloso mundo del dibujo gráfico y no sabes por dónde empezar, Turtle es el módulo que necesitas.

<style>
.admonition.note > .superfences-tabs > label:hover, .headerlink{ color: #018dc5 !important; }
.admonition.note { box-shadow: none; margin: 0; padding: 0; border-left: 0; border-radius: 0; font-size: 105%; }
.admonition.note label{ font-size: 91%; }
.admonition.note > .admonition-title { display: none; }
.img-content{ text-align:center;margin-top:25px; }
.lazy { max-width: 220px; }
</style>

# Introducción al módulo gráfico Turtle

El módulo de la tortuga es la herramienta educativa perfecta para aprender programación de forma visual dibujando sobre un lienzo. 

Se introdujo en el lenguaje Logo en 1966, sí, hace más de medio siglo, y si bien no es tan visual como programar con Scratch, permite trabajar directamente en un lenguaje como Python que la incorporó hace ya varios años. 

En cierto modo se puede considerar una introducción a la programación de videojuegos, así que si te interesa el tema quédate hasta el final porque podrías aprender algunas cosas muy interesantes.

Repositorio: <a href="https://github.com/hektorprofe/curso-python-turtle" target="_blank">https://github.com/hektorprofe/curso-python-turtle</a>

## Estructura base

Normalmente partiremos de una estructura básica, con la importación de la librería, la creación de un  espacio de dibujo y al final las rutinas de cierre:

```python
import turtle            # Cargamos el módulo de la tortuga

turtle.setup(500,500)    # Configuramos un espacio de dibujo

                         # El código iría aquí

turtle.done()            # Igualmente debemos poner abajo del todo
turtle.bye()             # Un done-bye para cerrar las rutinas
```

Para no tener que utilizar siempre el nombre turtle podemos importar el módulo como t:

```python
import turtle as t       # Si le damos el nombre t será más fácil

t.setup(500,500)

t.done()
t.bye() 
```

Ahora podemos añadir forma y color a la tortuga para que aparezca en nuestro espacio:

```python
t.shape("turtle")        # Le damos la forma de una tortuga 
t.color("green")         # Y un bonito color verde
```

Perfecto.

## Primer dibujo

El lienzo sobre el que trabajará nuestra tortuga es un espacio de 500x500 píxeles. ¿En qué punto se encuentra la tortuga?

```python
print(t.pos())
```

Por defecto se encuentra en el punto o coordenada (0, 0). Este punto se conoce como el origen, y es un concepto clave para aprender a crear videojuegos.
Si el punto de origen está en el centro, ¿qué valdrán las coordenadas de las esquinas de nuestro lienzo? 
Bueno, si tenemos en cuenta que el ancho es 500 píxeles, la mitad es 250. Así que si le decimos a la tortuga que se mueva hacia adelante 250 píxeles, debería posicionarse justo en el margen derecho.
Para decirle que vaya adelante, llamaremos a su método forward:

```python
t.forward(250)
print(t.pos())
```

Como veréis la tortuga recorrerá los 250 píxeles dibujando una bonita línea verde, y nos dirá que se encuentra en el punto (250, 0).

Ahora si le decimos que avance hacia arriba 250 píxeles más deberíamos ser capaces de llegar a la esquina superior derecha del lienzo. Para ello le diremos que gire 90 grados a la izquierda antes de ir adelante de nuevo:

```python
t.forward(250)
t.left(90)
t.forward(250)
print(t.pos())
```

Como véis la tortuga llega a la esquina superior derecha, cuyo punto es (250, 250).

Ahora os planteo el ejercicio de encontrar los puntos de las otras tres esquinas e ir mostrándolos en la terminal con print, pausad el vídeo y cuando las tengáis continuad para ver la solución.

```python
print("Origen", t.pos())
t.forward(250)
t.left(90)
t.forward(250)
print("Esquina superior derecha", t.pos())
t.left(90)
t.forward(500)
print("Esquina superior izquierda", t.pos())
t.left(90)
t.forward(500)
print("Esquina inferior izquierda", t.pos())
t.left(90)
t.forward(500)
print("Esquina inferior derecha", t.pos())
```

<div class="img-content">
    <img class="lazy" data-src="{{cdn}}/turtle/img01.jpg"/>
</div>

## Segundo dibujo

Ya hemos visto cómo ir hacia adelante con forward() y rotar a la izquierda con left(), pues también podemos ir hacia atrás con backward() y rotar a la derecha con right().

Además la tortuga puede o no dejar el rastro subiendo o bajando el lápiz que lleva. Con penup() lo levantamos para no dibujar, y con pendown() lo bajamos para seguir dibujando.

Sabiendo estas nuevas instrucciones os reto a dibujar un rectángulo de 400 píxeles de ancho por 300 de alto centrado en el lienzo de 500x500, es decir, deberéis levantar y bajar el lápiz cuando sea necesario para no mostrar el rastro.

```python
t.penup()
t.forward(200)  # nos posicionamos a la derecha
t.pendown()
t.left(90)
t.forward(150)  # dibujamos la mitad hacia arriba
t.left(90)
t.forward(400)
t.left(90)
t.forward(300)
t.left(90)
t.forward(400)
t.left(90)
t.forward(150)  # última mitad hacia arriba
```

<div class="img-content">
    <img class="lazy" data-src="{{cdn}}/turtle/img02.jpg"/>
</div>

## Tercer dibujo

A partir de ahora el tema se pone interesante de verdad, vamos a incorporar algo de programación estructurada a nuestros dibujos para hacer cosas sorprendentes.

Empecemos por una función.

Crear un cuadrado o un rectángulo es algo bastante común, así que podemos crear una función rectangulo() con las instrucciones básicas a partir de una anchura, una altura y una coordenada para su centro. 

Para redondearlo introduciremos el uso de la acción goto(), que le indica a la tortuga que vaya a una coordenada en específico de forma automática, y la acción seth() que le establece una dirección en grados hacia dónde mirar, siendo 0 a la derecha, 90 arriba, 180 a la izquierda y 270 abajo.

```python
def rectangulo(px, py, ancho, alto):
    
    # Nos posicionamos en la esquina superior derecha
    # del rectángulo que vamos a dibujar sin dejar rastro
    # y miramos hacia la izquierda para empezar siempre igual
    
    t.penup()
    t.goto(px + ancho / 2, py + alto / 2)  
    t.seth(180)
    t.pendown()
    
    # Dibujamos la estructura

    t.forward(ancho)
    t.left(90)
    t.forward(alto)
    t.left(90)
    t.forward(ancho)
    t.left(90)
    t.forward(alto)
    t.left(90)

rectangulo(0, 0, 400, 300)
rectangulo(0, 0, 300, 200)
rectangulo(0, 0, 150, 100)
rectangulo(0, 0, 100, 50)
```

Fácil, rápido y para toda la família.

## Cuarto dibujo

¿Sabéis lo que son los poligonos regulares? Son polígonos cuyos lados y ángulos interiores son iguales entre sí. La magia que tienen es que cuantos más lados tienen más se parecen a un círculo, y de hecho dícese que un círculo perfecto sería un polígono de infinitos lados. De ahí que en geometría se trabaje tanto con límites. 

Bueno, sea como sea creo que es interesante adaptar nuestra función para que no sólo dibuje cuadrados y rectángulos, sino cualquier tipo de polígono regular.

Para ello le pasaremos un parámetro extra con el número de costados que queremos dibujar, y en lugar de un ancho y una altura simplemente utilizaremos un radio. Ese radio nos servirá para crear la circunferencia circunscrita que será la base del polígono regular, que por cierto, podemos crear utilizando la acción circle de la tortuga, que toma precisamente ese radio. Fijaros:

```python
def poligono_regular(px, py, radio, lados):
    t.penup()
    t.goto(px, py - radio)  
    t.pendown()
    t.circle(radio)

poligono_regular(0, 0, 100, 7)
```

<div class="img-content">
    <img class="lazy" data-src="{{cdn}}/turtle/img04.jpg"/>
</div>

Ahora tenemos que calcular los grados que debemos girar y trazar nuestras líneas. En el caso del cuadrado era muy fácil, pues sabemos que hay que girar 90 grados. ¿Pero cómo lo haremos aquí? Bueno, sabemos que 90º es una cuarta parte de 360, así que extrapolando eso podemos calcular el ángulo dividiendo 360 entre el número de lados del polígono regular:
angulo = 360 / lados
print(angulo)

Sabiendo el ángulo, podemos posicionarnos en el centro de nuestro círculo y trazar líneas hacia fuera con la longitud del radio tantas veces como lados tenemos mientras vamos incrementando el ángulo que hemos conseguido. Fijaros:

```python
angulo = 360 / lados
print(angulo)

for i in range(lados):
    t.penup()           # Nos posicionamos al centro
    t.goto(px, py)  
    t.pendown()
    
    t.seth(angulo*i+1)  # Trazamos radios hacia afuera
    t.forward(radio)
    print( t.pos() )
```

<div class="img-content">
    <img class="lazy" data-src="{{cdn}}/turtle/img05.jpg"/>
</div>

Woo! Que bonito quesito nos ha quedado eh? Pero lo más importante es que tenemos todas las coordenadas de los vértices de nuestro polígono:

Podríamos almacenarlas en una lista:
 
```python
vertices = []  # La declaramos

for i in range(lados):
    t.penup()          
    t.goto(px, py)  
    t.pendown()
    
    t.seth(angulo*i+1) 
    t.forward(radio)
    vertices.append(t.pos())  # Los vamos añadiendo
```

Y ahora viene la magia. 
Vamos a hacer que la tortuga trace líneas entre esos vértices yendo de unos a otros utilizando la acción goto:

```python
# Nos posicionamos en la coordenada del último vértice
t.penup()
t.goto(vertices[-1])  
t.pendown()

# Y hacemos que la tortuga se mueva a cada uno de ellos
for v in vertices:
    t.goto(v)  
```

<div class="img-content">
    <img class="lazy" data-src="{{cdn}}/turtle/img07.jpg"/>
</div>

¡Siiii y ahí lo tenemos!

Sólo deberíamos hacer algunos ajustes a nuestro programa para que la tortuga sólo dibuje los costados:

```python
def poligono_regular(px, py, radio, lados):
    
    # Desactivamos el trazo
    t.penup()
    
    # Calculamos el ángulo
    angulo = 360 / lados
    print(angulo)
    
    # Creamos la lista para almacenar los vértices
    vertices = []
    
    for i in range(lados):
        t.goto(px, py) 
        t.seth(angulo*i+1)
        t.forward(radio)
        vertices.append(t.pos()) 
        
    # Nos posicionamos en la coordenada del último vértice
    t.goto(vertices[-1])  
    
    # Empezamos a dibujar
    t.pendown()
    
    # Y hacemos que la tortuga se mueva a cada uno de ellos
    for v in vertices:
        t.goto(v) 
```

<div class="img-content">
    <img class="lazy" data-src="{{cdn}}/turtle/img08.jpg"/>
</div>

¡Genial!

Evidentemente hay otras formas de hacerlo, pero lo interesante es que hemos conseguido que la tortuga trabaje por nosotros y busque todos los vértices para trazar el polígono.

Lo bueno es que podemos juguetear un montón utilizando bucles por ejemplo:

```python
# Hacemos que la tortuga se mueva muy rápido y dibujamos
# los polígonos regulares de 3 a 20 costados
t.speed(200)
for n in range(3, 21):
    poligono_regular(0, 0, n*10, n)
```

<div class="img-content">
    <img class="lazy" data-src="{{cdn}}/turtle/img09.jpg"/>
</div>

Sin duda nuestra tortuga está hecha toda una artista.

Por cierto, ¿os habéis fijado que cuantos más costados, más se parece a una redonda? Es lo que os decía al principio.

## Quinto dibujo

Finalmente un último experimento para añadir interactividad en tiempo real. Y es que nosotros podemos capturar por teclado un valor con el método textinput() de la tortuga y hacer que se mueva a nuestra voluntad a partir de varias condiciones:

```python
def ordenar():

    orden = t.textinput("Orden requerida", 
                        "Movimientos: a w s d - Salir: e")
    
    if orden == "d":
        t.seth(0)
    elif orden == "w":
        t.seth(90)
    elif orden == "a":
        t.seth(180)
    elif orden == "s":
        t.seth(270)
    elif orden == "e":
        t.bye()  # cerramos la ventana
    else:
        return   # si no es una opción retornamos
        
    t.forward(50)


while True:
    ordenar()

t.done()
t.bye()
```

<div class="img-content">
    <img class="lazy" data-src="{{cdn}}/turtle/img10.jpg"/>
</div>

Al añadir interactividad somos nosotros quienes controlamos a la tortuga en tiempo real, hemos creado un videojuego sin saberlo! ¿Qué os parece?

Ahora imaginad que no tuviéramos que presionar constantemente enter al introducir nuestras órdenes. Para conseguirlo haremos lo siguiente:

```python
import turtle as t

t.setup(500,500)

t.shape("turtle") 
t.color("green")

# Creamos funciones para cada acción
def derecha():
    t.seth(0)
    t.forward(20)
    
def izquierda():
    t.seth(180)
    t.forward(20)
    
def arriba():
    t.seth(90)
    t.forward(20)
    
def abajo():
    t.seth(270)
    t.forward(20)
    
def salir():
    t.bye()

# Enlazamos cada función a una tecla
t.onkey(arriba, "w")
t.onkey(izquierda, "a")
t.onkey(derecha, "d")
t.onkey(abajo, "s")
t.onkey(salir, "e")
    
# Hacemos que tortuga esté atenta al teclado
t.listen()

t.done()
t.bye()
```

<div class="img-content">
    <img class="lazy" data-src="{{cdn}}/turtle/img11.jpg"/>
</div>

## Conclusión

Durante estos pequeños experimentos he podido entender el gran potencial pedagógico que tiene el módulo de la tortuga.

Se trata de una herramienta educativa que combinada con Python puede ofrecer infinitas posibilidades de aprendizaje para entender de forma visual qué hace la programación más allá del código. 

Incluso puede ser una buena forma de introducirse en la programación de videojuegos.

Sea como sea este módulo me ha recordado cuando en mi infancia dibujaba con un juguete llamado Telesketch, y no sé porque me da la sensación de que debió inspirar a los creadores de la tortuga para hacer algo parecido a través de una computadora. 

## Bibliografía

* [Introducción visual a Python](https://hourofpython.com/una-introduccion-visual-a-python/index.html): Minicurso de Python gráfico 100% en español utilizando Turtle.
* [Documentación oficial](https://docs.python.org/3.6/library/turtle.html): El mejor lugar para aprender todas las funcionalidades de la tortuga.

___
<small class="edited"><i>Última edición: 16 de Marzo de 2021</i></small>