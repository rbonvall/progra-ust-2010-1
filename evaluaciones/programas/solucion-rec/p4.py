def son_anagramas(p1, p2):
    l1 = list(p1)
    l2 = list(p2)
    l1.sort()
    l2.sort()
    return l1 == l2

