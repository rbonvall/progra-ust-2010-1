Guía de ejercicios 3
====================

Estos ejercicios serán su preparación
para la prueba solemne 3
del viernes 18 de junio.

Palabras repetidas
------------------
Escriba una función ``palabras_repetidas(oracion)``
que reciba como parámetro una oración
y que retorne una lista con las palabras
que están repetidas::

    >>> palabras_repetidas('El partido terminó cero a cero')
    ['cero']
    >>> palabras_repetidas('El sobre está sobre el mueble')
    ['el', 'sobre']
    >>> palabras_repetidas('Ay, ahí no hay pan')
    []

Iguales o distintos
-------------------
Escriba una función ``todos_iguales(lista)``
que indique si todos los elementos de una lista son iguales::

    >>> todos_iguales([6, 6, 6])
    True
    >>> todos_iguales([6, 6, 1])
    False
    >>> todos_iguales([0, 90, 1])
    False

A continuación, escriba una función ``todos_distintos(lista)``
que indique si todos los elementos de una lista son distintos::

    >>> todos_distintos([6, 6, 6])
    False
    >>> todos_distintos([6, 6, 1])
    False
    >>> todos_distintos([0, 90, 1])
    True

Sus funciones deben funcionar para listas de cualquier tamaño::

    >>> todos_iguales([7, 7, 7, 7, 7, 7, 7, 7, 7])
    True
    >>> todos_distintos(list(range(1000)))
    True
    >>> todos_iguales([12])
    True

Póker
-----
En los juegos de naipes,
una carta tiene dos atributos:
un valor (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K)
y una pinta (♥, ♦, ♣, ♠).

En un programa,
el valor puede ser representado como un número
del 1 al 13,
y la pinta como un string:
♥ → ``'C'``,
♦ → ``'D'``,
♣ → ``'T'`` y
♠ → ``'P'``.

Una carta puede ser representada
como una tupla de dos elementos:
el valor y la pinta::

    carta1 = (5, 'T')
    carta2 = (10, 'D')

Para simplificar,
se puede representar el as como un 1,
y los «monos» J, Q y K como 11, 12 y 13::

    # as de picas y reina de corazones
    carta3 = (1, 'P')
    carta4 = (12, 'C')

En el juego de póker,
una mano tiene cinco cartas.
Esto sería un conjunto de cinco tuplas::

    mano = {(1, 'P'), (1, 'C'), (1, 'T'), (13, 'D'), (12, 'P')}

**Ejercicio 1:** en el póker,
un *full* es una mano en que tres cartas tienen un valor común,
y las otras dos tienen otro valor común.
Escriba una función que indique
si la mano es un full::

    >>> mano_1 = {(1, 'P'), (1, 'C'), (6, 'T'), (1, 'D'), (6, 'D')}
    >>> mano_2 = {(2, 'T'), (1, 'C'), (12, 'C'), (1, 'D'), (6, 'D')}
    >>> full(mano_1)
    True
    >>> full(mano_2)
    False

**Ejercicio 2:**
un *color* es una mano en que todas las cartas tienen la misma pinta.
Escriba una función que indique
si la mano es un color::

    >>> mano_1 = {(8, 'P'), (13, 'P'), (4, 'P'), (9, 'P'), (2, 'P')}
    >>> mano_2 = {(12, 'T'), (1, 'C'), (5, 'C'), (2, 'C'), (2, 'D')}
    >>> color(mano_1)
    True
    >>> color(mano_2)
    False

**Ejercicio 3:**
una *escalera* es una mano en que las cartas tienen valores consecutivos
(por ejemplo: 5, 6, 7, 8 y 9).
Escriba una función que indique
si la mano es una escalera::

    >>> mano_1 = {(4, 'P'), (7, 'C'), (3, 'C'), (6, 'T'), (5, 'T')}
    >>> mano_2 = {(12, 'T'), (7, 'C'), (3, 'C'), (12, 'C'), (5, 'T')}
    >>> escalera(mano_1)
    True
    >>> escalera(mano_2)
    False

Recorrido de diccionarios
-------------------------
**Ejercicio 1:**
escriba una función ``hay_llaves_pares(d)``
que indique si el diccionario ``d`` tiene alguna llave
que sea un número par.

A continuación, escriba una función ``hay_valores_pares(d)``
que indique si el diccionario ``d`` tiene algún valor
que sea un número par.

Para probar las funciones, ocupe diccionarios
cuyas llaves y valores sean sólo números enteros::

    >>> d1 = {1: 2, 3: 5}
    >>> d2 = {2: 1, 6: 7}
    >>> hay_valores_pares(d1)
    True
    >>> hay_valores_pares(d2)
    False
    >>> hay_llaves_pares(d1)
    False
    >>> hay_llaves_pares(d2)
    True

**Ejercicio 2:**
escriba una función ``maximo_par(d)``
que entregue el valor máximo
de la suma de una llave y un valor
del diccionario ``d``::

    >>> d = {5: 1, 4: 7, 9: 0, 2: 2}
    >>> maximo_par(d)
    11

**Ejercicio 3:**
escriba una función ``invertir(d)``
que entregue un diccionario
cuyas llaves sean los valores de ``d``
y cuyos valores sean las llaves respectivas::

    >>> invertir({1: 2, 3: 4, 5: 6})
    {2: 1, 4: 3, 6: 5}
    >>> apodos = {
    ...   'Suazo': 'Chupete',
    ...   'Sanchez': 'Maravilla',
    ...   'Medel': 'Pitbull',
    ...   'Valdivia': 'Mago',
    ... }
    >>> invertir(apodos)
    {'Maravilla': 'Sanchez', 'Mago': 'Valdivia', 'Chupete': 'Suazo', 'Pitbull': 'Medel'}

Subconjuntos
------------
Escriba una función ``subconjuntos(s)``
que entregue una lista de todos los subconjuntos posibles
del conjunto ``s``::

    >>> s = {4, 7, 8}
    >>> subconjuntos(s)
    [{}, {4}, {7}, {8}, {4, 7}, {8, 4}, {8, 7}, {8, 4, 7}]

Partidos
--------
Un partido de fútbol entre dos equipos
puede ser representado como una tupla de dos equipos::

    >>> partido = ('Chile', 'España')

El resultado del partido
puede ser representado como una tupla con los goles
marcados por cada equipo::

    >>> resultado = (4, 1)

Todos los partidos de un campeonato
pueden ser representados como un diccionario
que asocia a cada partido un resultado::

    >>> campeonato = {
    ...     ('Honduras', 'Chile'):    (1, 4),
    ...     ('España',   'Suiza'):    (1, 1),
    ...     ('Chile',    'Suiza'):    (2, 0),
    ...     ('España',   'Honduras'): (1, 0),
    ...     ('Chile',    'España'):   (5, 5),
    ...     ('Suiza',    'Honduras'): (1, 2);
    ... }

**Ejercicio 1:**
escriba una función ``equipos(campeonato)``
que entregue el conjunto de los equipos
que participaron del campeonato::

    >>> equipos(campeonato)
    {'Chile', 'Honduras', 'Suiza', 'España'}

**Ejercicio 2:**
escriba una función ``nro_empates(campeonato)``
que cuente cuántos partidos del campeonato
terminaron en empate::

    >>> nro_empates(campeonato)
    1

**Ejercicio 3:**
cuando un equipo gana un partido, recibe 3 puntos;
cuando empata, recibe 1 puntos, y cuando pierde, 0.
Escriba una función ``puntos(equipo, campeonato)``
que entregue cuántos puntos obtuvo el equipo
en el campeonato::

    >>> puntos('Chile', campeonato)
    7
    >>> puntos('Honduras', campeonato)
    3

**Ejercicio 4:**
la *diferencia de goles* de un equipo
es la suma de los goles que hizo
menos la suma de los goles que le hicieron.
Escriba una función ``dg(equipo, campeonato)``
que entregue la diferencia de goles
del equipo en el campeonato::


    >>> dg('Chile', campeonato)
    5
    >>> dg('Honduras', campeonato)
    -3

**Ejercicio 5:**
escriba una función ``mejor_partido(campeonato)``
que entregue cuál fue el partido con más goles::

    >>> mejor_partido(campeonato)
    ('Chile', 'España')

Cumpleaños
----------
Las fechas pueden ser representadas
como tuplas ``(año, mes, dia)``.

Para asociar a cada persona su fecha de nacimiento,
se puede usar un diccionario::

    >>> n = {
    ...     'Pepito': (1990, 10, 20),
    ...     'Yayita': (1992, 3, 3),
    ...     'Panchito': (1989, 10, 20),
    ...     'Perica': (1989, 12, 8),
    ...     'Fulanita': (1991, 2, 14),
    ... }

**Ejercicio 1:**
escriba una función ``mismo_dia(fecha1, fecha2)``
que indique si las dos fechas ocurren el mismo día del año
(aunque sea en años diferentes)::

    >>> mismo_dia((2010, 6, 11), (1990, 6, 11))
    True
    >>> mismo_dia((1981, 8, 12), (1981, 5, 12))
    False

**Ejercicio 2:**
escriba una función ``mas_viejo(n)``
que indique quién es la persona más vieja
según las fechas de nacimiento del diccionario ``n``::

    >>> mas_viejo(n)
    'Panchito'

**Ejercicio 3:**
escriba una función ``primer_cumple(n)``
que indique quién es la persona
que tiene el primer cumpleaños del año::

    >>> primer_cumple(n)
    'Fulanita'

Rectas
------
Una recta en el plano está descrita por la ecuación:

.. math::

    y = mx + b,

donde :math:`m` es la *pendiente*
y :math:`b` es el *intercepto*.
Todos los puntos de la recta
satisfacen esta ecuación.

En un programa,
una recta puede ser representada
como una tupla ``(m, b)``.

Los algoritmos para resolver los siguientes ejercicios
seguramente usted los aprendió en el colegio.
Si no los recuerda,
puede buscarlos en su libro de matemáticas favorito
o en internet.

**Ejercicio 1**:
escriba una función ``punto_en_recta(p, r)``
que indique si el punto ``p`` está en la recta ``r``::

    >>> recta = (2, -1)
    >>> punto_en_recta((2, 3), recta)
    True
    >>> punto_en_recta((0, -1), recta)
    True
    >>> punto_en_recta((1, 2), recta)
    False

**Ejercicio 2**:
escriba una función ``son_paralelas(r1, r2)``
que indique si las rectas ``r1`` y ``r2`` son paralelas,
es decir, no se intersectan en ningún punto.

**Ejercicio 3**:
escriba una función ``recta_que_pasa_por(p1, p2)``
que entregue la recta que pasa por los puntos ``p1`` y ``p2``::

    >>> recta_que_pasa_por((-2, 4), (4, 1))
    (-0.5, 3.0)

Puede comprobar que la función está correcta
verificando que ambos puntos están en la recta obtenida::

    >>> p1 = (-2, 4)
    >>> p2 = (4, 1)
    >>> r = recta_que_pasa_por(p1, p2)
    >>> punto_en_recta(p1, r)
    True
    >>> punto_en_recta(p2, r)
    True

**Ejercicio 4**:
escriba una función ``punto_de_interseccion(r1, r2)``
que entregue el punto donde las dos rectas se `intersectan`_::

    >>> r1 = (2, 1)
    >>> r2 = (-1, 4)
    >>> punto_de_interseccion(r1, r2)
    (1.0, 3.0)

.. _intersectan: http://www.mieres.uniovi.es/egi/dao/apuntes/planos_y_coordenadas.html

Compatibilidad entre personas
-----------------------------
Para este problema,
consideraremos las siguientes características de una persona:

* nombre,
* género (masculino o femenino),
* edad,
* música favorita, y
* signo zodiacal.

En el programa a realizar,
una persona será representada como una tupla::

  persona_1 = ('Pepito', 'M', 27, 'rock', 'leo')
  persona_2 = ('Yayita', 'F', 23, 'cumbia', 'virgo')

Dos personas son compatibles
si:

* son de géneros opuestos (un hombre y una mujer),
* tienen menos de diez años de diferencia,
* les gusta la misma música, y
* sus signos zodiacales son compatibles.

Para saber los signos compatibles,
existe un conjunto ``signos_compatibles``
que tiene tuplas ``(signo_mujer, signo_hombre)``,
que `usted puede descargar aquí`_.
Si una tupla está en el conjunto,
significa que los signos son compatibles::

    >>> ('aries', 'tauro') in signos_compatibles
    True

    # Significa que mujer aries
    # es compatible con hombre tauro.

    >>> ('capricornio', 'libra') in signos_compatibles
    False

    # Significa que mujer capricornio
    # no es compatible con hombre libra.

Escriba una función ``compatibles(p1, p2)``
que indique si dos personas son compatibles o no.

.. _usted puede descargar aquí: _static/signos.py

(más adelante iré subiendo más problemas)

.. include:: disqus.rst

