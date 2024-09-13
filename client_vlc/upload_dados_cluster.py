import os
from datetime import datetime

# Capturar a data atual
data_atual = datetime.now()

# Formatar a data para o formato DDMMYYYY
data_formatada = data_atual.strftime("%d%m%Y")

numero_coleta = 2

os.system("scp -P 2200 " + "client_pe_" + str(numero_coleta) + ".yaml qoeprediction@200.130.25.172:/home/qoeprediction/coleta" + str(numero_coleta) + "/client_pe_" + str(numero_coleta) + ".yaml")
os.system("scp -P 2200 " + "client_pb_" + str(numero_coleta) + ".yaml qoeprediction@200.130.25.172:/home/qoeprediction/coleta" + str(numero_coleta) + "/client_pb_" + str(numero_coleta) + ".yaml")
os.system("scp -P 2200 " + "client_mt_" + str(numero_coleta) + ".yaml qoeprediction@200.130.25.172:/home/qoeprediction/coleta" + str(numero_coleta) + "/client_mt_" + str(numero_coleta) + ".yaml")
os.system("scp -P 2200 " + "client_go_" + str(numero_coleta) + ".yaml qoeprediction@200.130.25.172:/home/qoeprediction/coleta" + str(numero_coleta) + "/client_go_" + str(numero_coleta) + ".yaml")
os.system("scp -P 2200 " + "client_ac_" + str(numero_coleta) + ".yaml qoeprediction@200.130.25.172:/home/qoeprediction/coleta" + str(numero_coleta) + "/client_ac_" + str(numero_coleta) + ".yaml")