Strings
=======
.. index:: string

Como ya vimos a principios de semestre,
un **string** es un tipo de datos
para representar texto.

El tipo de datos que representa los strings
se llama ``str``.

Un string puede ser creado de varias maneras:

.. index:: string literal

* usar un string literal entre comillas simples o dobles::

    >>> s = "hola"
    >>> t = 'mundo'
    >>> print(s)
    hola
    >>> print(t)
    mundo

.. index:: str()

* usando la función ``str()`` para convertir un valor de otro tipo
  a un string::

    >>> str(5)
    '5'
    >>> str([1, 2, 3])
    '[1, 2, 3]'

Un string es un tipo de datos **inmutable**.
Esto significa que una vez que uno ha creado un string,
uno no puede cambiar su valor.
Es por esto que todas las operaciones que uno efectúa sobre un string
crean strings nuevos, y no modifican el original.


Operaciones sobre strings
-------------------------
* ``len(s)`` entrega el largo del string; es decir, cuántos símbolos tiene::

    >>> len('paralelepipedo veloz!')
    21

  Los espacios y signos de puntuación tambien cuentan como símbolos.

* ``s1 + s2`` concatena los strings ``s1`` y ``s2``::

    >>> 'par' + "aguas"
    'paraguas'

* si ``n`` es un número entero, ``s * n`` repite ``n`` veces el string ``s``::

    >>> 'la' * 4
    'lalalala'

* ``t in s`` permite saber si el string ``t`` está contenido dentro de ``s``::

    >>> "h" in "zanahoria"
    True
    >>> "s" in "zanahoria"
    False
    >>> "pollo" in "repollos"
    True
    >>> "pollo" in "gallinero"
    False

* ``s[i]`` entrega el ``i``-ésimo símbolo del string, contando desde cero::

    >>> s = 'arroz'
    >>> s[0]
    'a'
    >>> s[2]
    'r'
    >>> s[-1]
    'z'

  Si el índice ``i`` no está en el rango de valores válido,
  ocurre un **error de índice**::

    >>> s[10]
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    IndexError: string index out of range

  Si el índice es negativo,
  los elementos se cuentan desde el final hacia atrás::

    >>> s[-1]
    'z'
    >>> s[-2]
    'o'

  El uso de índices funciona casi igual que en las listas.
  Una diferencia importante es que al obtener el elemento ``i``-ésimo
  de un string, siempre el resultado es un string de largo 1;
  en el caso de una lista, el elemento puede ser de cualquier tipo.

* ``s[i:j]`` permite obtener una rebanada del string,
  desde el elemento de índice ``i``
  hasta el de índice ``j``::

    >>> s = 'paraguas'
    >>> s[0:4]
    'para'
    >>> s[4:8]
    'guas'
    >>> s[4:]
    'guas'
    >>> s[:3]
    'par'

  Si se incluye un tercer entero, indica cada cuántos símbolos se incluirá::

    >>> s[2:8:2]
    'rga'
    >>> s[2:8:2]
    'rga'
    >>> s[::3]
    'paa'

  Una manera rápida de invertir un string es la siguiente::

    >>> s[::-1]
    'saugarap'

* ``s.split()`` particiona el string ``s`` usando los espacios como separadores,
  y entrega una lista con los strings resultantes::

    >>> s = 'Anita   lava la  tina'
    >>> s.split()
    ['Anita', 'lava', 'la', 'tina']

* ``s.split(sep)`` particiona el string ``s`` usando el string ``sep`` como separador,
  y entrega una lista con los strings resultantes::

    >>> s = 'Anita lava la tina'
    >>> s.split('a')
    ['Anit', ' l', 'v', ' l', ' tin', '']
    >>> 'perro'.split('r')
    ['pe', '', 'o']
    >>> 'pero'.split('r')
    ['pe', 'o']

* si ``l`` es una lista de strings, ``s.join(l)`` pega los elementos de ``l``
  usando ``s`` como "pegamento"::

    >>> l = ['abra', 'ca', 'dabra']
    >>> '-'.join(l)
    'abra-ca-dabra'
    >>> '...'.join(l)
    'abra...ca...dabra'
    >>> ''.join(l)
    'abracadabra'
    >>> ' punto '.join('www.santotomas.cl'.split('.'))
    'www punto santotomas punto cl'

* ``s.replace(u, v)`` reemplaza las apariciones del string ``u`` dentro de ``s``
  por el string ``v``::

    >>> 'lala'.replace('l', 'g')
    'gaga'
    >>> 'lala'.replace('m', 'g')
    'lala'

  La llamada a ``replace`` puede recibir un entero como tercer parámetro,
  que indica cuántos reemplazos serán realizados::

    >>> 'excelentemente'.replace('e', 'E', 3)
    'ExcElEntemente'

  Recuerde que los strings son inmutables.
  Al usar el método ``replace``, el string no es modificado,
  sino que se retorna un nuevo string en el que los símbolos están reemplazados::

    >>> s = 'El perro vive en la casa'
    >>> s.replace('perro', 'gato')
    'El gato vive en la casa'
    >>> s
    'El perro vive en la casa'

* Otros métodos menos importantes
  son mostrados a continuación::

    >>> s = 'Hola mundo.'
    >>> s.upper()          # convierte a mayúsculas
    'HOLA MUNDO.'
    >>> s.lower()          # convierte a minúsculas
    'hola mundo.'
    >>> s.swapcase()       # cambia mayúsculas y minúsculas
    'hOLA mUNDO.'
    >>> s.startswith('Ho') # comprueba que s comienza con 'Ho'
    True
    >>> s.endswith('.')    # comprueba que s termina con '.'
    True
    >>> s.center(20)       # centra s en un string de largo 20
    '    Hola Mundo.     '
    >>> s.partition('Mu')  # particiona s en tres partes usando 'Mu' como separador
    ('Hola ', 'Mu', 'ndo.')
    >>> s.index('u')       # encuentra el índice de 'u' dentro de s
    6
    >>> s.count('o')       # cuenta cuántas veces aparece 'o' en s
    2


 


.. include:: disqus.rst

