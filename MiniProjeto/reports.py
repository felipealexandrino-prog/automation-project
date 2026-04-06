import pandas as pd

table_df = pd.read_csv(r"C:\Users\Pichau\Downloads\vendas_projeto.csv")
table_df['total'] = table_df['preco'] * table_df['quantidade']
# 1. Visão Geral
#Quantidade total de vendas (linhas)
#Faturamento total da empresa
#Quantidade total de itens vendidos

#2. Desempenho por Produto
#faturamento total
#quantidade total vendida
#preço médio
#maior preço
table_prod = table_df.groupby('produto').agg({
    'total' : 'sum',
    'quantidade' : 'sum',
    'preco' : 'mean'
}).rename(columns={
    'total' : 'Faturamento_Total',
    'quantidade' : 'Quantidade_Total_Vendida',
    'preco' : 'Preco_Medio'
    
    
    }).sort_values(by = 'Faturamento_Total', ascending=False).reset_index()

maior_idx = table_df['preco'].idxmax()
maior_val = table_df['preco'].max()
maior_prod = table_df.loc[maior_idx, 'produto']
print(f"\nTABELA POR PRODUTO\n{table_prod}")
print(f"Produto com Maior Valor: {maior_prod} | {maior_val} R$")


# Categoria
#faturamento total por categoria
#qual categoria faturou mais
tablecat = table_df.groupby('categoria').agg({
    'total' : 'sum'
}).sort_values(by='total',ascending=False).reset_index()
print(f"\nTABELA POR CATEGORIA\n{tablecat}")
print(f"Categoria com maior faturamento {tablecat['categoria'][0]} | Faturou {tablecat['total'][0]} R$")
#Cidade
#quantidade total vendida por cidade
#qual cidade comprou mais
table_city = table_df.groupby('cidade').agg({
    'quantidade' : 'sum',
}).sort_values(by='quantidade', ascending=False).reset_index().rename(columns={
    'cidade' : 'Cidade_Analisada',
    'quantidade' : 'Quantidade_Vendida'
})

print(f"\nTABELA POR CIDADE\n{table_city}")
print(f"Cidade que comprou mais {table_city['Cidade_Analisada'][0]} | Quantidade: {table_city['Quantidade_Vendida'][0]}")

#Vendedor
#faturamento total por vendedor
#quem vendeu mais
table_seller = table_df.groupby('vendedor').agg({
    'total' : 'sum'
}).sort_values(by='total',ascending=False).reset_index().rename(columns={
    'vendedor' : 'Vendedor_Analisado',
    'total' : 'Total_Vendedor'
})

print(f"\nTABELA POR VENDEDORES\n{table_seller}")

#Frequência
#quantas vezes cada produto aparece

table_freq = table_df.value_counts('produto').reset_index().rename(columns={
    'produto' : 'Produto_Analisado',
    'count' : 'Frequência'
})
print(f"\nTABELA DE FREQUÊNCIA\n{table_freq}")

#Vendas
#mostrar as 3 maiores vendas (linhas)

table_sales = table_df.nlargest(3,'total').reset_index().rename(columns = {
    'produto' : 'Produto_Vendido',
    'index' : 'N.Venda',
    'categoria' : 'Categoria_Venda',
    'preco' : 'Preço_Produto',
    'quantidade' : 'Quantidade_Compra',
    'cidade' : 'Cidade',
    'vendedor' : 'Vendedor',
    'total' : 'Total_Compra'
})
print(f"\nTABELA TOP 3 MAIORES VENDAS\n{table_sales}")

#tabela com:
#produto
#cidade
#total vendido
table_analyse = table_df.groupby(['produto','cidade']).agg({
    'total' : 'sum'
    
}).reset_index().rename(columns= {
    'produto' : 'Produto_Analisado',
    'cidade' : 'Cidade',
    'total' : 'Total_Vendido'
})

print(f"TABELA POR PRODUTO / CIDADE\n{table_analyse}")
