n = int(input())
k = int(input())

numerador = 1
for i in range(n, n - k, -1):
    numerador = numerador * i

denominador = 1
for i in range(1, k + 1):
    denominador = denominador * i

print(numerador // denominador)

