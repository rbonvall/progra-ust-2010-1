Guía de ejercicios 1
====================

Estos ejercicios serán su preparación
para la prueba solemne 1
del viernes 30 de abril.


Conversión de temperaturas
--------------------------
Desarrolle un programa
cuya entrada sea una temperatura
en `grados Celsius`_
y su salida sea la temperatura
en `grados Fahrenheit`_.

La fórmula de conversión es:

.. math::

  F = \frac{9}{5}C + 32

.. _grados Celsius: http://es.wikipedia.org/wiki/Grados_Celsius
.. _grados Fahrenheit: http://es.wikipedia.org/wiki/Grados_Fahrenheit

Por ejemplo,
si la entrada es 55,
el programa debe entregar el resultado 129.2.


Planetas
--------
Desarrolle un programa
cuya entrada sea el radio de un planeta
y su salida sea:

* el área del planeta, y
* el volumen del planeta.

Utilice las fórmulas para `el área y el volumen de una esfera`_.

.. _el área y el volumen de una esfera: http://es.wikipedia.org/wiki/Esfera#.C3.81rea_y_volumen

Por ejemplo,
si la entrada es 6371.0 (el radio medio de la Tierra en kilómetros)
el programa debe entregar como salida::

    Area: 510064471.90978825
    Volumen: 1083206916845.7535

Recíproco
---------
El recíproco de un número real :math:`x`
se calcula como 1 dividido por :math:`x`,
excepto cuando :math:`x = 0`,
ya que el cero no tiene recíproco.

Desarolle un programa que reciba como entrada un número real,
y que entregue como salida el recíproco del número.
Si la entrada es 0,
la salida debe decir: ``el cero no tiene reciproco``.

Ecuación cuadrática
-------------------
Desarrolle un programa que resuelva
la `ecuación cuadrática`_ :math:`ax^2 + bx + c = 0`.

.. _ecuación cuadrática: diagramas-de-flujo.html

La entrada del programa serán
:math:`a`, :math:`b` y :math:`c`.
La salida serán las soluciones reales de la ecuación.

Por ejemplo,
si la entrada son los valores 1, 1.5 y —7,
la salida del programa debe ser::

    -3.5
    2.0

Si la entrada son los valores 4, 4 y 1,
la salida del programa debe ser::

    -0.5

Si la entrada son los valores 3, —3 y 1,
la salida del programa debe ser::

   no hay soluciones reales

Tabla del 7
-----------
Desarrolle un programa
que imprima la tabla de multiplicar del 7.

La salida del programa debe ser::

    7 x 1 = 7
    7 x 2 = 14
    7 x 3 = 21
    7 x 4 = 28
    7 x 5 = 35
    7 x 6 = 42
    7 x 7 = 49
    7 x 8 = 54
    7 x 9 = 63
    7 x 10 = 70

Contador de signos
------------------
Desarrolle un programa que pida al usuario
que ingrese varios números, uno por uno.
Cuando el usuario ingrese el 0,
el programa debe entregar como salida
la cantidad de números positivos
y negativos que ingresó el usuario.

Por ejemplo,
si el usuario ingresa los números
5, —4, —2, —7, 7, —1 y 0,
el programa debe entregar la salida::

    Positivos: 2
    Negativos: 4

Largo y corto
-------------
Desarrolle un programa
que tenga la siguiente entrada:

* primero, el usuario ingresa un número entero ``n``,
  que indica cuántas palabras ingresará a continuación;
* después el usuario ingresa ``n`` palabras.

La salida del programa
deben ser la palabra más larga
y la más corta
que ingresó el usuario.

Por ejemplo,
si el usuario ingresa:

* 5
* negro
* amarillo
* naranjo
* azul
* blanco

la salida debe ser::

  Mas larga: amarillo
  Mas corta: azul

Recuerde que la función ``len()`` permite obtener el largo de un string::

  >>> len('amarillo')
  8

Potencias fraccionales de 2
---------------------------
Desarrolle un programa
que tabule las potencias fraccionales de 2
(1/2, 1/4, 1/8, 1/16, ...)
y sus sumas parciales
en forma decimal.

La salida del programa debe comenzar así::

  P  Fraccion  Suma
  1  0.5       0.5
  2  0.25      0.75
  3  0.125     0.875
  4  0.0625    0.9375
     ...       ...

El programa debe terminar cuando la fracción
sea menor o igual que 0.00001.

La tercera columna
contiene la suma de todas las fracciones
calculadas hasta esa fila.

Primo o compuesto
-----------------
Desarrolle un programa
cuya entrada sea un entero positivo ``n``,
y cuya salida sea:

* ``primo``, si el número es primo, y
* ``compuesto``, si el número es compuesto.

Por ejemplo,
si la entrada es 29,
el programa debe decir ``primo``.
Si la entrada es 27,
el programa debe decir ``compuesto``.

m primos
--------
Usando como base el programa diseñado
en el ejercicio anterior,
desarrolle otro programa
que reciba como entrada un número entero positivo ``m``
y cuya salida sean los ``m`` primeros números primos.

Por ejemplo, si la entrada es 12,
la salida del programa debe ser::

  2
  3
  5
  7
  11
  13
  17
  19
  23
  29
  31
  37

Primos hasta m
--------------
Modifique el programa del ejercicio anterior
para que muestre los números primos
menores o iguales a ``m``.

Por ejemplo, si la entrada es 12,
la salida debe ser::

  2
  3
  5
  7
  11

Pi
--
Desarolle un programa para estimar el valor de :math:`\pi`
usando la siguiente suma infinita:

.. math::

    \pi = 4\left(1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \cdots\right)

La entrada del programa
debe ser un número entero ``n``
que indique cuántos términos de la suma se utilizará.

Por ejemplo,
si la entrada es 3,
el programa debe entregar como salida::

    3.466666666666667

Si la entrada es 1000,
la salida debe ser::

    3.140592653839794





.. include:: disqus.rst
