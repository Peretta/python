lim = int(input('N: '))

a, b = 1, 1
c = 0
while c < lim:
    c = a + b
    print (f'{a} + {b} = {c}')
    a = b
    b = c