import pandas as pd 

final_data = pd.read_excel("data/final_data_original.xlsx", sheet_name="Atletas")

dict_id = dict()
new_id = 0
for i in range(len(final_data)):
    dict_id[final_data["Nome Competidor"].iloc[i]] = final_data["ID Competidor"].iloc[i]

    if final_data["ID Competidor"].iloc[i] > new_id:
        new_id = final_data["ID Competidor"].iloc[i]

temp_data = pd.read_csv("df_merged_2024.csv")

conjunto_de_nomes = set(temp_data["Nome Competidor"])
conjunto_de_nomes_antigos = set(final_data["Nome Competidor"])

nomes_novos = conjunto_de_nomes - conjunto_de_nomes_antigos

for cada_atleta in nomes_novos:
    dict_id[cada_atleta] = new_id + 1
    new_id += 1

df_final = pd.DataFrame(data=list(dict_id.items()), columns=["Nome Competidor", "ID Competidor"])

df_final.to_excel("temp_data.xlsx")

