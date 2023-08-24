preco = int(input('Preço: '))
pagamento =  int(input('Pagamento: '))
notas = [50, 20, 10, 5, 2, 1]

troco = pagamento - preco

for nota in notas:
    while troco >= nota:
        print(f'Uma nota de {nota}')
        troco -= nota