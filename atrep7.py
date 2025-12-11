soma = 0  
numero = 1 
while numero <= 5: 
    nota = float(input(f"Digite a nota {numero}: "))  
    soma += nota 
    numero += 1  
media = soma / 5  
print(f"A média é {media}")
