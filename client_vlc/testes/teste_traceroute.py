# Autor : Sidney Loyola de Sá
# Projeto Desenvolvido para Analisar QoE a partir de dados de QoS
# Utilizando Grafos de Causalidade

import datetime
import json
import time
import os
def capturar_dados_rede():
    hops = []
    try:
        with open('trace_qoe.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                hops.append(linha[:-2])
                print(linha[-2])
            hops.pop(0)
            numero_elementos = len(hops)
            numero_preenchimentos = 10 - numero_elementos

            while(numero_preenchimentos > 0):
                hops.append(" ? ")
                numero_preenchimentos = numero_preenchimentos - 1

            print(numero_elementos)
            

    except Exception as erro:
        print('Ocorreu um erro...')
        print(erro)

    return hops

hops = capturar_dados_rede()

for hop in hops:
    print(hop)





