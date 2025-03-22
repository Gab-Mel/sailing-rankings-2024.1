import streamlit as st
import pandas as pd
from src.models.athlete import Athlete, AthleteRepository
from src.models.competition import Competition, CompetitionRepository
from src.models.final_data import FinalData, FinalDataRepository
from src.models.ranking_elo_40 import RankingElo40, RankingElo40Repository

st.write("""
# My first app
Hello *world!*
""")

def mostrar_atletas():
    lista = AthleteRepository().list()
    for i in range(len(lista)):
        st.write(lista[i])
        
def mostrar_competicoes():
    lista = CompetitionRepository().list()
    for i in range(len(lista)):
        st.write(lista[i])

def mostrar_perfil(lista):
    st.title('Perfil do Atleta')
    st.write('Nome:', lista['id'])
    st.write('Nacionalidade:', lista['score'])
    
def mostrar_grafico_pessoal(lista):
    st.line_chart(lista['score', 'class_vela', 'year'])


class_vela = st.selectbox('selecione a classe da vela', ['49ER', '49ERFX', 'ILCA 6', 'ILCA 7'])
year = st.selectbox('selecione o ano do ranking', ['2015', '2016', '2017', '2018', '2019', '2020', 
                                                   '2021', '2022', '2023', '2024', '2025', '2026', 
                                                   '2027'])
modelo_ranking = st.selectbox('selecione o modelo do ranking', ['Elo 40', 'Elo 50', 'Elo 60', 'Elo 70'])


#lista = AthleteRepository().list()

st.markdown(
    """
    <script>
    document.getElementById('imagem_select').addEventListener('change', function() {
        window.location.reload();
    });
    </script>
    """,
    unsafe_allow_html=True)





if st.button('mostrar atletas'):
    lista = RankingElo40Repository().list(year=str(year), class_vela=class_vela)
    df = pd.DataFrame(lista, columns=['id', 'score', 'class_vela', 'year'])
    for i in range(len(df)):
        if st.button(str(df['id'][i]) + 'Score:' + str(df['score'][i])):
            print('clicou')
            lista_rank = RankingElo40Repository().list_atleta(id_atleta=df['id'][i])
            print(lista_rank)
            mostrar_grafico_pessoal(lista_rank)
            
    st.write('You selected:', class_vela, year, modelo_ranking)


if st.button('ir para Gráfico'):
    lista = RankingElo40Repository().list_all(year=str(year), class_vela=class_vela)
    df = pd.DataFrame(lista, columns=['id', 'score', 'class_vela', 'year'])
    st.line_chart(df, x = 'year', y = 'score', color= 'id')

    st.write('You selected:', class_vela, year, modelo_ranking)

        #print('clicou')
        #mostrar_perfil(df.iloc[i])

st.page_link("pages/grafico.py", label="Ir para Gráfico")


# print(type(AthleteRepository().list()))



 
#df = pd.read_csv("my_data.csv")
#st.line_chart(df)