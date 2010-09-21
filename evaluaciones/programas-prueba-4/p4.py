archivo = open('nombres.txt')
s = 0
for linea in archivo:
    s = s + 1
print(s)
archivo.close()
