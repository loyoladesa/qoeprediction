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
    try:
        if os.path.isfile(nome_arquivo):
            with open(nome_arquivo, "a") as file:
                file.write(texto + "\n")
                file.close()
        else:
            with open(nome_arquivo, "a") as file:
                file.write("start,end,video,start_time,duration,size,bitrate,frames,width,heigth,rtt_min, rtt_avg, rtt_max, pacotes_transmitidos, pacotes_recebidos, pacotes_perdidos, ttl,qoe_value,hop_1,hop_2,hop_3,hop_4,hop_5,hop_6,hop_7,hop_8,hop_9,hop_10,hop_11,hop_12,hop_13,hop_14,hop_15" + "\n")
                file.write(texto + "\n")
                file.close()

    except Exception as e:
        print("Erro de Escita!" + e.__str__())
        with open("/home/log.log", "a") as file:
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
            mensagem = "Ocorreu uma exceção - assistir video "
            mensagem = mensagem + f"{datetime.datetime.now():%d/%b/%Y-%H:%M:%S} "
            mensagem = mensagem + erro.__str__()
            EscreveLog(mensagem, "/home/log.log")
            time.sleep(60)
    raise Exception("Falha ao Assistir Video")





def medirQoE(diretorio, nome_video, nome_json):

    try:
        #EscreveLog("iniciada função medir qoe", "/home/log.log")
        EscreveLog("Iniciado FUNÇÃO medir QOE" + f"{datetime.datetime.now():%d/%b/%Y-%H:%M:%S}", "/home/log.log")
        os.system("python3 -m itu_p1203 --accept-notice " + diretorio + nome_video + "  > " + diretorio  + nome_json)

        with open(diretorio + nome_json) as file:
            data = json.load(file)
        value_qoe = str(data[diretorio + nome_video]["O46"])
        EscreveLog("Terminada FUNÇÃO medir QOE" + f"{datetime.datetime.now():%d/%b/%Y-%H:%M:%S}", "/home/log.log")
        return value_qoe
    except Exception as erro:
        mensagem = "Ocorreu uma exceção - medir qoe "
        mensagem = mensagem + f"{datetime.datetime.now():%d/%b/%Y-%H:%M:%S} "
        mensagem = mensagem + erro.__str__()
        EscreveLog(mensagem, "/home/log.log")
        raise Exception("Falha ao medir qoe ")


def capturarDadosVideo(diretorio, nome_video):
    try:
        #EscreveLog("iniciada função capturar_dados_videos", "/home/log.log")
        os.system('ffprobe -v quiet -print_format json -show_format -show_frames "' + diretorio + nome_video + '" > "' + diretorio + nome_video + '.json"')

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

        return start_time, duration, size, bitrate, frames, width, height
    except Exception as erro:
        mensagem = "Ocorreu uma exceção - capturar dados video "
        mensagem = mensagem + f"{datetime.datetime.now():%d/%b/%Y-%H:%M:%S} "
        mensagem = mensagem + erro.__str__()
        EscreveLog(mensagem, "/home/log.log")
        raise Exception("Falha ao Capturar Dados Video ")

def capturar_dados_rede(ip,diretorio,nome_ping,nome_trace):
     try:
        #EscreveLog("iniciada função capturar_dados_rede", "/home/log.log")
        os.system("ping -c 4 " + ip + " > " + diretorio + nome_ping)
        os.system("traceroute -m 15 " + ip + " > " + diretorio + nome_trace)

        rtt_min = ""
        rtt_avg = ""
        rtt_max = ""
        pacotes_transmitidos = ""
        pacotes_recebidos = ""
        pacotes_perdidos = ""
        ttl = ""
        hops = []



        with open(diretorio+nome_trace, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                hops.append(linha[:-2])
            hops.pop(0)
            numero_elementos = len(hops)
            numero_preenchimentos = 15 - numero_elementos

            while (numero_preenchimentos > 0):
                hops.append(" ? ")
                numero_preenchimentos = numero_preenchimentos - 1


        with open(diretorio+nome_ping, 'r') as arquivo:
            linhas = arquivo.readlines()
            cont = 0

            for linha in linhas:

                if linha[0:3] == "rtt":
                    detalhes = linha.strip().split('/')
                    rtt_min = detalhes[3]
                    rtt_min = rtt_min[7:]
                    rtt_avg = detalhes[4]
                    rtt_max = detalhes[5]
                elif linha[0] == "4":
                    detalhes = linha.strip().split(',')
                    pacotes_transmitidos = linha[0]
                    pacotes_recebidos = detalhes[1]
                    pacotes_recebidos = pacotes_recebidos[1]
                    pacotes_perdidos = detalhes[2]
                    index_porcentagem = pacotes_perdidos.find("%")
                    pacotes_perdidos = pacotes_perdidos[1:index_porcentagem]
                else:
                    detalhes = linha.strip().split(' ')
                    #print(detalhes[0])
                    if (detalhes[0] == "PING"):
                        cont = cont + 1
                    elif detalhes[0] != "PING" and cont == 1:
                        ttl = detalhes[5][4:]
                        cont = cont + 1
        return rtt_min, rtt_avg, rtt_max, pacotes_transmitidos, pacotes_recebidos, pacotes_perdidos, ttl, hops

     except Exception as erro:
        mensagem = "Ocorreu uma exceção - capturar dados rede "
        mensagem = mensagem + f"{datetime.datetime.now():%d/%b/%Y-%H:%M:%S} "
        mensagem = mensagem + erro.__str__()
        EscreveLog(mensagem, "/home/log.log")
        raise Exception("Falha ao Capturar Dados Rede ")



def inserirDataset(diretorio, nome_csv, start, end, nome_video, start_time, duration, size, bitrate, frames, width,height,rtt_min,rtt_avg,rtt_max,pacotes_transmitidos,pacotes_recebidos,pacotes_perdidos,ttl,value_qoe,hops):
    try:
        #EscreveLog("iniciada função inserir_dataset", "/home/log.log")
        linha = start + "," + end + "," + nome_video + "," + start_time + "," + duration + "," + size + "," + bitrate + "," + frames + "," + width + "," + height + "," + rtt_min + "," + rtt_avg + "," + rtt_max + "," + pacotes_transmitidos + "," + pacotes_recebidos + "," + pacotes_perdidos + "," + ttl + "," + value_qoe
        indice = 0
        while (indice < 15):
            linha = linha + "," + hops[indice]
            indice = indice + 1

        nome_arquivo = diretorio + nome_csv
        salvar(nome_arquivo, linha)
    except Exception as erro:
        mensagem = "Ocorreu uma exceção - inserir dataset"
        mensagem = mensagem + f"{datetime.datetime.now():%d/%b/%Y-%H:%M:%S} "
        mensagem = mensagem + erro.__str__()
        EscreveLog(mensagem, "/home/log.log")
        raise Exception("Falha ao Inserir Dados no Dataset ")

def apagarArquivos(diretorio, nome_json, nome_video,nome_ping,nome_trace):
    os.system("sudo rm " + diretorio + nome_ping)
    os.system("sudo rm " + diretorio + nome_trace)
    os.system("sudo rm " + diretorio + nome_json)
    os.system("sudo rm " + diretorio + nome_video)
    os.system("sudo rm " + diretorio + nome_video + ".json")
    os.system("sudo rm " + diretorio + nome_video + "_frames.json")

def get_url_video(escolha_video):
    url_video = "https://qoernp.ngrok.app/hls/video_20_180p.m3u8"

    if escolha_video == 1:
        url_video = "https://qoernp.ngrok.app/hls/video_20_360p.m3u8"
    elif escolha_video == 2:
        url_video = "https://qoernp.ngrok.app/hls/video_20_720p.m3u8"
    elif escolha_video == 3:
        url_video = "https://qoernp.ngrok.app/hls/video_30_180p.m3u8"
    elif escolha_video == 4:
        url_video = "https://qoernp.ngrok.app/hls/video_30_360p.m3u8"
    elif escolha_video == 5:
        url_video = "https://qoernp.ngrok.app/hls/video_30_720p.m3u8"
    elif escolha_video == 6:
        url_video = "https://qoernp.ngrok.app/hls/video_60_180p.m3u8"
    elif escolha_video == 7:
        url_video = "https://qoernp.ngrok.app/hls/video_60_360p.m3u8"
    else:
        url_video = "https://qoernp.ngrok.app/hls/video_60_720p.m3u8"

    return escolha_video




#parâmetros do Script
diretorio = '/home/'
ip = "189.84.93.121"
cont = 1
quant = 13
escolha_video = 0

video_assistido = False
qoe_medido = False
dados_video_capturados = False
dados_rede_capturados = False
dados_dataset_inseridos = False

while cont < quant:
    EscreveLog("Iniciado PROCESSO medir QOE" + f"{datetime.datetime.now():%d/%b/%Y-%H:%M:%S}", "/home/log.log")

    # São parâmetros também, mas são dinâmicos de acordo com o vídeo a ser buscado
    complemento = str(cont)

    nome_video = "video_" + complemento + ".mp4"
    nome_json = "qoe_" + complemento + ".json"
    nome_csv = "qoe_value.csv"
    nome_ping = "ping_" + complemento + ".txt"
    nome_trace = "trace_" + complemento + ".txt"

    #Buscar Informações - Internet


    if (not video_assistido):
        try:
            url_video = get_url_video(escolha_video)
            start, end = assistirVideo(diretorio, nome_video,url_video)
            video_assistido = True
            escolha_video = escolha_video + 1
            if (escolha_video > 8) :
                escolha_video = 0
        except Exception as erro:
            EscreveLog(erro.__str__(), "/home/log.log")
        if video_assistido:
            try:
                value_qoe = medirQoE(diretorio, nome_video, nome_json)
                qoe_medido = True
            except Exception as erro:
                EscreveLog(erro.__str__(), "/home/log.log")
            if qoe_medido:
                try:
                    start_time, duration, size, bitrate, frames, width, height = capturarDadosVideo(diretorio,nome_video)
                    dados_video_capturados = True
                except Exception as erro:
                    EscreveLog(erro.__str__(), "/home/log.log")
                if dados_video_capturados:
                    try:
                        rtt_min, rtt_avg, rtt_max, pacotes_transmitidos, pacotes_recebidos, pacotes_perdidos, ttl, hops = capturar_dados_rede(ip, diretorio, nome_ping, nome_trace)
                        dados_rede_capturados = True
                    except Exception as erro:
                        EscreveLog(erro.__str__(), "/home/log.log")
                    if dados_rede_capturados:
                        try:
                            inserirDataset(diretorio, nome_csv,start,end,nome_video,start_time,duration,size,bitrate,frames, width, height, rtt_min, rtt_avg, rtt_max,pacotes_transmitidos, pacotes_recebidos, pacotes_perdidos, ttl, value_qoe,hops)
                            dados_dataset_inseridos = True
                        except Exception as erro:
                            EscreveLog(erro.__str__(), "/home/log.log")

    apagarArquivos(diretorio, nome_json, nome_video,nome_ping,nome_trace)

    if dados_dataset_inseridos:
        EscreveLog("Complemento = " + complemento, "/home/log.log")
        EscreveLog("Terminado PROCESSO medir QOE - " + "Complemento = " + complemento + f" {datetime.datetime.now():%d/%b/%Y-%H:%M:%S}", "/home/log.log")
        cont = cont + 1

    video_assistido = False
    qoe_medido = False
    dados_video_capturados = False
    dados_rede_capturados = False
    dados_dataset_inseridos = False

    time.sleep(60)



