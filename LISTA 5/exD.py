numeros = []
for i in range(18644, 33087):
    if '2' in str(i) and '7' not in str(i):
        numeros.append(i)

print(len(numeros))