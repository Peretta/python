#Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra o maior e o menor valor, sem usar as funções max e min
from random import sample
#sortear um número
vetor = sample(range(100), 10)
maior = vetor[0]
menor = vetor[0]

for x in vetor:
    if maior < x:
        maior = x
    if menor > x:
        menor = x
    
print('Lista: ', vetor)
print('Maior: ', maior)
print('Menor: ', menor)