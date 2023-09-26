#Faça um algoritmo que leia uma variável e some 5 caso seja par ou some 8 caso seja ímpar, imprimir o resultado desta operação. 

a = int(input("Digite um número:"))

if a % 2 == 0:
    print(a+5)
else:
    print(a+8)