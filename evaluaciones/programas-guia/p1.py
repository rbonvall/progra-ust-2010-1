s = 0
t = 0
for i in range(3):
    for j in range(3):
        s = s + 1
        if i < j:
            t = t + 1
    print(t)
    print(s)