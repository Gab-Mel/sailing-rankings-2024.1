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