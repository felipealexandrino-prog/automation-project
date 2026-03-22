import requests

requisicao = requests.get("https://jsonplaceholder.typicode.com/users")
data = requisicao.json()
city_wanted = "South Christy"
for d in data:
    print(d['name'])
    if d["address"]["city"] == city_wanted:
        print(f"{d['name']} mora em {city_wanted}")
print(f"Existem {len(data)} pessoas na base de dados")
    
with open("data.txt","w") as new_data:
    for p in data:
        new_data.write(f"{p['name']} - {p['address']['city']}\n")