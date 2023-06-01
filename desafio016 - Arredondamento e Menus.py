'''
NOTAS
":.0f" continua sendo valor float, apesar de mostrar um valor inteiro.
A funcionalidade do int() e do trunc() é a mesma.
Para arredondamento preciso de acordo com as regras matemáticas, usar round().
'''
def Inteiro():
    n=float(input('Digite um número quebrado: '))
    print('O valor transformado em inteiro é {}'.format(int(n)))
    print('O tipo do número é {}'.format(type(int(n))))

def Quebrar():
    n=float(input('Digite um número quebrado: '))
    print('O valor quebrado como inteiro é {:.0f}'.format(n))
    print('O tipo do número é {}'.format(type(n)))

def Truncar():
    from math import trunc
    n=float(input('Digite um número quebrado: '))
    print('O valor truncado é {}'.format(trunc(n)))
    print('O tipo do número é {}'.format(type(trunc(n))))

def Arredondar():
    n=float(input('Digite um número quebrado: '))
    print('O valor arredondado é {}.'.format(round(n)))
    print('O tipo do número é {}'.format(type(round(n))))

def Menu():
    Escolha = int(input('''Digite a função que você quer rodar
0 = Inteiro
1 = Quebrar
2 = Truncar
3 = Arredondar
Sua escolha é: '''))
    if Escolha == 0:
        Inteiro()
    elif Escolha == 1:
        Quebrar()
    elif Escolha == 2:
        Truncar()
    elif Escolha == 3:
        Arredondar()
    else:
        print('Selecione uma opção válida')
        Menu()

Menu()
