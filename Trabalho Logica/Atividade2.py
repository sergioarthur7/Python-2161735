#Faça um algoritmo que leia o nome, o sexo e o estado civil de uma pessoa. Caso sexo seja “F” e
estado civil seja “CASADA”, solicitar o tempo de casada (anos). 

nome = input("Qual o seu nome?")
sexo = input("Qual o seu sexo? F ou M:")
estciv = input("Qual o seu estado civil? C ou S:")
tempo = 0

if sexo == "F" or "f" and estciv == "C" or "c":
    tempo = input("Qual o seu tempo de casada?")
    