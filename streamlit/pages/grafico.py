import streamlit as st
import pandas as pd
from src.models.athlete import Athlete, AthleteRepository
from src.models.competition import Competition, CompetitionRepository
from src.models.final_data import FinalData, FinalDataRepository
from src.models.ranking_elo_40 import RankingElo40, RankingElo40Repository

class_vela = st.selectbox('selecione a classe da vela', ['49ER', '49ERFX', 'ILCA 6', 'ILCA 7'])
year = st.selectbox('selecione o ano do ranking', ['2015', '2016', '2017', '2018', '2019', '2020', 
                                                   '2021', '2022', '2023', '2024', '2025', '2026', 
                                                   '2027'])

lista_atletas = AthleteRepository().list()
lista_atletas = pd.DataFrame(lista_atletas, columns=['id', 'name', 'national', 'age'])
atletas = tuple(st.multiselect('selecione os atletas', list(lista_atletas['name'])))

if st.button('mostrar Gráfico'):
    lista = RankingElo40Repository().list_by_athletes(class_vela=class_vela, year=year, atletas=atletas)
    df = pd.DataFrame(lista, columns=['id', 'score', 'class_vela', 'year'])
    st.line_chart(df, x = 'year', y = 'score', color= 'id')

    st.write('You selected:', class_vela, year)