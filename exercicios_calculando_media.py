nota_1 = float(input('Dgite a primeira nota:'))
nota_2 = float(input('Dgite a segunda  nota:'))

media = nota_1 + nota_2     
try:
    if media >= 9.0 and media <= 10:
        print('O aluno recebeu nota "A"')
        print('Está aprovado!')
    elif media >= 7.5 and media < 9:
        print('O aluno recebeu nota "B"')
        print('Está aprovado!')
    elif media >=6 and media >7.5:
        print('O aluno recebeu nota "C"')
        print('Está aprovado!')
    elif media >= 4 and media < 6:
        print('O aluno recebeu nota "D"')
        print('Está reprovado!')
    else:
        print('O aluno recebeu nota "E"')
        print('Está reprovado!')

except:
    print('Você não digitou um valor valido!')