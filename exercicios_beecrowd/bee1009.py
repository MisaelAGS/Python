nome_vendedor = str(input())
num_salario_fixo = float(input())
num_vendas = float(input())
percentual_comissao = 15
num_salario_total = num_salario_fixo + (num_vendas * percentual_comissao / 100)
print('TOTAL = R$ {:.2f}'.format(num_salario_total))