import json
def carregar_eventos(caminho):
   

    with open(caminho, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
    elista = isinstance(dados,list)
    if not elista:
      raise ValueError("O JSON precisa conter uma lista de eventos")
    return dados
def ips_com_muitas_falhas(dicionario,limite = 2):
  falhas = {}
  for ips in dicionario:
    if ips["resultado"] == "falha":
      ip = ips["ip"]
      if ip not in falhas:
        falhas[ip] = 1
      else:
        falhas[ip] += 1
      
  return {
    ip: quantidade
    for ip, quantidade in falhas.items()
    if quantidade >= limite
}

def resumir_acessos(eventos_resumo):
  resumo = {}
  for log in eventos_resumo:
    if log["resultado"] == "falha":
      ip = log["ip"]
      if ip in resumo:
        resumo[ip]["falhas"] += 1
      else:
        resumo[ip] = {"falhas": 1, "sucessos" : 0}
    if log["resultado"] == "sucesso":
      ip = log["ip"]
      if ip in resumo:
        resumo[ip]["sucessos"] += 1
      else:
        resumo[ip] = { "falhas": 0 ,"sucessos": 1}
  return resumo

def listar_ips_unicos(eventos_resumo):
  sets = set()
  for log in eventos_resumo:
    ips = log["ip"]
    sets.add(ips)
  return sets
try:
    eventos = carregar_eventos("acessos.json")

except FileNotFoundError:
  print("ERRO! Arquivo JSON não encontrado!")

except json.JSONDecodeError:
  print("Erro! Arquivo não segue a sintaxe JSON!")

except ValueError as erro:
  print(f"Erro: {erro}")
  

else:
  
    print("Resumo:")
    print(resumir_acessos(eventos))

    print("IPs únicos:")
    print(listar_ips_unicos(eventos))

    print("IPs com pelo menos duas falhas:")
    print(ips_com_muitas_falhas(eventos, limite=2))

