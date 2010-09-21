n = int(input())
k = int(input())

resultado = 1
for i in range(n, n - k, -1):
    resultado = resultado * i
for i in range(1, k + 1):
    resultado = resultado // i

print(resultado)

