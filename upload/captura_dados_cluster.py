import os
import datetime
#import json
#import time
#import random
from datetime import datetime
from datetime import date
from pathlib import Path



def EscreveLog(mensagem, arquivo):
    try:
        with open(arquivo, "a") as file:
            file.write(str(mensagem) + "\n")
            file.close()

    except:
        print("Erro na Escrita:" + arquivo + " " + mensagem + f"{datetime.datetime.now():%d/%b/%Y-%H:%M:%S}")

# Capturar a data atual
data_atual = datetime.now()

# Formatar a data para o formato DDMMYYYY
#data_formatada = data_atual.strftime("%d%m%Y")
data_formatada = '20260726' 
numero_coleta = '16'

#kubectl exec -n qoeprediction test-qoe-ac-16 -- cat /home/qoe_value.csv > qoe_value_ac_20260726.csv

try:

            #os.system("kubectl cp -n qoeprediction test-qoe:/home/qoe_value.csv qoe_value_rn_" + data_formatada + ".csv")
            #-aleatorio 
            #os.system("kubectl cp -n qoeprediction test-qoe-ac-" + numero_coleta + ":/home/qoe_value.csv qoe_value_ac_" + data_formatada + ".csv")
            #os.system("kubectl cp -n qoeprediction test-qoe-ac-aleatorio:/home/qoe_value.csv qoe_value_ac-aleatorio_" + data_formatada + ".csv")
            os.system("kubectl exec -n qoeprediction test-qoe-ac-" + numero_coleta + " -- cat /home/qoe_value.csv > qoe_value_ac_" + data_formatada + ".csv")
            os.system("kubectl exec -n qoeprediction test-qoe-ac-aleatorio -- cat /home/qoe_value.csv > qoe_value_ac_aleatorio_" + data_formatada + ".csv")
            

            #os.system("kubectl cp -n qoeprediction test-qoe-es-" + numero_coleta + ":/home/qoe_value.csv qoe_value_es_" + data_formatada + ".csv")
            #os.system("kubectl cp -n qoeprediction test-qoe-es-aleatorio:/home/qoe_value.csv qoe_value_es-aleatorio_" + data_formatada + ".csv")
            os.system("kubectl exec -n qoeprediction test-qoe-es-" + numero_coleta + " -- cat /home/qoe_value.csv > qoe_value_es_" + data_formatada + ".csv")
            os.system("kubectl exec -n qoeprediction test-qoe-es-aleatorio -- cat /home/qoe_value.csv > qoe_value_es_aleatorio_" + data_formatada + ".csv")

            #os.system("kubectl cp -n qoeprediction test-qoe-go-" + numero_coleta + ":/home/qoe_value.csv qoe_value_go_" + data_formatada + ".csv")
            #os.system("kubectl cp -n qoeprediction test-qoe-go-aleatorio:/home/qoe_value.csv qoe_value_go-aleatorio_" + data_formatada + ".csv")
            os.system("kubectl exec -n qoeprediction test-qoe-go-" + numero_coleta + " -- cat /home/qoe_value.csv > qoe_value_go_" + data_formatada + ".csv")
            os.system("kubectl exec -n qoeprediction test-qoe-go-aleatorio -- cat /home/qoe_value.csv > qoe_value_go_aleatorio_" + data_formatada + ".csv")

            #os.system("kubectl cp -n qoeprediction test-qoe-mt-" + numero_coleta + ":/home/qoe_value.csv qoe_value_mt_" + data_formatada + ".csv")
            #os.system("kubectl cp -n qoeprediction test-qoe-mt-aleatorio:/home/qoe_value.csv qoe_value_mt-aleatorio_" + data_formatada + ".csv")
            os.system("kubectl exec -n qoeprediction test-qoe-mt-" + numero_coleta + " -- cat /home/qoe_value.csv > qoe_value_mt_" + data_formatada + ".csv")
            os.system("kubectl exec -n qoeprediction test-qoe-mt-aleatorio -- cat /home/qoe_value.csv > qoe_value_mt_aleatorio_" + data_formatada + ".csv")

            #os.system("kubectl cp -n qoeprediction test-qoe-pb-" + numero_coleta + ":/home/qoe_value.csv qoe_value_pb_" + data_formatada + ".csv")
            #os.system("kubectl cp -n qoeprediction test-qoe-pb-aleatorio:/home/qoe_value.csv qoe_value_pb-aleatorio_" + data_formatada + ".csv")
            os.system("kubectl exec -n qoeprediction test-qoe-pb-" + numero_coleta + " -- cat /home/qoe_value.csv > qoe_value_pb_" + data_formatada + ".csv")
            os.system("kubectl exec -n qoeprediction test-qoe-pb-aleatorio -- cat /home/qoe_value.csv > qoe_value_pb_aleatorio_" + data_formatada + ".csv")

            #os.system("kubectl cp -n qoeprediction test-qoe-pe-" + numero_coleta + ":/home/qoe_value.csv qoe_value_pe_" + data_formatada + ".csv")
            #os.system("kubectl cp -n qoeprediction test-qoe-pe-aleatorio:/home/qoe_value.csv qoe_value_pe-aleatorio_" + data_formatada + ".csv")
            os.system("kubectl exec -n qoeprediction test-qoe-pe-" + numero_coleta + " -- cat /home/qoe_value.csv > qoe_value_pe_" + data_formatada + ".csv")
            os.system("kubectl exec -n qoeprediction test-qoe-pe-aleatorio -- cat /home/qoe_value.csv > qoe_value_pe_aleatorio_" + data_formatada + ".csv")

            #os.system("kubectl cp -n qoeprediction test-qoe-rn-" + numero_coleta + ":/home/qoe_value.csv qoe_value_rn_" + data_formatada + ".csv")
            #os.system("kubectl cp -n qoeprediction test-qoe-rn-aleatorio:/home/qoe_value.csv qoe_value_rn-aleatorio_" + data_formatada + ".csv")
            os.system("kubectl exec -n qoeprediction test-qoe-rn-" + numero_coleta + " -- cat /home/qoe_value.csv > qoe_value_rn_" + data_formatada + ".csv")
            os.system("kubectl exec -n qoeprediction test-qoe-rn-aleatorio -- cat /home/qoe_value.csv > qoe_value_rn_aleatorio_" + data_formatada + ".csv")

            #os.system("kubectl cp -n qoeprediction test-qoe-rs-" + numero_coleta + ":/home/qoe_value.csv qoe_value_rs_" + data_formatada + ".csv")
            #os.system("kubectl cp -n qoeprediction test-qoe-rs-aleatorio:/home/qoe_value.csv qoe_value_rs-aleatorio_" + data_formatada + ".csv")
            os.system("kubectl exec -n qoeprediction test-qoe-rs-" + numero_coleta + " -- cat /home/qoe_value.csv > qoe_value_rs_" + data_formatada + ".csv")
            os.system("kubectl exec -n qoeprediction test-qoe-rs-aleatorio -- cat /home/qoe_value.csv > qoe_value_rs_aleatorio_" + data_formatada + ".csv")

            #os.system("kubectl cp -n qoeprediction test-qoe-rj:/home/qoe_value.csv qoe_value_rj_" + data_formatada + ".csv")

except Exception as erro:
            mensagem = "Ocorreu uma exceção - capturar_dados_cluster "
            mensagem = mensagem + f"{datetime.datetime.now():%d/%b/%Y-%H:%M:%S} "
            mensagem = mensagem + erro.__str__()
            EscreveLog(mensagem, "log.log")


