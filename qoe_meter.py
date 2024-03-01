# Versão 1.5
# Sidney Loyola de Sá
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
    try:
        if os.path.isfile(nome_arquivo):
            with open(nome_arquivo, "a") as file:
                file.write(texto + "\n")
                file.close()
        else:
            with open(nome_arquivo, "a") as file:
                file.write("start,end,video,start_time,duration,size,bitrate,frames,width,heigth,qoe_value" + "\n")
                file.write(texto + "\n")
                file.close()

    except Exception as e:
        print("Erro de Escita!" + e.__str__())
        with open("/home/log.log", "a") as file:
            file.write(e.__str__() + "\n")
            file.close()


# parâmetros do Script
diretorio = '/home/'
cont = 12
quant = 16


def assistirVideo(diretorio, nome_video):
    EscreveLog("iniciada função assistir video", "/home/log.log")
    start = datetime.datetime.now()
    os.system(
        "ffmpeg -i https://cdn.api.video/vod/vi4blUQJFrYWbaG44NChkH27/mp4/1080/source.mp4 -c copy -bsf:a aac_adtstoasc /home/" +nome_video)
    end = datetime.datetime.now()

    return start,end


def medirQoE(diretorio, nome_video, nome_json):
    EscreveLog("iniciada função medir qoe", "/home/log.log")
    os.system("python3 -m itu_p1203 --accept-notice " + diretorio + nome_video + "  > " + diretorio  + nome_json)

    with open(diretorio + nome_json) as file:
        data = json.load(file)
    value_qoe = str(data[diretorio + nome_video]["O46"])
    return value_qoe


while cont < quant:

    # São parâmetros também, mas são dinâmicos de acordo com o vídeo a ser buscado
    complemento = str(cont)
    cont = cont + 1
    nome_video = "source_" + complemento + ".mp4"
    nome_json = "qoe_" + complemento + ".json"
    nome_csv = "qoe_value.csv"
    EscreveLog("atualizado parâmetros", "/home/log.log")

    EscreveLog("nome do video: "+ nome_video, "/home/log.log")

    #start,end = assistirVideo(diretorio,nome_video)

    start = datetime.datetime.now()
    os.system(
        "ffmpeg -i https://cdn.api.video/vod/vi4blUQJFrYWbaG44NChkH27/mp4/1080/source.mp4 -c copy -bsf:a aac_adtstoasc /home/" + nome_video)
    end = datetime.datetime.now()


    EscreveLog("start: " + str(start), "/home/log.log")
    EscreveLog("end: " + str(end), "/home/log.log")

    EscreveLog("video assistido", "/home/log.log")

    value_qoe = medirQoE(diretorio,nome_video,nome_json)

    EscreveLog("qoe: " + value_qoe, "/home/log.log")

    os.system(
        'ffprobe -v quiet -print_format json -show_format -show_frames /home/"' + nome_video + '" > "/home/' + nome_video + '.json"')

    with open(diretorio + nome_video + ".json") as file:
        data_probe = json.load(file)
    start_time = data_probe['format']['start_time']
    duration = data_probe['format']['duration']
    size = data_probe['format']['size']
    bitrate = data_probe['format']['bit_rate']
    frames = str(len(data_probe['frames']))
    width = "-"
    height = "-"

    nao_achou = True
    indice = 0
    while nao_achou:
        if data_probe['frames'][indice]["media_type"] == "video":
            width = str(data_probe['frames'][indice]["width"])
            height = str(data_probe['frames'][indice]["height"])
            nao_achou = False
        else:
            indice = indice + 1
            if indice > 10:
                nao_achou = False


    linha = (str(start) + "," + str(end) + "," + nome_video + "," + start_time + "," + duration + "," + size + "," + bitrate + "," + frames + "," + width + "," + height + "," + value_qoe)
    nome_arquivo = diretorio + nome_csv
    salvar(nome_arquivo, linha)
    time.sleep(2)
