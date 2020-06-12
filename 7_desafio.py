lista = []
x = 0
maior = 0

while x < 5:
    lista.append(int(input(f"Insira {x+1}º número: ")))
    x += 1

print(f"O maior número é {max(lista)}")
