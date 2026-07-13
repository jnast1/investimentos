import json, urllib.request, datetime, sys

def buscar(cod, meses=38):
    fim = datetime.date.today()
    ini = fim - datetime.timedelta(days=meses*31)
    url = ("https://api.bcb.gov.br/dados/serie/bcdata.sgs.%d/dados?formato=json"
           "&dataInicial=%s&dataFinal=%s") % (cod, ini.strftime("%d/%m/%Y"), fim.strftime("%d/%m/%Y"))
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=45) as r:
            dados = json.loads(r.read().decode("utf-8"))
        if isinstance(dados, list) and dados:
            print("OK serie %d: %d registros, ultimo %s" % (cod, len(dados), dados[-1]))
            return dados
        print("VAZIO serie %d" % cod)
    except Exception as e:
        print("FALHA serie %d: %s" % (cod, e))
    return []

cdi   = buscar(4391)
ipca  = buscar(433)
selic = buscar(432)[-3:]

incc = []
for c in (192, 7456, 7457, 189):
    incc = buscar(c)
    if incc:
        print(">>> INCC obtido da serie %d" % c)
        break

saida = {
    "atualizado": datetime.datetime.utcnow().isoformat() + "Z",
    "cdi": cdi, "ipca": ipca, "incc": incc, "selic": selic,
}
with open("indices.json", "w", encoding="utf-8") as f:
    json.dump(saida, f, ensure_ascii=False)

print("\n=== RESUMO ===")
for k in ("cdi", "ipca", "incc", "selic"):
    print("%-6s %d registros" % (k, len(saida[k])))

if not cdi and not ipca:
    sys.exit("Nenhuma serie principal foi obtida")
