print ("Faça um programa que receba quatro números inteiros, calcule e mostre a soma desses números.")

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
n3 = int(input("Enter the third number: "))
n4 = int(input("Enter the fourth number: "))

result = (n1 + n2 + n3 + n4)

print(f"The sum of the four numbers is: {result}")


print ("Faça um programa que receba três notas, calcule e mostre a média aritmética entre elas.")

nota1 = float(input("Enter the first grade: "))
nota2 = float(input("Enter the second grade: "))
nota3 = float(input("Enter the third grade: "))

media = (nota1 + nota2 + nota3) / 3

print(f"The average of the three grades is: {media:.2f}")

print ("Faça um programa que receba três notas e seus respectivos pesos, calcule e mostre a média ponderada dessas notas.")

nota1 = float(input("Enter the first grade: "))
nota2 = float(input("Enter the second grade: "))
nota3 = float(input("Enter the third grade: "))
peso1 = int(input("Enter the weight of the first grade: "))
peso2 = int(input("Enter the weight of the second grade: "))
peso3 = int(input("Enter the weight of the third grade: "))

media = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)

print(f"The average of the three grades is: {media}")

print ("Faça um programa que receba o salário de um funcionário, calcule e mostre o novo salário, sabendo-se que este sofreu um aumento de 25%.")

salario = float(input("Enter the employee's salary: "))
novo_salario = salario * 1.25
print(f"The new salary of the employee is: {novo_salario}")
