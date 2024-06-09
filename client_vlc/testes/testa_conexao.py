import requests
import time


def fetch_data_from_internet(url):
    attempt = 0
    max_attempts = 10
    base_delay = 2  # segundos

    while attempt < max_attempts:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Isso gerará uma exceção para códigos de status HTTP 4xx/5xx
            return response.json()  # ou response.text, dependendo do formato da resposta
        except requests.exceptions.RequestException as e:
            attempt += 1
            print(f"Tentativa {attempt} falhou: {e}")
            delay = base_delay ** attempt
            print(f"Aguardando {delay} segundos antes de tentar novamente...")
            time.sleep(delay)

    raise Exception("Falha ao recuperar dados após várias tentativas.")


url = "https://api.exemplo.com/dados"

while True:
    try:
        dados = fetch_data_from_internet(url)
        # Processar os dados aqui
        print(dados)
        # Aguardar um intervalo antes da próxima solicitação, se necessário
        time.sleep(3600)  # Exemplo: esperar 1 hora
    except Exception as e:
        print(f"Erro crítico: {e}. Tentando novamente em 1 minuto...")
        time.sleep(60)
