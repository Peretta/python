def infoUser(excesso, multa):
    print('Excesso: ', excesso)
    print('Multa: ', multa)

peso = int(input("Peso: "))
excesso = 0
multa = 0
if peso < 50:
    infoUser(excesso, multa)
else:
    excesso = peso-50
    multa = excesso*4
    infoUser(excesso, multa)
