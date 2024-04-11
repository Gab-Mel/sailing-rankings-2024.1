import pandas as pd 
"""
df = pd.read_csv("scraping_2024/kite_wc_women_over.csv")
indices_transicao = df[df['RANK'] == "1ST"].index

corrida1 = df.iloc[:indices_transicao[1]].reset_index(drop=True)
corrida2 = df.iloc[indices_transicao[1]:].reset_index(drop=True)

corrida1.drop(corrida1.columns[0], axis=1, inplace=True)
corrida2.drop(corrida2.columns[0], axis=1, inplace=True)


corrida1.to_csv('kite_wc_women_over_gold.csv', index=False)
corrida2.to_csv('kite_wc_women_over_silver.csv', index=False)

df = pd.read_csv("scraping_2024/kite_wc_men_over.csv")
indices_transicao = df[df['RANK'] == "1ST"].index

corrida1 = df.iloc[:indices_transicao[1]].reset_index(drop=True)
corrida2 = df.iloc[indices_transicao[1]:indices_transicao[2]].reset_index(drop=True)
corrida3 = df.iloc[indices_transicao[2]:].reset_index(drop=True)

corrida1.drop(corrida1.columns[0], axis=1, inplace=True)
corrida2.drop(corrida2.columns[0], axis=1, inplace=True)
corrida3.drop(corrida2.columns[0], axis=1, inplace=True)

corrida1.to_csv('kite_wc_men_over_gold.csv', index=False)
corrida2.to_csv('kite_wc_men_over_silver.csv', index=False)
corrida3.to_csv('kite_wc_men_over_bronze.csv', index=False)

"""

df_1 = pd.read_csv("scraping_2024\kite_wc_men_over_bronze.csv")
df_2 = pd.read_csv("scraping_2024\kite_wc_men_over_silver.csv")

list_aux = list(df_2[df_2.columns[0]])
list_aux.append("31ST")

df_1.drop(df_1.columns[0], axis=1, inplace=True)

df_1["RANK"] = list_aux
df_1.to_csv('kite_wc_men_over_bronze.csv', index=False)