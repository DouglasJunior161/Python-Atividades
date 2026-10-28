# Faça um programa em Python que calcule e apresente o fatorial de um número inteiro e natural fornecido pelo usuário.  

 

# Exemplo: 5! = 5 x 4 x 3 x 2 x 1=120.   

# Por definição 0! = 1. 

num = int(input("Escreva um numero e farei o fatorial: "))
numfat = num

for c in range(numfat - 1, 0, -1):
    numfat *= c
print(f"{num}! = {numfat}")