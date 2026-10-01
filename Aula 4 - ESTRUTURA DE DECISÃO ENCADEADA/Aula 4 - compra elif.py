valor_compra = float(input())
codigo_pagamento = int(input())

a_vista = valor_compra * 0.1
credito = valor_compra * 0.05
parcela5x = valor_compra / 5
parcela10x = valor_compra / 10
acrescimo = parcela10x * 0.15

if codigo_pagamento == 1:
    print(f'{valor_compra - a_vista:.2f}')
elif codigo_pagamento == 2:
    print(f'{valor_compra - credito:.2f}')
elif codigo_pagamento == 3:
    print(f'{parcela5x:.2f}')
elif codigo_pagamento == 4:
    print(f'{parcela10x + acrescimo:.2f}')