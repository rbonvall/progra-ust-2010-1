Archivos
========

.. index:: memoria RAM, almacenamiento volátil

Todos los datos que un programa utiliza durante su ejecución
se encuentran en sus variables,
que están almacenadas en la `memoria RAM`_ del computador.

La memoria RAM es un medio de almacenamiento **volátil**:
cuando el programa termina, o cuando el computador se apaga,
todos los datos se pierden para siempre.

.. index:: disco duro, almacenamiento persistente

Para que un programa pueda guardar datos de manera permanente,
es necesario utilizar un medio de almacenamiento **persistente**,
de los cuales el más importante es el `disco duro`_.

.. index:: archivo

Los datos en el disco duro están organizados en archivos_.
Un **archivo** es una secuencia de datos
almacenados en un medio persistente
que están disponibles
para ser utilizados por un programa.
Todos los archivos tienen un nombre
y una ubicación dentro del sistema de archivos del sistema operativo.

Los datos en un archivo siguen estando presentes
después de que termina el programa que lo ha creado.
Un programa puede guardar sus datos en archivos
para usarlos en una ejecución futura,
e incluso puede leer datos
desde archivos creados por otros programas.

.. _memoria RAM: http://es.wikipedia.org/wiki/Memoria_RAM
.. _disco duro: http://es.wikipedia.org/wiki/Disco_duro
.. _archivos: http://es.wikipedia.org/wiki/Archivo_(informática)

Un programa no puede manipular los datos de un archivo directamente.
Para usar un archivo, un programa siempre abrir el archivo y
asignarlo a una variable, que llamaremos el **archivo lógico**.
Todas las operaciones sobre un archivo se realizan
a través del archivo lógico.

Dependiendo del contenido,
hay muchos tipos de archivos.
Nosotros nos preocuparemos sólo de los **archivos de texto**,
que son los que contienen texto,
y pueden ser abiertos y modificados usando un editor de texto
como el Bloc de Notas (Notepad).

Lectura de archivos
-------------------
Para leer datos de un archivo,
hay que abrirlo de la siguiente manera::

    archivo = open(nombre)

``nombre`` es un string que tiene el nombre del archivo.
``archivo`` es el archivo lógico a través del que
se manipulará el archivo.

Si el archivo no existe,
ocurrirá un **error de entrada y salida** (``IOError``).

La manera más simple de leer el contenido de un archivo
es hacerlo línea por línea.
Para esto,
basta con poner el archivo lógico en un ciclo for::

    for linea in archivo:
        # hacer algo

Una vez que los datos han sido leídos del archivo,
hay que cerrarlo::

    archivo.close()

Por ejemplo,
supongamos que tenemos el archivo ``himno.txt``
que tiene el siguiente contenido:

.. code-block:: none

    Puro Chile
    es tu cielo azulado
    puras brisas
    te cruzan también.

El archivo tiene cuatro líneas.
Cada línea termina con un símbolo "enter" (llamado **salto de línea**),
que indica que a continuación comienza una línea nueva.
En un string, el salto de línea se representa así: ``\n``.

El siguiente programa imprime
la primera letra de cada línea del himno::

    archivo = open('himno.txt')
    for linea in archivo:
        print(linea[0])
    archivo.close()

El ciclo for es ejecutado cuatro veces,
una por cada línea del archivo.
La salida del programa es::

    P
    e
    p
    t

Otro ejemplo:
el siguiente programa
imprime cuántos símbolos hay en cada línea::

    archivo = open('himno.txt')
    for linea in archivo:
        print(len(linea))
    archivo.close()

La salida es::

    11
    20
    13
    19

Note que el salto de línea (el "enter")
es considerado en la cuenta:

.. code-block:: none

    +--+--+--+--+--+--+--+--+--+--+--+
    |P |u |r |o |  |C |h |i |l |e |\n| = 11 símbolos
    +--+--+--+--+--+--+--+--+--+--+--+

Para obtener el string sin el salto de línea,
se puede usar el método ``strip``,
que elimina todos los símbolos de espaciado
al principio y al final del string::

    >>> s = '   Hola\n'
    >>> s.strip()
    'Hola'

Si modificamos el programa
para eliminar el salto de línea::

    archivo = open('himno.txt')
    for linea in archivo:
        print(len(linea.strip()))
    archivo.close()

entonces la salida es::

    10
    19
    12
    18

Lo importante es comprender
que los archivos son leídos línea por línea
usando el ciclo for.

Escritura de archivos
---------------------
(por redactar)

.. include:: disqus.rst

