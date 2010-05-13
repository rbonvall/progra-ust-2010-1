Laboratorio 12 de mayo
======================
En esta sesión de laboratorio se evaluará:

* `funciones`_,
* `módulos`_,
* `listas`_.

Además, hay que conocer muy bien toda la materia vista durante el semestre.

.. _funciones: funciones.html
.. _módulos: modulos.html
.. _listas: listas.html

El laboratorio debe ser resuelto usando el programa **PyScripter**.

Problema 1: módulo de listas
----------------------------
Crear un módulo llamado ``listas.py`` que tenga las siguientes funciones:

* una función ``promedio(l)``,
  cuyo parámetro ``l`` sea una lista de números reales,
  y que entregue el promedio de los números::

    >>> promedio([7.0, 3.1, 1.7])
    3.933333333333333
    >>> promedio([1, 4, 9, 16])
    7.5

* una función ``cuadrados(l)``,
  que entregue una lista con los cuadrados
  de los valores de ``l``::

    >>> cuadrados([1, 2, 3, 4, 5])
    [1, 4, 9, 16, 25]
    >>> cuadrados([3.4, 1.2])
    [11.559999999999999, 1.44]

* una función ``mas_largo(palabras)``,
  cuyo parámetro ``palabras`` es una lista de strings,
  que entregue cuál es el string más largo::

    >>> mas_largo(['raton', 'hipopotamo', 'buey', 'jirafa'])
    'hipopotamo'
    >>> mas_largo(['****', '**', '********', '**'])
    '********'

Problema 2: promedio de cuadrados
---------------------------------
Escriba un programa llamado ``nombre-apellido.py`` (con su nombre y su apellido)
que haga lo siguiente:

* preguntar al usuario cuántos valores va a ingresar (``n``),
* pedir al usuario que ingrese los ``n`` valores, y
* imprimir el promedio de los cuadrados de los números.

Por ejemplo, si el usuario quiere calcular el promedio de los cuadrados
de 5, 1 y 9,
primero debe escribir ``3``,
y a continuación ``5``, ``1`` y ``9``.
Entonces, el programa imprimirá ``35.6666``,
que es el promedio de 25, 1 y 89.

Utilice el módulo que creó para el problema 1.

Plazo de entrega
----------------
Al final de la clase.

.. include:: disqus.rst

