Ejercicios de la clase del 4 de junio
=====================================

Análisis de palabras
--------------------
1. ¿Cuántas letras distintas tiene la palabra «Mississippi»?
2. ¿Cuántas letras en común tienen las palabras «murciélago» y «gominola»?

Para resolver estas preguntas, podemos usar conjuntos.

Si metemos las letras del string ``'Mississippi'`` a un conjunto,
cada letra aparecerá una vez::

    >>> letras = set()
    >>> for letra in 'Mississippi':
    ...     letras.add(letra)
    ... 
    >>> letras
    {'i', 'p', 's', 'M'}

Una manera más fácil de hacer esto es crear el conjunto
usando el string como entrada::

    >>> set('Mississipi')
    {'i', 'p', 's', 'M'}

Si queremos crear una función que cuente las letras distintas,
debemos tener cuidado de convertir primero el string a minúsculas,
para que no tome las mayúsculas como letras diferentes::

    def nro_letras_distintas(palabra):
        return len(set(palabra.lower()))

Por ejemplo::

    >>> nro_letras_distintas('Abracadabra')
    5
    >>> nro_letras_distintas('Elefante')
    6

Para obtener las letras en común que tienen dos palabras,
podemos usar conjuntos y buscar su intersección::

    >>> set('murcielago') & set('gominola')
    {'a', 'g', 'i', 'm', 'l', 'o'}

Nuevamente, podemos crear una función que haga el trabajo::

    def nro_letras_en_comun(palabra1, palabra2):
        return len(set(palabra1.lower()) & set(palabra2.lower()))

    >>> nro_letras_en_comun('murcielago', 'gominola')
    6

Puntos y triángulos
-------------------
Un punto en un espacio de dos dimensiones
es representado a través de sus coordenadas :math:`x` e :math:`y`.
En un programa,
podemos representar un punto
usando una tupla ``(x, y)`` que contenga los valores de las coordenadas.

1. Escriba una función que calcule la distancia
   entre dos puntos :math:`p_1` y :math:`p_2`.

   La función debe recibir dos puntos ``p1`` y ``p2``,
   que son tuplas de dos elementos.
   Para poder calcular la distancia,
   hay que desempaquetar las coordenadas ``x`` e ``y``
   de ambos puntos::

       def distancia(p1, p2):
           x1, y1 = p1
           x2, y2 = p2
           return ((x1 - x2) ** 2 +
                   (y1 - y2) ** 2) ** 0.5

   (La fórmula utilizada se llama `distancia euclidiana`_)

   Podemos probar que nuestra función entrega resultados correctos::

       >>> distancia((4, -1), (7, -1))
       3.0
       >>> distancia((2, 3), (2, 3))
       0.0
       >>> distancia((0, 0), (1, 1))
       1.4142135623730951

.. _distancia euclidiana: http://es.wikipedia.org/wiki/Distancia_euclideana

2.  Un triángulo puede ser representado
    mediante las coordenadas de sus tres vértices.
    Escriba una función que reciba tres puntos
    y determine qué tipo de triángulo forman.

    La estrategia para resolver el problema
    es calcular las distancias entre todos los pares de vértices,
    lo que da el largo de los tres lados del triángulo.
    Viendo cuántos de los lados tienen el mismo largo
    se puede saber qué tipo de triángulo es::

        def tipo_de_triangulo(a, b, c):
            ab = distancia(a, b)
            bc = distancia(b, c)
            ac = distancia(a, c)
            if ab == bc == ac:
                return 'equilátero'
            elif ab == bc or ab == ac or bc == ac:
                return 'isóceles'
            else:
                return 'escaleno'

    Una manera más elegante de hacer lo mismo
    es meter todos los lados a un conjunto.
    Si hay lados con el mismo largo,
    serán ingresados sólo una vez al conjunto,
    por lo que podemos saber el tipo de triángulo
    viendo cuántos elementos quedan en el conjunto::

        def tipo_de_triangulo(a, b, c):
            lados = {distancia(a, b), distancia(b, c), distancia(a, c)}
            if len(lados) == 3:
                return 'escaleno'
            elif len(lados) == 2:
                return 'isóceles'
            else:
                return 'equilátero'

    Ya que cada valor entre 1 y 3 tiene asociado un tipo de triángulo,
    podemos usar un diccionario para hacer nuestra función
    más corta aún::

        def tipo_de_triangulo(a, b, c):
            tipos = {1: 'equilátero', 2: 'isóceles', 3: 'escaleno'}
            lados = {distancia(a, b), distancia(b, c), distancia(a, c)}
            return tipos[len(lados)]

    Algunos ejemplos de uso de la función::

        >>> a = (0, 0)
        >>> b = (2, 0)
        >>> tipo_de_triangulo(a, b, (1, 1))
        'isóceles'
        >>> tipo_de_triangulo(a, b, (3, 4))
        'escaleno'
        >>> tipo_de_triangulo(a, b, (1, 3 ** 0.5))
        'equilátero'

Lista de personas
-----------------
En la lista de personas que usamos en el `laboratorio de esta semana`_,

1. ¿Cuántos nombres distintos de personas hay?
2. ¿Cuál es el signo zodiacal más repetido?

.. _laboratorio de esta semana: lab-2-junio.html

(Por escribir)

.. include:: disqus.rst

