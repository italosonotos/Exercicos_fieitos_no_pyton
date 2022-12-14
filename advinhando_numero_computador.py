import random
print('#### Iníciando Jogo ####')
x = random.randint(0,100)
chance = 10
chute = input('Chute um número entre 0 a 100: ')


while chute != x:
    chute = int(chute)
    chance = chance -1
    print('Você errou, ainta tem {}',format(chance),'chances')
    chute = input('Chute um número entre 0 a 100: ')

    if chute == x:
        print('Parabens!! Você acertou!!')

    else:
        if chute > x:
            print('Você errou!!! Dica: É um número menor.')
        else:
            print('Você errou!!! Dica: É um número maior.')
            print('Você ainda possui {} chances.'.format(chance))
        if chance == 0:
            print('Suas chances acabaram, você perdeu!')


print('#### Fim do Jogo ####')
