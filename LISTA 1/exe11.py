#1º Passo) Converter o valor da potência em string
potencia = 2 ** 10000
potencia = str(potencia)

#2º Passo) Utilizar a função len para contar a quantidade de caracteres.
digitos = len(potencia)

#3º Passo) Imprimir o valor de digitos ao usuário
print (f"2 elevado a 1 milhão tem {digitos} digitos")