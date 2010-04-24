Ejercicios de la clase del 23 de abril
======================================
Estos son los ejercicios que hicimos en clases.
Les recomiendo estudiarlos bien,
probarlos en el computador
y comprobar que funcionan correctamente.

Ruteo 1
-------
Considere el siguiente programa.

.. literalinclude:: programas/ruteo-espuma.py
   :linenos:

1. Rutear el programa con la entrada
   ``a`` = 5, ``b`` = 1, ``c`` = 4.
2. Rutear el programa con la entrada
   ``a`` = 4, ``b`` = 5, ``c`` = 1.
3. Deducir qué hace el programa.

Solución
~~~~~~~~
Primer ruteo:

    +-----+-----+-----+-----+---------+
    |``a``|``b``|``c``|``t``|Salida   |
    +=====+=====+=====+=====+=========+
    |   5 |   1 |   4 |     |         |
    +-----+-----+-----+-----+---------+
    |     |     |     |   5 |         |
    +-----+-----+-----+-----+---------+
    |     |   1 |     |     |         |
    +-----+-----+-----+-----+---------+
    |     |     |   4 |     |         |
    +-----+-----+-----+-----+---------+
    |     |     |     |   6 |         |
    +-----+-----+-----+-----+---------+
    |   1 |     |     |     |         |
    +-----+-----+-----+-----+---------+
    |     |   5 |     |     |         |
    +-----+-----+-----+-----+---------+
    |     |     |     |   9 |         |
    +-----+-----+-----+-----+---------+
    |     |   4 |     |     |         |
    +-----+-----+-----+-----+---------+
    |     |     |   5 |     |         |
    +-----+-----+-----+-----+---------+
    |     |     |     |     |``1 4 5``|
    +-----+-----+-----+-----+---------+

Segundo ruteo:

    +-----+-----+-----+-----+---------+
    |``a``|``b``|``c``|``t``|Salida   |
    +=====+=====+=====+=====+=========+
    |   4 |   5 |   1 |     |         |
    +-----+-----+-----+-----+---------+
    |     |     |     |   6 |         |
    +-----+-----+-----+-----+---------+
    |     |   1 |     |     |         |
    +-----+-----+-----+-----+---------+
    |     |     |   5 |     |         |
    +-----+-----+-----+-----+---------+
    |     |     |     |   5 |         |
    +-----+-----+-----+-----+---------+
    |   1 |     |     |     |         |
    +-----+-----+-----+-----+---------+
    |     |   4 |     |     |         |
    +-----+-----+-----+-----+---------+
    |     |     |     |   9 |         |
    +-----+-----+-----+-----+---------+
    |     |   4 |     |     |         |
    +-----+-----+-----+-----+---------+
    |     |     |   5 |     |         |
    +-----+-----+-----+-----+---------+
    |     |     |     |     |``1 4 5``|
    +-----+-----+-----+-----+---------+

Lo que hace el programa es
ordenar los valores de ``a``, ``b`` y ``c``
de menor a mayor.

Ruteo 2
-------
Considere el siguiente programa.

.. literalinclude:: programas/ruteo-potencia.py
   :linenos:

1. Rutear el programa con la entrada
   ``a`` = 4, ``b`` = 3.
2. Deducir qué hace el programa.

Solución
~~~~~~~~

    +-----+-----+-----+--------+
    |``a``|``b``|``p``| Salida |
    +=====+=====+=====+========+
    |   4 |   3 |     |        |
    +-----+-----+-----+--------+
    |     |     |   1 |        |
    +-----+-----+-----+--------+
    |     |     |   3 |        |
    +-----+-----+-----+--------+
    |   3 |     |     |        |
    +-----+-----+-----+--------+
    |     |     |   9 |        |
    +-----+-----+-----+--------+
    |   2 |     |     |        |
    +-----+-----+-----+--------+
    |     |     |  27 |        |
    +-----+-----+-----+--------+
    |   1 |     |     |        |
    +-----+-----+-----+--------+
    |     |     |  81 |        |
    +-----+-----+-----+--------+
    |   0 |     |     |        |
    +-----+-----+-----+--------+
    |     |     |     | ``81`` |
    +-----+-----+-----+--------+

El programa entrega :math:`b^a`.



Tabla de verdad
---------------
Escribir un programa que muestre por pantalla
la tabla de verdad del predicado lógico
:math:`(\bar p\land q)\lor\bar r`.

Solución
~~~~~~~~
Hay que usar un ciclo ``for`` por cada variable
para darle a cada una primero el valor ``True``
y luego el valor ``False``:

.. literalinclude:: programas/tabla-verdad.py
   :linenos:

Números combinatorios
---------------------
El número combinatorio :math:`n` sobre :math:`k`
se define como:

.. math::

    \left(n\over k\right) = \frac{
        n\cdot(n - 1)\cdot(n - 2)\cdots(n - k + 1)
    }{
        1\cdot 2\cdot 3\cdots k
    }

Escribir un programa cuya entrada sean ``n`` y ``k``,
y que su salida sea el número combinatorio ``n`` sobre  ``k``.

Solución
~~~~~~~~
Como vimos en clases, hay varias maneras de resolver este ejercicio.

Una de ellas es calcular primero el denominador,
luego el numerador y al final hacer la división:

.. literalinclude:: programas/comb-1.py
   :linenos:

La segunda manera es primero hacer las multiplicaciones
y luego las divisiones, 
y llevar los resultados parciales
en una única variable ``resultado``:

.. literalinclude:: programas/comb-2.py
   :linenos:

Otra manera más corta es hacer juntas una multiplicación y una división
en cada iteración:

.. literalinclude:: programas/comb-3.py
   :linenos:

¡Estudien bien cómo funcionan los rangos!

Computador adivinador
---------------------
Hacer un programa que adivina el número que el usuario ha pensado.
El número está entre 0 y 100.
Cada vez que el programa intenta adivinar el número,
el usuario debe responder:

* ``=``, si el número entregado por el computador es el número pensado;
* ``<``, si el número pensado es menor al entregado;
* ``>``, si el número pensado es mayor al entregado.

Solución
~~~~~~~~
La estrategia para resolver este problema
consiste en recordar siempre
cuáles son los valores mínimo y máximo
que puede tener el número pensado,
de acuerdo a la información entregada por el usuario.

En cada intento de adivinar,
el computador entrega el promedio entre el mínimo y el máximo.
Si el número es menor, de inmediato quedan descartados
los números mayores que el promedio, y viceversa.

El programa queda así:

.. literalinclude:: programas/adivina.py
   :linenos:

A diferencia del programa que hicimos en clases,
aquí usamos una variable booleana ``adivinado``
que indica si el computador ya adivinó el número o no.
El ciclo se hace mientras el número no haya sido adivinado.
Cuando el computador acierta,
``adivinado`` cambia a ``True``
y el ciclo termina.

Como ejemplo,
podemos jugar usando el número 82.
Si no hacemos trampa,
el ruteo sería el siguiente:

    +----------+----------+------------+-------------+-------------+
    |``minimo``|``maximo``|``promedio``|``respuesta``|``adivinado``|
    +==========+==========+============+=============+=============+
    |        0 |      100 |            |             |   ``False`` |
    +----------+----------+------------+-------------+-------------+
    |          |          |         50 |             |             |
    +----------+----------+------------+-------------+-------------+
    |          |          |            |     ``'>'`` |             |
    +----------+----------+------------+-------------+-------------+
    |       51 |          |            |             |             |
    +----------+----------+------------+-------------+-------------+
    |          |          |         75 |             |             |
    +----------+----------+------------+-------------+-------------+
    |          |          |            |     ``'>'`` |             |
    +----------+----------+------------+-------------+-------------+
    |       76 |          |            |             |             |
    +----------+----------+------------+-------------+-------------+
    |          |          |         88 |             |             |
    +----------+----------+------------+-------------+-------------+
    |          |          |            |     ``'<'`` |             |
    +----------+----------+------------+-------------+-------------+
    |          |       87 |            |             |             |
    +----------+----------+------------+-------------+-------------+
    |          |          |         81 |             |             |
    +----------+----------+------------+-------------+-------------+
    |          |          |            |     ``'>'`` |             |
    +----------+----------+------------+-------------+-------------+
    |       82 |          |            |             |             |
    +----------+----------+------------+-------------+-------------+
    |          |          |         84 |             |             |
    +----------+----------+------------+-------------+-------------+
    |          |          |            |     ``'<'`` |             |
    +----------+----------+------------+-------------+-------------+
    |          |       83 |            |             |             |
    +----------+----------+------------+-------------+-------------+
    |          |          |         82 |             |             |
    +----------+----------+------------+-------------+-------------+
    |          |          |            |     ``'='`` |             |
    +----------+----------+------------+-------------+-------------+
    |          |          |            |             |    ``True`` |
    +----------+----------+------------+-------------+-------------+


.. include:: disqus.rst

