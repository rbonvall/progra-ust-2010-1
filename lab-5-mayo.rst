Laboratorio 5 de mayo
=======================
En esta sesión de laboratorio se evaluará:

* funciones.


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
que retorne ``True`` si el argumento ``x`` es par,
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
Cree una función ``factorial(n)``,
cuyo argumento ``n`` sea un número entero,
que retorne el valor :math:`n!`
(el factorial de ``n``).

A continuación, en el mismo programa,
cree una función ``factorial_reciproco(n)``,
que retorne el valor

.. math::

    \frac{1}{x!}.

Pruebe sus funciones en el intérprete interactivo::

    >>> factorial(5)
    120
    >>> factorial(0)
    1
    >>> factorial(20)
    2432902008176640000
    >>> factorial_reciproco(0)
    1.0
    >>> factorial_reciproco(2)
    0.5
    >>> factorial_reciproco(4)
    0.041666666666666664
    >>> factorial_reciproco(9)
    2.7557319223985893e-06

.. include:: disqus.rst

