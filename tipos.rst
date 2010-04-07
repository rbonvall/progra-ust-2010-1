Tipos de datos
==============

.. index:: tipo de datos

Un **tipo de datos** es una propiedad de un valor
que determina su dominio (qué valores puede tomar),
qué operaciones se le pueden aplicar
y cómo es representado internamente por el computador.

A continuación revisaremos los tipos de datos más usados.
Además de estos, existen muchos otros,
y más adelante aprenderemos a crear
nuestros propios tipos de datos.

Números enteros
---------------
.. index:: número entero, int

El tipo ``int`` permite representar números enteros.

Los valores que puede tomar un ``int`` son
todos los números enteros:
``... -3, -2, -1, 0, 1, 2, 3, ...``.

El nombre ``int`` viene del inglés *integer*,
que significa «entero».

Todas las operaciones aritméticas y relacionales
pueden ser aplicadas sobre valores del tipo ``int``.

Los números enteros literales
se escriben con un signo opcional
seguido por una secuencia de dígitos::

    1570
    +4591
    -12

Números reales
--------------
.. index:: número real, número de punto flotante, float

El tipo ``float`` permite representar números reales.

El nombre ``float`` viene del término `punto flotante`_,
que es la manera en que el computador representa internamente
los números reales.

.. _punto flotante: http://es.wikipedia.org/wiki/Punto_flotante

Todas las operaciones aritméticas y relacionales
pueden ser aplicadas sobre valores del tipo ``float``.

Cuando se combinan valores reales y enteros en una operación,
el entero es convertido a un número real antes de evaluarla.
Por ejemplo, ``5.3 + 2`` primero es convertida a ``5.3 + 2.0``
y luego entrega el valor ``7.3``.

Hay que tener mucho cuidado,
porque los números reales no se pueden representar
de manera exacta en un computador.
Por ejemplo,
el número decimal 0.7
es representado internamente por el computador
con la aproximación 0.69999999999999996.
Todas las operaciones entre valores ``float``
son aproximaciones.

Los números reales literales
se escriben separando la parte entera de la decimal
con un punto.
Si la parte decimal es cero, puede ser omitida::

    881.9843
    -3.14159
    1024.

.. index:: notación científica

Otra representación es la notación científica,
en la que se escribe un factor y una potencia de diez
separados por una letra ``e``.  Por ejemplo::

    6.02e23
    9.1094e-31
    -2.45E4

Estos valores son iguales, respectivamente, a
:math:`6.02\times 10^{23}`,
:math:`9.1094\times 10^{-31}` y
:math:`-24500.0`.


Valores lógicos
---------------
.. index:: bool, valor lógico, valor booleano

Los valores lógicos ``True`` y ``False``
son de tipo ``bool``, que representa valores lógicos.

El nombre ``bool`` viene del matemático `George Boole`_,
quien creó un sistema algebraico para la lógica binaria.
Por lo mismo,
a ``True`` y ``False`` también se les llama
**valores booleanos**.

.. _George Boole: http://es.wikipedia.org/wiki/George_Boole

Las operaciones lógicas ``and``, ``or`` y ``not``
pueden ser aplicadas sobre valores booleanos,
y entregan como resultado un valor booleano.

Las operaciones relacionales
``<``, ``>``, ``==``, etc.,
pueden ser aplicadas sobre valores de tipos comparables,
pero siempre entregan como resultado un valor booleano.

Texto
-----
.. index:: string, tipo de datos de texto, str

Los valores que representan texto.

Listas
------


Nulo
----

Comentarios
-----------
.. include:: disqus.rst

