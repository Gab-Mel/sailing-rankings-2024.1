from bs4 import BeautifulSoup
import requests
import pandas as pd 
import sys

sys.stdout.reconfigure(encoding='utf-8')

url = "https://jpvm.org/results/2024/ILCA_6_Worlds/womens_results.html"

page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

nomes_tags = soup.find_all("tr")
nomes_filtrados = [tag.text for tag in nomes_tags]

list_of_data = list()

for i in range(len(nomes_filtrados)):
    linha = nomes_filtrados[i].replace("\x9a", "").replace("\n", "-")

    #colunas
    if i == 0:
        coluna = linha[1:-1]
        coluna = coluna.replace("-\u00A0-", "-").replace(" / ", "-")
        coluna = (coluna.upper()).split("-")
        coluna[15] = "M/F6"
        coluna.pop(16)
    
    # linha 1 a 102
    elif i <= 102:
        linha = linha[1:-1]
        linha = (linha.replace("--", "-")).upper()

        linha = linha.split("-")

        # porra de um nome confuso
        if i == 1:
            linha[3] = linha[3] + " " + linha[4]
            linha.pop(4)

        if i != 52:
            list_of_data.append(linha)

df = pd.DataFrame(list_of_data, columns=coluna)
df.to_csv('ilca_6_wc.csv', index=False)