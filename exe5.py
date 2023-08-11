#1º Passo) Receber o valor do produto e a porcentagem do desconto.
preco_sem_desconto = float(input("Digite o preço da mercadoria: "))
porcentagem = float(input("Digite a porcentagem do desconso: "))

#2º Passo) Calcular o valor do desconto e o preço atualizado.
desconto = porcentagem/100 * preco_sem_desconto
preco_com_desconto = preco_sem_desconto  - desconto

#3º Passo) Informar ao cliente a quantidade do desconto e o preço a pagar.
print('Valor do desconto:', desconto, '\n', 'Preço a pagar', preco_com_desconto)