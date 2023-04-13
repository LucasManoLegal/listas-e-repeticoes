#Exercicio-8
print("Números inteiros - Exercício 8")
Idades = []
Alturas = []
for i in range(0,5):
    print('Insira uma idade')
    idade = input()
    print('Insira uma altura (em metros)')
    altura = input()
    Idades.append(idade)
    Alturas.append(altura)

Idades.reverse()
Alturas.reverse()

contador = 0
for i in Idades:
    print('Pessoa ' + str(contador + 1) + ':' )
    print('Idade: ' + str(i))
    print('Altura: '+ str(Alturas[contador]))
    contador += 1 