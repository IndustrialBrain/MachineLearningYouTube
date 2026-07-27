import requests

# URL da API
url = "https://api.thecatapi.com/v1/breeds"

# Fazer a requisição GET
response = requests.get(url)

# Verificar se a requisição foi bem-sucedida
if response.status_code == 200:
    # Converter a resposta em JSON
    data = response.json()
    
    # Exibir a primeira raça de gato na resposta
    print("Primeira raça de gato na resposta:", data[2]["name"])
else:
    print("Erro na requisição:", response.status_code)
