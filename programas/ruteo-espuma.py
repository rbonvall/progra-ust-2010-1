a = int(input())
b = int(input())
c = int(input())

t = b + c
b = (t - abs(b - c)) // 2
c = t - b

t = a + b
a = (t - abs(a - b)) // 2
b = t - a

t = b + c
b = (t - abs(b - c)) // 2
c = t - b

print(a, b, c)
