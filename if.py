vel = int(input('Você tem noção da velocidade em que você estava? '))
if vel > 80:
    valor= (vel-80)*7
    print('Você foi multado em R$', valor)
else:
    print('Você está dentro da velocidade permitida, dirija com moderação.')
    