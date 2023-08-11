#1º Passo) Receber a temperatura em fahrenheit.
F = float(input('Digite o valor da temperatura em graus Fahrenheit: '))

#2º Passo) Realizar a conversão
C = float(5 * (F-32)/9) 

#3º Passo) Mostrar a conversão ao usuário
print(F,"F = ", C,"ºC")