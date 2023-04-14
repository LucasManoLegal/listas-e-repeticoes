#Exercício 8

números = [5, 10, 15, 20, 25]
soma = 0
média = 0

print("Lista dos números" + str(números))

for i in números:
    soma = sum(números)
print("Soma dos números " + str(soma))

for i in números:
    média = soma/len(números)
print("Média dos números " + str(média))