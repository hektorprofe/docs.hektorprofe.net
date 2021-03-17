title: Ficheros CSV | Curso de Python | Hektor Profe
description: Veamos como almacenar y recuperar listas y diccionarios en ficheros CSV con Python.

# Ficheros CSV

**CSV**: Valores separados por comas (Comma Separated Values)

Documentación: [https://docs.python.org/3/library/csv.html](https://docs.python.org/3/library/csv.html)

## Escritura de listas en CSV

```python
import csv

contactos = [
    ("Manuel", "Desarrollador Web", "manuel@ejemplo.com"),
    ("Lorena", "Gestora de proyectos", "lorena@ejemplo.com"),
    ("Javier", "Analista de datos", "javier@ejemplo.com"),
    ("Marta", "Experta en Python", "marta@ejemplo.com")
]

with open("contactos.csv", "w", newline="\n") as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    for contacto in contactos:
        writer.writerow(contacto)
```

## Lectura de listas en CSV

```python
with open("contactos.csv", newline="\n") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    for nombre, empleo, email in reader:
        print(nombre, empleo, email)
```

## Escritura de diccionarios en CSV

```python
import csv

contactos = [
    ("Manuel", "Desarrollador Web", "manuel@ejemplo.com"),
    ("Lorena", "Gestora de proyectos", "lorena@ejemplo.com"),
    ("Javier", "Analista de datos", "javier@ejemplo.com"),
    ("Marta", "Experta en Python", "marta@ejemplo.com")
]

with open("contactos.csv", "w", newline="\n") as csvfile:
    campos = ["nombre", "empleo", "email"]
    writer = csv.DictWriter(csvfile, fieldnames=campos)
    writer.writeheader()
    for nombre, empleo, email in contactos:
        writer.writerow({
            "nombre": nombre, "empleo": empleo, "email": email
        })
```

## Lectura de diccionarios en CSV

```python
with open("contactos.csv", newline="\n") as csvfile:
    reader = csv.DictReader(csvfile)
    for contacto in reader:
        print(contacto["nombre"], contacto["empleo"], contacto["email"])
```

---

<small class="edited"><i>Última edición: 17 de Marzo de 2021</i></small>
