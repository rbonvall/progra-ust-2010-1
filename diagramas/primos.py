n = int(input())
d = 2
while d <= n//2:
    if n % d == 0:
        print(n, "es compuesto")
        exit()
    else:
        d = d + 1
print(n, "es primo")

