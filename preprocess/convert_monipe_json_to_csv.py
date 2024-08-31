import time
import sys
import os
import getopt
import datetime
import json # only used in raw data


FUSO_BRASIL = 10800 # precisa tirar a diferenca do gmtime

'''
for item in data:
        date = str(time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(item["ts"] - FUSO_BRASIL)))
        item["ts"] = date # formated date

        

time_start = date_to_epoch(date_start)        
str_time_start = "time-start="+str(time_start)
url = BASE + "/" + "?source="+source+"&destination="+destination+"&"+test_id+"&"+str_time_start
'''

def date_to_epoch(date, end=False):
    if date is None: return

    year = int(date[:4])
    month = int(date[4:6])
    day = int(date[6:])

    if not end: return int(datetime.datetime(year, month, day, 0, 0, 0).timestamp())

    #return int(datetime.datetime(year, month, day+1, 0, 0, 0).timestamp()) -1
    return int(datetime.datetime(year, month, day, hour=23, minute=59, second=59).timestamp())

def json_read(path):
    # Abrir o arquivo JSON
    with open(path, 'r') as file:
        # Carregar os dados JSON em um dicionário Python
        dados = json.load(file)

    return dados


if __name__ == "__main__":

    print("Desenvolvendo Conversor do JSON MONIPE para CSV")
    print("entrada: 20240829")
    data_saida = date_to_epoch("20240829")
    data_saida_end = date_to_epoch("20240830",end=True)
    print(f"saída: {data_saida}")
    print(f"saída-end: {data_saida_end}")

    print("Dados JSON")
    dados = json_read('dados_rnp/rn-rj.json')
    print(dados[0])

