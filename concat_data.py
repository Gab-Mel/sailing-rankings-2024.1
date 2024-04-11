import pandas as pd 
import numpy as np 

# TRATANDO AS NOMES
def trata_nomes(valor:str):
    """
    """
    if valor.count("(") != 0:
        return valor.split("(")[0].strip()
    else:
        return valor

def merge(data_path:str, first_race:int, last_race:int, name_index:int, nome_classe:str, position_index:int=0, flag_name:str="OVER"):
    """
    """

    dataframe = pd.read_csv(data_path)

    lista_de_dados = list()

    for i in range(first_race, last_race + 1):
        each_column = dataframe.columns[i]

        for each_line in range(len(dataframe)):
            lista_temporaria = list()

            linha = list(dataframe.iloc[each_line])

            #identificador
            lista_temporaria.append(trata_nomes(linha[name_index]) + " - " + nome_classe)

            # nome da ragata
            lista_temporaria.append(each_column)

            # nome do atleta ou dupla
            lista_temporaria.append(linha[name_index])

            # pontuacao
            lista_temporaria.append(dataframe[each_column].iloc[each_line])

            # nome classe
            lista_temporaria.append(nome_classe)

            # flag
            lista_temporaria.append(flag_name)

            # posição
            if linha[position_index] != "RANK":
                lista_temporaria.append(linha[position_index])
                lista_de_dados.append(lista_temporaria)

    return lista_de_dados

df_1 = pd.DataFrame(columns=["Identificador", "Regata", "Nome Competidor", "Pontuação Regata (Nha)", "Classe Vela", "Flag Name", "Posição Geral"], data=merge("scraping_2024/kite_wc_women_over_silver.csv", 6, 24, 2, "Kite Fem.", flag_name="Silver"))
df_2 = pd.DataFrame(columns=["Identificador", "Regata", "Nome Competidor", "Pontuação Regata (Nha)", "Classe Vela", "Flag Name", "Posição Geral"], data=merge("scraping_2024/kite_wc_women_over_gold.csv", 6, 24, 2, "Kite Fem.", flag_name="Gold"))
df_3 = pd.DataFrame(columns=["Identificador", "Regata", "Nome Competidor", "Pontuação Regata (Nha)", "Classe Vela", "Flag Name", "Posição Geral"], data=merge("scraping_2024/kite_wc_men_over_silver.csv", 6, 25, 2, "Kite Masc.", flag_name="Silver"))
df_4 = pd.DataFrame(columns=["Identificador", "Regata", "Nome Competidor", "Pontuação Regata (Nha)", "Classe Vela", "Flag Name", "Posição Geral"], data=merge("scraping_2024/kite_wc_men_over_bronze.csv", 5, 24, 1, "Kite Masc.", 25, flag_name="Bronze"))
df_5 = pd.DataFrame(columns=["Identificador", "Regata", "Nome Competidor", "Pontuação Regata (Nha)", "Classe Vela", "Flag Name", "Posição Geral"], data=merge("scraping_2024/kite_wc_men_over_gold.csv", 6, 25, 2, "Kite Masc.", flag_name="Gold"))
df_6 = pd.DataFrame(columns=["Identificador", "Regata", "Nome Competidor", "Pontuação Regata (Nha)", "Classe Vela", "Flag Name", "Posição Geral"], data=merge("scraping_2024/iqfoil_wc_women.csv", 11, 33, 6, "IQFoil Fem.", 1))
df_7 = pd.DataFrame(columns=["Identificador", "Regata", "Nome Competidor", "Pontuação Regata (Nha)", "Classe Vela", "Flag Name", "Posição Geral"], data=merge("scraping_2024/iqfoil_wc_men.csv", 11, 32, 6, "IQFoil Masc.", 1))
df_8 = pd.DataFrame(columns=["Identificador", "Regata", "Nome Competidor", "Pontuação Regata (Nha)", "Classe Vela", "Flag Name", "Posição Geral"], data=merge("scraping_2024/ilca_7_wc.csv", 6, 16, 4, "ILCA 7", 1))
df_9 = pd.DataFrame(columns=["Identificador", "Regata", "Nome Competidor", "Pontuação Regata (Nha)", "Classe Vela", "Flag Name", "Posição Geral"], data=merge("scraping_2024/ilca_7_ec_gold.csv", 7, 14, 4, "ILCA 7", 1, flag_name="Gold"))
df_10 = pd.DataFrame(columns=["Identificador", "Regata", "Nome Competidor", "Pontuação Regata (Nha)", "Classe Vela", "Flag Name", "Posição Geral"], data=merge("scraping_2024/ilca_7_ec_silver.csv", 7, 13, 4, "ILCA 7", 1, flag_name="Silver"))
df_11 = pd.DataFrame(columns=["Identificador", "Regata", "Nome Competidor", "Pontuação Regata (Nha)", "Classe Vela", "Flag Name", "Posição Geral"], data=merge("scraping_2024/ilca_7_ec_bronze.csv", 7, 13, 4, "ILCA 7", 1, flag_name="Bronze"))
df_12 = pd.DataFrame(columns=["Identificador", "Regata", "Nome Competidor", "Pontuação Regata (Nha)", "Classe Vela", "Flag Name", "Posição Geral"], data=merge("scraping_2024/ilca_6_wc.csv", 6, 16, 4, "ILCA 6", 1))
df_13 = pd.DataFrame(columns=["Identificador", "Regata", "Nome Competidor", "Pontuação Regata (Nha)", "Classe Vela", "Flag Name", "Posição Geral"], data=merge("scraping_2024/ilca_6_ec_silver.csv", 7, 13, 4, "ILCA 6", 1, flag_name="Silver"))
df_14 = pd.DataFrame(columns=["Identificador", "Regata", "Nome Competidor", "Pontuação Regata (Nha)", "Classe Vela", "Flag Name", "Posição Geral"], data=merge("scraping_2024/ilca_6_ec_gold.csv", 7, 14, 4, "ILCA 6", 1, flag_name="Gold"))
df_15 = pd.DataFrame(columns=["Identificador", "Regata", "Nome Competidor", "Pontuação Regata (Nha)", "Classe Vela", "Flag Name", "Posição Geral"], data=merge("scraping_2024/cleaned_data/470_mixed.csv", 7, 17, 5, "470", 2))
df_16 = pd.DataFrame(columns=["Identificador", "Regata", "Nome Competidor", "Pontuação Regata (Nha)", "Classe Vela", "Flag Name", "Posição Geral"], data=merge("scraping_2024/cleaned_data/49er_wc.csv", 6, 23, 4, "49er", 2))
df_17 = pd.DataFrame(columns=["Identificador", "Regata", "Nome Competidor", "Pontuação Regata (Nha)", "Classe Vela", "Flag Name", "Posição Geral"], data=merge("scraping_2024/cleaned_data/49erfx_wc.csv", 6, 22, 4, "49erfx", 2))

df_final = pd.concat([df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8, df_9, df_10, df_11, df_12, df_13, df_14, df_15, df_16, df_17])

df_final = df_final.dropna(subset=['Pontuação Regata (Nha)']).reset_index(drop=True)

df_final['Nome Competidor'] = df_final['Nome Competidor'].apply(trata_nomes)

# TRATANDO AS POSIÇÕES
def trata_posicao(valor:str):
    """
    """
    return str(valor).replace("TH", "").replace("ST", "").replace("RD", "").replace("ND", "")

df_final['Posição Geral'] = df_final['Posição Geral'].apply(trata_posicao)

# TRATANDO PONTUAÇÕES
def trata_pontuacao(valor:str):
    try:
        return float(valor.split("-")[0])
    except:
        return 0

df_final['Pontuação Regata'] = df_final['Pontuação Regata (Nha)'].apply(trata_pontuacao)

df_final = df_final.loc[df_final['Pontuação Regata'] != 0].reset_index(drop=True)

# TRATANDO DESCARTES
# tem que olhar depois para alguns valores inusitados
def trata_descartes(valor:str):
    try:
        return valor.split("-")[1]
    except:
        return valor
    
df_final['Descarte'] = df_final['Pontuação Regata (Nha)'].apply(trata_descartes)

#TRATANDO PUNIÇÕES
def trata_punicoes(valor:str):
    try:
        return valor.split("-")[2]
    except:
        return ""
    
df_final['Punição'] = df_final['Pontuação Regata (Nha)'].apply(trata_punicoes)

# TRATA FLOTILHA
def trata_flotilha(valor:str):
    lista = ["F", "SF", "QF", "MEDAL", "FINAL"]
    if valor in lista:
        return "MEDAL RACE"
    else:
        return "GERAL"

df_final['Flotilha'] = df_final['Regata'].apply(trata_flotilha)

df_final.to_csv('df_merged_2024.csv', index=False)