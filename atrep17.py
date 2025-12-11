soma = 0
cont = 0
while True:
    idade = int(input("Idade (0 para parar): "))
    if idade == 0:
        break
    soma += idade
    cont += 1
if cont > 0:
    print("Média =", soma / cont)
else:
    print("Nenhuma idade informada.")
