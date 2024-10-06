qtd_positivos = 0
soma_valores_positivos = 0
for i in range(6):
    num = float(input())
    if num > 0:
        qtd_positivos += 1
        soma_valores_positivos += num
print(f'{qtd_positivos} valores positivos')
print('{:.1f}'.format(soma_valores_positivos / qtd_positivos))