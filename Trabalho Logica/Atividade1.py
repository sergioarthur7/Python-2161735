#Faça um algoritmo que leia os valores A, B, C e imprima na tela se a soma de A + B é menor
que C. 

a = float(input("Digite um número:"))
b = float(input("Digite um número:"))
c = float(input("Digite um número:"))

soma = a+b

if soma < c:
    print("A soma de a + c e menor que c", soma)