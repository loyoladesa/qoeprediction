# Autor : Sidney Loyola de Sá
# Projeto Desenvolvido para Analisar QoE a partir de dados de QoS
# Utilizando Grafos de Causalidade


import datetime
import json
import time
import os
from pathlib import Path
from datetime import date


def EscreveLog(mensagem, arquivo):
    try:
        with open(arquivo, "a") as file:
            file.write(str(mensagem) + "\n")
            file.close()

    except:
        print("Erro na Escrita:" + arquivo + " " + mensagem + f"{datetime.datetime.now():%d/%b/%Y-%H:%M:%S}")


def salvar(nome_arquivo, texto):
    #EscreveLog("iniciada função salvar", "/home/log.log")
    try:
        if os.path.isfile(nome_arquivo):
            with open(nome_arquivo, "a") as file:
                file.write(texto + "\n")
                file.close()
        else:
            with open(nome_arquivo, "a") as file:
                file.write("start,end,video,start_time,duration,size,bitrate,frames,width,heigth,rtt_min, rtt_avg, rtt_max, pacotes_transmitidos, pacotes_recebidos, pacotes_perdidos, ttl,qoe_value" + "\n")
                file.write(texto + "\n")
                file.close()

    except Exception as e:
        print("Erro de Escrita!" + e.__str__())
        with open("/home/log.log", "a") as file:
            file.write(e.__str__() + "\n")
            file.close()
def assistirVideo(diretorio, nome_video):
    EscreveLog("iniciada função assistir video" + f"{datetime.datetime.now():%d/%b/%Y-%H:%M:%S}", "/home/log.log")
    start = str(datetime.datetime.now())
    os.system("ffmpeg -i https://cdn.api.video/vod/vi4blUQJFrYWbaG44NChkH27/mp4/1080/source.mp4 -c copy -bsf:a aac_adtstoasc " + diretorio + nome_video)
    end = str(datetime.datetime.now())
    EscreveLog("terminada função assistir video" + f"{datetime.datetime.now():%d/%b/%Y-%H:%M:%S}", "/home/log.log")
    return start, end

def medirQoE(diretorio, nome_video, nome_json):
    EscreveLog("iniciada função medir qoe" + f"{datetime.datetime.now():%d/%b/%Y-%H:%M:%S}", "/home/log.log")
    os.system("python3 -m itu_p1203 --accept-notice " + diretorio + nome_video + "  > " + diretorio + nome_json)

    with open(diretorio + nome_json) as file:
        data = json.load(file)
    value_qoe = str(data[diretorio + nome_video]["O46"])
    EscreveLog("terminada função medir qoe" + f"{datetime.datetime.now():%d/%b/%Y-%H:%M:%S}", "/home/log.log")
    return value_qoe


diretorio = "/home/"
nome_video = "video.mp4"
nome_json = "video.json"
start,end = assistirVideo(diretorio,nome_video)
#time.sleep(10000)
qoe = medirQoE(diretorio,nome_video,nome_json)
EscreveLog("Teste bem sucedido: " + f"{datetime.datetime.now():%d/%b/%Y-%H:%M:%S}", "/home/log.log")