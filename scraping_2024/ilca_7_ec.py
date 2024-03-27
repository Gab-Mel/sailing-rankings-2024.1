from bs4 import BeautifulSoup
import requests
import pandas as pd 
import sys

sys.stdout.reconfigure(encoding='utf-8')

url = "https://eurilca.eu/documents/303/results/ilca7.html"

page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

nomes_tags = soup.find_all("tr")
nomes_filtrados = [tag.text for tag in nomes_tags]

list_of_data = list()

for i in range(len(nomes_filtrados)):
    linha = nomes_filtrados[i].replace("\x9a", "").replace("\n", "-")

    # coluna
    if i == 1:
        coluna = linha[1:-1]
        coluna = coluna.replace("-\u00A0-", "-")
        coluna = (coluna.upper()).split("-")
        coluna.insert(5, "UNKNOW")
    
    if i >= 2 and i <= 112:
        linha = linha[1:-1]
        linha = linha.replace("-\u00A0-", "-").replace("--", "-")
        linha = (linha.upper()).split("-")

        if i == 16 or i == 70 or i == 90 or i == 93:
            linha[3] = linha[3] + " " + linha[4]
            linha.pop(4)

        try: 
            int(linha[5])
            linha.insert(5, "NO")
        except:
            pass
            
        if i!=48 and i!=94:
            list_of_data.append(linha)

df = pd.DataFrame(list_of_data, columns=coluna)
df.to_csv('ilca_7_ec.csv', index=False)