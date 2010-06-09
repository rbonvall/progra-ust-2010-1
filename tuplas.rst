Tuplas
======
.. index:: tupla

Una **tupla** es una secuencia de valores agrupados.

Una tupla sirve para agrupar, como si fueran un único valor,
varios valores relacionados.

El tipo de datos que representa a las tuplas se llama ``tuple``.
El tipo ``tuple`` es inmutable: una tupla no puede ser modificada
una vez que ha sido creada.

.. index:: tupla literal

Una tupla puede ser creada
poniendo los valores separados por comas y entre paréntesis.
Por ejemplo,
podemos crear una tupla que tenga el nombre y el apellido de una persona::

    >>> persona = ('Perico', 'Los Palotes')
    >>> persona
    ('Perico', 'Los Palotes')

Desempaquetado de tuplas
------------------------
.. index:: desempaquetado

Los valores de una tupla pueden ser recuperados
asignando la tupla a las variables respectivas.
Esto se llama **desempaquetar la tupla** (en inglés: *unpack*)::

    >>> nombre, apellido = persona
    >>> nombre
    'Perico'

Si se intenta desempaquetar una cantidad incorrecta de valores,
ocurre un error de valor::

    >>> a, b, c = persona
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: need more than 2 values to unpack

Además, también es posible extraer los valores usando su índice::

    >>> persona[1]
    'Los Palotes'

Comparación de tuplas
---------------------
Dos tuplas son iguales
cuando tienen el mismo tamaño
y cada uno de sus elementos correspondientes
tienen el mismo valor::

    >>> (1, 2) == (3 // 2, 1 + 1)
    True
    >>> (6, 1) == (6, 2)
    False
    >>> (6, 1) == (6, 1, 0)
    False

.. index:: orden lexicográfico

Para determinar si una tupla es menor que otra,
se utiliza lo que se denomina **orden lexicográfico**.
Si los elementos en la primera posición de ambas tuplas son distintos,
ellos determinan el ordenamiento de las tuplas::

    >>> (1, 4, 7) < (2, 0, 0, 1)
    True
    >>> (1, 9, 10) < (0, 5)
    False

La primera comparación es ``True`` porque ``1 < 2``.
La segunda comparación es ``False`` porque ``1 > 0``.
No importa el valor que tengan los siguientes valores,
o si una tupla tiene más elementos que la otra.

Si los elementos en la primera posición son iguales,
entonces se usa el valor siguiente para hacer la comparación::

    >>> (6, 1, 8) < (6, 2, 8)
    True
    >>> (6, 1, 8) < (6, 0)
    False

La primera comparación es ``True`` porque ``6 == 6`` y ``1 < 2``.
La segunda comparación es ``False`` porque ``6 == 6`` y ``1 > 0``.

Si los elementos respectivos siguen siendo iguales,
se sigue probando con los siguientes.
Si a una tupla se le acaban los elementos para comparar
antes que a la otra, entonces es inmediatamente menor que la otra::

    >>> (1, 2) < (1, 2 ,4)
    True
    >>> (1, 3) < (1, 2, 4)
    False

La primera compación es ``True`` porque ``1 == 1``, ``2 == 2``,
y ahí se acaban los elementos de la primera tupla.
La segunda comparación es ``False`` porque ``1 == 1`` y ``3 < 2``;
en este caso sí se alcanza a determinar el resultado antes que se acaben los elementos
de la primera tupla.

Este método de comparación es el mismo que se utiliza
para poner palabras en orden alfabético
(por ejemplo, en guías telefónicas y diccionarios)::

    >>> 'auto' < 'auxilio'
    True
    >>> 'auto' < 'autos'
    True
    >>> 'mes' < 'mesa' < 'mesadas' < 'mesas' < 'meses' < 'mi'
    True

.. include:: disqus.rst

