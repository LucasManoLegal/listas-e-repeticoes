#Exercício 3

contador = 0
while(contador == 0):
    print('Digite seu nome:')
    nome = input()
    if len(nome) < 3:
        print('Nome inválido. (precisa ter mais que 3 caracteres)')
    else:
        contador = 1

contador = 0
while(contador == 0):
    print('Digite sua idade:')
    idade = int(input())
    if idade > 0 and idade < 150:
        contador = 1
    else:
        print('Idade inválida. (entre 0 e 150)')

contador = 0
while(contador == 0):
    print('Digite seu salário:')
    salário = int(input())
    if salário > 0:
        contador = 1
    else:
        print('Salário inválido.')

contador = 0
while(contador == 0):
    print("Digite o seu sexo ('M' para Masculino/'F' para Feminino)")
    sexo = input()
    if sexo == 'F' or sexo == 'M':
        contador = 1
    else:
        print('Informação inválida.')

contador = 0
while(contador == 0):
    print("Digite o seu Estado Civil ('s' para Solteiro/'c' para Casado/'v' para Viúvo/'d' para Divorciado)")
    estadoCivil = input()
    if estadoCivil == 's' or estadoCivil == 'c' or estadoCivil == 'v' or estadoCivil == 'd':
        contador = 1
    else:
        print('Informação inválida.')