#1º Passo) Receber valores de dias, horas, minutos e segundos
dias = int(input("Digite uma quantidade de dias: "))
horas = int(input("Digite uma quantidade de horas: "))
minutos = int(input("Digite uma quantidade de minutos: "))
segundos = int(input("Digite uma quantidade de segundos: "))

#2º Passo) Converter valores de dias, horas, minutos para segundos e depois somar
segundos_finais = (dias*24*60*60)+(horas*60*60)+(minutos*60)+(segundos)

#3º Passo) Imprimir valores para o usuário
print("Isso corresponde a ",segundos_finais, "segundos")