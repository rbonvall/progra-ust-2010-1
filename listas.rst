Listas
======
.. index:: lista

Una **lista** es una colección ordenada de valores.

En Python, el tipo de datos que representa a las listas
se llama ``list``.

Cómo crear listas
-----------------
Las dos maneras principales de crear una lista son:

* usar una lista literal, con los valores entre corchetes::

    >>> ['hola ' + 'mundo', 24 * 7, True or False]
    ['hola mundo', 168, True]
    >>> primos = [2, 3, 5, 7, 11]
    >>> primos
    [2, 3, 5, 7, 11]
    >>> []
    []

* usar la función ``list`` aplicada sobre un iterable::

    >>> list('hola')
    ['h', 'o', 'l', 'a']
    >>> list(range(10))
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> list()
    []

Operaciones sobre listas
------------------------

* ``len(l)`` entrega el largo de la lista;
  es decir, cuántos elementos tiene::

    >>> colores = ['azul', 'rojo', 'verde', 'amarillo']
    >>> len(colores)
    4
    >>> len([True, True, True])
    3
    >>> len([])
    0

* ``l[i]`` entrega el ``i``-ésimo valor de la lista.
  El valor ``i`` se llama **índice** del valor.
  Hay que tener cuidado ya que se empieza a contar desde 0,
  y no desde 1::

    >>> colores = ['azul', 'rojo', 'verde', 'amarillo']
    >>> colores[0]
    'azul'
    >>> colores[3]
    'amarillo'

  Si el índice ``i`` indica un elemento que no está en la lista,
  ocurre un **error de índice**::

    >>> colores[4]
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    IndexError: list index out of range

  Si el índice es negativo,
  los elementos se cuentan desde el final hacia atrás::

    >>> colores[-1]
    'amarillo'
    >>> colores[-4]
    'azul'

* ``l.append(x)`` agrega el elemento ``x`` al final de la lista::

    >>> primos = [2, 3, 5, 7, 11]
    >>> primos.append(13)
    >>> primos.append(17)
    >>> primos
    [2, 3, 5, 7, 11, 13, 17]

* ``sum(x)`` entrega la suma de los valores de la lista::

    >>> sum([1, 2, 1, -1, -2])
    1
    >>> sum([])
    0

* ``l1 + l2`` concatena las listas ``l1`` y ``l2``::

    >>> list('perro') + [2, 3, 4]
    ['p', 'e', 'r', 'r', 'o', 2, 3, 4]

* ``l * n`` repite ``n`` veces la lista ``l``::

    >>> [3.14, 6.28, 9.42] * 2
    [3.14, 6.28, 9.42, 3.14, 6.28, 9.42]
    >>> [3.14, 6.28, 9.42] * 0
    []

* ``x in l`` permite saber si el elemento ``x`` está o no en la lista::

    >>> r = list(range(0, 20, 2))
    >>> r
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
    >>> 12 in r
    True
    >>> 15 in r
    False

* ``l[i:j]`` permite obtener una rebanada de la lista,
  desde el elemento de índice ``i``
  hasta el de índice ``j``::

    >>> x = [1.5, 3.3, 8.4, 3.1, 2.9]
    >>> x[2:4]
    [8.4, 3.1]

* ``l.count(x)`` cuenta cuántas veces está
  el elemento ``x`` en la lista::

    >>> list('paralelepipedo').count('p')
    3

* ``l.index(x)`` entrega cuál es el índice del valor ``x``::

    >>> colores = ['azul', 'rojo', 'verde', 'amarillo']
    >>> colores.index('verde')
    2
    >>> colores.index('fucsia')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: 'fucsia' is not in list

* ``l.remove(x)`` elimina el elemento ``x`` de la lista.
* ``l.reverse()`` invierte la lista.
* ``l.sort()`` ordena la lista.


Tarea 2
-------
.. index:: tarea 2

**La tarea 2 debe ser entregada en la clase del viernes 14 de mayo.**

Escribir una función llamada ``desviacion_estandar(valores)``
cuyo parámetro ``valores`` sea una lista de números reales.

La función debe retornar
la `desviación estándar`_ de los valores:

.. math::

   DE = \sqrt{\sum_i (x_i - m)^2/n}

.. _desviación estándar: http://es.wikipedia.org/wiki/Desviaci%C3%B3n_est%C3%A1ndar

donde :math:`n` es la cantidad de valores,
:math:`m` es el promedio de los valores, y
:math:`x_i` es cada uno de los valores.

Esto significa que hay que hacerlo siguiendo estos pasos:

* calcular el promedio de los valores;
* a cada valor hay que restarle el promedio, y el resultado elevarlo al cuadrado;
* sumar todos los valores obtenidos;
* dividir la suma por la cantidad de valores; y
* sacar la raíz cuadrada (o elevar a :math:`0.5`) del resultado.

Puede probar su función en el intérprete interactivo::

    >>> desviacion_estandar([1.3, 1.3, 1.3])
    0.0
    >>> desviacion_estandar([4.0, 1.0, 11.0, 13.0, 2.0, 7.0])
    4.459696053419884
    >>> desviacion_estandar([1.5, 9.5])
    4.0

.. include:: disqus.rst

