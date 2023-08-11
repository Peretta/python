dias = int(input("Digite uma quantidade de dias: "))
horas = int(input("Digite uma quantidade de horas: "))
minutos = int(input("Digite uma quantidade de minutos: "))
segundos = int(input("Digite uma quantidade de segundos: "))

dias = dias*24*60*60
horas = horas*60*60
minutos = minutos*60
segundos = dias+horas+minutos+segundos

print("Isso corresponde a ",segundos, "segundos")