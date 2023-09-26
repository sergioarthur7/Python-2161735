# Escreva um algoritmo que leia três valores inteiros e diferentes e mostre-os em ordem decrescente.

valor1 = int(input("Insira o primeiro valor inteiro: "))
valor2 = int(input("Insira o segundo valor inteiro: "))
valor3 = int(input("Insira o terceiro valor inteiro: "))

maior = max(valor1, valor2, valor3)

menor = min(valor1, valor2, valor3)

meio = valor1 + valor2 + valor3 - maior - menor

print(f"Os valores em ordem decrescente são: {maior}, {meio}, {menor}")