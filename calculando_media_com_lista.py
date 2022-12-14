lista= []
media = 0

print('Digite os 4 nota para saber a media ponderada:')

for i in range(4):
    lista.append(float(input('Nota'+' '+ str(i+1)+":" )))
    media += lista[i]
    media =media /4
    print(lista)
    print ('A media ponderada é :',media)