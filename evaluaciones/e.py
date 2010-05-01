e = 0.0
denominador = 1
contador = 0
while 1/denominador >= 0.0001:
    e = e + 1/denominador
    contador = contador + 1
    denominador = denominador * contador
print(e)

