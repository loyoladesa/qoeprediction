from __future__ import division
import datetime
from datetime import timedelta
import fnmatch

import gzip
import glob
import math
import os
import os.path
from os import walk
import pandas as pd
import Persistencia as p
import re
import sys
import shutil
import zipfile





class OrganizaDadosRNP:
    def __init__(self,arquivoLog="Log.log"):
        self.arquivoLog = arquivoLog

    # Escreve log em arquivo
    def EscreveLog(self, mensagem):
        try:
            with open(self.arquivoLog, "a") as file:
                file.write(str(mensagem) + "\n")
                file.close()

        except:
            print("Erro na Escrita:" + mensagem + " " + str(datetime.datetime.now()))

    # Escreve registros em arquivo
    def EscreveArquivo(self, registros, nomeArquivo):
        for registro in registros:
            try:
                with open(nomeArquivo, "a") as file:
                    file.write(str(registro))
                    file.close()
            except:
                self.EscreveLog(
                    "Erro escrita em disco:" + nomeArquivo + " " + str(datetime.datetime.now()))

    # Cria um arquivo vazio
    def EscreveArquivoVazio(self, nomeArquivo):
        try:
            with open(nomeArquivo, "w") as file:
                file.write("")
                file.close()
        except:
            self.EscreveLog(
                "Erro escrita em disco:" + self.arquivo + nomeArquivo + " " + str(datetime.datetime.now()))

    def run(self):

        # ETAPA 1 : Cria Parâmetros de acesso aos arquivos
        #local_arquivos_a_serem_processados = 'C:/Users/loyol/PycharmProjects/globo_traces/venv/Dados_RNP/Organizacao_Dados/organizador'

        #local_arquivos_a_serem_processados = 'D:/Dados_RNP_SET_2022/atraso_bidir/packet_count_lost_bidir/'
        #log_file = 'D:/Dados_RNP_SET_2022/Organizacao_Dados/organizador/Log.log'
        #teste_file = 'C:/Users/loyol/PycharmProjects/globo_traces/venv/Dados_RNP/Organizacao_Dados/organizador/dataset/teste.csv'
        #diretorio_arquivos_a_serem_salvos = 'D:/Dados_RNP_SET_2022/Organizacao_Dados/dataset_set_2022/atraso_bidir/packet_count_lost_bidir/'

        #local_arquivos_a_serem_processados = 'D:/Dados_RNP_SET_2022/atraso_bidir/packet_reorders_bidir/'
        #log_file = 'D:/Dados_RNP_SET_2022/Organizacao_Dados/organizador/Log.log'
        #teste_file = 'C:/Users/loyol/PycharmProjects/globo_traces/venv/Dados_RNP/Organizacao_Dados/organizador/dataset/teste.csv'
        #diretorio_arquivos_a_serem_salvos = 'D:/Dados_RNP_SET_2022/Organizacao_Dados/dataset_set_2022/atraso_bidir/packet_reorders_bidir/'

        log_file = 'D:/Dados_RNP_SET_2022/Organizacao_Dados/organizador/Log.log'
        teste_file = 'C:/Users/loyol/PycharmProjects/globo_traces/venv/Dados_RNP/Organizacao_Dados/organizador/dataset/teste.csv'

        diretorio = 'atraso_unidir/packet_loss_rate'
        metrica = 'packet_loss_rate'

        local_arquivos_a_serem_processados = 'D:/Dados_RNP_SET_2022/' + diretorio + '/'
        diretorio_arquivos_a_serem_salvos = 'D:/Dados_RNP_SET_2022/Organizacao_Dados/dataset_set_2022/' + diretorio + '/'


        self.arquivoLog = log_file

        self.EscreveLog("ORGANIZAÇÃO DOS DADOS DA RNP: " + " " + str(datetime.datetime.now()))
        tipoArquivo = 'csv'


        #Listas de POPs
        #pop_origem = ['ac', 'al', 'am', 'ap', 'ba', 'ce', 'df', 'es', 'go', 'ma']
        #pop_destino = ['ac', 'al', 'am', 'ap', 'ba', 'ce', 'df', 'es', 'go', 'ma', 'mg', 'ms', 'mt', 'pa', 'pb', 'pe','pi', 'pr', 'rj', 'rn', 'ro', 'rr', 'rs', 'sc', 'se', 'sp', 'to']

        pop_origem = ['ac', 'al', 'am', 'ap', 'ba', 'ce', 'df', 'es', 'go', 'ma', 'mg', 'ms', 'mt', 'pa', 'pb', 'pe','pi', 'pr', 'rj', 'rn', 'ro', 'rr', 'rs', 'sc', 'se', 'sp', 'to']
        #pop_origem = ['rr', 'rs', 'sc', 'se', 'sp', 'to']
        pop_destino = ['ac', 'al', 'am', 'ap', 'ba', 'ce', 'df', 'es', 'go', 'ma', 'mg', 'ms', 'mt', 'pa', 'pb', 'pe','pi', 'pr', 'rj', 'rn', 'ro', 'rr', 'rs', 'sc', 'se', 'sp', 'to']

        # ETAPA 2 : -Percorre a pasta com os arquivos e Cria Dataset
        #           -recupera as informações que desejamos utilizar em nosso dataset
        self.EscreveLog("Inicío Criar Dataset: " + " " + str(datetime.datetime.now()))

        for origem in pop_origem:
            pasta = diretorio_arquivos_a_serem_salvos + '/' + origem + '/'
            os.mkdir(pasta)
            print('Pasta criada!',origem)
            for destino in pop_destino:
                caminho = local_arquivos_a_serem_processados + origem + '/' + destino
                dataset_file = pasta + metrica + '_' + origem + '_' + destino + '.csv'
                print('Dataset:',dataset_file)
                print('Caminho:',caminho)
                # lista que tera as linhas a serem escritas
                registros = []
                registros.append("TimeStamp;Latitude;Longitude;Valor;POP_origem;POP_destino;cod_metrica""\n")
                self.EscreveArquivo(registros, dataset_file)
                #Varre o local_arquivos_a_serem_processados com os arquivos a serem lidos
                print('Log1')
                for conteudo in glob.glob(os.path.join(caminho, '*')):
                    print('Varrer Local:',caminho)
                    if fnmatch.fnmatch(conteudo, '*.'+tipoArquivo):
                        print('Conteudo:',conteudo)
                        nomeArquivo = conteudo.replace(caminho + "\\", "")
                        mensagem = "Nome do Arquivo = " + nomeArquivo
                        print(mensagem)
                        self.EscreveLog(mensagem+ " " + str(datetime.datetime.now()))

                        try:
                            with open(conteudo, 'r') as infile:

                                registros = []
                                # Para cada linha do arquivo de entrada
                                for linha in infile.readlines():
                                    print(linha)
                                    registros.append(linha)

                                self.EscreveArquivo(registros, dataset_file)
                                self.EscreveLog(
                                    "Fim da leitura do arquivo " + str(conteudo) + " " + str(datetime.datetime.now()))
                                print("Fim da leitura do arquivo " + str(conteudo) + " " + str(datetime.datetime.now()))
                        except:
                            self.EscreveLog(
                                "Erro leitura arquivo " + str(conteudo) + "-" +  " " + str(datetime.datetime.now()))
                            self.EscreveLog("Unexpected error:" + str(sys.exc_info()[0]))
                            print("Unexpected error:", sys.exc_info()[0])






if __name__ == '__main__':
        programa = OrganizaDadosRNP()
        programa.run()
        print('Processamento Terminado! ' + str(datetime.datetime.now()))

