#1º Passo) Receber a quantidade de cigarros por dia e a quantidade de anos de uso
qnt = int(input('Digite a quantidade de cigarros fumados por dia: '))
anos = int(input('Digite a quantos anos você usa cigarro: '))

#2º Passo) Calcular quantos cigarros são fumados por dia e quantos dias são perdidos com cada cigarro
cigarros_dias = anos*365*qnt
tempo = cigarros_dias*(10/60/24)

#3º Passo) Mostrar ao usuário quantos dias de vida foram rezidos
print("Dias de vida diminuidos em: ",tempo, "dias")