lista = []

print('Digite 10 numeros!')

for i in range(10):
    lista.append(float(input('Numero'+str(i+1)+':')))
    lista.reverse()

print('Lista inversa',lista)
    
