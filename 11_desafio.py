num1 = int(input("Insira 1ª número inteiro: "))
num2 = int(input("Insira 2ª número inteiro: "))

acumulador = 0

print("O intervalo da soma")
for i in range(num1, num2):
    print(i)
    acumulador += i
print("A soma é:",acumulador)
