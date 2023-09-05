q = int(input('Quantidade de elementos do conjunto: '))
n = int(input('Digite um número: '))

resposta = []
binario = []
conjunto = []

i=0

def criar_conjunto(i, q):
    while i < q:
        e = input(f'{i+1}º elemento: ')
        conjunto.append(e)
        i = i+1
    return conjunto

def conversor(n):
    while n >=1 :
        binario.append(n%2)
        n = n//2

    while q > len(binario):
        binario.append(0)

    binario.reverse()
    return binario

def encontrando(i, binario, conjunto):
    for a in conjunto:
        if binario[i] == 1:
            resposta.append(a)
        i = i+1
    print(resposta)
    
criar_conjunto(i, q)
conversor(n)
encontrando(i, binario, conjunto)