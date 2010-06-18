t1 = (20, 0, 4)
t2 = (20, 1)
print(t1 < t2)

s = 'waka waka'
w = s.split('a')
print(w[1])

x, y = ((27, 3), 9)
z, w = x
print(y + w)

d = {7: 8, 3: 1}
s = 0
for k in d:
    s = s + d[k]
print(s)

d = {}
for i in range(20):
    d[i % 3] = i
print(len(d))

p = 'decentemente'
s = set(p)
l = list(s)
l.sort()
print(l[0])


