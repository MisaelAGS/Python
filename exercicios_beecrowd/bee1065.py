qtd_pares = 0
for i in range(5):
    num = int(input())
    if num % 2 == 0:
        qtd_pares += 1
print(f'{qtd_pares} valores pares')