import random
print('******************* Iniciando jogo *******************')
lista = ['pedra','papel','tesoura']
escolha_usoario = str(input('Digite sua escolha:'))
escolha = random.choice(lista)




if (escolha_usoario == 'pedra') and (escolha == 'papel'):
    print('A maquina escolheu {}'.format(escolha))
    print('Que pena,você perdeu!')
    x = input('Digite [S] para continuar ou [F] para finalizar tudo MAIÚSCULO!! :')

    while x == 'S':
        escolha_usoario = str(input('Digite sua escolha:'))
        print('A maquina escolheu {}'.format(escolha))
        print('Que pena,você perdeu!')
    
    else:
        print('Tchau')


if (escolha_usoario == 'tesoura') and (escolha == 'pedra'):
    print('A maquina escolheu {}'.format(escolha))
    print('Que pena,você perdeu!')
    x = input('Digite [S] para continuar ou [F] para finalizar tudo MAIÚSCULO!! :')
    
    while x == 'S':
        escolha_usoario = str(input('Digite sua escolha:'))
        print('A maquina escolheu {}'.format(escolha))
        print('Que pena,você perdeu!')
    
    else:
        print('Tchau')
        

if (escolha_usoario == 'papel') and (escolha == 'tesoura'):
    print('A maquina escolheu {}'.format(escolha))
    print('Que pena,você perdeu!')
    x = input('Digite [S] para continuar ou [F] para finalizar tudo MAIÚSCULO!! :')
    print('A maquina escolheu {}'.format(escolha))
    print('Que pena,você perdeu!')

    while x == 'S':
        escolha_usoario = str(input('Digite sua escolha:'))
    
    else:
        print('Tchau')
    
        

else:
    print('A maquina escolheu {}'.format(escolha))
    print('Que legal,você ganhou!')
    x = input('Digite [S] para continuar ou [F] para finalizar tudo MAIÚSCULO!! :')

    if x == 'S':
        escolha_usoario = str(input('Digite sua escolha:'))
        print('A maquina escolheu {}'.format(escolha))
        print('Que pena,você perdeu!')
    
    else:
        print('Tchau')

print('******************* Fim de jogo *******************')
        

