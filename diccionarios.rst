Diccionarios
============
.. index:: diccionario

Un **diccionario** es tipo de datos
que permite asociar pares de valores.

.. index:: llave (diccionario), valor (diccionario)

Un diccionario puede ser visto
como una colección de **llaves**,
cada una de las cuales tiene asociada un **valor**.
Las llaves no están ordenadas
y no hay llaves repetidas.
La única manera de acceder a un valor
es a través de su llave.

Cómo crear diccionarios
-----------------------
La manera principal de crear un diccionario es usando un diccionario literal.
La llave es asociada al valor usando dos puntos::

    >>> telefonos = {'Pepito': 5552437, 'Jaimito': 5551428, 'Yayita': 5550012}

En este ejemplo,
las llaves son ``'Pepito'``, ``'Jaimito'`` y ``'Yayita'``,
y los valores asociados a ellas son, respectivamente,
``5552437``, ``5551428`` y ``5550012``.

Un diccionario vacío puede ser creado usando ``{}`` o con la función ``dict()``::

    >>> d = {}
    >>> d = dict()

Cómo usar un diccionario
------------------------
El valor asociado a la llave ``k`` en el diccionario ``d``
se puede obtener mediante ``d[k]``. ::

    >>> telefonos['Pepito']
    5552437
    >>> telefonos['Jaimito']
    5551428

Si la llave no está presente en el diccionario,
ocurre un **error de llave** (``KeyError``)::

    >>> telefonos['Fulanito']
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyError: 'Fulanito'

Se puede agregar una llave nueva
simplemente asignándole un valor::

    >>> telefonos['Susanita'] = 4448139
    >>> telefonos
    {'Pepito': 5552437, 'Susanita': 4448139, 'Jaimito': 5551428, 'Yayita': 5550012}

Note que el orden en que quedan las llaves en el diccionario
no es necesariamente el mismo orden en que fueron agregadas.

Si se asigna un valor a una llave que ya estaba en el diccionario,
el valor anterior se sobreescribe.
Recuerde que un diccionario no puede tener llaves repetidas::

    >>> telefonos
    {'Pepito': 5552437, 'Susanita': 4448139, 'Jaimito': 5551428, 'Yayita': 5550012}
    >>> telefonos['Jaimito'] = 4448139
    >>> telefonos
    {'Pepito': 5552437, 'Susanita': 4448139, 'Jaimito': 4448139, 'Yayita': 5550012}

Los valores sí pueden estar repetidos.
En el ejemplo anterior, Jaimito y Susanita tienen el mismo número.

Para borrar una llave, se puede usar la sentencia ``del``::

    >>> del telefonos['Yayita']
    >>> telefonos
    {'Pepito': 5552437, 'Susanita': 4448139, 'Jaimito': 4448139}

Si se usa un diccionario en un ciclo ``for``,
en cada iteración se obtiene una llave::

    >>> for k in telefonos:
    ...     print(k)
    ...
    Pepito
    Susanita
    Jaimito

Para iterar sobre las llaves, se usa ``d.values()``::

    >>> for v in telefonos.values():
    ...     print(v)
    ...
    5552437
    4448139
    4448139

También es posible crear listas de llaves o valores::

    >>> list(telefonos)
    ['Pepito', 'Susanita', 'Jaimito']
    >>> list(telefonos.values())
    [5552437, 4448139, 4448139]

``len(d)`` entrega cuántos pares llave-valor hay en el diccionario::

    >>> numeros = {15: 'quince', 24: 'veinticuatro'}
    >>> len(numeros)
    2
    >>> len({})
    0

``k in d`` permite saber si la llave ``k`` está en el diccionario ``d``::

    >>> patas = {'gato': 4, 'humano': 2, 'pulpo': 8, 'perro': 4, 'ciempiés': 100}
    >>> 'perro' in patas
    True
    >>> 'gusano' in patas
    False

Para saber si una llave *no* está en el diccionario,
se puede usar ``not in``::

    >>> 'gusano' not in patas
    True

.. include:: disqus.rst

