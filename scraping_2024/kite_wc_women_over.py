from bs4 import BeautifulSoup
import requests
import pandas as pd 
import sys

sys.stdout.reconfigure(encoding='utf-8')

url = "https://www.formulakite.org/sailwave/liveresults_women.html"

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
        coluna.pop(4)
    
    #linhas
    elif i <= 52 and i != 26:
        linha = linha[1:-1]
        linha = (linha.replace("-\u00A0-", "-")).upper().split("-")

        if i == 40:
            linha[2] = linha[2] + " " + linha[3]
            linha.pop(3)

        list_of_data.append(linha)


df = pd.DataFrame(list_of_data, columns=coluna)
df.to_csv('kite_wc_women_over.csv', index=False)