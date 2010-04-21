Laboratorio 21 de abril
=======================
En esta sesión de laboratorio se evaluará:

* condicionales:

  * if,
  * if-else,
  * if-elif-else;

* ciclos:

  * while,
  * for usando ``range``.

Además hay que conocer muy bien la materia previa:

* asignaciones,
* entrada,
* salida.

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


Problema 1: notas
-----------------
**Entrada**:
    una nota de una prueba
    (un valor ``float`` entre 1.0 y 7.0).
**Salida**:
    ``rojo`` o ``azul``,
    dependiendo si la nota es mayor o menor a 4.0.

Por ejemplo,
si la entrada es 3.1,
la salida debe ser::

    rojo

Si la entrada es 5.7,
la salida debe ser::

    azul

Problema 2:
-----------------
**Entrada**:
    cuatro notas.
**Salida**:
    la situación del ramo según el promedio final:

    * si es menor a 3.0, debe decir ``reprobado``;
    * si está entre 3.0 y 6.0, debe decir ``examen``;
    * se es mayor que 6.0, debe decir ``eximido``.

Por ejemplo,
si los valores de la entrada son 5.1, 3.8, 1.4 y 4.9,
la salida debe ser::

    examen

Problema 3: factorial
---------------------
**Entrada**:
    un número entero positivo ``n``.
**Salida**:
    el factorial de ``n``.

El factorial de un número :math:`n`,
simbolizado :math:`n!`,
es el producto de los primeros :math:`n` números naturales.

Por ejemplo,
si la entrada es 5,
la salida debe ser::

    120

ya que :math:`1\times 2\times 3\times 4\times 5 = 120`.

Problema 4: no múltiplos
------------------------
**Entrada**:
    un número entero positivo ``n``.
**Salida**:
    los números naturales menores o iguales a ``n``
    que no son múltiplos ni de 3 ni de 7.

Por ejemplo,
si la entrada es 24,
la salida debe ser::

    1
    2
    4
    5
    8
    10
    11
    13
    16
    17
    19
    20
    22
    23
    24

Problema 5: dígitos
-------------------
**Entrada**:
    un número entero ``n``.
**Salida**:
    la cantidad de dígitos que tiene ``n``.

Por ejemplo,
si la entrada es 2048,
la salida debe ser::

    4

El operador de división entera ``//``
le será útil.

Problema 6: ``n``-ésimo número de Fibonacci
-------------------------------------------
**Entrada**:
    un entero positivo ``n``.
**Salida**:
    el ``n``-ésimo número de Fibonacci.

Por ejemplo,
si la entrada es 8,
la salida debe ser::

    21

¡Recuerde su tarea!

Problema 7: es Fibonacci
------------------------
**Entrada**:
    un entero positivo ``m``.
**Salida**:
    ``si`` o ``no``
    dependiendo si ``m`` es o no un número de Fibonacci.

Por ejemplo,
si la entrada es 17,
la salida debe ser::

    no

Si la entrada es 21,
la salida debe ser::

    si

¡Recuerde su tarea!

