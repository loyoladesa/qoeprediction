import os
from datetime import datetime

# Capturar a data atual
data_atual = datetime.now()

# Formatar a data para o formato DDMMYYYY
data_formatada = data_atual.strftime("%d%m%Y")




os.system("kubectl cp -n qoeprediction test-qoe:/home/qoe_value.csv qoe_value_rn_" + data_formatada + ".csv")
os.system("kubectl cp -n qoeprediction test-qoe-ac:/home/qoe_value.csv qoe_value_ac_" + data_formatada + ".csv")
os.system("kubectl cp -n qoeprediction test-qoe-go:/home/qoe_value.csv qoe_value_go_" + data_formatada + ".csv")
os.system("kubectl cp -n qoeprediction test-qoe-mt:/home/qoe_value.csv qoe_value_mt_" + data_formatada + ".csv")
os.system("kubectl cp -n qoeprediction test-qoe-pb:/home/qoe_value.csv qoe_value_pb_" + data_formatada + ".csv")
os.system("kubectl cp -n qoeprediction test-qoe-pe:/home/qoe_value.csv qoe_value_pe_" + data_formatada + ".csv")
os.system("kubectl cp -n qoeprediction test-qoe-rj:/home/qoe_value.csv qoe_value_rj_" + data_formatada + ".csv")

