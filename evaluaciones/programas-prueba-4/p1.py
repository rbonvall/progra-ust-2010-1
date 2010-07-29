archivo = open('productos.txt')
for linea in archivo:
    print(linea[0])
archivo.close()
