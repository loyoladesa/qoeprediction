def teste_simples():
    if (not passou_teste):
        print("Executa o teste novamente")
    else:
        raise Exception("Passou no teste")

def teste_lancar_excecao():
    try:
        teste_simples()
    except Exception as erro:
        raise Exception(erro.__str__())


passou_teste = False
teste_simples()

passou_teste = True
try:
    teste_lancar_excecao()
except Exception as erro:
    print(erro.__str__())



