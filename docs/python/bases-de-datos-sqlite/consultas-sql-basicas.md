title: Consultas SQL básicas | Curso de Python | Hektor Profe
description: ¿Qué es una base de datos? También conocidas como bancos de datos son simplemente conjuntos de datos que hacen referencia a información perteneciente a un mismo contexto.

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

# Consultas SQL básicas

## Primeros pasos

Conexión a la base de datos, creación y desconexión:

!!! info "" 
    
    ```python
    # Importamos el módulo
    import sqlite3

    # Nos conectamos a la base de datos ejemplo.db (la crea si no existe)
    conexion = sqlite3.connect('ejemplo.db')

    # Cerramos la conexión, si no la cerramos quedará abierta
    # y no podremos gestionar el fichero
    conexion.close()
    ```

## Crear una tabla

Antes de ejecutar una consulta (query) en código SQL, tenemos que crear un cursor:

!!! info "" 
    
    ```python
    import sqlite3

    conexion = sqlite3.connect('ejemplo.db')

    # Creamos el cursor
    cursor = conexion.cursor()

    # Ahora crearemos una tabla de usuarios con nombres, edades y emails
    cursor.execute("CREATE TABLE IF NOT EXISTS usuarios " \
        "(nombre VARCHAR(100), edad INTEGER, email VARCHAR(100))")

    # Guardamos los cambios haciendo un commit
    conexion.commit()

    conexion.close()
    ```

## Inserción con INSERT

!!! info "" 
    
    ```python
    import sqlite3

    conexion = sqlite3.connect('ejemplo.db')
    cursor = conexion.cursor()

    # Insertamos un registro en la tabla de usuarios
    cursor.execute("INSERT INTO usuarios VALUES " \
        "('Hector', 27, 'hector@ejemplo.com')")

    # Guardamos los cambios haciendo un commit
    conexion.commit()

    conexion.close()
    ```

## Lectura con SELECT

Recuperando el primer registro con *.fetchone()*:

!!! info "" 
    
    ```python
    import sqlite3

    conexion = sqlite3.connect('ejemplo.db')
    cursor = conexion.cursor()

    # Recuperamos los registros de la tabla de usuarios
    cursor.execute("SELECT * FROM usuarios")

    # Mostrar el cursos a ver que hay ?
    print(cursor)

    # Recorremos el primer registro con el método fetchone, devuelve una tupla
    usuario = cursor.fetchone()
    print(usuario)

    conexion.close()
    ```

    ```
    ('Hector', 27, 'hector@ejemplo.com')
    ``` 

## Inserción múltiple

Insertando varios registros con *.executemany()*:

!!! info "" 
    
    ```python
    import sqlite3

    conexion = sqlite3.connect('ejemplo.db')
    cursor = conexion.cursor()

    # Creamos una lista con varios usuarios
    usuarios = [('Mario', 51, 'mario@ejemplo.com'),
                ('Mercedes', 38, 'mercedes@ejemplo.com'),
                ('Juan', 19, 'juan@ejemplo.com')]

    # Ahora utilizamos el método executemany() para insertar varios
    cursor.executemany("INSERT INTO usuarios VALUES (?,?,?)", usuarios)

    # Guardamos los cambios haciendo un commit
    conexion.commit()

    conexion.close()
    ```

## Lectura múltiple

Recuperando varios registros con *.fetchall()*:

!!! info "" 
    
    ```python
    import sqlite3

    conexion = sqlite3.connect('ejemplo.db')
    cursor = conexion.cursor()

    # Recuperamos los registros de la tabla de usuarios
    cursor.execute("SELECT * FROM usuarios")

    # Recorremos todos los registros con fetchall
    # y los volcamos en una lista de usuarios
    usuarios = cursor.fetchall()

    # Ahora podemos recorrer todos los usuarios
    for usuario in usuarios:
        print(usuario)

    conexion.close()
    ``` 

    ```
    ('Hector', 27, 'hector@ejemplo.com')
    ('Mario', 51, 'mario@ejemplo.com')
    ('Mercedes', 38, 'mercedes@ejemplo.com')
    ('Juan', 19, 'juan@ejemplo.com')
    ``` 

___
<small class="edited"><i>Última edición: 5 de Octubre de 2018</i></small>