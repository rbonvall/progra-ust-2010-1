Sentencias de control
=====================
.. index:: sentencia

Un programa es una sucesión de **sentencias**
que son ejecutadas secuencialmente.

Por ejemplo, el siguiente programa tiene tres sentencias::

    n = int(input('Ingrese n: '))
    m = int(input('Ingrese m: '))
    suma = n + m
    print('La suma de n y m es:', suma)

Las primeras tres son asignaciones,
y la última es una llamada a función.
Al ejecutar el programa,
cada una de estas sentencias es ejecutada,
una después de la otra, una sola vez.

.. index:: sentencia de control

Además de las sentencias simples,
que son ejecutadas en secuencia,
existen las **sentencias de control**
que permiten modificar el flujo del programa
introduciendo ciclos y condicionales.

.. index:: condicional

Un **condicional** es un conjunto de sentencias
que pueden o no ejecutarse,
dependiendo del resultado de una condición.

.. index:: ciclo

Un **ciclo** es un conjunto de sentencias
que son ejecutadas varias veces,
hasta que una condición de término es satisfecha.

Tanto los condicionales como los ciclos
contienen a otras sentencias.



Condicional if
--------------
.. index:: if
.. image:: _static/imagenes/if.png
   :alt: (Diagrama de flujo if)
   :align: right

La sentencia **if**
(en español: «si»)
ejecuta instrucciones
sólo si se cumple una condición.
Si la condición es falsa,
no se hace nada.

La sintaxis es la siguiente::

    if condición:
        sentencias

Por ejemplo,
el siguente programa felicita a alguien
que aprobó la asignatura::

    nota = int(input('Ingrese su nota: '))
    if nota >= 55:
        print('Felicitaciones')

Condicional if-else
------------------------
.. index:: if-else
.. image:: _static/imagenes/if-else.png
   :alt: (Diagrama de flujo if-else)
   :align: right

La sentencia **if-then-else**
(«si-o-si-no»)
decide qué instrucciones ejecutar
dependiendo si una condición es verdadera o falsa.
La sintaxis es la siguiente::

    if condición:
        sentencias en el caso verdadero
    else
        sentencias en el caso falso

Por ejemplo,
el siguiente programa indica a alguien si es mayor de edad::

    edad = int(input('¿Cuál es su edad?'))
    if edad < 18:
        print('Usted es menor de edad')
    else:
        print('Usted es adulto')

El siguiente programa realiza acciones distintas
dependiendo de si el número de entrada
es par o impar::

    n = int(input('Ingrese un número: '))
    if n % 2 == 0:
        print('El número es par')
        print('La mitad del número es', n // 2)
    else:
        print('El número es impar')
        print('El sucesor del número es', n + 1)
    print('Listo')

La última sentencia no está indentada,
por lo que no es parte del condicional,
y será ejecutada siempre.

Ciclo while
-----------
.. index:: while
.. image:: _static/imagenes/while.png
   :alt: (Diagrama de flujo while)
   :align: right

El ciclo **while**
(«mientras»)
ejecuta una secuencia de instrucciones
mientras una condición sea verdadera.

La condición es evaluada antes de cada iteración.
Si la condición es inicialmente falsa,
el ciclo no se ejecutará ninguna vez.

La sintaxis es la siguiente::

    while condición:
        sentencias

Por ejemplo,
el siguiente programa
multiplica dos números enteros
sin usar el operador ``*``::

    m = int(input())
    n = int(input())
    p = 0
    while m > 0:
        p = p + n
        m = m - 1
    print('El producto de m y n es', p)

Para ver cómo funciona este programa,
hagamos un ruteo con la entrada ``m`` = 4
y ``n`` = 7:

    ===== ===== ===== 
    ``p`` ``m`` ``n`` 
    ----- ----- -----
              4     7
        0             
        7     3       
       14     2
       21     1
       28     0
    ===== ===== ===== 

En cada iteración,
el valor de ``m`` decrece en 1.
Cuando llega a 0,
la condición del ``while`` deja de ser verdadera
por lo que el ciclo termina.
De este modo,
se consigue que el resultado sea
sumar ``m`` veces el valor de ``n``.


Ciclo for
---------
.. index:: for

