Expresiones
===========
.. index:: literal, variable, operador, llamada a función, expresión

Como vimos anteriormente,
una **expresión** es una combinación de valores y operaciones
que al ser evaluados entregan un valor.

Algunos elementos que pueden formar parte de una expresión son:
valores **literales** (como ``2``, ``5.7`` u ``"hola"``),
**variables**, **operadores** y **llamadas a funciones**.

Por ejemplo,
la siguiente expresión entrega el valor 10 al ser evaluada::

    4 * 3 - 2

El valor de la siguiente expresión
depende del valor que tiene la variable ``n``
en el momento de la evaluación::

    n / 7 + 5

Operadores
----------
.. index:: operador, operador unario, operador binario, operando

Un **operador** es un símbolo en una expresión
que representa una operación aplicada a los valores sobre los que actúa.

Los valores sobre los que actúa un operador se llaman **operandos**.
Un **operador binario** es el que tiene dos operandos, mientras que
un **operador unario** es el que tiene sólo uno.

Por ejemplo,
en la expresión ``2.0 + x``
el operador ``+`` es un operador binario que representa la suma,
y sus operandos son ``2.0`` y ``x``.

Los principales operadores se pueden clasificar en:
lógicos, aritméticos y relacionales.
Hay otros más que veremos más adelante.

Operadores lógicos
~~~~~~~~~~~~~~~~~~
.. index:: operador lógico, operador booleano

Los **operadores lógicos** son los que tienen valores lógicos
(verdadero y falso) como operandos y como resultado.
Los valores lógicos posibles son
``True`` (verdadero) y ``False`` (falso).

Hay tres operadores lógicos:

.. index:: and, or, not

* **and** (en español: «y») representa la conjunción lógica;
* **or** (en español: «o») representa la disyunción lógica.
* **not** (en español: «negación») representa la negación lógica.

Los operadores ``and`` y ``or`` son binarios,
mientras que ``not`` es unario.

La siguiente tabla muestra todos los resultados posibles
de las operaciones lógicas.
Las primeras dos columnas representan los valores de los operandos,
y las siguientes tres, los resultados de las operaciones.

========= ========= =========== ========== =========
``p``     ``q``     ``p and q`` ``p or q`` ``not p``
--------- --------- ----------- ---------- ---------
``True``  ``True``  ``True``    ``True``   ``False``
``True``  ``False`` ``False``   ``True``
``False`` ``True``  ``False``   ``True``   ``True``
``False`` ``False`` ``False``   ``False``
========= ========= =========== ========== =========


Operadores aritméticos
~~~~~~~~~~~~~~~~~~~~~~
.. index:: operador aritmético


Operadores relacionales
~~~~~~~~~~~~~~~~~~~~~~~
.. index:: operador relacional




Precedencia
-----------
.. index:: precedencia de operadores

* ``or``
* ``and``
* ``not``
* ``in``, ``not in``, ``<``, ``<=``, ``>``, ``>=``, ``!=``, ``==``
* ``+``, ``-`` (suma y resta)
* ``*``, ``/``, ``//``, ``%``
* ``+``, ``-`` (positivo y negativo)
* ``**``


