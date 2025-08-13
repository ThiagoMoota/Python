'''
1) Escreva uma função para criar e retornar uma matriz numérica n x m
2) Escreva uma função que receba uma matriz numérica por parâmetro e retorne a soma de todos os elementos contidos na matriz
3) Escreva uma função para imprimir a soma (resultado)
4) Escreva uma função main() para testar o programa
'''

def criar_matriz(n_linhas, n_colunas):
    matriz = [] #lista vazia
    for i in range(n_linhas): #laço de repetição para percorrer o número de elementos
        linha = [] #lista vazia
        for j in range(n_colunas):
            n = int(input('Número: '))
            linha.append(n) 
        matriz.append(linha)
    return matriz

def somar_elementos(matriz):
    soma = 0 #variável acumuladora
    for linha in range(len(matriz)): #percorrer lista maior
        for coluna in range(len(matriz[linha])): #percorrer a lista que está dentro da lista
            soma+= matriz[linha][coluna]
    return soma

#função imprimir 
def imprimir(soma):
    print(f'Soma total: {soma}')

#função main() para testar o programa
def main():
    matriz = criar_matriz(3, 3)
    soma = somar_elementos(matriz)
    imprimir(soma) #void

#Principal
main()
