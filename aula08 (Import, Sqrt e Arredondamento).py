'''
NOTAS
"{:.2f}" para mostrar duas casas decimais. math.ceil para arrendondar para cima e math.floor para baixo.
Se utilizar "from math import", não precisa usar "math.", pode ser utilizado direto
'''
import math
n = int(input('Digite um número '))
raiz = int(math.sqrt(n))
print (raiz)