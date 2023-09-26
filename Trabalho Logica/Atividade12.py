#Escreva um algoritmo que leia o número de identificação, as 3 notas obtidas por um aluno nas 3 verificações e a média dos exercícios que fazem parte da avaliação, e calcule a média de aproveitamento. A atribuição dos conceitos obedece a tabela abaixo. O algoritmo deve escrever o número do aluno, suas notas, a média dos exercícios, a média de aproveitamento, o conceito correspondente e amensagem 'Aprovado' se o conceito for A, B ou C, e 'Reprovado' se o conceito for D ou E. 

num_indent = input("Número de indentificação do aluno:")
nota1 = int(input("Nota 1:"))
nota2 = int(input("Nota 2:"))
nota3 = int(input("Nota 3:"))
med_exerc = float(input("Media dos exercicios:"))

med_aprov =  float(nota1 + nota2 * 2 + nota3 * 3 + med_exerc) / 7

if med_aprov >=90:
    print("Aprovado, A")
elif med_aprov >= 75 and med_aprov < 90:
    print("Aprovado, B")
elif med_aprov >= 60 and med_aprov < 75:
    print("Aprovado, C")
elif med_aprov >= 40 and med_aprov < 60:
    print("Reprovado, D")
else:
    print("Reprovado, E")