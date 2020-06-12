

while True:
    nome = input("Insira um nome de utilizador: ")
    senha = input("Insira um password: ")

    if(nome != senha):
        print("Logado com sucesso!")
        break
    else:
        print("Erro a logar, o nome não pode ser igual a senha.")

