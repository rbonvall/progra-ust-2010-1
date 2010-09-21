archivo = open('nombres.txt')
for linea in archivo:
    print(len(linea))
archivo.close()
