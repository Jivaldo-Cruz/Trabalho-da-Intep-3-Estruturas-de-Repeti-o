                                                                                                                                                                                                                                                                                                                                                                                                                      
base = int(input("Insira a base: "))
expoente = float(input("Insira o expoente: "))

total = 1
cont = 0

while cont < expoente:
    total *= base
    cont += 1
#mas eu podia fazer base**expoente iria dar resultado certo
#mas como stor pediu estrutura de repetição obrigatorio
    
print(f"{base} elevado à {expoente} é = {total}")
