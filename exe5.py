preco_sem_desconto = float(input("Digite o preço da mercadoria: "))
porcentagem = float(input("Digite a porcentagem do desconso: "))
desconto = porcentagem/100 * preco_sem_desconto
preco_com_desconto = preco_sem_desconto  - desconto
print('Valor do desconto:', desconto, '\n', 'Preço a pagar', preco_com_desconto)