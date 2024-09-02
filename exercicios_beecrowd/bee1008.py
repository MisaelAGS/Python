num_funcionario = int(input())
num_horas_trabalhadas = int(input())
num_salario_por_hora = float(input())
num_salario_total = num_salario_por_hora * num_horas_trabalhadas
print(f'NUMBER = {num_funcionario}')
print('SALARY = U$ {:.2f}'.format(num_salario_total))