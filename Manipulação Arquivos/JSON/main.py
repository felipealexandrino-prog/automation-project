import json
import requests
#👉 Mostre:
#Cidade
#Estado
#CEP formatado
requisicao = requests.get("https://cep.awesomeapi.com.br/json/01001000")
print(requisicao)
dic_cep = requisicao.json()
print(dic_cep)
cidade = dic_cep["city"]
estado = dic_cep["state"]
cep = dic_cep["cep"]
print(f"Cidade: {cidade} | Estado:  {estado} | CEP: {cep}")
    
    
def exibir():
    if estado == "SP":
        return f"Cidade: {cidade} | Estado:  {estado} | CEP: {cep} | CEP DE {estado} -> {cep}"
        
    else:
        return f"Cep não é de são paulo :("
    
    
    
with open("arquivojson.txt","w") as arq:
    arq.write(exibir())
