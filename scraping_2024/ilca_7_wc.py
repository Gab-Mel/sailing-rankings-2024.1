from bs4 import BeautifulSoup
import requests
import pandas as pd 
import sys

sys.stdout.reconfigure(encoding='utf-8')

url = "https://jpvm.org/results/2024/ILCA_7/results.html"

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
        coluna[15] = coluna[15] + "/" + coluna[16]
        coluna.pop(16)

    # linha 1 a 154
    elif i <= 154:
        linha = linha[1:-1]
        linha = (linha.replace("--", "-")).upper()
        linha = linha.split("-")

        if i == 7 or i == 50:
            linha[3] = linha[3] + " " + linha[4]
            linha.pop(4)

        if i != 52 and i != 104:
            list_of_data.append(linha)

# tá faltando o total e o net, mas dá pra arrumar
df = pd.DataFrame(list_of_data, columns=coluna)
df.to_csv('ilca_7_wc.csv', index=False)