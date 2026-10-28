# Você está desenvolvendo uma ferramenta para um workshop de matemática em uma escola. O instrutor deseja uma maneira simples de analisar um conjunto de números fornecidos pelos alunos. A ferramenta deve ser capaz de contar quantos desses números são pares e quantos são ímpares. O objetivo é facilitar a análise dos dados fornecidos e auxiliar os alunos na compreensão dos conceitos de números pares e ímpares.

# Para isso, desenvolva um programa em Python que solicite ao usuário a quantidade de números inteiros que ele deseja digitar. O programa deve então permitir a entrada desses números e, após o input, calcular e exibir, nesta ordem, a quantidade total de números pares e a quantidade total de números ímpares.



# Entrada
# Solicitar Quantidade de Números:
# O programa deve solicitar ao usuário a quantidade total de números que ele deseja digitar (n). O valor de n deve ser um número inteiro positivo.
# Entrada dos Números:
# O programa deve permitir ao usuário digitar n números inteiros, um por vez.




# Saída
# O programa deve exibir a quantidade total de números pares e a quantidade total de números ímpares, nesta ordem.

repeticao = int(input())
par = 0
impar = 0
for c in range(repeticao):
    num = int(input())
    if num % 2 == 0:
        par += 1
    else:
        impar += 1
print(f"{par}\n{impar}")