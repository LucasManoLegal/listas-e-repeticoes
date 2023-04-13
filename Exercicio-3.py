#Exercício 3
print('Notas dos 4 alunos')
Lista3 = [7.5, 8, 10, 9]

def calcularnotas (Lista3):
    QuantidadeDeNúmeros = len(Lista3)
    sum(Lista3) / QuantidadeDeNúmeros
    Média = sum(Lista3) / QuantidadeDeNúmeros
    return Média
print(calcularnotas(Lista3))