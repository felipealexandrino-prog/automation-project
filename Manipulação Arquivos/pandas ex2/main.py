import pandas as pd

dados = {
    "produto": ["mouse", "teclado", "monitor", "mouse", "monitor", "teclado", "mouse", "headset"],
    "categoria": ["periferico", "periferico", "tela", "periferico", "tela", "periferico", "periferico", "periferico"],
    "preco": [50, 150, 900, 50, 850, 150, 50, 200],
    "quantidade": [2, 1, 1, 3, 2, 2, 1, 1],
    "cidade": ["SP", "RJ", "SP", "MG", "SP", "RJ", "MG", "SP"]
}

dados_df = pd.DataFrame(dados)
dados_df['total'] = dados_df['preco'] * dados_df['quantidade']
print(dados_df)
agrup = dados_df.groupby('produto')['total'].sum()
print(f"TABELA ÚNICA POR PRODUTO\n{agrup}")
bigval = agrup.max()
bigprod = agrup.idxmax()
print(f"Maior venda: {bigprod.upper()} | {bigval} R$ ")
agrupcat = dados_df.groupby('categoria')['total'].sum()
bigcat = agrupcat.idxmax()
bigwin = agrupcat.max()
print(f"TABELA POR CATEGORIA\n{agrupcat}")
print(f"Categoria com maior lucro: {bigcat.upper()} | {bigwin} R$")
agrupcid = dados_df.groupby('cidade')['quantidade'].sum()
bigcid = agrupcid.idxmax()
bigqnt = agrupcid.max()
print(f"TABELA POR QUANTIDADE COMPRADA POR CIDADE\n {agrupcid}")
print(f"Cidade que mais comprou itens: {bigcid} | {bigqnt} UND")
print(f"TABELA DE ORDEM QUE OS PRODUTOS MAIS APARECERAM!")
print(dados_df["produto"].value_counts())
print("TOP 3 MAIORES VENDAS!")
print(dados_df.nlargest(3,'total'))


