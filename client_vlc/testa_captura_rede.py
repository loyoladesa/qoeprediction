# Autor : Sidney Loyola de Sá
# Projeto Desenvolvido para Analisar QoE a partir de dados de QoS
# Utilizando Grafos de Causalidade

import datetime
import json
import time
import os
def capturar_dados_rede():
    rtt_min = 0
    rtt_avg = 0
    rtt_max = 0
    pacotes_transmitidos = 0
    pacotes_recebidos = 0
    pacotes_perdidos = 0
    ttl = 0


    try:
        with open('ping.txt', 'r') as arquivo:
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

    except Exception as erro:
        print('Ocorreu um erro...')
        print(erro)

    return rtt_min,rtt_avg,rtt_max,pacotes_transmitidos,pacotes_recebidos,pacotes_perdidos,ttl


rtt_min,rtt_avg,rtt_max, pacotes_transmitidos,pacotes_recebidos,pacotes_perdidos,ttl = capturar_dados_rede()
print(f"rtt_min = {rtt_min}")
print(f"rtt_avg = {rtt_avg}")
print(f"rtt_max = {rtt_max}")
print(f"ttl = {ttl}")
print(f"packets_transmitted = {pacotes_transmitidos}")
print(f"packets_received = {pacotes_recebidos}")
print(f"packets_lost = {pacotes_perdidos}")



