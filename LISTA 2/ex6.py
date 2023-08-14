ganho = float(input("Ganho/Hora: "))
horas = float(input('Horas/mês: '))

salarioBruto = ganho*horas
impostoRenda = 0.11*salarioBruto
inss = 0.08*salarioBruto
sindicato = 0.05*salarioBruto
salarioLiquido = salarioBruto - impostoRenda - inss - sindicato

print(f'Salário Bruto: ${salarioBruto:.2f}\nImposto de renda: R${impostoRenda:.2f}\nINSS: R${inss:.2f}\nSindicato: R${sindicato:.2f}\nSalário Liquido: R${salarioLiquido:.2f}')