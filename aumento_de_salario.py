'''
 Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver  programa que calculará os reajustes.
 um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
'''
print('==========Bem vindo ao tabajara==========')
salario_atual  = float(input('Digite o salario para saber o aumento:'))


if salario_atual < 280:
    novo_salario = salario_atual *0.20
    print('================================')
    print('Salario atual R$',salario_atual)
    print('O aumento será R$',novo_salario)
    print('Novo salario R$',novo_salario+salario_atual)
    print('================================')

elif salario_atual > 280.00 and salario_atual < 700.00:
    novo_salario = salario_atual *0.15
    print('================================')
    print('Salario atual R$',salario_atual)
    print('O aumento será R$',novo_salario)
    print('Novo salario R$',novo_salario+salario_atual)
    print('================================')

elif salario_atual > 7000 and salario_atual < 1500:
    novo_salario = salario_atual *0.10
    print('================================')
    print('Salario atual R$',salario_atual)
    print('O aumento será R$',novo_salario)
    print('Novo salario R$',novo_salario+salario_atual)
    print('================================')

else:
    novo_salario = salario_atual *0.05
    print('================================')
    print('Salario atual R$',salario_atual)
    print('O aumento será R$',novo_salario)
    print('Novo salario R$',novo_salario+salario_atual)
    print('================================')
