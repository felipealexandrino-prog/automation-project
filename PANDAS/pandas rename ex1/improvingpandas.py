import pandas as pd
table_df = pd.read_csv(r"C:\Users\Pichau\Downloads\vendas_dia2.csv")



#DESEMPENHO POR PRODUTO
#faturamento total
#média de quantidade vendida
#maior preço registrado
table_df['total'] = table_df['preco'] * table_df['quantidade']
tableprod = table_df.groupby('produto').agg({
    'total' : 'sum',
    'quantidade' : 'mean',
    'preco' : 'max'
    
    
    
}).rename(columns = {
    'total' : 'Faturamento_Total',
    'quantidade' : 'media_qnt_vendida',
    'preco' : 'maior_preco'
})
print(tableprod)



#DESEMPENHO POR CATEGORIA
#faturamento total
#quantidade total vendida
tablecat = table_df.groupby('categoria').agg({
    'total' : 'sum',
    'quantidade' : 'sum'
    
}).rename(columns = {
    'total' : 'Faturamento_Total',
    'quantidade' : 'Quantid.Vend.'
    
})
print(tablecat)


#DESEMPENHO POR CIDADE
#Apresentar o faturamento total por cidade
#Ordenar do maior para o menor
tablecity = table_df.groupby('cidade').agg({
    'total' : 'sum'
    
}).rename(columns = {
    'total' : 'Faturamento_Total'
}).sort_values(by='Faturamento_Total',ascending=False)
print(tablecity)

#PRODUTO POR CIDADE
#total vendido por produto em cada cidade
prodcity_df = table_df.groupby(['produto','cidade']).agg({
    
        'total' : 'sum'

    
    
}).rename(columns = {
    'total':'Total_Vendido_Cidade'
}).reset_index()
print(prodcity_df)

#Ranking de Produtos
#organizada
#com nomes claros nas colunas
#ordenada pelo faturamento total (maior → menor)
finaltable = table_df.groupby('produto').agg({
    'total': 'sum'
}).reset_index().rename(columns={
    'produto': 'Nome_Produto',
    'total': 'Faturamento_Total'
}).sort_values(by='Faturamento_Total', ascending=False)

print(finaltable)

#Desempenho por Vendedor
#faturamento total por vendedor
#quantidade total vendida

sellertable = table_df.groupby('vendedor').agg({
    'total' : 'sum',
    'quantidade' : 'sum'
}).rename(columns={
    'total' : 'Faturamento_Vendedor',
    'quantidade' : 'Quantidade_Vendida',
}).sort_values(by='Faturamento_Vendedor',ascending=False)
maiorvend = sellertable['Faturamento_Vendedor'].idxmax()
maiorval = sellertable['Faturamento_Vendedor'].max()
print(sellertable)
print(f"Maior Vendedor: {maiorvend} | Valor: {maiorval} R$")
