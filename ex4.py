salario_atual = float(input('Digite o sálario: R$'))
modulo_da_porcetagem = float(input('Digite a porcetagem do aumento salarial: '))
porcetagem = modulo_da_porcetagem/100
salario_final = salario_atual + (salario_atual*porcetagem)
print(salario_atual, " com ", modulo_da_porcetagem, "% de aumento corresponde a: ", salario_final)