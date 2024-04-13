from bs4 import BeautifulSoup
import requests
import pandas as pd 
import sys

sys.stdout.reconfigure(encoding='utf-8')

url = "https://2024iqworldslanzarote.sailti.com/en/default/races/resultsajax/id/7550/idsc2r/22724/allResults/1/handicap"

page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

nomes_tags = soup.find_all("td")
nomes_filtrados = [tag.text for tag in nomes_tags]

list_of_data = list()

list_of_index = list(range(0, 32))


for each_column in range(0, 94):

    # essa lista tem os indices de cada um dos dados que eu quero acessar
    list_of_index_aux = [x + each_column*32 for x in list_of_index]
    
    linha = list()

    
    # 0 - colocação
    linha.append(nomes_filtrados[list_of_index_aux[0]])
    
    # 1 - país e número do barco
    linha.append(nomes_filtrados[list_of_index_aux[1]].split(" ")[2])
    linha.append(nomes_filtrados[list_of_index_aux[1]].split(" ")[3])

    
    # 2 - bow (vazio)
    linha.append("")

    # 3 - patrocinadores
    linha.append(nomes_filtrados[list_of_index_aux[3]])
    
    # 4 - nome do atleta
    linha.append(nomes_filtrados[list_of_index_aux[4]].upper().strip())

    # 5 - clube
    linha.append(nomes_filtrados[list_of_index_aux[5]].upper().strip())

    # 6 - categoria
    linha.append(nomes_filtrados[list_of_index_aux[6]].upper().strip())

    # 7 - NET
    linha.append(nomes_filtrados[list_of_index_aux[7]])

    # 8 - TOTAL
    linha.append(nomes_filtrados[list_of_index_aux[8]])
    
    # 9-28 - 1Q-20F
    for j in range(9, 29):
        linha.append(nomes_filtrados[list_of_index_aux[j]].replace("\x9a", "").replace("\n", "").replace("\r", "").split(" ")[2])

    # 29 - QF
    try:
        linha.append(nomes_filtrados[list_of_index_aux[29]].replace("\r", "").replace("\x9a", "").replace("\n", "").split(" ")[2])
    except:
        linha.append("")

    # 30 - SM
    try:
        linha.append((nomes_filtrados[list_of_index_aux[30]].replace("\r", "").replace("\x9a", "").replace("\n", "").split(" "))[2])
    except:
        linha.append("")

    # 31 - F
    try:
        linha.append((nomes_filtrados[list_of_index_aux[31]].replace("\r", "").replace("\x9a", "").replace("\n", "").split(" "))[2])
    except:
        linha.append("")
    
    list_of_data.append(linha)


coluna = ["RANK", "COUNTRY", "BOAT_NUMBER", "BOW", "SPONSOR", "CREW", "CLUB", "CATEGORY", "NETT", "TOTAL",
                   "1Q", "2Q", "3Q", "4Q", "5Q", "6Q", "7Q", "8Q", "9Q", "10Q", "11F", "12F", "13F", "14F",
                   "15F", "16F", "17F", "18F", "19F", "20F", "QF", "SF", "F"]

df = pd.DataFrame(list_of_data, columns=coluna)
df.to_csv('scraping_2024/iqfoil_wc_women.csv', index=False)