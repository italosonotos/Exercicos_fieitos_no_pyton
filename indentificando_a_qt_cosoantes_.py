lista =[]
cosoantes = 0

print('Digite uma frase por gentileza')

for i in range(30):
    lista.append(input('Total de caracteres'+' '+str(i+1)))
    char = lista[i]

    if (char not in ('a','e','i','o','u')):
        cosoantes += 1

print('Total de cosoantes:',cosoantes)