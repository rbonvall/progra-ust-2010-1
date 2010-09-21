n = int(input())
k = int(input())

resultado = 1
for i in range(1, k + 1):
    resultado = resultado * (n - i + 1) // i

print(resultado)

