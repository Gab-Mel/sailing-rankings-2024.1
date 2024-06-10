import pandas as pd
from src.models.athlete import Athlete, AthleteRepository
from src.models.competition import Competition, CompetitionRepository
from src.models.final_data import FinalData, FinalDataRepository
from src.models.ranking_elo_40 import RankingElo40, RankingElo40Repository

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
    return pd.read_excel('../dados_finais_2024/competicoes.xlsx')

def sumulas():
    return pd.read_excel('../dados_finais_2024/sumulas.xlsx')
"""
atletas = atleta()
competicoes = competicoes()
final_data = sumulas()
atleta_repository = AthleteRepository()
competition_repository = CompetitionRepository()
final_data_repository = FinalDataRepository()


for i in range(len(atletas)):
    id = atletas['ID Competidor'][i]
    name = atletas['Nome Competidor'][i]
    nationality = "None"
    age = 0
    
    atleta_repository.create(id=id, name=name, 
                             nationality=nationality, age=age)

for i in range(len(competicoes)):
    if competicoes['ID Competição'][i] is not None:
        id = competicoes['ID Competição'][i]
        name = competicoes['Nome Competição'][i]
        year = None
        competition_repository.create(id=id, name=name, year=year)
    
for i in range(len(final_data)):
    id = final_data['ID Resultado'][i]
    id_atleta = final_data['ID Competidor'][i]
    id_competicao = final_data['ID Competição'][i]
    classe_vela = final_data['Classe Vela'][i]
    pontuacao_regata = final_data['Pontuação Regata'][i]
    descarte = final_data['Descarte'][i]
    flotilha = final_data['Flotilha'][i]
    posicao = final_data['Posição Geral'][i]
    punicao = final_data['Punição'][i]
    if final_data['Pontuação Total'][i] == 'DNF':
        pontuacao_total = 0
    else:
        pontuacao_total = final_data['Pontuação Total'][i]
    nett = final_data['Nett'][i]
    final_data_repository.create(id=id, athlete_id=id_atleta, 
                                 competition_id=id_competicao, 
                                 classe_vela=classe_vela, 
                                 pontuacao_regata=pontuacao_regata, 
                                 descarte=descarte, flotilha=flotilha, 
                                 posicao=posicao, punicao=punicao, 
                                 pontuacao_total=pontuacao_total, nett=nett)


ranking = ranking_elo_40_49ER()
ranking_elo_40_repository = RankingElo40Repository()

for i in range(len(ranking)):
    name=ranking['Unnamed: 0'][i]
    score = ranking['Rating'][i]
    class_vela = '49ER'
    ano = 2024
    ranking_elo_40_repository.create(id_atleta=name, score=score, class_vela=class_vela, year=ano)
                                
ranking = ranking_elo_40_49ERFX()
for i in range(len(ranking)):
    name=ranking['Unnamed: 0'][i]
    score = ranking['Rating'][i]
    class_vela = '49ERFX'
    ano = 2024
    ranking_elo_40_repository.create(id_atleta=name, score=score, class_vela=class_vela, year=ano)

ranking = ranking_elo_ILCA_6()
for i in range(len(ranking)):
    name=ranking['Unnamed: 0'][i]
    score = ranking['Rating'][i]
    class_vela = 'ILCA 6'
    ano = 2024
    ranking_elo_40_repository.create(id_atleta=name, score=score, class_vela=class_vela, year=ano)

ranking = ranking_elo_ILCA_7()
for i in range(len(ranking)):
    name=ranking['Unnamed: 0'][i]
    score = ranking['Rating'][i]
    class_vela = 'ILCA 7'
    ano = 2024
    ranking_elo_40_repository.create(id_atleta=name, score=score, class_vela=class_vela, year=ano)
"""

from src.utils.models import *
import pandas as pd
import warnings


ranking_elo_40_repository = RankingElo40Repository()

data = pd.read_excel('../dados_finais_2024/final_data.xlsx')

data = data[data['Classe Vela'] == "ILCA 7"]

for competition in data['Nome Competição']:
        data.loc[data['Nome Competição'] == competition, 'Ano'] = int(re.findall(r'\d{4}', competition)[0])

def ranking_by_year(ano:int=2024) -> pd.DataFrame:
    """
    """
    data_fun = data[data['Ano'] <= ano]

    elo = EloRating(ratings={competitor: 1500 for competitor in data_fun['Nome Competidor'].unique()}, k=40)

    # get data in the format needed for error calculation
    data_dict = []
    grouped_data = data_fun.groupby(["Ano","Nome Competição", "Nome Competidor", ]).agg({"Posição Geral": "min"}
        ).sort_values(by=["Ano", "Nome Competição", "Posição Geral"], ascending=True).reset_index()

    for ano in grouped_data["Ano"].unique():
        for comp in grouped_data[grouped_data["Ano"] == ano]["Nome Competição"].unique():
            results = grouped_data[(grouped_data["Ano"] == ano) & (grouped_data["Nome Competição"] == comp)]["Posição Geral"].values
            names = grouped_data[(grouped_data["Ano"] == ano) & (grouped_data["Nome Competição"] == comp)]["Nome Competidor"].values
            data_dict.append([results, names])

    elo.fit(data_dict)
    ratings = elo.ratings

    ratings = pd.DataFrame.from_dict(ratings, orient='index', columns=['Rating']).sort_values(by="Rating").sort_values(by="Rating", ascending=False)
    return ratings

rk_2015 = ranking_by_year(2015)
rk_2016 = ranking_by_year(2016)
rk_2017 = ranking_by_year(2017)
rk_2018 = ranking_by_year(2018)
rk_2019 = ranking_by_year(2019)
rk_2020 = ranking_by_year(2020)
rk_2021 = ranking_by_year(2021)
rk_2022 = ranking_by_year(2022)
rk_2023 = ranking_by_year(2023)
rk_2024 = ranking_by_year(2024)

print(rk_2015.keys())

for i in range(len(rk_2015)):
    name=rk_2015.iloc[i].name
    score = rk_2015['Rating'][i]
    class_vela = 'ILCA 7'
    ano = 2015
    ranking_elo_40_repository.create(id_atleta=name, score=score, class_vela=class_vela, year=ano)
    
print('2015')

for i in range(len(rk_2016)):
    name=rk_2016.iloc[i].name
    score = rk_2016['Rating'][i]
    class_vela = 'ILCA 7'
    ano = 2016
    ranking_elo_40_repository.create(id_atleta=name, score=score, class_vela=class_vela, year=ano)
    
print('2016')

for i in range(len(rk_2017)):
    name=rk_2017.iloc[i].name
    score = rk_2017['Rating'][i]
    class_vela = 'ILCA 7'
    ano = 2017
    ranking_elo_40_repository.create(id_atleta=name, score=score, class_vela=class_vela, year=ano)
    
print('2017')
    
for i in range(len(rk_2018)):
    name=rk_2018.iloc[i].name
    score = rk_2018['Rating'][i]
    class_vela = 'ILCA 7'
    ano = 2018
    ranking_elo_40_repository.create(id_atleta=name, score=score, class_vela=class_vela, year=ano)
    
print('2018')
    
for i in range(len(rk_2019)):
    name=rk_2019.iloc[i].name
    score = rk_2019['Rating'][i]
    class_vela = 'ILCA 7'
    ano = 2019
    ranking_elo_40_repository.create(id_atleta=name, score=score, class_vela=class_vela, year=ano)

print('2019')

for i in range(len(rk_2020)):
    name=rk_2020.iloc[i].name
    score = rk_2020['Rating'][i]
    class_vela = 'ILCA 7'
    ano = 2020
    ranking_elo_40_repository.create(id_atleta=name, score=score, class_vela=class_vela, year=ano)

print('2020')
    
for i in range(len(rk_2021)):
    name=rk_2021.iloc[i].name
    score = rk_2021['Rating'][i]
    class_vela = 'ILCA 7'
    ano = 2021
    ranking_elo_40_repository.create(id_atleta=name, score=score, class_vela=class_vela, year=ano)

print('2021')

for i in range(len(rk_2022)):
    name=rk_2022.iloc[i].name
    score = rk_2022['Rating'][i]
    class_vela = 'ILCA 7'
    ano = 2022
    ranking_elo_40_repository.create(id_atleta=name, score=score, class_vela=class_vela, year=ano)

print('2022')
   
for i in range(len(rk_2023)):
    name=rk_2023.iloc[i].name
    score = rk_2023['Rating'][i]
    class_vela = 'ILCA 7'
    ano = 2023
    ranking_elo_40_repository.create(id_atleta=name, score=score, class_vela=class_vela, year=ano)

print('2023')
   
for i in range(len(rk_2024)):
    name=rk_2024.iloc[i].name
    score = rk_2024['Rating'][i]
    class_vela = 'ILCA 7'
    ano = 2024
    ranking_elo_40_repository.create(id_atleta=name, score=score, class_vela=class_vela, year=ano)