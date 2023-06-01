import random
from time import sleep

pcgame = ['Pedra', 'Papel', 'Tesoura']
pcescolha = random.choice(pcgame)

print('''Sua opções
[0] Pedra
[1] Papel
[2] Tesoura
''')
escolha = int(input('Qual é a sua jogada ? '))
def inicio():
    sleep(1)
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO')
    sleep(1)

if escolha == 0 or escolha == 1 or escolha == 2:
    if escolha == 0 and pcescolha == 'Tesoura':
        inicio()
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('O computador jogou {}'.format(pcescolha))
        print('Você jogou Pedra')
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('Jogador vence')
    elif escolha == 0 and pcescolha == 'Papel':
        inicio()
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('O computador jogou {}'.format(pcescolha))
        print('Você jogou Pedra')
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('Computador vence')
    elif escolha == 0 and pcescolha == 'Pedra':
        inicio()
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('O computador jogou {}'.format(pcescolha))
        print('Você jogou Pedra')
        print('EMPATE')
    elif escolha == 1 and pcescolha == 'Pedra':
        inicio()
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('O computador jogou {}'.format(pcescolha))
        print('Você jogou Papel')
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('Jogador vence')
    elif escolha == 1 and pcescolha == 'Tesoura':
        inicio()
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('O computador jogou {}'.format(pcescolha))
        print('Você jogou Papel')
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('Computador vence')
    elif escolha == 1 and pcescolha == 'Papel':
        inicio()
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('O computador jogou {}'.format(pcescolha))
        print('Você jogou Papel')
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('Empate')
    elif escolha == 2 and pcescolha == 'Papel':
        inicio()
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('O computador jogou {}'.format(pcescolha))
        print('Você jogou Tesoura')
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('Jogador vence')
    elif escolha == 2 and pcescolha == 'Pedra':
        inicio()
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('O computador jogou {}'.format(pcescolha))
        print('Você jogou Tesoura')
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('Computador vence')
    elif escolha == 2 and pcescolha == 'Tesoura':
        inicio()
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('O computador jogou {}'.format(pcescolha))
        print('Você jogou Tesoura')
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('EMPATE')
else:
    print('Opção Invalida')