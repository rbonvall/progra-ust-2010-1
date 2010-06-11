l = 2 * [3, 4]
print(l)

s = {78, 15, 91, 15}
print(len(s))

d = {78: 15, 91: 15}
print(len(d))

c = (1990, 4, 9)
f = (1990, 1, 12)
print(c < f)

a, b, c = (1990, 4, 9)
d, e, f = (1990, 1, 12)
print(c < f)

a = 'gato'
a.replace('g', 'p')
print(a)

t = 'papagayo'
w = t.split('a')
print(w[3])

a = set('perro')
b = set('gato')
print(a | b)

a = {'perro'}
b = {'gato'}
print(a | b)

a = [2, 3, 5, 7, 9]
print(a[a[0]])

l = [[1, 2], [3, 4]]
print(len(l))

w = 'Viva Chile'
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
    l.append(x * y)
print(l)

