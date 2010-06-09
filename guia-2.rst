Guía de ejercicios 2
====================

Estos ejercicios serán su preparación
para la prueba solemne 2
del miércoles 19 de mayo.

Mediana
-------
La `mediana`_ de un conjunto de ``n`` valores
es el valor para el que hay tantos elementos mayores como menores.

Por ejemplo,
la mediana de 6, 0, 3, 9, 4, 2 y 8 es el valor 4,
ya que tiene tres elementos mayores (6, 8 y 9)
y tres elementos menores (0, 2 y 3).

Escriba una función ``mediana(L)``
que entregue la mediana de los elementos de la lista ``L``.

Pruebe su función en el intérprete interactivo::

    >>> mediana([6, 1, 3, 9, 4, 2, 8])
    4
    >>> mediana([3.3, 3.6, 3.5])
    3.5
    >>> mediana([1000, 2000, 3000])
    2000
    >>> mediana([1000, 2000, 3000, 4000])
    3000

.. _mediana: http://es.wikipedia.org/wiki/Mediana_%28estad%C3%ADstica%29


Palíndromo
----------
Un `palíndromo`_ es una palabra que se lee igual
de adelante para atras y de atrás para adelante.

1. Escriba una función ``es_palindromo(palabra)``,
   que retorne ``True`` si ``palabra`` es palíndromo,
   o ``False`` si no lo es::

     >>> es_palindromo('perro')
     False
     >>> es_palindromo('rallar')
     True

.. _palíndromo: http://es.wikipedia.org/wiki/Pal%C3%ADndromo

2. Escriba una función ``es_palindromo(oracion)``,
   que haga lo mismo, pero omitiendo los espacios de la oración::

     >>> es_palindromo('anita lava la tina')
     True
     >>> es_palindromo('acaso hubo buhos aca')
     True


Eliminar repetidos
------------------
Escriba una función ``sin_repetidos(valores)``,
donde ``valores`` es una lista de valores,
que retorne una lista con los mismos valores,
pero sin elementos repetidos::

    >>> sin_repetidos([5, 3, 4, 2, 4, 4, 3, 1])
    [5, 3, 4, 2, 1]
    >>> sin_repetidos([])
    []
    >>> sin_repetidos(['casa', 'perro', 'casa'])
    ['casa', 'perro']


Campeonato de fútbol
--------------------
Escriba una función ``campeonato(equipos)``,
donde ``equipos`` es una lista de nombres de equipos de fútbol,
que haga lo siguiente:

* tomar los equipos de dos en dos,
  y pedirle al usuario que ingrese el resultado del partido entre ellos;
* retornar la lista de los equipos ganadores::

    >>> equipos = ['Unión Temuco', 'Unión La Calera', 'Curicó Unido',
    ...            'Municipal Iquique', 'Antofagasta', 'Concepción',
    ...            'Puerto Montt', 'Rangers']
    >>> ganadores = campeonato(equipos)
    ... # Aquí el programa debe preguntar los resultados
    >>> ganadores
    ['Unión La Calera', 'Curicó Unido', 'Concepción', 'Puerto Montt']

Puede usar ``input()`` adentro de la función.


Distancias
----------
La siguiente tabla
indica las distancias entre algunas ciudades chilenas:

  ============= ========== ========== ========== ============ ==========
  **Distancia** Arica      Santiago   Valparaíso San Fernando Temuco
  Arica                  0       2050       2015         2190       2725
  Santiago            2050          0        119          140        675
  Valparaíso          2015        119          0          255        790
  San Fernando        2190        140        255            0        535
  Temuco              2725        675        790          535          0
  ============= ========== ========== ========== ============ ==========

En un programa,
esta información puede representarse
como una lista de ciudades y una lista de listas de distancias::

    >>> ciudades = ['Arica', 'Santiago', 'Valparaiso',
    ...             'San Fernando', 'Temuco']
    >>> distancias = [[   0, 2050, 2015, 2190, 2725],
    ...               [2050,    0,  119,  140,  675],
    ...               [2015,  119,    0,  255,  790],
    ...               [2190,  140,  255,    0,  535],
    ...               [2725,  675,  790,  535,    0]]

Por ejemplo,
la distancia entre Valparaíso y San Fernando
puede ser obtenida así::

    >>> distancias[2][3]
    255

Escriba una función ``kms(itinerario)``,
donde ``itinerario`` es una lista de ciudades,
que retorne los kilómetros que hay que recorrer
para visitar esas ciudades en orden::

    >>> kms(['Temuco', 'Santiago', 'San Fernando', 'Arica'])
    3005

Total de la compra
------------------
Escriba una función ``total(precios, cantidades)``,
donde ``precios`` es una lista de precios de productos,
y ``cantidades`` es una lista de las cantidades
que se comprará de cada producto.
La función debe calcular el total de la compra::

    >>> p = [2500, 10000, 3250]
    >>> c = [5, 1, 2]
    >>> total(p, c)
    29000


Control de asistencia
---------------------
La asistencia de los alumnos a clases
puede ser llevada en una tabla como la siguiente:

  ============== = = = = = = =
  **Asistencia** 1 2 3 4 5 6 7
  -------------- - - - - - - -
  Pepito         ✓ ✓ ✓        
  Yayita         ✓ ✓ ✓   ✓   ✓
  Fulanita       ✓ ✓ ✓ ✓ ✓ ✓ ✓
  Panchito       ✓ ✓ ✓   ✓ ✓ ✓
  ============== = = = = = = =

En un programa,
esta información puede ser representada
usando listas::

    >>> alumnos = ['Pepito', 'Yayita', 'Fulanita', 'Panchito']
    >>> asistencia = [
    ...     [True,  True,  True,  False, False, False, False],
    ...     [True,  True,  True,  False, True,  False, True ],
    ...     [True,  True,  True,  True,  True,  True,  True ],
    ...     [True,  True,  True,  False, True,  True,  True ]]

Por ejemplo, para saber si Panchito asistió a la cuarta clase,
puede hacerse de la siguiente manera::

    >>> i = alumnos.index('Panchito')
    >>> clase = 4
    >>> asistencia[i][clase - 1]
    False

1. Escriba una función ``porcentaje_asistencia(alumno)``
   que retorne el porcentaje de asistencia de un alumno::

     >>> porcentaje_asistencia('Fulanita')
     100.0
     >>> porcentaje_asistencia('Pepito')
     42.857142857142854

2. Escriba una función ``asistencia_clase(n)``
   que retorne el porcentaje de asistencia
   de la clase número ``n``::

     >>> asistencia_clase(1)
     100.0
     >>> asistencia_clase(4)
     25.0

3. Escriba una función ``alumno_ejemplar()``,
   que retorne el alumno que tiene mejor asistencia::

     >>> alumno_ejemplar()
     'Fulanita'


Evaluación de polinomios
------------------------
Un `polinomio`_ es una función matemática
de la forma:

.. math::

   p(x) = a_0 + a_1 x + a_2 x^2 + a_3 x^3 +
          \cdots + a_n x^n,

donde :math:`x` es el parámetro
y :math:`a_0, a_1, \dots, a_n`
son números reales dados.

.. _polinomio: http://es.wikipedia.org/wiki/Polinomio

Algunos ejemplos de polinomios son:

* :math:`p(x) = 1 + 2x + x^2`,
* :math:`q(x) = 4 - 17x`,
* :math:`r(x) = -1 - 5x^3 + 3x^5`,
* :math:`s(x) = 5x^{40} + 2x^{80}`.

Evaluar un polinomio
significa reemplazar :math:`x` por un valor
y obtener el resultado.
Por ejemplo, si evaluamos el polinomio :math:`p`
en el valor :math:`x = 3`,
obtenemos el resultado:

.. math::
   
   p(3) = 1 + 2\cdot 3 + 3^2 = 16

Un polinomio puede ser representado
como una lista de los valores :math:`a_0, a_1, \dots, a_n`.
Por ejemplo,
los polinomios anteriores
pueden ser representados así
en un programa::

    >>> p = [1, 2, 1]
    >>> q = [4, -17]
    >>> r = [-1, 0, -5, 0, 3]
    >>> s = [0] * 40 + [5] + [0] * 39 + [2]

Escriba una función ``evaluar(p, x)``
que evalúe el polinomio ``p``
(representado como una lista)
en el valor ``x``::

    >>> evaluar(p, 3)
    16
    >>> evaluar(q, 0.0)
    4.0
    >>> evaluar(r, 1.1)
    -2.82347
    >>> evaluar([4, 3, 1], 3.14)
    23.2796

.. Triángulo de Pascal
.. -------------------
.. El `triángulo de Pascal`_
.. es una
.. 
.. 
.. .. verbatim::
.. 
..               1
..             1   1
..           1   2   1
..         1   3   3   1
..       1   4   6   4   1
..     1   5  10   10  5   1
.. 
.. .. _triángulo de Pascal: http://es.wikipedia.org/wiki/Tri%C3%A1ngulo_de_Pascal

.. include:: disqus.rst

