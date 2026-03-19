#Mostrar produtos formatados Produto: | Preço: 
#Mostrar apenas produtos acima de 500
#Contar quantos produtos estão acima de 1000
cont = 0
maior = 0
menor = 0 
soma = 0
media = 0
pre = 0
produto = ""
maiorval = pre
maiorprod = produto
menorval = float('inf')
menorprod = produto
with open ("basedados.txt","r") as dados:
    arq = dados.readlines()
    
    for linhas in arq:
        linhas = linhas.strip()
        campo = linhas.split(",")
        produto = campo[0]
        preco = campo[1]
        pre = float(preco)  
        print(f"Produto:{produto} | Preço:{pre}")
        if pre > 500:
            print(f"\n!Produtos acima de 500! \nProd: {produto} | Pre: {pre} ")
        soma += pre
        if pre > 1000:
            cont += 1
        
        if pre > maiorval:
            maiorprod = produto
            maiorval = pre
        if pre < menorval:
            menorprod = produto
            menorval = pre            
            
        
    media = soma / len(arq)        
    print(f"Foram contabilizados {cont} produtos acima de 1000 reais!")
with open("infovalor.txt","w") as novoarq:
    novoarq.write(f"Produto mais caro : {maiorprod} | Valor: {maiorval}\n")
    novoarq.write(f"Produto mais barato : {menorprod} | Valor: {menorval}\n")
    novoarq.write(f"Média de valores: {media}")

