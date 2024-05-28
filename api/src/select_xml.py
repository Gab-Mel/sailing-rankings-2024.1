import pandas as pd

#listRanking = pd.read_excel('src/final_data.xlsx')

def ranking_elo_40_49ER():
    return pd.read_csv('../rankings_2024/elo/elo-40-49ER.csv')

def ranking_elo_40_49ERFX():
    return pd.read_csv('../rankings_2024/elo/elo-40-49ERFX.csv')

def ranking_elo_ILCA_6():
    return pd.read_csv('../rankings_2024/elo/elo-40-ILCA 6.csv')

def ranking_elo_ILCA_7():
    return pd.read_csv('../rankings_2024/elo/elo-40-ILCA 7.csv')

def atleta():
    return pd.read_excel('../dados_finais_2024/atletas.xlsx')

def competicoes():
    return pd.read_excel('../dados_finais_2024/final_data.xlsx')

def sumulas():
    return pd.read_excel('../dados_finais_2024/sumulas.xlsx')

sumulas = sumulas()
print(sumulas['Classe Vela'].value_counts())
#print(retun_xlsx())
#print(listRanking.keys())