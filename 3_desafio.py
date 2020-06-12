
while True:
    nome = input("Insira um nome: ")
    idade = int(input("Insira sua idade: "))
    salario = float(input("Insira seu salário: "))
    sexo = input("Insira seu sexo masculino[M] e feminino[F]: ")
    civil = input("Estado Civil: 's', 'c', 'v', 'd'; - solteiro, casado, viúvo e divorciado: ")

    if(len(nome) > 3 and idade > 0 and idade <= 150 and salario > 0):
        if(sexo.lower() == "m"):
            sexo = "Masculino"
        elif(sexo.lower() == "f"):
            sexo = "Feminino"
        else:
            print("As informações não podem ser válidadas!\nTens que digitar 'M' ou 'F'")
            break
            
        if(civil.lower() == "s"):
            civil = "Solteiro/a"
        elif(civil.lower() == "c"):
            civil = "Casado/a"
        elif(civil.lower() == "v"):
            civil = "Viúvo/a"
        elif(civil.lower() == "d"):
            civil = "Divorciado"
        else:
            print("As informações não podem ser válidadas!")
            print("Estado civil: 's', 'c', 'v', 'd'; - solteiro, casado, viúvo e divorciado")
            break
            
        print
        print("Todas as informações aceite!")
        print(f"Nome: {nome}\nIdade: {idade}\nSalário: {salario}\nSexo: {sexo}\nCivil: {civil}")
        break
    else:
        print(f"{'='*70}")
        print("As informações não podem ser válidadas!")
        print("Nome > 3, idade de 0 à 150, salário maior que 0, sexo: 'M' ou 'F', estado civil: 's', 'c', 'v', 'd'; - solteiro, casado, viúvo e divorciado")
    
