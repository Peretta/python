a = int(input('A: '))
b = int(input('B: '))
c = int(input('C: '))

if a>b and a>c:
    print('O maior número é: ',a)
elif b>a and b>c:
    print('O maior número é: ',b)
elif c>a and c>b:
    print('O maior número é: ',c)
else:
    print('Os números são iguais.')