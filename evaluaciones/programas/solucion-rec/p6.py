archivo_notas = open('notas.txt')
archivo_reporte = open('reporte.txt', 'w')

for linea in archivo_notas:
    valores = linea.split(':')
    nombre = valores[0]
    notas = list(map(float, valores[1:]))
    promedio = sum(notas)/len(notas)
    if promedio < 4.0:
        print(nombre, 'reprobado', file=archivo_reporte)
    else:
        print(nombre, 'aprobado', file=archivo_reporte)

archivo_notas.close()
archivo_reporte.close()

