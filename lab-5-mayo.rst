Laboratorio 5 de mayo
=======================
En esta sesión de laboratorio se evaluará:

* `funciones`_.

Además, hay que conocer muy bien toda la materia vista durante el semestre.

.. _funciones: funciones.html

Cómo resolver los problemas
---------------------------
El laboratorio debe ser resuelto usando el programa **PyScripter**.

Para resolver cada problema,
hay que crear un programa nuevo,
cuyo nombre debe ser ``nombre-apellido-pM.py``,
donde:

* ``nombre-apellido`` es el nombre del alumno,
* ``M`` es el número del problema.

Por ejemplo, cuando el alumno Perico Los Palotes
resuelva el problema 5,
el programa deberá llamarse
``perico-los-palotes-p5.py``.

Los problemas resueltos
deberán ser subidos a la `intranet académica`_
antes del término de la sesión.

.. _intranet académica: http://mensaje.santotomas.cl/

Problema 1: número par
----------------------
Cree una función ``par(x)``
que retorne ``True`` si ``x`` es par,
y ``False`` si es impar.

Pruébela en el intérprete interactivo::

    >>> par(16)
    True
    >>> par(29)
    False
    >>> par('hola')
    Traceback (most recent call last):
    TypeError: not all arguments converted during string formatting


Problema 2: factorial recíproco
-------------------------------
Usando la función ``factorial(n)``
presentada en la `sección anterior`_,
cree una función ``factorial_reciproco(n)``
que retorne el valor

.. math::

    \frac{1}{x!}.

.. _sección anterior: funciones.html

Pruébela en el intérprete interactivo::

    >>> factorial_reciproco(0)
    1.0
    >>> factorial_reciproco(2)
    0.5
    >>> factorial_reciproco(4)
    0.041666666666666664
    >>> factorial_reciproco(9)
    2.7557319223985893e-06

Luego, en el mismo programa,
cree una función ``suma_fr(k)``
que retorne la suma de los factoriales recíprocos
desde 1 hasta ``k``:

.. math::

    \frac{1}{0!} +
    \frac{1}{1!} +
    \frac{1}{2!} + \cdots +
    \frac{1}{k!}

Pruébela en el intérprete interactivo::

    >>> suma_fr(0)
    1.0
    >>> suma_fr(1)
    2.0
    >>> suma_fr(5)
    2.7166666666666663
    >>> suma_fr(21)
    2.7182818284590455

Problema 3: tríos pitagóricos
-----------------------------
Un trío pitagórico
se define como un conjunto de tres números
:math:`a`, :math:`b` y :math:`c`
que cumplen con la relación

.. math::

   a^2 + b^2 = c^2

Cree una función ``son_pitagoricos(a, b, c)``
que retorne ``True`` si ``a``, ``b`` y ``c``
son un trío pitagórico,
y ``False`` si no lo son::

    >>> son_pitagoricos(3, 4, 5)
    True
    >>> son_pitagoricos(4, 6, 9)
    False
    >>> son_pitagoricos(5, 12, 13)
    True

A continuación,
en el mismo programa
cree una función ``pitagoricos()``
(sin parámetros)
que imprima por pantalla
todos los tríos pitagóricos
con valores menores que 10::

    >>> pitagoricos()
    0 0 0
    0 1 1
    0 2 2
    0 3 3
    0 4 4
    0 5 5
    0 6 6
    0 7 7
    0 8 8
    0 9 9
    1 0 1
    2 0 2
    3 0 3
    3 4 5
    4 0 4
    4 3 5
    5 0 5
    6 0 6
    7 0 7
    8 0 8
    9 0 9

.. include:: disqus.rst

