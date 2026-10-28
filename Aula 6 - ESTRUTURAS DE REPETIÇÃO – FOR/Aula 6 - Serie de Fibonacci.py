# Problema clássico usando for: Série de Fibonacci

# Nesta videoaula, resolver emos o seguinte problema em Python: 

# A Sequência de Fibonacci é a sequência numérica proposta pelo matemático Leonardo Pisa, mais conhecido como Fibonacci:  

# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ... 

 

# Foi a partir de um problema criado por ele que Fibonacci detectou a existência de uma regularidade matemática. Trata-se do exemplo clássico  que aparece em muitos fenômenos da natureza. 

# Analisaremos o que acontece nesta série, que é infinita, pela perspectiva da lógica de programação e implementaremos um programa em Python que mostre os oito primeiros números desta série.  

 

# Curiosidade: Veja o link a seguir  para conhecer como a série de Fibonacci está presente na natureza.  

n1 = 1
n2 = 1
for i in range(8):
    print(n1, end=" ")
    n3 = n1 + n2
    n1 = n2
    n2 = n3