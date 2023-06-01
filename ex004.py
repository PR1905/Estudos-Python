objeto = input('Vamos testar a classe do que você escrever: ')

print('O tipo primitivo desse valor é:', type(objeto))
print('O seu objeto é composto apenas de espaços?', objeto.isspace())
print('O seu objeto é alfanumérico?', objeto.isalnum())
print('O seu objeto é todo em maíusculo?', objeto.isupper())
print('O seu objeto é todo em minúsculo?', objeto.islower())
print('O seu objeto é um número?', objeto.isnumeric())