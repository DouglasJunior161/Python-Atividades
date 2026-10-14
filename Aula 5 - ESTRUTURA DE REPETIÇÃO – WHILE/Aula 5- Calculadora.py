# Faremos um programa em Python para resolver o seguinte problema: 

# Elabore um programa em Python que mostre um menu para o usuário escolher uma operação ou sair do programa. Por exemplo:  \

 

# Soma .................... + 

# Subtração ............. - 

# Multiplicação......... * 

# Divisão................... / 

# Sair ....................... 0 

 

# O programa deve reconhecer a opção escolhida pelo usuário e solicitar a entrada de dois números caso a opção escolhida seja uma das operações. 
# Depois de fazer a operação e mostrar o resultado , o programa deve continuar em execução para que o usuário selecione operação e outros números. O programa só terminará , caso o usuário digite 0. 

print("Calculadora, digite qual operação deseja realizar:\nSoma - +\nSubtração - -\nMultiplicação - *\nDivisão - /\nSair - 0")


opcao = input("Escolha uma opção: ")

while opcao != "0":
    if opcao == "+":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 + num2
        print(f"O resultado da soma é: {resultado}")
    elif opcao == "-":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 - num2
        print(f"O resultado da subtração é: {resultado}")
    elif opcao == "*":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 * num2
        print(f"O resultado da multiplicação é: {resultado}")
    elif opcao == "/":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        if num2 != 0:
            resultado = num1 / num2
            print(f"O resultado da divisão é: {resultado}")
        else:
            print("Erro: Divisão por zero não é permitida.")
    else:
        print("Opção inválida. Tente novamente.")

    opcao = input("\nEscolha uma opção (ou digite 0 para sair): ")