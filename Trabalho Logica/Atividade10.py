#  O IMC – Indice de Massa Corporal é um critério da Organização Mundial de Saúde para dar uma indicação sobre a condição de peso de uma pessoa adulta. A fórmula é IMC = peso / ( altura )2 Elabore um algoritmo que leia o peso e a altura de um adulto e mostre sua condição de acordo com a tabela abaixo. 

peso = float(input("Qual o seu peso:"))
altura = float(input("Qual é a sua altura:"))

imc = peso/(altura**2)

if imc < 16:
    print("Magreza grave", round(imc,1))
elif imc <= 16.9:
    print("Magreza moderada", round(imc, 1))
elif imc <= 18.4:
    print("Magreza leve", round(imc, 1))
elif imc <= 24.9:
    print("Peso normal", round(imc, 1))
elif imc <= 29.9:
    print("Sobrepeso", round(imc, 1))
elif imc <= 34.9:
    print("Obesidade grau 1 (leve)", round(imc, 1))
elif imc <= 39.9:
    print("Obesidade grau 2 (moderada)", round(imc, 1))
else:
    print("Obesidade grau 3 (grave)", round(imc, 1))

