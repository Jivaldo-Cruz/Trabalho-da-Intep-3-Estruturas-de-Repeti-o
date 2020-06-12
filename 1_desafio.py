while True:
    nota = float(input("Insira um valor entre 0 à 10: "))
    if(nota > 10):
        print("Nota inválida!")
    elif(nota < 0):
        print("Nota inválida!")
    else:
        print("Válido!")
        break
