# Versão 1.6
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


def assistirVideo(diretorio, nome_video):
    # EscreveLog("iniciada função assistir video", "/home/log.log")
    start = str(datetime.datetime.now())
    os.system("ffmpeg -i https://4ec7-189-84-93-121.ngrok-free.app/hls/transformers_720p.mp4/master.m3u8 -c copy -bsf:a aac_adtstoasc " + diretorio + nome_video)
    # os.system("ffmpeg -i http://192.168.0.109:8000/hls/stream.m3u8 -c copy -bsf:a aac_adtstoasc " + diretorio + nome_video)
    end = str(datetime.datetime.now())

    return start, end


def medirQoE(diretorio, nome_video, nome_json):
    # EscreveLog("iniciada função medir qoe", "/home/log.log")
    os.system("python3 -m itu_p1203 --accept-notice " + diretorio + nome_video + "  > " + diretorio + nome_json)

    with open(diretorio + nome_json) as file:
        data = json.load(file)
    value_qoe = str(data[diretorio + nome_video]["O46"])
    return value_qoe


def capturarDadosVideo(diretorio, nome_video):
    # EscreveLog("iniciada função capturar_dados_videos", "/home/log.log")
    os.system(
        'ffprobe -v quiet -print_format json -show_format -show_frames "' + diretorio + nome_video + '" > "' + diretorio + nome_video + '.json"')

    with open(diretorio + nome_video + ".json") as file:
        data_probe = json.load(file)
    start_time = data_probe['format']['start_time']
    duration = data_probe['format']['duration']
    size = data_probe['format']['size']
    bitrate = data_probe['format']['bit_rate']
    frames = str(len(data_probe['frames']))
    EscreveLog(str(data_probe['frames']), diretorio + nome_video + "_frames.json")
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

    return start_time, duration, size, bitrate, frames, width, height


def inserirDataset(diretorio, nome_csv, start, end, nome_video, start_time, duration, size, bitrate, frames, width,
                   height, value_qoe):
    linha = (
                start + "," + end + "," + nome_video + "," + start_time + "," + duration + "," + size + "," + bitrate + "," + frames + "," + width + "," + height + "," + value_qoe)
    nome_arquivo = diretorio + nome_csv
    salvar(nome_arquivo, linha)


def apagarArquivos(diretorio, nome_json, nome_video):
    os.system("sudo rm " + diretorio + nome_json)
    os.system("sudo rm " + diretorio + nome_video)
    os.system("sudo rm " + diretorio + nome_video + ".json")
    os.system("sudo rm " + diretorio + nome_video + "_frames.json")


# parâmetros do Script
diretorio = '/home/'
cont = 1
quant = 4

while cont < quant:
    # São parâmetros também, mas são dinâmicos de acordo com o vídeo a ser buscado
    complemento = str(cont)
    cont = cont + 1
    nome_video = "source_" + complemento + ".mp4"
    nome_json = "qoe_" + complemento + ".json"
    nome_csv = "qoe_value.csv"

    start, end = assistirVideo(diretorio, nome_video)

    value_qoe = medirQoE(diretorio, nome_video, nome_json)

    start_time, duration, size, bitrate, frames, width, height = capturarDadosVideo(diretorio, nome_video)

    inserirDataset(diretorio, nome_csv, start, end, nome_video, start_time, duration, size, bitrate, frames, width,
                   height, value_qoe)
    apagarArquivos(diretorio, nome_json, nome_video)

    time.sleep(2)