num = ""

for x in range(20):
    print(x + 1)
    num += str(x + 1)#converte para string de modo concatenar
    num += " "#para dar espaçamento. para converter 'num' para int() temos que comentar está linha
print(num)#imprime como uma string. se comentar o espaçamento podes converter num para int(), usando int(num)
