#1º Passo) Receber o salário e a porcentagem do aumento.
salario_atual = float(input('Digite o sálario: R$'))
porcetagem = float(input('Digite a porcetagem do aumento salarial: '))

#2º Passo) Calcular o valor do aumento e reajustar salário
aumento = porcetagem/100*salario_atual
salario_final = salario_atual + aumento

#3º Passo) Imprimir o aumento e o salario final
print(salario_atual, " com um aumento de R$", aumento, " corresponde a: ", salario_final)