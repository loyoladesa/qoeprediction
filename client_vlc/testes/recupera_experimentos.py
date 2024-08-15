import os

COMANDO = "sudo cp /var/lib/docker/volumes/dados_qoe/_data/qoe_value.csv  /mnt/c/Documents\ and\ Settings/loyol/Meus\ Documentos/arquivos_resultados_experimentos/exp_1/"

'''
numero = 1

while numero < 4:

    os.system("sudo rm /var/lib/docker/volumes/dados_qoe/_data/qoe_" +  str(numero) + ".json")
    os.system("sudo rm /var/lib/docker/volumes/dados_qoe/_data/source_" + str(numero) + ".mp4")
    os.system("sudo rm /var/lib/docker/volumes/dados_qoe/_data/source_" + str(numero) + ".mp4.json")
    os.system("sudo rm /var/lib/docker/volumes/dados_qoe/_data/source_" + str(numero) + ".mp4_frames.json")

    numero = numero + 1

'''
os.system(COMANDO)