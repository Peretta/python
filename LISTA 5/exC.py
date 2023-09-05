pares = []
for i in range(1067, 3627):
    if i%2 == 0 and i%7 == 0:
        pares.append(i)
print(len(pares))