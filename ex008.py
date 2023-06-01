#Escreva um programa que leia um número em metros e o converta em centímetros e milímetros.
m = int(input('Digite um número em metros: '))
cm = m * 100
mm = cm * 100
print('{}m equivalem a {}cm e {}mm.'.format(m, cm, mm))