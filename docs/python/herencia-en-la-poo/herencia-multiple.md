title: Herencia múltiple | Curso de Python | Hektor Profe
description: En esta unidad veremos en qué consiste eso de la herencia y cómo aprovecharla para ahorrarnos muchísimas líneas de código.

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

# Herencia múltiple

Finalmente hablemos de la herencia múltiple: la capacidad de una subclase de heredar de múltiples superclases. 

Esto conlleva un problema, y es que si varias superclases tienen los mismos atributos o métodos, la subclase sólo podrá heredar de una de ellas.

En estos casos Python dará prioridad a las clases más a la izquierda en el momento de la declaración de la subclase:

!!! info "" 
    ```python
    class A:
        def __init__(self):
            print("Soy de clase A")
        def a(self):
            print("Este método lo heredo de A")
            
    class B:
        def __init__(self):
            print("Soy de clase B")
        def b(self):
            print("Este método lo heredo de B")
            
    class C(B,A):
        def c(self):
            print("Este método es de C")


    c = C()
    c.a()
    c.b()
    c.c()
    ```

    ```
    Soy de clase B
    Este método lo heredo de A
    Este método lo heredo de B
    Este método es de C
    ```

___
<small class="edited"><i>Última edición: 29 de Septiembre de 2018</i></small>