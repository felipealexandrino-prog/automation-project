import pandas as pd
#TAKING DATA
archive_df = pd.read_csv(r"C:\Users\Pichau\Downloads\vendas_treino.csv")


#CODING
#MISSION ONE
archive_df['total'] = archive_df['quantidade'] * archive_df['preco']


#MISSION TWO
table1 = archive_df.groupby('produto')['total'].sum()
bigfat = table1.max()
namebigfat = table1.idxmax()
print(table1)
print(f"O produto com maior faturamento foi {namebigfat.upper()} | {bigfat} R$")

#MISSION THREE
tablecat = archive_df.groupby('categoria')['total'].sum()
bigcategory = tablecat.idxmax()
cattotal = tablecat.max()
print(tablecat)
print(f"A categoria mais vendida foi {bigcategory.upper()} | {cattotal} R$")

#MISSION FOUR
tablecity = archive_df.groupby('cidade')['quantidade'].sum()
bigcity = tablecity.idxmax()
citytotal = tablecity.max()
print(tablecity)
print(f"A cidade com  mais compras foi {bigcity.upper()} | {citytotal}")

#MISSION FIVE
ranking = archive_df.nlargest(3,'total')
print(archive_df)
print(f"\nRANKING DAS 3 MAIORES VENDAS!\n")
print(ranking)


#MISSION SIX
operations = archive_df.value_counts('produto')
operationmax = operations.idxmax()
operationqnt = operations.max()
print(operations)
print(f"O produto com mais vendas foi {operationmax.upper()} com {operationqnt} vendas!")

