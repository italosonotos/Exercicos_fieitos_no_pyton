numero_1 = input('Digite um número inteiro: ')
 
if numero_1.isdigit():
    numero_int = int(numero_1)
    if numero_int % 2 == 0:
        print(f'{numero_int} é par!')
    else:
        print(f'{numero_int} é ímpar!')
else:
    print('O valor digitado não é válido!')