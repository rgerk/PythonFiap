nota1 = int( input("Digite a nota 1: "))
nota2 = int( input("Digite a nota 2: "))

media = (nota1 + nota2) / 2

if media >= 6:
    print("VOCE FOI APROVADO: " + "MEDIA: ", media)
elif media < 4:
    print("VOCE ESTA EM REPROVADO:" + "MEDIA: ", media)
else:
    print("VOCE ESTA EM RECUPERACAO: " + "MEDIA: ", media)   
