import time
import glob
import fnmatch
import sys
import os
import os.path
import getopt
import datetime
import json


FUSO_BRASIL = 10800 # precisa tirar a diferenca do gmtime
ARQUIVO_LOG = "log.log"
DIRETORIO_BASE = "C:/Users/loyol/OneDrive/Notebook/Sidney/Doutorado/Pesquisa/TESE/Experimentos/RNP/MONIPE"

def json_read(path):
    # Abrir o arquivo JSON
    try:
        with open(path, 'r') as file:
            # Carregar os dados JSON em um dicionário Python
            print(path)
            dados = json.load(file)
            return dados
    except Exception as e:
        print(path)
        print("Exceção:")
        print(e)


def med(lista):
    return sum(lista)/len(lista)

metrica = "histogram-rtt"
caminho = DIRETORIO_BASE+"/"+metrica+"/"
nomeArquivo = "ac-rj-1.json"
dados = json_read(caminho+nomeArquivo)
keys = dados[0]["val"].keys()
lista_keys = list(keys)
lista_keys_num = [float(s) for s in lista_keys]

print("Item 0: ",dados[0])
print("ts: ",dados[0]["ts"])
print("val: ",dados[0]["val"])
print("val-keys: ",keys)
print("val-keys type: ",type(lista_keys))
print("lista-keys: ",lista_keys)
print("MAX: ",max(lista_keys_num))
print("Media: ",med(lista_keys_num))
print("Min: ",min(lista_keys_num))
