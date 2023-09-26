import time

nome = input("Qual seu nome?")
print("Prazer em te conhecer", nome)

time.sleep(2)

salario = float(input("Digite seu salário:"))
    
if salario <= 2112.00:
    print("Você está isento de pagar o IR (imposto de renda)", salario)
        
elif salario <= 2826.65:
    calcs = salario - (salario * 0.075)
    print("Você pagou uma taxa de 7,5%. Seu salario agora é de:", round(calcs, 2))
    
elif salario <= 3751.05:
    calcs = salario - (salario * 0.15)
    print("Você pagou uma taxa de 15%. Seu salario agora é de:", round(calcs, 2))
elif salario <= 4664.68:
    calcs = salario - (salario * 0.225)
    print("Você pagou uma taxa de 22,5%. Seu salario agora é de:", round(calcs, 2))
else:
    calcs = salario - (salario * 0.275)
    print("Você pagou uma taxa de 27,5%. Seu salario agora é de:", round(calcs, 2))