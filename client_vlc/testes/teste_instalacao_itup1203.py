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

EscreveLog("Teste bem sucedido: " + f"{datetime.datetime.now():%d/%b/%Y-%H:%M:%S}", "/home/log.log")