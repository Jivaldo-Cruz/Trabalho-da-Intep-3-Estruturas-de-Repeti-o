num = int(input("Insira um número para fatorar: "))

for x in range(num, 1, -1):
    num *= x-1
    print(x)
print(num)
