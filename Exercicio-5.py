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