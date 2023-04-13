#Exercício 7
print ("Conjunto dos números inteiros")
conjuntoDosNumeros = [10, 6, 12, 3, 1]
print (conjuntoDosNumeros)
print ("Soma dos números")

def soma (conjuntoDosNumeros):
    soma = 0
    for i in conjuntoDosNumeros:
        soma += i
    return soma
print (soma(conjuntoDosNumeros))
print ("Multiplicação dos números")

def multiplicação (conjuntoDosNumeros):
    multiplicação = 1
    for i in conjuntoDosNumeros:
        multiplicação *= i
    return multiplicação
print (multiplicação(conjuntoDosNumeros))