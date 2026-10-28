# Desenvolva um programa em Python para gerenciar uma conta corrente com um saldo inicial de R$1000,00. O programa deve apresentar um menu com as seguintes opções:

# Mostrar Saldo: Exibe o saldo atual da conta.
# 1 - Sacar: Permite ao usuário sacar um valor da conta, desde que haja saldo suficiente. Exibe o saldo atualizado (se não for possível sacar, irá aprsentar o saldo atual sem alteração de value).
# 3 - Depositar: Permite ao usuário depositar um valor na conta. Exibe o saldo atualizado.
# 4 - Sair: Encerra o programa.
# Controle de Fluxo:
# O programa deve exibir o menu e permitir que o usuário escolha uma opção até que o usuário escolha a opção de sair (opção 4).




# Entrada
# O usuário deve informar o número da opção desejada a cada repetição do menu.

# Se a opção for 2: o usuário informa o valor a sacar;

# Se a opção for 3: o usuário informa o valor a depositar.



# Saída
# Se a opção for 1: exibe o saldo atual da conta, com 2 casas decimais e apresenta o menu novamente;

# Se a opção for 2: após receber p valor do saque e atualizar o saldo, exibe o saldo atual da conta, com 2 casas decimais e apresenta o menu novamente;

# Se a opção for 3: após receber p valor do despósito e atualizar o saldo, exibe o saldo atual da conta, com 2 casas decimais e apresenta o menu novamente;

# Se a opção for 4: encerra o programa.

saldo = 1000.0
opcao = int(input(""))

while opcao != 4:
    if opcao == 1:
        print(f"{saldo:.2f}")
    elif opcao == 2:
        saque = float(input(""))
        if saque <= saldo:
            saldo -= saque
            print(f"{saldo:.2f}")
        else:
            print(f"{saldo:.2f}")
    elif opcao == 3:
        deposito = float(input(""))
        saldo += deposito
        print(f"{saldo:.2f}")
    elif opcao == 4:
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção entre 1 e 4.")
    opcao = int(input(""))
