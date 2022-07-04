title: Primer contacto con la POO | Curso de Python | Hektor Profe
description: En esta unidad aprenderemos sobre un paradigma de programación distinto que cambió la forma de entender la programación.

# Primer contacto con la POO

Para entender en qué se basa este paradigma (modelo de solución de problemas), en lugar de empezar con teoría os propongo jugar un poco con dos códigos distintos. Ambos implementan una estructura de clientes y funciones para trabajar con ellos, pero uno está creado con programación estructurada (la clásica cuyas bases hemos estudiado hasta ahora) y la otra con programación orientada a objetos.

Lo único que tenéis que hacer es probar ambos códigos (sin necesidad de analizarlos), luego sacad vuestras propias conclusiones sobre cuál os parece más útil e intuitivo de aplicar y extender en el mundo real.

## Ejemplo estructurado

!!! info "" 
    
    ```python
    # Definimos unos cuantos clientes
    clientes= [
        {'Nombre': 'Hector', 'Apellidos':'Costa Guzman', 'dni':'11111111A'},
        {'Nombre': 'Juan', 'Apellidos':'González Márquez', 'dni':'22222222B'} 
    ]

    # Creamos una función que muestra un cliente en una lista a partir del DNI
    def mostrar_cliente(clientes, dni):
        for c in clientes:
            if (dni == c['dni']):
                print('{} {}'.format(c['Nombre'],c['Apellidos']))
                return
        print('Cliente no encontrado')

    # Creamos una función que borra un cliente en una lista a partir del DNI
    def borrar_cliente(clientes, dni):
        for i,c in enumerate(clientes):
            if (dni == c['dni']):
                del( clientes[i] )
                print(str(c),"> BORRADO")
                return
            
        print('Cliente no encontrado')    

    ### Fíjate muy bien cómo se utiliza el código estructurado
    
    print("==LISTADO DE CLIENTES==")
    print(clientes)

    print("\n==MOSTRAR CLIENTES POR DNI==")
    mostrar_cliente(clientes, '11111111A')
    mostrar_cliente(clientes, '11111111Z')

    print("\n==BORRAR CLIENTES POR DNI==")
    borrar_cliente(clientes, '22222222V')
    borrar_cliente(clientes, '22222222B')

    print("\n==LISTADO DE CLIENTES==")
    print(clientes)
    ```

    ```
    ==LISTADO DE CLIENTES==
    [{'Nombre': 'Hector', 'Apellidos': 'Costa Guzman', 'dni': '11111111A'}, 
    {'Nombre': 'Juan', 'Apellidos': 'González Márquez', 'dni': '22222222B'}]

    ==MOSTRAR CLIENTES POR DNI==
    Hector Costa Guzman
    Cliente no encontrado

    ==BORRAR CLIENTES POR DNI==
    Cliente no encontrado
    {'Nombre': 'Juan', 'Apellidos': 'González Márquez', 'dni': '22222222B'} > BORRADO

    ==LISTADO DE CLIENTES==
    [{'Nombre': 'Hector', 'Apellidos': 'Costa Guzman', 'dni': '11111111A'}]
    ```

## Ejemplo orientado a objetos

!!! info ""
    
    ```python
    ### No intentes entender este código, sólo fíjate en cómo se utiliza abajo  

    # Creo una estructura para los clientes
    class Cliente:
        
        def __init__(self, dni, nombre, apellidos):
            self.dni = dni
            self.nombre = nombre
            self.apellidos = apellidos
            
        def __str__(self):
            return '{} {}'.format(self.nombre,self.apellidos)

    # Y otra para las empresas
    class Empresa:
        
        def __init__(self, clientes=[]):
            self.clientes = clientes
            
        def mostrar_cliente(self, dni=None):
            for c in self.clientes:
                if c.dni == dni:
                    print(c)
                    return
            print("Cliente no encontrado")
        
        def borrar_cliente(self, dni=None):
            for i,c in enumerate(self.clientes):
                if c.dni == dni:
                    del(self.clientes[i])
                    print(str(c),"> BORRADO")
                    return
            print("Cliente no encontrado")

    ### Ahora utilizaré ambas estructuras 

    # Creo un par de clientes
    hector = Cliente(nombre="Hector", apellidos="Costa Guzman", dni="11111111A")
    juan = Cliente("22222222B", "Juan", "Gonzalez Marquez")

    # Creo una empresa con los clientes iniciales
    empresa = Empresa(clientes=[hector, juan])

    # Muestro todos los clientes
    print("==LISTADO DE CLIENTES==")
    print(empresa.clientes)

    print("\n==MOSTRAR CLIENTES POR DNI==")
    # Consulto clientes por DNI
    empresa.mostrar_cliente("11111111A")
    empresa.mostrar_cliente("11111111Z")

    print("\n==BORRAR CLIENTES POR DNI==")
    # Borro un cliente por DNI
    empresa.borrar_cliente("22222222V")
    empresa.borrar_cliente("22222222B")

    # Muestro de nuevo todos los clientes
    print("\n==LISTADO DE CLIENTES==")
    print(empresa.clientes)
    ```

    ```
    ==LISTADO DE CLIENTES==
    [<__main__.Cliente object at 0x0000023F567B42E8>,
    <__main__.Cliente object at 0x0000023F567B4320>]

    ==MOSTRAR CLIENTES POR DNI==
    Hector Costa Guzman
    Cliente no encontrado

    ==BORRAR CLIENTES POR DNI==
    Cliente no encontrado
    Juan Gonzalez Marquez > BORRADO

    ==LISTADO DE CLIENTES==
    [<__main__.Cliente object at 0x0000023F567B42E8>]
    ```

¿No os parece que el código orientado a objetos es más autoexplicativo a la hora de utilizarlo? Además con programación estructurada tenemos que enviar la lista que queremos consultar todo el rato, mientras que con la POO tenemos esas "estructuras" como la empresa que contienen los clientes, todo queda como más ordenado.

___
<small class="edited"><i>Última edición: 27 de Septiembre de 2018</i></small>