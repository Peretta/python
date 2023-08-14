a = int(input('A: '))
b = int(input('B: '))
c = int(input('C: '))

if a<b and a<c:
    print('O menor número é: ',a)
elif b<a and b<c:
    print('O menor número é: ',b)
elif c<a and c<b:
    print('O menor número é: ',c)
else:
    print('Os números são iguais.')