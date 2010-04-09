Tipos de datos básicos
======================

.. index:: tipo de datos

Un **tipo de datos** es una propiedad de un valor
que determina su dominio (qué valores puede tomar),
qué operaciones se le pueden aplicar
y cómo es representado internamente por el computador.

A continuación revisaremos los tipos de datos más básicos.
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

Al combinar valores reales y enteros en una operación,
los enteros son convertidos a reales
antes de evaluarla.
Por ejemplo, la expresión ``2 + 5.1``
es convertida a ``2.0 + 5.1``,
y tiene el valor ``7.1``.


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

A los valores que representan texto
se les llama **strings**,
y tienen el tipo ``str``.

Los strings literales
pueden ser representados
con texto entre comillas simples o comillas dobles::

   "ejemplo 1"
   'ejemplo 2'

Los operadores aritméticos no pueden ser aplicadas sobre strings,
salvo dos excepciones:

1. El operador ``+`` aplicado a dos strings
   no representa la suma,
   sino la **concatenación**,
   que significa pegar los strings
   uno después del otro.
   Por ejemplo, la expresión ``"hola" + "mundo"``
   tiene el valor ``"holamundo"``.

2. El operador ``*`` aplicado a un string y a un número entero
   no representa la multiplicación,
   sino la **repetición**,
   es decir, el string es repetido tantas veces como indica el número.
   Por ejemplo, la expresión ``'a' * 3``
   tiene el valor ``'aaa'``.

Las operaciones relacionales permiten comparar strings alfabéticamente.
Por ejemplo, la siguiente expresión tiene el valor ``True``::

    "ala" < "alamo" < "bote" < "botero" < "boteros" < "zapato"

Para conocer el largo de un string,
se utiliza la función ``len()``.
Por ejemplo, la expresión ``len('universidad')``
tiene el valor ``11``.

La función ``input()``,
que usamos para leer la entrada del usuario,
siempre entrega como resultado un string.
Hay que tener la precaución
de convertir los valores que entrega
al tipo adecuado.
Por ejemplo,
el siguiente programa tiene
un error de incompatibilidad de tipos::

    n = input('Escriba un número:')
    doble = 2 * n
    print('El doble de n es', doble)

Nulo
----
.. index:: tipo nulo, None

Existe un valor muy especial que se llama ``None``.

``None`` es un valor que se utiliza
en contextos en que ningún valor es válido.
En inglés, *none* significa «ninguno».

El valor ``None`` tiene su propio tipo,
que es diferente al de todos los demás valores.


Conversión de tipos
-------------------
.. index:: conversión de tipos

Los tipos de los valores
indican qué operaciones pueden ser aplicadas sobre ellos.

A veces es necesario convertir valores de un tipo a otro
para poder operar sobre ellos.
Existen dos tipos de conversiones:
implícitas y explícitas.

Las conversiones implícitas
son las que se hacen automáticamente
según el contexto.
Las conversiones implícitas
más importantes son las siguientes:

* cuando se utiliza un entero
  en un contexto real,
  el entero es convertido al real correspondiente;

* cuando se utiliza cualquier valor
  en un contexto booleano,
  es convertido al valor ``True``,
  excepto por los siguientes casos,
  en que es convertido al valor ``False``:

  * el valor ``0``,
  * el string vacío ``''``,
  * ``None``.

* cuando se utiliza un valor lógico
  en un contexto entero,
  ``True`` es convertido a ``1``
  y ``False`` a ``0``.

Las conversiones explícitas se realizan
usando el nombre del tipo de destino
como si fuera una función.

Por ejemplo,
para convertir un valor al tipo entero,
se utiliza la función ``int``::

    int('45')  # entrega el valor 45
    int('abc') # error
    int(3.891) # entrega el valor 3
    int(True)  # entrega el valor 1
    int(None)  # error

Para convertir un valor en un string,
se utiliza la función ``str``::

    str(87)     # entrega el valor '87'
    str(True)   # entrega el valor 'True'






Comentarios
-----------
.. include:: disqus.rst

