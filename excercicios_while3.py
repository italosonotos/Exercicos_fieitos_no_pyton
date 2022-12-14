while True:
    numero1 = input('Digite um numero:')
    numero2 = input('Digite um numero:')
    operador = input('Digite o operador (+ - / *)')
    
    numeros_validos = None 

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None
        
    if numeros_validos is None:
        print('Um ou ambos numeros numeros digitados não sao validos!')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('operador invalido')
        continue 
    if len(operador) >1:
        print('Digite apenas um operador')
        continue


    sair = input("quer sair? [S]im:").lower().startswithc('s')
    
    if sair is True:
      break