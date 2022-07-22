title: Módulo gráfico Matplotlib | Python | Academia | Hektor Profe
description: Aprende a visualizar y personalizar tus gráficos de datos con esta potente biblioteca utilizada en conjunto con numpy y pandas.

# Introducción al módulo gráfico Matplotlib

<!-- <div class="contenedor_youtube">
  <iframe width="838" height="470" src="https://www.youtube.com/embed/r0NBTtxUYrs" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div> -->

## Primer gráfico

Empezaremos nuestra andadura viendo el gráfico más simple, el de líneas.

Dando por hecho que estáis continuando [el curso de numpy](/curso/introduccion-analisis-datos-python-numpy) y tenéis el entorno preparado, lo primero será cargar **mumpy** y **matplotlib** en una celda:

```python
# %%
import numpy as np
import matplotlib.pyplot as plt
```

Supongamos que necesitamos un gráfico que muestre los ahorros que hemos tenido durante los últimos 4 meses.

Vamos a declarar una lista con ellos:

```python
ahorros = [50, 100, 30, 65]
```

Ahora con **matplotlib** podemos dibujar un gráfico a partir de esta lista sin mucha complicación:

```python
plt.plot(ahorros)
```

¿Qué os parece? ¿Os esperábais algo más complejo?

Este gráfico tiene dos ejes, el horizontal (X) con 4 números de 0 a 3 y el vertical con los ahorros (Y) que empieza con el mínimo 30 hasta el máximo 100. Estos números corresponden a los índices de los valores en la lista y **matplotlib** genera una escala a partir de ellos.

El primer elemento con índice 0 es el 50, el segundo de índice 1 el 100 y así sucesivamente.

Así pues podemos crear gráficos a partir de listas pero también podemos hacerlo con arrays de **numpy**, ahí está gracia de todo.

Por ejemplo podemos generar un array aleatorio de ahorros para el último año (12 meses):

```python
# %%
ahorros = np.random.randint(100, size=[12])
plt.plot(ahorros)
```

Como véis con **numpy** tenemos una forma perfecta de generar valores aleatorios para nuestros gráficos de ejemplo.

Por cierto, nuestros gráficos se muestran porque como ya sabéis **jupyter** muestra la última celda automáticamente, de ahí que nos aparezca el nombre del objeto y su dirección en la memoria.

Podemos evitar que aparezca esa línea llamando explícitamente al método **show()** del gráfico:

```python
# %%
plt.plot(ahorros)
plt.show()
```

Es una buena práctica para no mostrar información de más, así que vamos a usarlo de ahora en adelante.

## Ejes y mapeados

En esta segunda lección aprenderemos a:

- Mapear texto en los ejes numéricos.
- A trabajar con el eje X y el eje Y.
- A crear gráficos con los ejes invertidos.

### Mapeado de texto en los ejes

Por defecto en los gráficos no podemos mostrar texto en los ejes porque estos se basan en valores numéricos.

Lo que podemos hacer es mapear los textos a mostrar en una lista del mismo tamaño que el número de valores del eje (x para el horizontal e y para el vertical), utilizando los métodos **xticks()** o **yticks()**:

```python
# %%
import numpy as np
import matplotlib.pyplot as plt

ahorros = np.random.randint(100, size=[6])
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio']
mapeado = range(len(meses))

plt.plot(ahorros)           # Añadimos el gráfico
plt.xticks(mapeado, meses)  # Mapeamos los valores horizontales
plt.show()                  # Finalmente lo mostramos
```

### Eje X y eje Y

Bien, hasta ahora los gráficos que hemos visualizado los hemos creado a partir de vectores de una dimensión.

Al utilizar un único vector en el método **.plot()** éste lo toma como los valores del eje Y y genera el eje X automáticamente a partir de la longitud del vector.

Ahora bien, nosotros podemos decidir los valores del eje X si los pasamos en otro vector como primer parámetro:

```python
# %%
x = np.arange(6)
y = np.random.randint(20, size=[6])

plt.plot(x, y)
plt.show()
```

### Gráficos invertidos

Algo interesante es que cambiando el orden de los ejes podemos generar un gráfico invertido:

```python
# %%
plt.plot(y, x)
plt.show()
```

### Ejemplo curioso

Ahora bien, ¿qué ocurriría si los valores en X también fueran aleatorios?

```python
# %%
x = np.random.randint(20, size=[6])
y = np.random.randint(20, size=[6])

plt.plot(x, y)
plt.show()
```

Pues como véis se genera un gráfico muy extraño.

Los gráficos lineales se rigen en función del tiempo, eso implica que uno de los ejes debe ser un valor incremental. Al generar valores aleatorios hemos "roto" completamente esa lógica y como resultado nos queda un gráfico donde las líneas se cruzan por todas partes.

La gracia de los gráficos es facilitar la comprensión en lugar de dificultarla así que deberíais evitar ejemplos como este.

## Límites

En algunas ocasiones necesitaremos manipular los límites inferiores y superiores de los ejes. Eso podemos hacerlo gracias a los métodos:

- **plt.xlim(min, max)**
- **plt.ylim(min, max)**

Por ejemplo volvamos al ejemplo de los ahorros de la lección anterior

```python
# %%
import numpy as np
import matplotlib.pyplot as plt

ahorros = np.random.randint(100, size=[6])
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio']
mapeado = range(len(meses))

plt.plot(ahorros)           # Añadimos el gráfico
plt.xticks(mapeado, meses)  # Mapeamos los valores horizontales
plt.show()                  # Finalmente lo mostramos
```

En este gráfico estamos manejando un array de datos aleatorios de 0 a 100. Sin embargo el gráfico establecerá los límites en los meses con más y menos ahorros.

Podemos establecer que utilice 0 y 100 como escala para el eje Y con los ahorros aunque no tengamos ningún valor explícito con ellos:

```python
# %%
# Límites verticales
plt.plot(ahorros)           # Añadimos el gráfico
plt.xticks(mapeado, meses)  # Mapeamos los valores horizontales
plt.ylim(0, 100)            # Configuramos el límite vertical
plt.show()                  # Finalmente lo mostramos
```

Utilizando los límites podemos centrarnos en una parte específica del gráfico.

Por ejemplo si quisiéramos mostrar únicamente los meses de Marzo, Abril y Mayo, podemos limitar el eje X a los valores numéricos de los meses 2, 3 y 4 con un range de 2 a 4:

```python
# %%
# Límites horizontales
plt.plot(ahorros)           # Añadimos el gráfico
plt.xticks(mapeado, meses)  # Mapeamos los valores horizontales
plt.xlim(2, 4)              # Configuramos el límite horizontal
plt.ylim(0, 100)            # Configuramos el límite vertical
plt.show()                  # Finalmente lo mostramos
```

En cierta forma podemos considerarlo una forma de zoom así que no lo olvidéis.

## Títulos, etiquetas y leyendas

Sigamos con el ejemplo de los ahorros y vamos a utilizarlo para aprender a personalizar nuestros gráficos, añadiéndoles títulos, etiquetas y leyendas.

Podríamos añadir a nuestro gráfico el titulo "Ahorros del primer semestre" y unas etiquetas para los eje X e Y con "Meses" y "Cantidad en €" respectivamente.

Para ello utilizaremos los métodos:

- **plt.title("Título")**
- **plt.xlabel("Etiqueta horizontal")**
- **plt.ylabel("Etiqueta vertical")**

```python
# %%
import numpy as np
import matplotlib.pyplot as plt

ahorros = np.random.randint(100, size=[6])
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio']
mapeado = range(len(meses))

plt.plot(ahorros)                         # Añadimos el gráfico
plt.xticks(mapeado, meses)                # Mapeamos los valores horizontales
plt.xlim(2, 4)                            # Configuramos el límite horizontal
plt.title("Ahorros del primer semestre")  # Configuramos el título
plt.xlabel("Meses")                       # Configuramos la etiqueta del eje X
plt.ylabel("Cantidad en €")               # Configuramos la etiqueta del eje Y
plt.show()                                # Finalmente lo mostramos
```

El otro elemento informativo que podemos añadir son las leyendas utilizando:

- **plt.legend(LOCALIZACION)**

Podemos elegir optativamente una localización a partir de las distintas opciones que nos indican en [la documentación de matplotlib](https://matplotlib.org/1.3.1/api/pyplot_api.html#matplotlib.pyplot.legend) y que os dejaré recopiladas abajo en los apuntes:

- **'best'** => 0
- **'upper right'** => 1
- **'upper left'** => 2
- **'lower left'** => 3
- **'lower right'** => 4
- **'right'** => 5
- **'center left'** => 6
- **'center right'** => 7
- **'lower center'** => 8
- **'upper center'** => 9
- **'center'** => 10

Por defecto se usa la opción 0 para detectar automáticamente el mejor sitio donde poner la leyenda:

```python
# %%
# Mostramos una leyenda
plt.plot(ahorros)                         # Añadimos el gráfico
plt.xticks(mapeado, meses)                # Mapeamos los valores horizontales
plt.xlim(2, 4)                            # Configuramos el límite horizontal
plt.title("Ahorros del primer semestre")  # Configuramos el título
plt.xlabel("Meses")                       # Configuramos la etiqueta del eje X
plt.ylabel("Cantidad en €")               # Configuramos la etiqueta del eje Y
plt.legend(loc=4)                         # Mostramos la leyenda
plt.show()                                # Finalmente lo mostramos
```

Veréis que nos aparece un cuadradito pero no muestra nada, eso es porque tenemos que configurar el texto para del gráfico, algo que definiremos con la propiedad **label** al usar **plot()**:

```python
# %%
# Mostramos una leyenda con un texto
plt.plot(ahorros, label="Evolución")      # Añadimos el gráfico con un texto
plt.xticks(mapeado, meses)                # Mapeamos los valores horizontales
plt.xlim(2, 4)                            # Configuramos el límite horizontal
plt.title("Ahorros del primer semestre")  # Configuramos el título
plt.xlabel("Meses")                       # Configuramos la etiqueta del eje X
plt.ylabel("Cantidad en €")               # Configuramos la etiqueta del eje Y
plt.legend()                              # Mostramos la leyenda automáticamente
plt.show()                                # Finalmente lo mostramos
```

En este escenario donde dibujamos un único vector de datos una leyenda no tiene mucho sentido, pero si en lugar de uno tubiéramos por ejemplo tres vectores representando los ahorros de tres personas la cosa cambiaría:

```python
# %%
# Mostramos los ahorros de tres personas diferentes
import numpy as np
import matplotlib.pyplot as plt

meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio']
mapeado = range(len(meses))

plt.plot(np.random.randint(100, size=[6]), label="Pedro")
plt.plot(np.random.randint(100, size=[6]), label="Marta")
plt.plot(np.random.randint(100, size=[6]), label="Ana")
plt.xticks(mapeado, meses)
plt.xlim(2, 4)
plt.title("Ahorros del primer semestre")
plt.xlabel("Meses")
plt.ylabel("Cantidad en €")
plt.legend()
plt.show()
```

Esto que acabamos de hacer se denomina **visualización de múltiples series**, representando cada serie una de las líneas del gráfico.

Con esto que sabemos y un poco de comprensión de listas podemos hacer otro ejemplo muy rápidamente para dibujar las tablas de multiplicas del 1 al 10:

```python
# %%
# Tablas de multiplicar del 1 al 10
for t in range(1, 11):
    plt.plot(
        range(1, 11),                   # Eje X
        [t * n for n in range(1, 11)],  # Eje Y
        label=f"Tabla del {t}"          # Leyenda
    )
plt.title('Tablas')
plt.xlabel('Número')
plt.ylabel('Resultado')
plt.legend()
plt.show()
```

Para que luego digan que Python no mola...

## Estilos de línea y marcadores

En esta lección vamos a seguir personalizando nuestros gráficos, concretamente las líneas y los marcadores.

### Líneas

Vamos a empezar con las líneas usando nuestro ejemplo de los ahorros y lo haremos justo en el momento de añadir el gráfico de cada persona.

Tenemos las siguientes propiedades básicas:

- **linewidth (lw)**: Ancho de la línea
- **linestyle (ls)**: Estilo de la línea \*
- **color**: Color de la línea (número y decimal)
- **alpha**: Opacidad de la línea (de 0 a 1)

```python
# %%
# Personalizamos las líneas
import numpy as np
import matplotlib.pyplot as plt

meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio']
mapeado = range(len(meses))

plt.plot(np.random.randint(100, size=[6]),
         label="Pedro", color="red", ls="-", lw="3")
plt.plot(np.random.randint(100, size=[6]),
         label="Marta", color="#0000ff", ls="--", lw="4")
plt.plot(np.random.randint(100, size=[6]),
         label="Ana", color="green", ls="-.", lw="4")
plt.xticks(mapeado, meses)
plt.legend()
plt.show()
```

(\*) En la [documentación oficial](https://matplotlib.org/api/lines_api.html#matplotlib.lines.Line2D.set_linestyle) podéis consultar otras opciones para configurar las líneas.

### Marcadores

En los gráficos lineales los marcadores hacen referencia a los puntos o vértices donde se dibujan los valores.

Vamos a ver los siguientes métodos:

- **marker**: Tipo de marcador \*
- **markersize**: Tamaño del marcador
- **markerfacecolor**: Color del marcador (número y decimal)
- **markeredgecolor**: Color del borde (número y decimal)
- **markeredgewidth**: Tamaño del borde

```python
# %%
# Personalizamos los marcadores

meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio']
mapeado = range(len(meses))

plt.plot(np.random.randint(100, size=[6]),
         marker="o", markersize="8", markeredgewidth="2",
         markerfacecolor="green", markeredgecolor="white")
plt.plot(np.random.randint(100, size=[6]),
         marker="*", markersize="10", markeredgewidth="2",
         markerfacecolor="red", markeredgecolor="white")
plt.plot(np.random.randint(100, size=[6]),
         marker="D", markersize="5", markeredgewidth="2",
         markerfacecolor="orange", markeredgecolor="white")
plt.xticks(mapeado, meses)
plt.legend()
plt.show()
```

(\*) La lista completa de marcadores posibles la encontraréis en la [documentación oficial](https://matplotlib.org/api/markers_api.html).

## Subgráficos

Ya hemos visto cómo crear gráficos. ¿Pero y si queremos dibujar más de un gráfico en el mismo espacio? ¿Por ejemplo para hacer una comparativa de los ahorros de cada personas cada sin sobreponer las líneas en la misma figura? Para esos casos podemos utilizar subgráficos.

La regla de oro para añadir subgráficos es imaginar que estamos dibujando una tabla y cada subgráfico se dibujará en una celda dentro de esa tabla.

Por tanto lo que debemos indicarle a **matplotlib** es en qué celda debe dibujar cada subgráfico:

```python
# %%
# Dibujos con subgráficos
import numpy as np
import matplotlib.pyplot as plt

plt.subplot(1, 3, 1)  # Tabla 1x3 y dibujaremos en la celda 1
plt.plot(np.random.randint(100, size=[6]), label="Pedro", color="green")
plt.ylim(0, 100)
plt.legend()

plt.subplot(1, 3, 2)  # Tabla 1x3 y dibujaremos en la celda 2
plt.plot(np.random.randint(100, size=[6]), label="Marta", color="red")
plt.ylim(0, 100)
plt.legend()

plt.subplot(1, 3, 3)  # Tabla 1x3 y dibujaremos en la celda 3
plt.plot(np.random.randint(100, size=[6]), label="Ana", color="cyan")
plt.ylim(0, 100)
plt.legend()

plt.show()  # Dibujamos el conjunto
```

Tened en cuenta que tenréis que dibujar cada subgráfico individualmente con su propia configuración, títulos, etiquetas, leyendas... y finalmente usar **plt.show()** para mostrar el conjunto de subgráficos.

Podemos hacer otro ejemplo generado dinámicamente utilizando un bucle para que veáis como hacer lo mismo pero con varias filas:

```python
# %%
# Dibujando 9 subgráficos
for i in range(9):
    plt.subplot(3, 3, i+1)  # Tabla 3x3
    plt.plot(np.random.randint(100, size=[6]))
    plt.plot(np.random.randint(100, size=[6]))
    plt.ylim(0, 100)

plt.show()
```

## Figuras

Hasta ahora todo lo que hemos hecho con **matplotlib** ha sido dibujar gráficos en celdas, pero en la vida real necesitaremos manejar estos gráficos para poder exportarlos y utilizarlos en nuestros programas y aplicaciones web.

Para manejarlos se utilizan las figuras, la versión orientada a objetos de todo lo que hemos estado haciendo usando instancias y métodos. Cambia un poco la sintaxis así que tenedlo en cuenta:

```python
# %%
# Gráficos usando figuras
import numpy as np
import matplotlib.pyplot as plt

# La figura crea un espacio donde dibujar el gráfico
fig = plt.figure()

# Necesitamos definir una relación de tamaños para el rectángulo del dibujo (l,b,w,h)
# Nota: En jupyter l(eft) y b(ottom) para el primer gráfico no se tienen en cuenta
rect = (0, 0, 1, 1)

# Añadimos los límites para crear un objeto de ejes sobre el que dibujar el gráfico
axes = fig.add_axes(rect)

# A partir de este objeto podremos crear nuestro gráfico como si fuera el clásico plt
axes.plot(np.random.randint(100, size=[6]), label="Pedro", color="green")
axes.plot(np.random.randint(100, size=[6]), label="Marta", color="red")
axes.plot(np.random.randint(100, size=[6]), label="Ana", color="cyan")

# La mayor diferencia ahora es a la hora de personalizar el gráfico, teniéndonos
# que referir a los métodos con la palabra set precediendo del nombre clásico
axes.set_ylim(0, 100)
axes.set_xlabel("Meses")
axes.set_ylabel("Cantidad en €")
axes.set_title("Ahorros del primer semestre")

# La parte de mapear los nombres cambia un poco y requiere usar dos métodos
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio']
mapeado = range(len(meses))
axes.set_xticks(mapeado)
axes.set_xticklabels(meses)

# Finalmente mostramos la figura
fig.show()
```

¿Cuál es la gracia de todo esto? Pues que al ser un objeto independiente podemos modificar su tamaño estableciendo una relación de pulgadas en ancho/alto y una densidad de píxeles por pulgada (dpi):

```python
fig = plt.figure(figsize=(1, 1), dpi=100)
fig = plt.figure(figsize=(4, 2), dpi=100)
fig = plt.figure(figsize=(3, 4), dpi=100)
```

Una vez tengamos los gráficos podemos guardarlos abriéndolos con doble clic y usando el botón de exportar que soporta **png**, **svg** y **pdf**.

## Tipos de gráficos

Esta última lección es una galería donde veremos diferentes tipos de gráficos que nos ofrece **matplotlib**. En esencia se utilizan igual que el gráfico lineal así que no entraremos en detalles, pero igualmente os dejaré los códigos y enlaces a la documentación de cada tipo por si queréis aprender más.

### Gráfico lineal (plot)

Es el que hemos utilizado durante todo el curso, no requieren indicar nada específico a la hora de crearlos.

- [Documentación oficial](https://matplotlib.org/devdocs/api/_as_gen/matplotlib.pyplot.plot.html)

```python
# %%
# Gráfico lineal
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 11)
y = np.random.randint(10, size=10)

plt.plot(x, y)
plt.show()
```

### Gráfico de líneas verticales (stem)

Este gráfico es muy útil para ilustrar valores positivos y negativos.

- [Documentación oficial](https://matplotlib.org/devdocs/api/_as_gen/matplotlib.pyplot.stem.html)

```python
# %%
# Gráfico de líneas verticales
plt.stem(x, y)
plt.show()
```

### Gráfico de series comparadas (fill_between)

Con éste podemos rellenar el espacio que hay entre dos series en el eje Y, pero hay que dibujarlas de más excluyente a menos para que no solapen los colores.

- [Documentación oficial](https://matplotlib.org/devdocs/api/_as_gen/matplotlib.pyplot.fill_between.html)

```python
# %%
# Gráfico de series comparadas
for t in range(1, 11)[::-1]:
    plt.fill_between(
        range(1, 11),
        [t * n for n in range(1, 11)],
        label=f"Tabla del {t}"
    )
plt.title("Tablas de multiplicar")
plt.legend(loc='upper left')
plt.show()
```

### Gráfico circular o de pastel (pie)

El gráfico de "quesitos" como yo lo llamo es muy útil para representar porcentajes.

- [Documentación oficial](https://matplotlib.org/devdocs/api/_as_gen/matplotlib.pyplot.pie.html)

```python
# %%
# Gráfico circular o de pastel
# https://es.wikipedia.org/wiki/Anexo:Destinos_tur%C3%ADsticos_mundiales

turistas = [86.9, 81.8, 75.9, 60.7, 58.2, 39.3, 37.7, 37.6, 37.5, 35.4]
paises = ['Francia', 'España', 'EEUU', 'China', 'Italia',
          'México', 'Reino Unido', 'Turquía', 'Alemania', 'Tailandia']

explode = [0, 0.2, 0, 0, 0, 0.4, 0, 0, 0, 0]  # Destacar algunos

plt.pie(turistas, labels=paises, explode=explode,
        autopct='%1.1f%%', shadow=True, startangle=90)
plt.title('TOP 10 DESTINOS TURÍSTICOS EN 2017')
plt.show()
```

### Gráfico de cajas y bigotes (boxplot)

Este tipo nos permite hacernos una idea de valores medios gracias a las cajas, mientras por otro lado los bigotes nos indican valores límitantes.

- [Documentación oficial](https://matplotlib.org/devdocs/api/_as_gen/matplotlib.pyplot.boxplot.html)

```python
# %%
# Gráfico de cajas y bigotes
# https://es.wikipedia.org/wiki/Estatura

jap = np.random.uniform(166, 176, 100)
ale = np.random.uniform(175, 185, 100)
arg = np.random.uniform(170, 180, 100)

# Cambio los colores para que se vea bien en VSC con tema oscura
plt.boxplot([jap, ale, arg],
            notch=True, patch_artist=True,
            capprops=dict(color="green"),
            medianprops=dict(color="orange"),
            whiskerprops=dict(color="yellow"))
plt.xticks([1, 2, 3], ['Japón', 'Alemania', 'Argentina'])
plt.ylabel('Estaturas (cm)')
plt.show()
```

### Gráfico histograma (hist)

Los histogramas sirven para hacernos una idea de la frecuencia de distribución de valores en un rango determinado.

- [Documentación oficial](https://matplotlib.org/devdocs/api/_as_gen/matplotlib.pyplot.hist.html)

```python
# %%
# Gráfico histograma
alturas = np.random.uniform(170, 180, 1000)

# El rango se define con bins, debe ser menor que el número de muestras
plt.hist(alturas, bins=10, edgecolor='black')

plt.title("Distribución de 1000 alturas")
plt.xlabel("Altura media (cm)")
plt.ylabel("Muestras")
plt.show()
```

Otro ejemplo con [distribución gaussiana](https://es.wikipedia.org/wiki/Distribuci%C3%B3n_normal) a partir de un vector normal con **numpy** que tiende a dibujar una campana con su máximo justo en medio:

```python
# %%
# Gráfico histograma gaussiano
numeros = numpy.random.normal(size=1000)

plt.hist(numeros, bins=10, edgecolor='black')

plt.title("Histograma Gaussiano")
plt.xlabel("Valor")
plt.ylabel("Frecuencia")
plt.show()
```

### Gráfico de barras (bar)

Este es el clásico gráfico donde las barras nos indican cantidades en el eje Y para los valores en el eje X.

- [Documentación oficial](https://matplotlib.org/devdocs/api/_as_gen/matplotlib.pyplot.bar.html)

```python
# %%
# Gráfico de barras
# http://www.datosmacro.com/prima-riesgo/espana

fechas = ['19/08/2019', '20/08/2019', '21/08/2019', '22/08/2019', '23/08/2019']
primas = [79, 80, 79, 80, 82]

plt.bar(range(5), primas, edgecolor='black')

plt.xticks(range(5), fechas, rotation=60)
plt.title("PRIMA DE RIESGO EN ESPAÑA")
plt.ylim(min(primas)-1, max(primas)+1)
plt.show()
```

### Gráfico de barras horizontales (barh)

Es una variante del anterior con las columnas dispuestas horizontalmente, por lo que cambian los ejes de las etiquetas y límites:

- [Documentación oficial](https://matplotlib.org/devdocs/api/_as_gen/matplotlib.pyplot.barh.html)

```python
# %%
# Gráfico de barras horizontales
# http://www.datosmacro.com/prima-riesgo/espana

fechas = ['19/08/2019', '20/08/2019', '21/08/2019', '22/08/2019', '23/08/2019']
primas = [79, 80, 79, 80, 82]

plt.barh(range(5), primas, edgecolor='black')

plt.yticks(range(5), fechas, rotation=60)
plt.title("PRIMA DE RIESGO EN ESPAÑA")
plt.xlim(min(primas)-1, max(primas)+1)
plt.show()
```

### Gráfico de escaleras (step)

Otro gráfico muy simple que nos muestra las variaciones de forma continuada dibujando una escalera:

- [Documentación oficial](https://matplotlib.org/devdocs/api/_as_gen/matplotlib.pyplot.step.html)

```python
# %%
# Gráfico de escaleras
x = np.arange(1, 11)
y = np.random.randint(10, size=10)

plt.step(x, y)
plt.show()
```

### Más gráficos

Esta biblioteca nos ofrece muchísimos más tipos de gráficos, por eso os sugiero explorar más tipos de gráficos en la [galería oficial de matplotlib](http://matplotlib.org/gallery.html), ahí encontraréis cientos y cientos de ejemplos.

Con esto acabamos el curso, espero que lo hayáis disfrutado tanto como yo creándolo.

---

<small class="edited"><i>Última edición: 16 de Marzo de 2021</i></small>
