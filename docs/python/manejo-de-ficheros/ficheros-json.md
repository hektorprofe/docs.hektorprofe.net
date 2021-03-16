title: Ficheros JSON | Curso de Python | Hektor Profe
description: Veamos como almacenar y recuperar listas y diccionarios en ficheros JSON con Python.

<style>
.admonition.note > .superfences-tabs > label:hover, .headerlink{
    color: #018dc5 !important;
}
.admonition.info{
    font-size: 100%;
}
.admonition.info label{
    font-size: 91%;
}
.admonition.note > .admonition-title {
    display: none;
}
</style>

# Ficheros JSON

JSON significa: Notación de objeto de JavaScript (javascript object notation)

Documentación: [https://docs.python.org/3/library/json.html](https://docs.python.org/3/library/json.html)

## Escritura de datos en JSON

```python
import json

contactos = [
    ("Manuel", "Desarrollador Web", "manuel@ejemplo.com"),
    ("Lorena", "Gestora de proyectos", "lorena@ejemplo.com"),
    ("Javier", "Analista de datos", "javier@ejemplo.com"),
    ("Marta", "Experta en Python", "marta@ejemplo.com")
]

datos = []

for nombre, empleo, email in contactos:
    datos.append({"nombre":nombre, "empleo":empleo, "email":email})

with open("contactos.json", "w") as jsonfile:
    json.dump(datos, jsonfile)
```

## Lectura de datos en JSON

```python
with open("contactos.json") as jsonfile:
    datos = json.load(jsonfile)
    for contacto in datos:
        print(contacto["nombre"], contacto["empleo"], contacto["email"])
```

---

<small class="edited"><i>Última edición: 17 de Marzo de 2021</i></small>
