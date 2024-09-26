import os
from datetime import datetime

# Capturar a data atual
data_atual = datetime.now()

# Formatar a data para o formato DDMMYYYY
data_formatada = data_atual.strftime("%d%m%Y")


#os.system("scp -P 2200 qoeprediction@200.130.25.172:/home/qoeprediction/qoe_value_rn_" + data_formatada + ".csv qoe_value_rn_" + data_formatada + ".csv")
os.system("scp -P 2200 qoeprediction@200.130.25.172:/home/qoeprediction/qoe_value_ac_" + data_formatada + ".csv qoe_value_ac_" + data_formatada + ".csv")
os.system("scp -P 2200 qoeprediction@200.130.25.172:/home/qoeprediction/qoe_value_go_" + data_formatada + ".csv qoe_value_go_" + data_formatada + ".csv")
os.system("scp -P 2200 qoeprediction@200.130.25.172:/home/qoeprediction/qoe_value_mt_" + data_formatada + ".csv qoe_value_mt_" + data_formatada + ".csv")
#os.system("scp -P 2200 qoeprediction@200.130.25.172:/home/qoeprediction/qoe_value_pb_" + data_formatada + ".csv qoe_value_pb_" + data_formatada + ".csv")
os.system("scp -P 2200 qoeprediction@200.130.25.172:/home/qoeprediction/qoe_value_pe_" + data_formatada + ".csv qoe_value_pe_" + data_formatada + ".csv")
