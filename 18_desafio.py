listaValor = []
acumulador = 0

n = int(input("Quantos números queres digitar no conjunto de N?: "))

for x in range(n):
    listaValor.append(int(input(f"Insira {x+1}º valor: ")))
    acumulador += listaValor[x]

print(f"O conjunto de N: {listaValor}")
print(f"A soma dos valores é {acumulador}")
print(f"O maior número é {max(listaValor)} e o menor número é {min(listaValor)}")
