import numpy as np
#estou a aprender numpy então não sei se vai ser problema usar cá, porque facilita

lista = []
x = 0

while x < 5:
    lista.append(int(input(f"Insira {x + 1}º número: ")))
    x += 1
arr = np.array(lista)

print("A soma é:",arr.sum())#soma
print("A media é:",arr.mean())#média


#outra forma de fazer isso é
#só fiz desta forma para mostar que consigo fazer sem biblioteca
"""
soma = 0
media = 0
for z in lista:#usando lista
    soma += z
    media = soma / len(lista)
print(f"{'='*70}\nEstá é a outra forma")
print("A soma é:",soma,"E a média é",media)
"""    
