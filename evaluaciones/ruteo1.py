n = int(input())
r = 0
b = 10
while n > 0:
    d = n % b
    n = n // b
    r = b * r + d
print(r)

