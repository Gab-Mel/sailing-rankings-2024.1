import pandas as pd
import numpy as np


def merge(data_path:str, first_race:int, last_race:int, name_index:int, nome_classe:str, position_index:int=0):
    """
    """

    dataframe = pd.read_csv(data_path)

    lista_de_dados = list()

    for i in range(first_race, last_race + 1):
        each_column = dataframe.columns[i]

        for each_line in range(len(dataframe)):
            lista_temporaria = list()

            linha = list(dataframe.iloc[each_line])

            # nome da ragata
            lista_temporaria.append(each_column)

            # nome do atleta ou dupla
            lista_temporaria.append(linha[name_index])

            # pontuacao
            lista_temporaria.append(dataframe[each_column].iloc[each_line])

            # nome classe
            lista_temporaria.append(nome_classe)

            # posição
            if linha[position_index] != "RANK":
                lista_temporaria.append(linha[position_index])
                lista_de_dados.append(lista_temporaria)

    return lista_de_dados
            
df_1 = pd.DataFrame(columns=["Regata", "Nome Competidor", "Pontuação Regata", "Classe Vela", "Posição Geral"], data=merge("scraping_2024/kite_wc_women_over.csv", 6, 24, 2, "Kite Fem."))
df_2 = pd.DataFrame(columns=["Regata", "Nome Competidor", "Pontuação Regata", "Classe Vela", "Posição Geral"], data=merge("scraping_2024/kite_wc_men_over.csv", 6, 25, 2, "Kite Mas."))
df_3 = pd.DataFrame(columns=["Regata", "Nome Competidor", "Pontuação Regata", "Classe Vela", "Posição Geral"], data=merge("scraping_2024/iqfoil_wc_women.csv", 10, 32, 5, "IQFOIL"))
df_4 = pd.DataFrame(columns=["Regata", "Nome Competidor", "Pontuação Regata", "Classe Vela", "Posição Geral"], data=merge("scraping_2024/iqfoil_wc_men.csv", 10, 31, 5, "IQFOIL"))
df_5 = pd.DataFrame(columns=["Regata", "Nome Competidor", "Pontuação Regata", "Classe Vela", "Posição Geral"], data=merge("scraping_2024/ilca_7_wc.csv", 5, 15, 3, "ILCA 7"))
df_6 = pd.DataFrame(columns=["Regata", "Nome Competidor", "Pontuação Regata", "Classe Vela", "Posição Geral"], data=merge("scraping_2024/ilca_7_ec.csv", 10, 13, 3, "ILCA 7"))
df_7 = pd.DataFrame(columns=["Regata", "Nome Competidor", "Pontuação Regata", "Classe Vela", "Posição Geral"], data=merge("scraping_2024/ilca_6_wc.csv", 5, 15, 3, "ILCA 6"))
df_8 = pd.DataFrame(columns=["Regata", "Nome Competidor", "Pontuação Regata", "Classe Vela", "Posição Geral"], data=merge("scraping_2024/ilca_6_ec.csv", 10, 13, 3, "ILCA 6"))
df_9 = pd.DataFrame(columns=["Regata", "Nome Competidor", "Pontuação Regata", "Classe Vela", "Posição Geral"], data=merge("scraping_2024/470_mixed.csv", 5, 16, 3, "470"))
df_10 = pd.DataFrame(columns=["Regata", "Nome Competidor", "Pontuação Regata", "Classe Vela", "Posição Geral"], data=merge("scraping_2024/49er_wc.csv", 4, 20, 2, "49er"))
df_11 = pd.DataFrame(columns=["Regata", "Nome Competidor", "Pontuação Regata", "Classe Vela", "Posição Geral"], data=merge("scraping_2024/49erfx_wc.csv", 4, 20, 2, "49erfx"))

# MERGE DOS DADOS
df_final = pd.concat([df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8, df_9, df_10, df_11])

# TRATANDO AS POSIÇÕES

def trata_posicao(valor:str):
    """
    """
    return str(valor).replace("TH", "").replace("ST", "").replace("RD", "").replace("ND", "")

df_final['Posição Geral'] = df_final['Posição Geral'].apply(trata_posicao)

# TRATANDO NOMES
def trata_nomes(valor:str):
    """
    """
    if valor.count("(") != 0:
        return valor.split("(")[0].strip()
    else:
        return valor

df_final['Nome Competidor'] = df_final['Nome Competidor'].apply(trata_nomes)

# TRATANDO PONTUAÇÃO
def trata_pontuacao(valor:str):
    """
    """
    # valores normais 15
    try:
        return int(valor)
    except:

        # valores com ponto, mas sem parêntese 15.0
        try:
            return int(str(valor).split(".")[0])
        
        except:
            try:
                # valores com ponto, e com parêntese (15.0)
                return int(str(valor).split(".")[0][1:])
            
            except:
                # valores sem pontos, mas com parêntes (15)
                try:
                    return int(str(valor).split(")")[0][1:])
                
                except:
                    # começam com numeros
                    try:
                        return int(str(valor)[1:3])
                    except:
                        try:
                            return int(str(valor).split("(")[1][0:2])
                        except:
                            try:
                                return int(str(valor).split(" ")[1][0:2])
                            except:
                                try:
                                    return int(str(valor).split(".")[1])
                                except:
                                    print(valor)
                                    return "Nada"

df_final["Pontuação Regata"] = df_final["Pontuação Regata"].apply(trata_pontuacao)  

print(df_final["Pontuação Regata"].value_counts())