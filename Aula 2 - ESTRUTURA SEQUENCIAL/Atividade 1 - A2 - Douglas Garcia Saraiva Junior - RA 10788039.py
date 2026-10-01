# EXERCÍCIO 1 – Escreva um programa em Python que permita ao usuário digitar dois números inteiros e exibir o resultado para cada uma das seguintes operações, nesta ordem: soma, subtração, multiplicação, divisão, divisão truncada, resto e exponenciação

print ("Exercício 1 - Digite dois números inteiros")

num1 = int(input())
num2 = int(input())

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2
divisao_truncada = num1 // num2
resto = num1 % num2
exponenciacao = num1 ** num2

print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")
print(f"Divisão Truncada: {divisao_truncada}")
print(f"Resto: {resto}")
print(f"Exponenciação: {exponenciacao}")

# EXERCÍCIO 2 – Faça um programa em Python que leia dois números inteiros e exiba o quadrado da diferença do primeiro valor pelo segundo. 

print (" Exercício 2 - Digite dois números inteiros")

numero1 = int(input())
numero2 = int(input())

diferenca = numero1 - numero2
quadrado_diferenca = diferenca ** 2

print(f"O quadrado da diferença é: {quadrado_diferenca}")

# EXERCÍCIO 3 – Faça um programa em Python que resolva o seguinte problema: 

# Um concurso possui um prêmio no montante de R$ 780.000,00 para dividir entre três ganhadores da seguinte forma: 

# - o primeiro ganhador receberá 46% do prêmio; 

# - o segundo ganhador receberá 32% do prêmio; 

# - o terceiro ganhador receberá o restante do prêmio. 

# Calcule e mostre o valor do prêmio de cada ganhador, nesta ordem: primeiro colocado, segundo colocado e terceiro colocado.

# Observe que este programa não tem valor de entrada feita pelo usuário. 

premio = 780000.00
Ganhador1 = premio * 0.46
Ganhador2 = premio * 0.32
Ganhador3 = premio - (Ganhador1 + Ganhador2)

print(f"Prêmio do primeiro ganhador: R$ {Ganhador1:.2f}")
print(f"Prêmio do segundo ganhador: R$ {Ganhador2:.2f}")
print(f"Prêmio do terceiro ganhador: R$ {Ganhador3:.2f}")