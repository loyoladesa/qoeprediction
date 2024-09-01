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

def EscreveLog(mensagem):
    try:
        with open(ARQUIVO_LOG, "a") as file:
            file.write(str(mensagem) + "\n")
            file.close()

    except:
        print("Erro na Escrita:" + mensagem + " " + str(datetime.datetime.now()))

# Escreve registros em arquivo
def EscreveArquivo(registros, nomeArquivo):
    for registro in registros:
        try:
            with open(nomeArquivo, "a") as file:
                file.write(str(registro))
                file.close()
        except Exception as e:
            EscreveLog("Erro escrita em disco:" + nomeArquivo + " " + str(datetime.datetime.now()))
            EscreveLog(f"Erro: {e}")

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



def get_codigo(metrica):
    if metrica == "histogram-rtt":
        return 11
    if metrica == "packet-count-lost-bidir":
        return 21
    if metrica == "packet-loss-rate-bidir":
        return 24
    if metrica == "packet-reorders-bidir":
        return 25
    if metrica == "failures":
        return 70
    if metrica == "packet-retransmits":
        return 71
    if metrica == "throughput":
        return 77




def get_origem(nome_arquivo):
    #RN, AC, GO, MT, PB, PE, RJ
    origem = nome_arquivo[:2]

    if origem == "ac":
        return 1
    if origem == "go":
        return 9
    if origem == "mt":
        return 13
    if origem == "pb":
        return 15
    if origem == "pe":
        return 16
    if origem == "rj":
        return 19
    if origem == "rn":
        return 20


def get_destino(nome_arquivo):
    destino = nome_arquivo[3:5]

    if destino == "ac":
        return 1
    if destino == "go":
        return 9
    if destino == "mt":
        return 13
    if destino == "pb":
        return 15
    if destino == "pe":
        return 16
    if destino == "rj":
        return 19
    if destino == "rn":
        return 20

def med(lista):
    soma = sum(lista)
    numero_elementos = len(lista)
    if numero_elementos > 0:
        resultado =  soma/numero_elementos
        formatado = "{:.2f}".format(resultado)
        return  formatado

    return None

def histogram_rtt_json_to_csv(dados,cod_metrica,pop_origem,pop_destino):
    linhas = []
    linhas.append("TimeStamp;RTT_min;RTT_avg;RTT_max;POP_origem;POP_destino;cod_metrica\n")

    for item in dados:
        ts = item["ts"]
        valor = item["val"]
        data = ts_to_date(ts)
        keys = valor.keys()
        lista_keys = list(keys)
        lista_keys_num = [float(s) for s in lista_keys]
        rtt_min = min(lista_keys_num)
        rtt_avg = med(lista_keys_num)
        rtt_max = max(lista_keys_num)
        linha = f"{data};{rtt_min};{rtt_avg};{rtt_max};{pop_origem};{pop_destino};{cod_metrica}\n"
        linhas.append(linha)
    return linhas

def json_to_csv(dados,metrica,nome_arquivo):
    linhas = []
    cod_metrica = get_codigo(metrica)
    pop_origem = get_origem(nome_arquivo)
    pop_destino = get_destino(nome_arquivo)

    if metrica == "histogram-rtt":
        linhas = histogram_rtt_json_to_csv(dados,cod_metrica,pop_origem,pop_destino)
    else:
        linhas.append("TimeStamp;Valor;POP_origem;POP_destino;cod_metrica\n")


        for item in dados:
            ts = item["ts"]
            valor = item["val"]
            data = ts_to_date(ts)
            linha = f"{data};{valor};{pop_origem};{pop_destino};{cod_metrica}\n"
            linhas.append(linha)
    EscreveArquivo(linhas,f'{DIRETORIO_BASE}/{metrica}/{nome_arquivo}.csv')

def ts_to_date(ts):
    date = str(time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(ts - FUSO_BRASIL)))
    return date

def convert_dados_json_to_csv(metrica):
    caminho = DIRETORIO_BASE+"/"+metrica+"/"
    for conteudo in glob.glob(os.path.join(caminho, '*')):
        print('Caminho:', caminho)
        if fnmatch.fnmatch(conteudo, '*.' + "json"):
            print('Conteudo:', conteudo)
            tamanhoCaminho = len(caminho)
            nomeArquivo = conteudo[tamanhoCaminho:]
            print('Nome do Arquivo: ',nomeArquivo)
            dados = json_read(conteudo)
            json_to_csv(dados,metrica,nomeArquivo)




if __name__ == "__main__":


    print("LENDO O CONTEUDO DAS PASTAS")
    #metricas = ["packet-count-lost-bidir","packet-loss-rate-bidir","packet-reorders-bidir","throughput","histogram-rtt"]
    metricas = ["histogram-rtt"]
    for metrica in metricas:
        convert_dados_json_to_csv(metrica)

    print("SCRIPT FINALIZADO")




