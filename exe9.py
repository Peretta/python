#1º Passo) Receber o valor em km e dias.
km = float(input('Digite a quantidade de km rodados com o carro alugado: '))
dias = int(input('Digite a quantidade de dias que você utilizou o carro: '))

#2º Passo) Calcular o valor a ser pago em dias e por km rodado.
preco = 60*dias + 0.15*km

#2º Passo) Imprimir valor para o usuário
print('O valor a ser pago é: ', preco)