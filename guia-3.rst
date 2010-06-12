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

(más adelante subiré más ejercicios)

.. include:: disqus.rst

