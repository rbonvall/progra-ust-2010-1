print('p    q    r    predicado')

for p in [True, False]:
    for q in [True, False]:
        for r in [True, False]:
            print(p, q, r, (not p or q) and not r)
