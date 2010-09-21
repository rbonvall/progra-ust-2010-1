minimo = 0
maximo = 100
adivinado = False

while not adivinado:
    promedio = (minimo + maximo) // 2
    respuesta = input('¿El número es ' + str(promedio) + '? ')
    if respuesta == '<':
        maximo = promedio - 1
    elif respuesta == '>':
        minimo = promedio + 1
    elif respuesta == '=':
        adivinado = True

print('¡Bien!')
