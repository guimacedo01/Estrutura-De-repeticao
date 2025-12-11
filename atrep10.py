maior = float('-inf')
menor = float('inf')   
for numero in range(10): 
    num = int(input(f"Número {numero+1}: "))  
    if  num > maior: 
        maior = num
    if num < menor:  
        menor = num
print(f"Maior: {maior}, Menor: {menor}")