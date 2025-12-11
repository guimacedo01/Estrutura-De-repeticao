qtd = 0
soma = 0
maior = -9999
menor = 9999
pares = 0
while True:
    n = int(input("Número (0 para sair): "))
    if n == 0:
        break
    qtd += 1
    soma += n

    if n > maior:
        maior = n
    if n < menor:
        menor = n
    if n % 2 == 0:
        pares += 1
media = soma / qtd
print("Quantidade:", qtd)
print("Média:", media)
print("Maior:", maior)
print("Menor:", menor)
print("Pares:", pares)
