n = int(input())
is_prime = True
for d in range(2, n//2 + 1):
    if n % d == 0:
        is_prime = False

if is_prime:
    print('primo')
else:
    print('compuesto')

