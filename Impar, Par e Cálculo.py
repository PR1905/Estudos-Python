'''
NOTAS
% para calcular o resto de uma divisão
== para realizar um cálculo
'''
from time import sleep
n = int(input('\033[36mDigite algum número qualquer: '))
m = n % 2
print('\033[30mAnalisando o número\033[m \033[36m{}\033[m'.format(n))
sleep(2)
if m == 0:
    print('\033[35m=\033[m' * 17)
    print('\033[34mEsse número é par')
    print('\033[35m=\033[m'* 17)
else:
    print('\033[35m=\033[m' * 20)
    print('\033[31mEsse número é impar')
    print('\033[35m=\033[m' * 20)
print('\033[7;30m--FIM--\033[m')
