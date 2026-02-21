# Autor : Sidney Loyola de Sá
# Projeto Desenvolvido para Analisar QoE a partir de dados de QoS
# Utilizando Grafos de Causalidade
# Versão 1.0



import datetime
import json
import time
import os
from pathlib import Path
from datetime import date



# LABELS

erro_escrita = "Erro na Escrita: "
cabecalho = "start,end,video,start_time,duration,size,bitrate,frames,width,heigth,rtt_min, rtt_avg, rtt_max, pacotes_transmitidos, pacotes_recebidos, pacotes_perdidos, ttl,qoe_value,hop_1,hop_2,hop_3,hop_4,hop_5,hop_6,hop_7,hop_8,hop_9,hop_10,hop_11,hop_12,hop_13,hop_14,hop_15"
diretorio_log = "/home/log.log"
falha_assistir = "Falha ao Assistir Video"
ocorrencia_excecao = "Ocorreu uma exceção - assistir video "

def EscreveLog(mensagem, arquivo):
    try:
        with open(arquivo, "a") as file:
            file.write(str(mensagem) + "\n")
            file.close()

    except:
        print(erro_escrita + arquivo + " " + mensagem + f"{datetime.datetime.now():%d/%b/%Y-%H:%M:%S}")

def salvar(nome_arquivo, texto):
    try:
        if os.path.isfile(nome_arquivo):
            with open(nome_arquivo, "a") as file:
                file.write(texto + "\n")
                file.close()
        else:
            with open(nome_arquivo, "a") as file:
                file.write( cabecalho + "\n")
                file.write(texto + "\n")
                file.close()

    except Exception as e:
        print(erro_escrita + e.__str__())
        with open(diretorio_log, "a") as file:
            file.write(e.__str__() + "\n")
            file.close()

def assistirVideo(diretorio, nome_video,url_video):
    tentativas = 0
    max_tentativas = 5
    while tentativas < max_tentativas:
        try:

            start = str(datetime.datetime.now())
            # os.system("ffmpeg -i https://cdn.api.video/vod/vi4blUQJFrYWbaG44NChkH27/mp4/1080/source.mp4 -c copy -bsf:a aac_adtstoasc " + diretorio + nome_video)
            # os.system("ffmpeg -i http://192.168.0.109:8000/hls/stream.m3u8 -c copy -bsf:a aac_adtstoasc " + diretorio + nome_video)
            os.system("ffmpeg -i " + url_video + " -c copy -bsf:a aac_adtstoasc " + diretorio + nome_video)
            end = str(datetime.datetime.now())
            return start, end

        except Exception as erro:
            tentativas = tentativas + 1
            mensagem = ocorrencia_excecao
            mensagem = mensagem + f"{datetime.datetime.now():%d/%b/%Y-%H:%M:%S} "
            mensagem = mensagem + erro.__str__()
            EscreveLog(mensagem, diretorio_log)
            time.sleep(60)
    raise Exception(falha_assistir)

arquivo = "registro_logs.txt"
mensagem = "log: medir_itup1203 - " + f"{datetime.datetime.now():%d/%b/%Y-%H:%M:%S} - "


nome_arquivo = "arquivo.csv"
texto = "Primeira Linha"
diretorio = "/home/"

url_video = "http://service-5:5215/hls/video_20_180p.m3u8"
nome_video = "video_1.mp4"


EscreveLog(mensagem + url_video,arquivo)
salvar(nome_arquivo,texto)

start, end = assistirVideo(diretorio, nome_video,url_video)
