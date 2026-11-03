eventos_resumo = [
    {"ip": "192.0.2.10", "resultado": "falha"},
    {"ip": "192.0.2.20", "resultado": "sucesso"},
    {"ip": "192.0.2.10", "resultado": "sucesso"},
    {"ip": "192.0.2.10", "resultado": "falha"},
    {"ip": "192.0.2.20", "resultado": "falha"},
    {"ip": "192.0.2.30", "resultado": "sucesso"}
]
def listar_ips_unicos(eventos_resumo):
  sets = set()
  for log in eventos_resumo:
    ips = log["ip"]
    sets.add(ips)
  return sets

print(listar_ips_unicos(eventos_resumo))
assert listar_ips_unicos(eventos_resumo) == {'192.0.2.20', '192.0.2.10', '192.0.2.30'}
assert listar_ips_unicos([]) == set()
