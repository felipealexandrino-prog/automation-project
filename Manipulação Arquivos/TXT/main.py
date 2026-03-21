while True:
    usuario = input("Digite seu usuário: ")
    senha = input("Digite sua senha: ")

    encontrado = False

    with open("dados.txt","r") as base:
        for linha in base:
            linha = linha.strip()
            dados = linha.split(",")

            nome_cad = dados[0]
            senha_cad = dados[1]

            if usuario == nome_cad and senha == senha_cad:
                print("LOGIN REALIZADO!")
                encontrado = True
                break

            elif usuario == nome_cad and senha != senha_cad:
                print("SENHA INCORRETA!")
                encontrado = True
                break

    if not encontrado:
        print("USUÁRIO NÃO ENCONTRADO!")  
    
