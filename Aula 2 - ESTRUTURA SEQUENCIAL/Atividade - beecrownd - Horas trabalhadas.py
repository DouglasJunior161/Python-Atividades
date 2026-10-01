reais_hora = float(input())
horas_trabalhadas = int(input())

salario_bruto = reais_hora * horas_trabalhadas
inss = salario_bruto * 0.08
taxa_sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - inss - taxa_sindicato

print(f"{salario_bruto:.2f}")
print(f"{inss:.2f}")
print(f"{taxa_sindicato:.2f}")
print(f"{salario_liquido:.2f}") 