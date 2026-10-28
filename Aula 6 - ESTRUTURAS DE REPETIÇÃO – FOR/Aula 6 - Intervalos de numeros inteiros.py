# Você está desenvolvendo um aplicativo educacional para um professor de matemática que deseja ajudar seus alunos a praticar a identificação e listagem de intervalos de números inteiros. O professor quer um programa que possa receber dois números inteiros e exibir todos os números inteiros que estão entre esses dois valores, excluindo os próprios limites. Esse exercício ajuda os alunos a entender conceitos de intervalos e sequências numéricas.

# Desta forma você deve criar um programa em Python que solicite ao usuário dois números inteiros e, com base nesses números, gere e exiba todos os números inteiros que estão no intervalo entre eles. Leve em consideração que o usuário irá informar o primeiro número menor que o segundo número.



# Entrada
# O programa deve solicitar ao usuário que insira dois números inteiros. Esses números definem os limites do intervalo.



# Saída
# O programa deve exibir todos os números inteiros que estão no intervalo entre os dois números fornecidos, um em cada linha.

num1 = int(input())
num2 = int(input())

for int in range(num1 + 1, num2):
    print(int)