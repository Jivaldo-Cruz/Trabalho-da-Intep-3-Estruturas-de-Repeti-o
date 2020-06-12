#não sei se meu raciocinio está correto

a = 80000
b = 200000
c = 3
cont = 0
total = 0
x = (a * c) / 100

while True:
    total += x
    cont += 1
    if(total >= b):
        break
    

print(f"É necessario {cont} anos para que o A seja maior ou igual a B.")
