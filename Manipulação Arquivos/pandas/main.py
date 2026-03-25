import pandas as pd
dados = {
    "produto": ["mouse", "teclado", "mouse", "monitor", "teclado"],
    "preco": [50, 150, 50, 800, 150],
    "quantidade": [2, 1, 3, 1, 2]
}
dados_df = pd.DataFrame(dados)
print(f"PRODUTOS ACIMA DE 100\n",dados_df[dados_df['preco'] > 100])
dados_df['total'] = dados_df['preco'] * dados_df['quantidade']
print(dados_df.sort_values('preco',ascending=False))
print(dados_df.groupby("produto")["total"].sum())