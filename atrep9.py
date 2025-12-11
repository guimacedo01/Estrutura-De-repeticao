soma_pares = 0 
soma_impares = 0 
for numero in range(10): 
    num = int(input(f"Número {numero+1}: "))  
    if num % 2 == 0: 
        soma_pares = soma_pares + num  
    else:  
        soma_impares = soma_impares + num  
print(f"Soma pares: {soma_pares}, ímpares: {soma_impares}")  