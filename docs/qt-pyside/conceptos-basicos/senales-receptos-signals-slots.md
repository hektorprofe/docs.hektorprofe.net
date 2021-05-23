title: Señales y receptores (Signals y Slots) | Curso Qt/PySide | Hektor Profe

# Señales y receptores (Signals y Slots)

Tenemos un botón en nuestro programa pero no hace nada.

En Qt para añadir una funcionalidad a un Widget necesitamos conectarlo a una acción, algo que se consigue mediante señales y slots.

Las señales son notificaciones emitidas por los widgets cuando sucede algo. Por ejemplo un botón envía una señal de "botón pulsado" cuando un usuario hace clic en él.

Pues bien, de poco sirve que un widget envíe una señal si nadie es consciente de ello. Para ese propósito existen los receptores, conocidos como `slots`:

```python
# Definimos un receptor para conectar la señal clicked a un método
button.clicked.connect(self.boton_clicado)

def boton_clicado(self):
    print("¡Me has clicado!")
```

Veamos otras señales de los botones para practicar:

```python
# Pulsación y liberación
button.pressed.connect(self.boton_pulsado)
button.released.connect(self.boton_liberado)

def boton_pulsado(self):
    print("¡Me has pulsado!")

def boton_liberado(self):
    print("¡Me has liberado!")
```

```python
# Señal para controlar el botón como un altenrador true/salse
button.setCheckable(True)
button.clicked.connect(self.boton_alternador)

def boton_alternador(self, valor):
    print("¿Alternado?", valor)
```

Con esto os podéis hacer una idea de cómo las señales están pendientes de todo lo que ocurre sobre los widgets para permitirnos actuar en consecuencia.


___
<small class="edited"><i>Última edición: 22 de Marzo de 2021</i></small>