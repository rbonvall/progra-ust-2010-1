Módulos
=======
.. index:: módulo

Un **módulo** es un archivo
que contiene definiciones de funciones y variables.

Las definiciones contenidas en un módulo
pueden ser usadas por varios programas.
Esto permite crear funciones una sola vez
y luego reusarlas cada vez que uno las necesite,
sin que sea necesario tener que escribirlas
cada vez.

Uso de módulos
--------------
Como ejemplo,
usaremos el módulo ``math``,
que contiene definiciones
de funciones y constantes matemáticas.

Algunas funciones incluídas en el módulo ``math`` son:

* ``exp(x)``: calcula la `función exponencial`_ de :math:`x` (:math:`e^x`);
* ``log(x)``: calcula el `logaritmo natural`_ de :math:`x` (:math:`\ln x`);
* ``log(x, n)``: calcula el `logaritmo en base n`_ de :math:`x` (:math:`\log_n x`);
* ``sqrt(x)``: calcula la `raíz cuadrada`_ de :math:`x` (:math:`\sqrt{x}`);
* ``cos(x)``: calcula el `coseno`_ de :math:`x` radianes (:math:`\cos{x}`);
* ``sin(x)``: calcula el `seno`_ de :math:`x` radianes (:math:`\sin{x}`).

.. _función exponencial: http://es.wikipedia.org/wiki/Funci%C3%B3n_exponencial
.. _logaritmo natural: http://es.wikipedia.org/wiki/Logaritmo_natural
.. _logaritmo en base n: http://es.wikipedia.org/wiki/Logaritmo
.. _raíz cuadrada: http://es.wikipedia.org/wiki/Ra%C3%ADz_cuadrada
.. _coseno: http://es.wikipedia.org/wiki/Coseno
.. _seno: http://es.wikipedia.org/wiki/Seno_%28trigonometr%C3%ADa%29

Además, ``math`` define dos constantes:

* ``e``: el número :math:`e\approx 2.718281`;
* ``pi``: el número :math:`\pi\approx 3.141592`.

(La lista de todas las definiciones del módulo ``math``
está disponible en la `documentación oficial`_ de Python)

.. _documentación oficial: http://docs.python.org/py3k/library/math.html

.. index:: importar módulo, import

Si queremos usar estas funciones y constantes en nuestros programas,
primero tenemos que importarlas desde el módulo ``math``.
Por ejemplo,
podemos escribir un programa
que muestre el valor de la función seno de los números
:math:`0, \pi/8, 2\pi/8, 3\pi/8, \dots, 7\pi/8, \pi`::

    from math import sin, pi

    for i in range(9):
        x = i * pi / 8
        y = sin(x)
        print("seno(", x, ") = ", y)

La salida de este programa es::

    seno( 0.0 ) =  0.0
    seno( 0.392699081699 ) =  0.382683432365
    seno( 0.785398163397 ) =  0.707106781187
    seno( 1.1780972451 ) =  0.923879532511
    seno( 1.57079632679 ) =  1.0
    seno( 1.96349540849 ) =  0.923879532511
    seno( 2.35619449019 ) =  0.707106781187
    seno( 2.74889357189 ) =  0.382683432365
    seno( 3.14159265359 ) =  1.22460635382e-16

Como vemos,
en el programa podemos usar la función ``sin``
aunque no la hayamos creado nosotros.
En general, la sintaxis para importar definiciones de un módulo es::

    from módulo import definiciones

Esto debe ir al comienzo del programa.

Una alternativa es importar todas las definiciones
que están en el módulo::

    from módulo import *

En el caso del módulo ``math``,
esto importaría todas las funciones indicadas arriba.

Creación de módulos
-------------------
Además de los módulos provistos por Python,
un programador puede crear sus propios módulos,
en los que puede incluir las funciones creadas por uno.

Un módulo es simplemente un archivo con extensión ``.py``
que está en la misma carpeta del programa que lo utiliza.

Por ejemplo,
podemos crear un archivo llamado ``lab.py``
que contenga todas las funciones que escribimos
en `el laboratorio anterior`_::

    # archivo lab.py

    def par(n):
        return n % 2 == 0

    def factorial(n):
        producto = 1
        for i in range(1, n + 1):
            producto *= i
        return producto

    def factorial_reciproco(n):
        return 1/factorial(n)

.. _el laboratorio anterior: lab-5-mayo.html

Luego,
podemos importar estas funciones desde otro programa
para poder usarlas::

    # archivo loto.py

    from lab import factorial

    n = 39
    k = 6
    combinaciones = factorial(n) / (factorial(n - k) - factorial(k))
    p = 100 / combinaciones

    print("La probabilidad de ganarse el Loto es", p, "por ciento")


.. include:: disqus.rst

