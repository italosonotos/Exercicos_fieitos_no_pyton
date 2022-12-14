sexo = input('Digite [M] para masculino [F] para feminino:')
horas_trabalhada = float(input('Digite o total de horas trbalhadas:'))
valor_hora = 30
codigo = '99999'


while True:
    
    if (sexo == 'M'):
        salario_bruto = (horas_trabalhada * valor_hora)
        salario_liquido = (salario_bruto * 0.10)
        print('========================================')
        print('Seu salario bruto R$',salario_bruto)
        print('A media do salario R$',salario_liquido)
        print('salario liquido R$',salario_bruto-salario_liquido)
        print('========================================')
        codigo = input('Digite 99999 para finalizar:')
        print('========================================')

        if(codigo == '99999'):
            print('Tchau')
            break
        else:
            sexo = input('Digite [M] para masculino [F] para feminino:')
            horas_trabalhada = float(input('Digite o total de horas trbalhadas:'))
    

        

    if (sexo == 'F'):
        salario_bruto = (horas_trabalhada * valor_hora)
        salario_liquido = (salario_bruto * 0.05)
        print('========================================')
        print('Seu salario bruto R$',salario_bruto)
        print('A media do salario R$',salario_liquido)
        print('salario liquido R$',salario_bruto-salario_liquido)
        print('========================================')
        codigo = input('Digite 99999 para finalizar:')
        print('========================================')

        if(codigo == '99999'):
            print('Tchau')
            break
        else:
            sexo = input('Digite [M] para masculino [F] para feminino:')
            horas_trabalhada = float(input('Digite o total de horas trbalhadas:'))
        