#Sorteie 20 inteiros entre 1 e 100 numa lista. Armazene os números pares na lista PAR e os números ímpares na lista IMPAR. Imprima as três listas.
#teste de mesa (passo a passo)

from random import sample

vetor = sample(range(100), 20)
print(vetor)
for x in vetor:
    if x % 2 == 0:
        print(f'{x} é par')
    else:
        print(f'{x} é impar')
