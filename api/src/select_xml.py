import pandas as pd

listRanking = pd.read_excel('final_data.xlsx')

def retun_xlsx():
    return listRanking

print(retun_xlsx())