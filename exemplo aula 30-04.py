#Escreva um programa que leia 5 nomes e exiba a quantidade
# que iniciam com vogal e armazene esses nomes em uma lista (e os exiba)


nomes = []
qtde = 0
nome = []
listavogais = []

for i in range(5):
    nome = input('Digite seu nome: ')
    nomes.append(nome)

for nome in nomes:
    if nome[0] == 'A' or nome[0] == 'E' or nome[0] == 'I' or nome[0] == 'O' or nome[0] == 'U':
        qtde+=1
        listavogais.append(nome)

#imprimindo as informações
print(f'Quantidade: {qtde}')
print(listavogais)

print('----------------------------------------------')

#percorrendo a lista e acessando os elementos um por um
print('Nomes iniciados com vogal: ')
for nome in listavogais:
    print(f'Nome: {nome}')
