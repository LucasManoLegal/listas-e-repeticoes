#Exercício 1
print('Valores dos 5 números inteiros')
Lista1 = [1, 2, 3, 4, 5]
print(Lista1)

#Exercício 2
print('Valores dos 10 números reais em ordem decrescente')
Lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Lista2.reverse()
print(Lista2)

#Exercício 3
print('Notas dos 4 alunos')
Lista3 = [7.5, 8, 10, 9]

def calcularnotas (Lista3):
    QuantidadeDeNúmeros = len(Lista3)
    sum(Lista3) / QuantidadeDeNúmeros
    Média = sum(Lista3) / QuantidadeDeNúmeros
    return Média
print(calcularnotas(Lista3))
