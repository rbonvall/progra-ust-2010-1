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
deberán ser subidos a la intranet académica
antes del término de la sesión.


Problema 1
----------
*Entrada*:
    el nombre del usuario.
*Salida*:
    un mensaje saludando al usuario.

Por ejemplo,
si el usuario escribe ``Ricardo``,
el programa debe entregar el mensaje ``Hola Ricardo``.


Problema 2
----------
*Entrada*:
    cuatro notas obtenidas por un alumno.
*Salida*:
    el promedio de las notas.

Por ejemplo,
si el usuario ingresa las notas ``6.5``, ``4.1``, ``1.7`` y ``7.0``,
el programa debe entregar ``El promedio es 4.825``.


Problema 3
----------
*Entrada*:
    tres números enteros.
*Salida*:
    los tres números ordenados de menor a mayor.

Por ejemplo,
si el usuario ingresa ``13``, ``5``, ``9``,
el programa debe entregar ``5``, ``9`` y ``13``.

Pueden utilizar las funciones ``max()`` y ``min()``,
entregan respectivamente el máximo y el mínimo
de sus argumentos.  Por ejemplo::

    min(13, 5, 9)
    max(13, 5, 9)

entregan respectivamente los valores 5 y 13.

