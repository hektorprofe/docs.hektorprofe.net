title: Objetos dentro de objetos | Curso de Python | Hektor Profe
description: En esta unidad aprenderemos sobre un paradigma de programación distinto que cambió la forma de entender la programación.

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

# Objetos dentro de objetos

Hasta ahora no lo hemos comentado, pero al ser las clases un nuevo tipo de dato resulta más que obvio que se pueden poner en colecciones e incluso utilizarlos dentro de otras clases. 

Os voy a dejar un pequeño código de ejemplo sobre un catálogo de películas para que lo estudiéis detenidamente:

!!! info ""

    ```python
    class Pelicula:
        
        # Constructor de clase
        def __init__(self, titulo, duracion, lanzamiento):
            self.titulo = titulo
            self.duracion = duracion
            self.lanzamiento = lanzamiento
            print('Se ha creado la película:', self.titulo)
            
        def __str__(self):
            return '{} ({})'.format(self.titulo, self.lanzamiento)


    class Catalogo:
        
        peliculas = []  # Esta lista contendrá objetos de la clase Pelicula
        
        def __init__(self, peliculas=[]):
            self.peliculas = peliculas
            
        def agregar(self, p):  # p será un objeto Pelicula
            self.peliculas.append(p)
            
        def mostrar(self):
            for p in self.peliculas:
                print(p)  # Print toma por defecto str(p)

        
    p = Pelicula("El Padrino", 175, 1972)
    c = Catalogo([p])  # Añado una lista con una película desde el principio
    c.mostrar()
    c.agregar(Pelicula("El Padrino: Parte 2", 202, 1974))  # Añadimos otra
    c.mostrar()
    ```

    ``` 
    Se ha creado la película: El Padrino
    El Padrino (1972)
    Se ha creado la película: El Padrino: Parte 2
    El Padrino (1972)
    El Padrino: Parte 2 (1974)
    ```

___
<small class="edited"><i>Última edición: 27 de Septiembre de 2018</i></small>