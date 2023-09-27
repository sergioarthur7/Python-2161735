#Escreva um algoritmo que lê dois valores booleanos (lógicos) e então determina se ambos são VERDADEIROS ou FALSOS.

t = bool(input('Digite True ou False: '))
f = bool(input('Digite True ou False: '))

t = t == 'True'
f = f == 'True'

if t and f:
    print('Ambos os valores são verdadeiros')
else:
    print('Ambos os valores não são verdadeiros')
