# sailing-rankings-2024.1
Esse repositório armazena todos os scripts e resultados do projeto Fields 2024.1 juntamente com os avanços obtidos pela equipe do semestre anterior que pode ser vizualizado em [```saling-rankings```](https://github.com/cristianolarrea/sailing-rankings) desenvolvido em parceria da FGV EMAp com a CBVela. O desenvolvimento do projeto de 2024 é de autoria de:

# sailing-rankings

* Emanuel Bissiatti de Almeida
* Gabriel de Melo Lima
* Matheus Fillype Ferreira de Carvalho
* Sillas Rocha da Costa

O objetivo do projeto era atualizar os dados das competições de vela mundiais e nacionais e melhorar os modelos de ranking para os competidores de classes olímpicas da vela mundial. 

## Modelos de Ranking
Os modelos de ranking a se trabalhar são:
- Elo ranking
  - Variações do parâmetro k
- Keener's Method
  - Versões _alpha_ e _beta_
  - Versões com e sem _time decay_

## Organização do repositório

### Recursos fornecidos pela equipe anterior:

[`data`](data): pasta contendo os dados gerais do projeto. 
  - [`final_data.xlsx`](data/final_data.xlsx): Banco de dados completo construído durante o projeto, completamente tratado e pronto para uso
  - [`banco_sem_processamento.xlsx`](data/banco_sem_processamento.xlsx): Banco de dados obtido após o fim do processo de coleta, antes do processamento e limpeza, para controle e versionamento. Não utilizar para análises ou elaboração de rankings
  - [`banco_campeonatos.xlsx`](data/banco_campeonatos.xlsx): Arquivo contendo campeonatos presentes no banco e ids.
  - [`mapped_competitions.xlsx`](data/mapped_competitions.xlsx): Arquivo contendo cada competição presente no banco (campeonato e ano) e o link para acessar os resultados originais

[`eda`](eda): pasta com o arquivo [`eda.ipynb`](eda/eda.ipynb), onde foi desenvolvida uma análise mais profunda dos dados coletados, com manipulações e visualizações a partir de perguntas e hipóteses definidas pelo grupo em contato com a equipe de negócios

[`general_cleaning`](general_cleaning): pasta contendo os notebooks utilizados para a limpeza dos dados brutos coletados via webscraping
  - [`fleetPoints.ipynb`](general_cleaning/fleetPoints.ipynb): pipeline de ajustes (1) da coluna de ID do campeonato de acordo com o nome do campeonato e (2) do formato da coluna com a pontuação das regatas, tratando todos os casos atípicos
  - [`cleaning_names`](general_cleaning/cleaning_names): subpasta com o pipeline de tratamento (via código e manual) dos nomes dos competidores
  - [`duplicates_fixer.ipynb`](general_cleaning/duplicates_fixer.ipynb):

[`mapping`](mapping): script auxiliar simples para indicar quais competições já haviam tido os dados extraídos em relação à lista de competições com dados mapeados em páginas da internet

[`rankings`](rankings): pasta contendo os arquivos `.csv` de ranking das classes 49er, 49erFX, Ilca 6, Ilca 7
  - [`rankings`](rankings/final_results): pasta com os resultados finais para uso geral
  - [`rankings`](rankings/trainsets): pasta com os arquivos de treino para cálculo de métricas de erro

[`scrapers`](scrapers): pasta contendo mapeamentos de páginas com súmulas, scripts para realização da raspagem de dados e os dados resultantes do scraping
  - [`clusters`](scrapers/clusters): pasta com os scripts e mapeamentos
      - [`Clusters-Sumulas.xlsx`](scrapers/clusters/Clusters-Sumulas.xlsx): mapeamento de súmulas em diferentes clusters, com imagem do estilo da página HTML
      - [`Mapeamento.xlsx`](scrapers/clusters/Mapeamento.xlsx): mapeamento de competições mais antigas de 49er, 49erFX, Ilca 6 e Ilca 7, separadas por cluster
      - Arquivos `.ipynb` para a extração dos dados de cada um dos clusters, com indicação do cluster no nome do arquivo
      - [`utils.py`](scrapers/clusters/utils.py): arquivo com funções auxiliares para padronização dos dados extraídos
  - [`scraped-data`](scrapers/scraped-data): arquivos com todos os dados extraídos
  - [`source-data`](scrapers/source-data):

[`src`](src): pasta contendo os scripts associados à elaboração dos métodos de ranking (modelos e métricas)
  - [`models.py`](src/models.py): arquivo `.py` contendo a funções para execução dos modelos, desde fits a métricas de erro.
  - [`using_models.py`](src/using_models.py): arquivo exemplificando a execução de ambos os modelos
  - [`using_keeners.py`](src/using_keeners.py): arquivo exemplificando a execução específica do Keeners
  - [`using_elo.py`](src/using_elo.py): arquivo exemplificando a execução específica do Elo
  - [`keeners.py`](src/keeners.py): arquivo utilizado durante a contrução do Keeners (somente para testes e estudo do modelo, não deve ser usado para gerar rankings)
  - [`generate-elo-ranking.py`](src/generate-elo-ranking.py): arquivo utilizado durante a contrução do Elo (somente para testes e estudo do modelo, não deve ser usado para gerar rankings)
  - [`prediction_error`](src/prediction_error): arquivo utilizado durante a elaboração da métrica de erro de predição (somente para testes e estudo, não deve ser usado para gerar rankings)

### Atualizações:

[`dados`](dados_finais_2024): contem os dados atualizados do projeto.
  - [`final_data.xlsx`](data/final_data.xlsx): Banco de dados completo construído durante o projeto, completamente tratado e pronto para uso;
  - [`competições](dados_finais_2024/competicoes.xlsx): Lista de competições coletadas;
  - [`sumulas`](dados_finais_2024/sumulas.xlsx): Banco de dados contendo todos os dados de atualização ainda não processados;
  - [`atletas`](dados_finais_2024/atletas.xlsx): Lista contendo todos os atletas participantes das competições mapeadas.
