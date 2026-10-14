# Faça um programa em Python para um caixa de mercado que imprima um recibo de compras.

# O programa deve receber o nome de N produtos que estão sendo comprados (N simboliza uma quantidade variada). A  entrada das informações da compra encerram quando o usuário digitar para o nome do produto a palavra fim.

# Este progama também deve receber as informações de quantidade e valor unitário, nesta ordem de cada um destes produtos, exceto do que finaliza a entrada de dados (produto de nome fim).

# Exiba o valor total de cada produto comprado e no final o valor total das compras de todos os produtos.





# Entrada
# Nome do produto, em letra minúscula;

# Quantidade do produto;

# Valor unitário do produto.



# Saída
# Valor total de cada produto, com 2 cassaas decimais;

# No final valor total das compras,com 2 cassaas decimais.


resultado = 0
multiplicacao = 0
produto = input("")

while produto != "fim": 
    
    if produto != "fim":
        unidade = int(input(""))
        preco = float(input(""))
        multiplicacao = unidade * preco
    print(f"{multiplicacao:.2f}")
    resultado += multiplicacao
    produto = input("")


print(f"{resultado:.2f}")
