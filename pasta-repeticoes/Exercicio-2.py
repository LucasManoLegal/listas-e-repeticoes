#Exercício 2

Condição = True

while Condição != False:
    print("Digite seu usuário")
    Usuário = input()
    print("Digite sua senha")
    Senha = input()
    if Usuário != Senha:
        print ("Acessado")
        Condição = False
    else:
        print ("Acesso Negado - O usuário não precisa ser diferente da senha")