palavra_secreva = 'italo'
letras_acertadas = ''
numeros_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra:')
    numeros_tentativas += 1

    if len(letra_digitada) >1:
        print('Digite apenas uma letra!')
        continue
    if letra_digitada in letras_acertadas:
        letras_acertadas += letra_digitada

        palavra_formada = ' '
    for letra_secreta in palavra_secreva:
        if letra_secreta in letras_acertadas:
            palavra_formada += palavra_secreva
        else:
                palavra_formada = '*'
                print('Palavra formada:',palavra_formada)
    if palavra_formada == palavra_secreva:
        print('Parabens!!')
        print('Você conseguiu')
        print(palavra_secreva)
