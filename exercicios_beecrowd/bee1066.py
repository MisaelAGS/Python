qtd_pares = 0
qtd_impares = 0
qtd_positivos = 0
qtd_negativos = 0
for i in range(5):
    num = int(input())
    if num % 2 == 0:
        qtd_pares += 1
    if num % 2 != 0:
        qtd_impares += 1
    if num > 0:
        qtd_positivos += 1
    if num < 0:
        qtd_negativos += 1
print(f'{qtd_pares} valor(es) par(es)')
print(f'{qtd_impares} valor(es) impar(es)')
print(f'{qtd_positivos} valor(es) positivo(s)')
print(f'{qtd_negativos} valor(es) negativo(s)')