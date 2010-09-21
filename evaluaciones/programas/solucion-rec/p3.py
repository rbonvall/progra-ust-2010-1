n = 1   # o cualquier valor diferente de cero
positivos = 0
negativos = 0

while n != 0:
    n = int(input('Ingrese un numero: '))
    if n > 0:
        positivos = positivos + 1
    elif n < 0:
        negativos = negativos + 1

print('Positivos:', positivos)
print('Negativos:', negativos)

