#Escreva um algoritmo que lê dois valores booleanos (lógicos) e então determina se ambos são
VERDADEIROS ou FALSOS.

a = bool(input('Digite True ou False: '))
b = bool(input('Digite True ou False: '))

a = a == 'True'
b = b == 'True'

if a and b:
    print('Ambos os valores são verdadeiros')
else:
    print('Ambos os valores não são verdadeiros')