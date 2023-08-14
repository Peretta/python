a = int(input('Lado A: '))
b = int(input('Lado B: '))
c = int(input('Lado C: '))  

if a > b+c or b > c+a or c > a+b:
    print('Não é um triângulo. \nUm dos lados é maior que a soma dos outros!')
elif a == b == c:
    print('É um triângulo Equilátero')
elif a != b != c:
    print('É um triângulo Escaleno')
else:
    print('É um triângulo Isósceles')


