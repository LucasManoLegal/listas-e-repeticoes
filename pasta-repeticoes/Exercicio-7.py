#Exercicio-7

numeros = [1, 14, 7, 18, 7]
maior = 0
index = 0

while(index != len(numeros)):
    if(maior < numeros[index]):
        maior = numeros[index]
    index += 1
print(' Maior número: ' + str(maior))