import random
numero= random.randint(1,20)
tentativas = 0
while True:
    chute = int(input("tente adivinhar"))
    tentativas += 1
    if chute == numero:
        print("certo")
        break
    elif chute < numero:
        print("tente um maior")
    else:
        print("numero menor")
