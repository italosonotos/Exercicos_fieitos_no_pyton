"""
Criar um algoritmo em PORTUGOL que possa ler um conjunto de pedidos de 
compra e calcule o valor total da compra. 
Cada pedido é composto pelos seguintes campos: 
- Número de pedido; 
- Data do pedido (dia, mês, ano); 
- Preço unitário
"""
import random
x = random.randrange(1,1000)
print(x)
dia_compra = input('Digite o Dia da compra no formato dd:')
mes_compra = input('Digite o Mês da compra no formato mm:')
ano_compra = input('Digite o Ano da compra no formato aaaa:')
preco_compra = float(input("Digite o valor da compra R$:"))
numero_tentativa = 0

print('===========Cumpom Fiscal===========')
print('Numero do pedido:{}'.format(x))
print('Compra realizada no dia {} de {} de {}'.format(dia_compra,mes_compra,ano_compra))
print('Total da compra R${}'.format(preco_compra))
print('======================')