import pandas as pd
data_df = pd.read_csv(r'C:\Users\Pichau\Downloads\vendas_agg_treino.csv')
tableprod = data_df.groupby('produto').agg ({
    'total' : 'sum',
    'quantidade' : 'mean',
    'preco' : 'max'
})
print(f"TABELA DADOS PRODUTO\n{tableprod}")


tablecat = data_df.groupby('categoria').agg({
    'total' : 'sum',
    'quantidade' : 'sum'
})
print(f"TABELA DADOS CATEGORA \n{tablecat}")

tableprod2 = data_df.groupby('produto').agg({
    'total' : ['sum','mean']
    
})
print(tableprod2)




tablealong = data_df.groupby(['produto','cidade']).agg({
    'total' : 'sum'
})

print(tablealong)