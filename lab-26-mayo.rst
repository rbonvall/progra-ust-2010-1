Laboratorio 26 de mayo
======================
En esta sesión de laboratorio se evaluará:

* strings.

Este laboratorio debe ser respondido **en papel**,
y entregado al final de la sesión.

En cada ejercicio,
evalúe las expresiones,
analice los resultados,
y responda la pregunta que se le plantea.

Ejercicio 1
-----------
::

    >>> len("amigo")
    >>> len('paralelepipedo')
    >>> len('')

**Pregunta:** ¿qué hace la función ``len`` cuando su parámetro es un string?

Ejercicio 2
-----------
::

    >>> "Exijo una explicacion".split()
    >>> "   pan    leche  huevos    harina".split()
    >>> "perro".split()

**Pregunta:** ¿qué hace el método ``.split()``?

Ejercicio 3
-----------
::

    >>> "Exijo una explicacion".split('a')
    >>> 'www.santotomas.cl'.split(".")
    >>> "perro".split('r')
    >>> "perro".split('x')

**Pregunta:** ¿qué hace el método ``.split(c)`` cuando recibe un parámetro?

Ejercicio 4
-----------
::

    >>> "Su nota fue {}".format(3.7)
    >>> "Su nota fue {}".format(5.1)
    >>> "{} se saco un {}".format("Pepito", 4.3)
    >>> "{} + {} = {}".format(2, 3, 5)
    >>> "{} vs {}: {}-{}".format("Chile", "Espana", 4, 1)
    >>> "{1} vs {0}: {3}-{2}".format("Chile", "Espana", 4, 1)

**Pregunta:** ¿qué hace el método ``.format()``?

Ejercicio 5
-----------
::

    >>> "h" in "zanahoria"
    >>> "s" in "zanahoria"
    >>> "pollo" in "repollo"
    >>> "pollo" in "gallinero"

**Pregunta:** ¿qué hace el operador ``in`` cuando sus operandos son strings?

Ejercicio 6
-----------
::

    >>> 'lala'.replace('l', 'g')
    >>> 'lala'.replace('m', 'g') 
    >>> 'papanatas'.replace('pa', '') 

**Pregunta:** ¿qué hace el método ``.replace()``?

Ejercicio 7
-----------
::

    >>> 'lala'.replace('l', 'g', 1)
    >>> 'mequetrefe'.replace('e', 'x', 2) 
    >>> 'rallar'.replace('ll', 'sc', 0)

**Pregunta:** ¿qué hace el método ``.replace()``
cuando recibe un tercer parámetro?

Ejercicio 8
-----------
::

    >>> 'rinoceronte'.startswith('r')
    >>> 'rinoceronte'.startswith('i')
    >>> 'perro'.startswith('pe')
    >>> 'perro'.startswith('rro')

**Pregunta:** ¿qué hace el método ``.startswith()``?

Ejercicio 9
-----------
::

    >>> 'patio'.upper()
    >>> 'Patio'.upper()
    >>> 'PATIO'.upper()

**Pregunta:** ¿qué hace el método ``.upper()``?

Ejercicio 10
------------
::

    >>> 'patio'.swapcase()
    >>> 'Patio'.swapcase()
    >>> 'PATIO'.swapcase()
    
**Pregunta:** ¿qué hace el método ``.swapcase()``?

Ejercicio 11
------------
::

    >>> 'x'.join(["abc", "def", "ghi"])
    >>> ''.join([])
    >>> ''.join(['lapiz'])
    >>> ''.join(['lapiz', 'goma'])
    >>> '-'.join(['43', '21', '78'])

**Pregunta:** ¿qué hace el método ``.join()``?

Ejercicio 12
------------
::

    >>> l = ['6', '1', '7']
    >>> s = "617"
    >>> l[2]
    >>> s[2]
    >>> len(l)
    >>> len(s)
    >>> l + l
    >>> s + s
    >>> l[0] = '9'
    >>> s[0] = 9
    >>> 10 * l
    >>> 10 * s
    >>> l.count('7')
    >>> s.count('7')
    >>> l[1:3]
    >>> s[1:3]

**Pregunta:** ¿qué operaciones aplicables a listas
no son aplicables a strings?

