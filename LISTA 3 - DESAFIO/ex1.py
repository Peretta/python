n = int(input('Número: '))
i = 1

while i * (i+1) * (i+2) < n:
    i = i+1
if i * (i+1) * (i+2) == n:
    print(f'É um número triangular \n {i}*{i+1}*{i+2}*={n}')
else:
    print('Não é um número triangular')