Funciones
=========
.. index:: función

Una **función** es una sección de un programa
que realiza una tarea específica
de manera independiente al resto del código.

Una función es en esencia un mini programa:
tiene entrada, proceso y salida.

Hasta ahora hemos utilizado algunas funciones
que son provistas por Python.
Por ejemplo, la función ``abs``
entrega el valor absoluto de un número::

    x = float(input())
    a = abs(x)
    print(a)

Este programa es equivalente a::

    x = float(input())
    if x < 0:
        a = x
    else:
        a = -x
    print(a)

Usar funciones tiene varias ventajas:

* los programas son más cortos,
  pues todo el proceso es reemplazado por una simple llamada a la función;
* los programas son más fáciles de entender,
  pues el nombre de la función indica qué es lo que se está haciendo;
* no es necesario escribir el mismo código varias veces en el programa,
  pues la misma función puede ser reutilizada todas las veces que sea necesario;
* permiten utilizar operaciones complejas
  sin preocuparse de cómo están implementadas;
* permiten descomponer tareas complicadas
  en subtareas más sencillas.

Las funciones son valores como cualquier otro.
Por ejemplo,
es posible asignar una función a una variable::

    >>> A = abs
    >>> A(-3)
    3

.. index:: operador de llamada de función

La operación más importante que se puede aplicar a una función
es el **operador de llamada**,
representado con paréntesis después del nombre de la función::

    abs         # la función abs
    abs(-2)     # llamada a la función abs

Componentes de una función
--------------------------
.. index:: argumento, valor de retorno

Una función tiene tres partes importantes:

* los **argumentos**,
  ue son los valores que son entregados a la función;
* **código de la función**,
  que son las operaciones que hace la función; y
* el **valor de retorno**,
  que es el valor final que entrega la función.

Por ejemplo,
en la siguiente llamada a función::

    max(5, 1, 4)

los argumentos son 5, 1 y 4, y el valor de retorno es 5.
El código de la función no es visible
al ocupar la función.

Definición de funciones
-----------------------
Además de las funciones provistas por Python,
uno puede crear sus propias funciones.

Por ejemplo,
nos gustaría crear una función ``factorial(n)``,
que calcule el factorial de un número entero ``n``::

    >>> factorial(0)
    1
    >>> factorial(5)
    120
    >>> factorial(11)
    39916800

Esta función puede ser creada de la siguiente manera::

    def factorial(n):
        producto = 1
        for i in range(1, n + 1):
            producto = producto * i
        return producto

``n`` es el **parámetro** de la función.
Cuando la función sea llamada,
``n`` tomará el valor del argumento entregado.

La sentencia ``return producto``
termina la ejecución de la función
y entrega como resultado el valor de la expresión.

En general,
la sintaxis para definir una función es::

    def nombre_de_la_función(parámetros):
        ...

La palabra ``def`` indica que estamos definiendo una función.
A continuación va el código de la función,
que se encarga de calcular el resultado que se desea entregar.
Una vez que este resultado ya se ha obtenido,
puede ser retornado con la sentencia ``return``.

Variables globales y locales
----------------------------
.. index:: variable local

Las variables utilizadas dentro de una función
(incluyendo los parámetros)
sólo existen durante la llamada a la función.
No es posible usarlas
desde fuera de la función.
Se dice que las variables usadas por la función
son **variables locales**.

Por ejemplo,
al haber definido la función ``factorial`` más arriba,
las variables ``producto`` y ``n``
no pueden ser usadas afuera de la función::

    >>> factorial(4)
    24
    >>> print(producto)
    Traceback (most recent call last):
    NameError: name 'producto' is not defined

Las variables que no están dentro de una función
se llaman **variables globales**.
Uno puede usar el valor de una variable global
desde una función::

    >>> n = 5
    >>> def f(x):
    ...     return n + x
    ...
    >>> f(2)
    7
    >>> f(3)
    8
    >>> n = 1000
    >>> f(2)
    1002

Sin embargo,
no se puede asignar la variable global dentro de la función,
ya que la asignación crea una variable local::

    >>> n = 5       # global
    >>> def f(x):
    ...     n = x   # local
    ...
    >>> f(3)
    >>> n           # global
    5

.. include:: disqus.rst

