qnt = int(input('Digite a quantidade de cigarros fumados por dia: '))
anos = int(input('Digite a quantos anos você usa cigarro: '))
dias = anos*365
cigarros = qnt*dias
tempo = cigarros*(10/60/24)
print(tempo)