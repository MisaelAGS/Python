qtd_num = int(input())
for i in range(qtd_num):
    num_analisado = int(input())
    if num_analisado == 0:
        print('NULL')
    elif num_analisado % 2 == 0 and num_analisado < 0:
        print('EVEN NEGATIVE')
    elif num_analisado % 2 == 0 and num_analisado > 0:
        print('EVEN POSITIVE')
    elif num_analisado % 2 != 0 and num_analisado < 0:
        print('ODD NEGATIVE')
    elif num_analisado % 2 != 0 and num_analisado > 0:
        print('ODD POSITIVE')