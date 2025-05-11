import requests

key = '19002c02a8534dae992122419251903'
def obter_previsao(cidade):
    url = f"http://api.weatherapi.com/v1/current.json?key={key}&q={cidade}"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        return dados['current']['temp_c'], dados['current']['condition']['text']
    else:
        return None
cidade = input("Digite o nome da cidade: ")
previsao = obter_previsao(cidade)
if previsao:
    print(f"A temperatura em {cidade} é {previsao[0]}°C com {previsao[1]}.")
else:
    print("Não foi possível obter a previsão do tempo.")