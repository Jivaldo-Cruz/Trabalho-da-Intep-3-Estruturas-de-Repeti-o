listaValor = []
acumulador = 0

n = int(input("Quantos números queres digitar no conjunto de N?: "))

for x in range(n):
    tentar = int(input(f"Insira {x+1}º valor: "))
    if(tentar <= 100):
        listaValor.append(tentar)

for i in listaValor:
    acumulador += i


print(f"O conjunto de N: {listaValor}")
print(f"A soma dos valores é {acumulador}")
print(f"O maior número é {max(listaValor)} e o menor número é {min(listaValor)}")
