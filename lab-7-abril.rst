Laboratorio 7 de abril
======================
En esta sesión de laboratorio se evaluará:

* asignaciones,
* entrada, y
* salida.

Las asignaciones son de la forma::

    variable = expresion

La entrada se hace con la función ``input()``,
cuyo argumento es un mensaje para el usuario::

    s = input('Ingrese un valor')

El valor entregado por ``input()`` 
es de tipo ``str`` (texto).
Para convertir la entrada a otro tipo de datos
hay que utilizar el tipo de destino como función.
Por ejemplo, para leer un número real,
se puede hacer así::

    s = input('Ingrese un número real')
    x = float(s)

O también se puede hacer todo en una sola sentencia::

    x = float(input('Ingrese un número real'))

La salida se hace con la función ``print()``,
cuyos argumentos son todos los mensajes
que se va a entregar al usuario en una misma línea.
Estos mensajes pueden ser texto
o valores de cualquier tipo.

Por ejemplo,
para escribir el mensaje ``Hola mundo``,
un programa podría hacerlo de varias maneras diferentes::

    print('Hola mundo')
    
    print('Hola', 'mundo')

    saludo = 'Hola'
    print(saludo, 'mundo')


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


Problema 1: saludo
------------------
**Entrada**:
    el nombre del usuario.
**Salida**:
    un mensaje saludando al usuario.

Por ejemplo,
si el usuario escribe ``Ricardo``,
el programa debe entregar el mensaje ``Hola Ricardo``.


Problema 2: promedio
--------------------
**Entrada**:
    cuatro notas obtenidas por un alumno.
**Salida**:
    el promedio de las notas.

Por ejemplo,
si el usuario ingresa las notas ``6.5``, ``4.1``, ``1.7`` y ``7.0``,
el programa debe entregar el resultado ``4.825``.


Problema 3: círculos
--------------------
**Entrada**:
    el radio de un círculo.
**Salida**:
    el perímetros y el área del círculo.

Por ejemplo,
si el usuario ingresa el radio ``5.1``,
el programa debe entregar el perímetro ``32.04422``
y el área ``81.71276``.


Problema 4: número invertido
----------------------------
**Entrada**:
    un número entero de tres dígitos.
**Salida**:
    el número con los dígitos en orden inverso.

Por ejemplo,
si el usuario ingresa el número 391,
el programa debe entregar el 193.

Puede usar los operadores ``%`` y ``//``.


Problema 5: parte decimal
-------------------------
**Entrada**:
    un número real.
**Salida**:
    la parte decimal del número.

Por ejemplo,
si el usuario ingresa el número ``14.2857``,
el programa debe entregar ``0.2857``.

Recuerde que la función ``int``
entrega la parte entera del número.


Problema 6: años bisiestos
--------------------------
**Entrada**
    un año.
**Salida**
    ``True`` si un año es bisiesto,
    ``False`` si el año no es bisiesto.

Los años bisiestos son los divisibles por 4,
pero con una excepción:
si el año es el último del siglo (termina con dos ceros),
entonces es bisiesto sólo si es divisible por 400.

Los siguientes años sí son bisiestos:
1600, 1940, 1984, 1996, 2000, 2008.

Los siguientes años no son bisiestos:
1800, 1900, 1985, 2010, 2100.


Problema 7: ordenamiento
------------------------
**Entrada**:
    tres números enteros.
**Salida**:
    los tres números ordenados de menor a mayor.

Por ejemplo,
si el usuario ingresa ``13``, ``5`` y ``9``,
el programa debe entregar ``5``, ``9`` y ``13``.

Puede utilizar las funciones ``max()`` y ``min()``,
entregan respectivamente el máximo y el mínimo
de sus argumentos.  Por ejemplo::

    min(7, 13, 5, 11)
    max(7, 13, 5, 11)

entregan respectivamente los valores 5 y 13.

Si no se le ocurre cómo resolver este problema,
intente primero resolverlo con sólo dos números.

