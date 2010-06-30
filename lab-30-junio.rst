Laboratorio 30 de junio
=======================

Lectura de archivos
-------------------
Para abrir un archivo, se utiliza la función ``open``.
Por ejemplo,
para leer datos de un archivo llamado ``datos.txt``,
primero hay que abrirlo así::

    archivo = open('datos.txt')

La manera más facil de leer el archivo
es hacerlo línea por línea.
Se puede hacer usando un ciclo ``for``
que recorre el archivo::

    for linea in archivo:
        print(linea)

En cada iteración,
``linea`` es un string con el contenido de una línea del archivo.
Este string incluye el "enter" que marca el final de la línea.

Después de usar un archivo,
hay que cerrarlo::

    archivo.close()

Para los siguientes ejercicios,
descarge el archivo juegos.txt_,
que tiene la información de los números jugados
en cartones del Loto.

.. _juegos.txt: _static/juegos.txt

Ejercicio 1
-----------
¿Cuántos cartones de Loto fueron jugados?

Ejercicio 2
-----------
Escriba una función ``hay_ganadores(numeros)``,
donde ``numeros`` es el conjunto de los seis números de un sorteo,
que indique si alguien se ganó el Loto::

    >>> hay_ganadores({13, 33, 5, 38, 1, 19})
    True
    >>> hay_ganadores({14, 21, 1, 36, 9, 17})
    False

Ejercicio 3
-----------
Escriba una función ``n_aciertos(numeros, n)``,
que indique cuántas personas tuvieron ``n`` aciertos,
donde ``numeros`` es el conjunto de los seis números de un sorteo::

    >>> n_aciertos({13, 33, 5, 38, 1, 19}, 4)
    17
    >>> n_aciertos({20, 39, 6, 27, 12, 4}, 3)
    229
    >>> n_aciertos({1, 2, 3, 4, 5, 6}, 5)
    2

