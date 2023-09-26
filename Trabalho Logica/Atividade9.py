# Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que calcule seu peso ideal.

altura = float(input("Qual sua altura?"))
sexo = input("Qual o seu sexo? F ou M:")

pesoidealm = (72.7 * altura) - 58
pesoidealf = (62.1 * altura) - 44.7

if sexo == "F" or "f":
    print(round(pesoidealf, 1))
elif sexo == "M" or "m":
    print(round(pesoidealm, 1))
else:
    print("Sexo não identificado")