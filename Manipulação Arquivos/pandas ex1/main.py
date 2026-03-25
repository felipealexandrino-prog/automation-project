import pandas as pd
#🎯 MISSÕES

# 1️⃣ Criar coluna total
# 👉 preco * quantidade
# 2️⃣ Qual produto vendeu MAIS (em dinheiro)?
# 👉 dica: usa groupby
# 3️⃣ Qual categoria faturou mais?
# 👉 (periferico vs tela)
# 4️⃣ Qual produto teve a MAIOR quantidade vendida?
# 👉 não é dinheiro, é quantidade
# 5️⃣ BONUS (nível 🔥)

# Mostra isso organizado:
# - total vendido (R$)
# - média de quantidade
# - maior preço
# 👉 tudo agrupado por produto

dados = {
    "produto": ["mouse", "teclado", "mouse", "monitor", "teclado", "mouse"],
    "categoria": ["periferico", "periferico", "periferico", "tela", "periferico", "periferico"],
    "preco": [50, 150, 50, 800, 150, 50],
    "quantidade": [2, 1, 1, 1, 3, 4]
}

data_df = pd.DataFrame(dados)
colprice = data_df['preco']
colquant = data_df['quantidade']
data_df['total'] = colprice * colquant
print("TABELA EM ORDEM VALOR TOTAL!\n",data_df.sort_values('total',ascending=False))
mais_vendido = data_df.groupby("produto")["total"].sum()
produto = mais_vendido.idxmax()
valor = mais_vendido.max()
print(f"Produto que mais vendeu: {produto.upper()} -> R$ {valor}")
