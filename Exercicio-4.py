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