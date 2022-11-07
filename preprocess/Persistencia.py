class Persistencia:
    def __init__(self,arquivoLog="Log.log"):
        self.arquivoLog = arquivoLog


    # Escreve log em arquivo
    def EscreveLog(self, mensagem,arquivo):
        try:
            with open(arquivo, "a") as file:
                file.write(str(mensagem) + "\n")
                file.close()

        except:
            print("Erro na Escrita:" + arquivo+" "+mensagem + f"{datetime.datetime.now():%d/%b/%Y-%H:%M:%S}")

    # Cria um arquivo vazio
    def EscreveArquivoVazio(self, nomeArquivo):
        try:
            with open(nomeArquivo, "w") as file:
                file.write("")
                file.close()
        except:
            self.EscreveLog("Erro escrita em disco:" + nomeArquivo + " " + str(datetime.datetime.now()))

    # Escreve registros em arquivo
    def EscreveArquivo(self, registros, nomeArquivo):
        for registro in registros:
            s = registro.split(',')

            if len(s) == 18:
                try:
                    with open(self.arquivo + nomeArquivo + ".csv", "a") as file:
                        file.write(str(registro) + "\n")
                        file.close()
                except:
                    self.EscreveLog(
                        "Erro escrita em disco:" + nomeArquivo + " " + str(datetime.datetime.now()))



    def SalvarDataframe(self,df,nomeArquivo):
        try:
            string = df.to_csv(nomeArquivo, index=False)
            return str
        except Exception as e:
            return str(e)






