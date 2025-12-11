while True:
    print("MENU")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Sair")
    op = int(input("escolha:"))
    if op == 3:
        print("saindo")
        break

    n1 = float(input("n1: "))
    n2 = float(input("n2: "))
    if op == 1:
        print("Resultado:", n1 + n2)
    elif op == 2:
        print("Resultado:", n1 - n2)
    else:
        print("Opção inválida!")
