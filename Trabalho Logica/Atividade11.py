# Elabore um algoritmo que calcule o que deve ser pago por um produto, considerando o preço
normal deetiqueta e a escolha da condição de pagamento. Utilize os códigos da tabela a seguir
para ler qual acondição de pagamento escolhida e efetuar o cálculo adequado. 

precodop = float(input("Digite o preço do produto:"))

print("Formas de pagamento")
print("1. À vista em dinheiro ou cheque, recebe 10% de desconto")
print("2. À vista no cartão de crédito, recebe 15% de desconto")
print("3. Em duas vezes, preço de etiqueta sem juros")
print("4. Em duas vezes, preço de etiqueta mais juros de 10%")


formadepg = int(input("Digite a forma de pagamento:"))

if formadepg == 1:
    print("Preço com desconto:", precodop - (precodop * 0.10))
elif formadepg == 2:
    print("Preço com desconto:", precodop - (precodop * 0.15))
elif formadepg == 3:
    print("Preço em duas vezes sem juros:", precodop / 2)
elif formadepg == 4:
    preco_com_juros = precodop + (precodop * 0.10)
    print("Preço em duas vezes com juros de 10%:", preco_com_juros / 2)
else:
    print("Opção de pagamento inválida.")
