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
.. index:: orden lexicográfico


.. include:: disqus.rst

