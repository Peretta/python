#Faça um programa que crie dois vetores com 10 elementos aleatórios entre 1 e 100. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores. Imprima os três vetores.

from random import randint

vetorA = []
vetorB = []
vetorC = []


for x in range(10):
    y = randint(1, 100)
    vetorA.append(y)
    vetorC.append(y)
    y = randint(1, 100)
    vetorB.append(y)
    vetorC.append(y)

print(vetorA)
print(vetorB)
print(vetorC)