l = [4, 3] * 2
print(l)

d = {78: 15, 91: 15}
print(len(d))

s = {78, 15, 91, 15}
print(len(s))

a, b, c = (1990, 4, 9)
d, e, f = (1990, 1, 12)
print(c < f)

c = (1990, 4, 9)
f = (1990, 1, 12)
print(c < f)

a = 'gata'
a.replace('g', 'r')
print(a)

t = 'papagayos'
w = t.split('a')
print(w[3])

a = {'perro'}
b = {'gato'}
print(a | b)

a = set('perro')
b = set('gato')
print(a | b)

l = [[1, 2], [3, 4]]
print(len(l))

a = [2, 4, 8, 16, 32]
print(a[a[0]])

w = 'Vamos Chile'
print(len(w))

a = set()
a.add(6)
a.add(3)
a.add(-1)
print(a[0])

d = {}
for i in range(3):
    d[i] = i * i
for k in d:
    print(d[k])

t = [(1, 2), (3, 4)]
l = []
for x, y in t:
    l.append(x + y)
print(l)

