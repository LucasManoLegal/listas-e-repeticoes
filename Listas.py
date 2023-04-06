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

#Exercício 4
print('Consoantes e vogais')
Lista4 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',]
ListaDeVogais = ['a', 'e', 'i', 'o', 'u']
ListaDeConsoantes = []
consoantes = 0
contador = 0
for i in Lista4:
    if not Lista4 [contador] in ListaDeVogais:
        consoantes += 1
        ListaDeConsoantes.append(Lista4[contador])
    contador+=1
print(ListaDeConsoantes)
print(consoantes)

#Exercício 5
print('Números pares e ímpares')
TodosNum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
ListaPares = []
ListaImpares = []
contador = 0

for i in TodosNum:
    if TodosNum [contador]%2:
        ListaImpares.append(TodosNum[contador])
    else:
        ListaPares.append(TodosNum[contador])
    contador+= 1
print("Números", TodosNum)
print("Números Ímpares", ListaImpares)
print("Números Pares", ListaPares)

#Exercício 6
print('Notas dos Alunos')
Aluno1 = [7.5, 9, 8, 10] 
Aluno2 = [8.5, 9.5, 8, 10]
Aluno3 = [7.5, 10, 7, 8]
Aluno4 = [9, 9.5, 10, 10]
Aluno5 = [5, 6.5, 7, 7,5]
Aluno6 = [7.5, 7, 8.5, 9]
Aluno7 = [8.5, 7, 6, 6.5]
Aluno8 = [10, 10, 10, 10]
Aluno9 = [9.5, 10, 8.5, 7]
Aluno10 = [10, 7, 8, 5]

TodosAlunos = [Aluno1, Aluno2, Aluno3, Aluno4, Aluno5, Aluno6, Aluno7, Aluno8, Aluno9, Aluno10]
for i in TodosAlunos:
    média = média / 4
    TodosAlunos.append(média)
    
