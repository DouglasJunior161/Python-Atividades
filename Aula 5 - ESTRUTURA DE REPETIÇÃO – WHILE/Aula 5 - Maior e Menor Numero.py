# Faremos o programa em Python para resolver o seguinte problema: 

# Elabore um programa em Python que solicite um conjunto de números (encerrando a entrada de dados com 0) .  

# Determine o menor e o  maior valor do conjunto e a soma dos valores  digitados.

print("Digite um conjunto de números (digite 0 para encerrar):")
numero = float(input("Digite um número: "))

soma = 0
maior = numero
menor = numero

while numero != 0:
    soma += numero
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
    numero = float(input("Digite um número: "))

print(f"O maior valor é: {maior}")
print(f"O menor valor é: {menor}")
print(f"A soma dos valores é: {soma}")