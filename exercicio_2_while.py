nome = 'Victor Hugo' 
 
tamanho_nome = len(nome)-1
print(nome)
print(tamanho_nome)
print(nome[3])
 
nova_string= ''
indice = 0
condicao = True 
while condicao:
    condicao = indice < tamanho_nome
    nova_string += f'*{nome[indice]}'
    indice += 1
 
nova_string += '*'
print(nova_string)