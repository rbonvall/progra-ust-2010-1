Guía de ejercicios 4
====================

Estos ejercicios serán su preparación
para la prueba solemne 4
del viernes 9 de julio.

Los ejercicios del `último laboratorio`_
también servirán de preparación.

.. _último laboratorio: lab-30-junio.html

Sumas por fila y columna
------------------------
El archivo ``datos1.txt``
tiene tres números enteros en cada fila:

.. code-block:: none

    45 12 98
    1 12 65
    7 15 76
    54 23 1
    65 2 84

1. Escriba una función ``suma_lineas(nombre_archivo)``
   que entregue una lista con las sumas
   de todas las líneas del archivo::

    >>> suma_lineas('datos1.txt')
    [155, 78, 98, 78, 151]

2. Escriba una función ``suma_columnas(nombre_archivo)``
   que entregue una lista con las sumas
   de las tres columnas del archivo::

    >>> suma_columnas('datos1.txt')
    [172, 64, 324]

Inventario
----------
Una tienda tiene la información de sus productos
en un archivo llamado ``productos.txt``.
Cada línea del archivo tiene tres datos:

* el código del producto (un número entero),
* el nombre del producto, y
* la cantidad de unidades del producto
  que quedan en bodega.

Los datos están separados por un símbolo ``/``.
Por ejemplo,
el siguiente puede ser el contenido del archivo:

.. code-block:: none

    1265/Reloj/26
    613/Cuaderno/87
    9801/Vuvuzela/3
    321/Lápiz/12
    5413/Tomate/5

1. Escriba una función ``existe_producto(codigo)``
   que indique si existe el producto
   con el código dado::

    >>> existe_producto(1784)
    False
    >>> existe_producto(321)
    True
    >>> existe_producto(613)
    True
    >>> existe_producto(0)
    False

2. Escriba una función ``por_reabastecer()``
   que cree un nuevo archivo llamado ``por_reabastecer.txt``
   que contenga los datos de todos los productos
   de los que queden menos de 10 unidades.

   En este caso,
   el archivo ``por_reabastecer.txt``
   debe quedar así:

.. code-block:: none

    9801/Vuvuzela/3
    5413/Tomate/5

.. include:: disqus.rst

