#1º Passo) Receber a distância e a velocidade média.
distancia = float(input("Digite a distância da viagem em Km: "))
velocidade = float(input("Digite a velocidade média do carro durante a viagem em Km/h: "))

#2º Passo) Realizar o cálculo de horas
horas = distancia/velocidade

#3º Passo) Informar ao cliente as horas que serão levadas.
print('O tempo para a conclusão desta viagem será de: ', horas, "h")