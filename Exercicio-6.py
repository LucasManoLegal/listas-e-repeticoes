#Exercício 6
print('Notas dos Alunos')
listaAlunos = [["Michael", [9, 10, 8, 10]],["Jimmy", [5, 6, 4, 3]],["Kimberly",  [10, 7, 8, 8]],["Walter", [10, 9, 7, 10]],["Gustavo", [9, 6, 7, 10]], ["Jesse", [3, 2, 5, 4]],["Lalo", [7, 6, 8, 7]],["Skyler", [9, 8, 6, 10]],["Chuck", [10, 7, 5, 10]],["Hector", [6, 7, 5, 6]]]

def calcularMédias (listaAlunos):
    listadeMéias = []
    for aluno in listaAlunos:
        média = sum(aluno[1]) / len(aluno[1])
        listadeMéias.append(média)


    listaDeAprovados = []
    for aluno in listadeMéias:
        if aluno >= 7:
            listaDeAprovados.append(aluno) 
    print(listadeMéias)
    print(len(listaDeAprovados))

calcularMédias(listaAlunos)