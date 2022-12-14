nome = input('Digite seu nome:')
tamanho_nome = len(nome)

if tamanho_nome >=1:
    if tamanho_nome <=4:
        print('Seu nome é curto')
    if tamanho_nome >=5 and tamanho_nome <=6:
        print('seu nome é normal')
    else:
        print('Seu nome é muito grande')

else:
    ('Digite alguma coisa por gentileza')