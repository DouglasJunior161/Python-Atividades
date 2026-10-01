tipo_investimento = int(input())
valor_investido = float(input())
meses = int(input())

if tipo_investimento == 1:
    valor_futuro = valor_investido * (1 + 0.005) ** meses
    print(f'{valor_futuro:.2f}')
elif tipo_investimento == 2:
    valor_futuro = valor_investido * (1 + 0.008) ** meses
    print(f'{valor_futuro:.2f}')
elif tipo_investimento == 3:
    valor_futuro = valor_investido * (1 + 0.01) ** meses
    print(f'{valor_futuro:.2f}')