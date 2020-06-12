acumulador = 0
impares = []
pares = []
for x in range(10):
    add = int(input(f"Insira {x + 1}º número: "))
    if(add % 2 == 0):
        pares.append(add)
    else:
        impares.append(add)
    acumulador += add

print(f"O soma total é: {acumulador}")
print(f"O números pares: {pares}")
print(f"Os números impares: {impares}")
