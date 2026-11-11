# Faça um programa em Python que tenha como objetivo:
# Verificar se os valores de entrada forma um triângulo ou não (emitir mensagem (string) identifica a dos exemplos),
# Caso os valores de entrada formem um triângulo, identificar o tipo de triângulo (emitir mensagem (string) identifica a dos exemplos).


# Para isso seu programa deve ter uma função para:

# 1) Verificação da Formação de um Triângulo: 

# A primeira função, eh_triangulo(a, b, c), é responsável por verificar se os três lados podem formar um triângulo. Para isso, a função aplica a condição fundamental da geometria:

# O comprimento de cada lado deve ser menor que a soma dos outros dois lados. Isso pode ser expresso matematicamente como:

# a + b > c

# a + c > b

# b + c > a

# Se todas essas condições forem verdadeiras, os lados formam um triângulo e desta forma deve ser emitida a mensagem: Os lados formam um triângulo 
# Caso contrário, o programa deve emitir a mensagem: Os lados não formam um triângulo



# 2) Identificação do Tipo de Triângulo
# Caso as medidas formem um triângulo, a segunda função, tipo_triangulo(a, b, c), é chamada para determinar o tipo do triângulo:

# Equilátero: Todos os lados são iguais (a = b = c).
# Isósceles: Dois lados são iguais (a = b ou b = c ou a = c).
# Escaleno: Todos os lados são diferentes (a ≠ b ≠ c).
# A função retorna uma string indicando o tipo de triângulo.




# ENTRADA DE DADOS
# O usuário deve fornecer três valores numéricos inteiros que representam as medidas dos lados de um triângulo. Cada valor deve ser maior que zero.



# SAÍDA DE DADOS
# O programa deve fornecer feedback ao usuário:

# Se os lados formam um triângulo, deve emitir a mensagem Os lados formam um triângulo em uma linha e na outra linha o tipo de triângulo que pode ser Equilátero, Isósceles ou Escaleno


# Se os lados não formam um triângulo, deve emitir a mensagem Os lados não formam um triângulo

def entrada():
    return(int(input()), int(input()), int(input()))

def verifica_triangulo(a, b, c):
    return a + b > c and a + c > b and b + c > a

def tipo_triangulo(a, b, c):
    if a == b == c:
        return "Equilátero"
    elif a == b or b == c or a == c:
        return "Isósceles"
    else:
        return "Escaleno"

def main():
    a, b, c = entrada()
    if verifica_triangulo(a, b, c):
        print("Os lados formam um triângulo")
        print(tipo_triangulo(a, b, c))
    else:
        print("Os lados não formam um triângulo")
main()