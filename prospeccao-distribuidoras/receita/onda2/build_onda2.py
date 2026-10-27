import json, re, csv, collections
P = {x["base"]: x for x in json.load(open("out2/pool4.json"))}
sel = json.load(open("out2/sel90.json"))
CNAE = {c: d for c, d in csv.reader(open("rf_ref/cnae_utf8.csv", encoding="utf8"), delimiter=";")}
CAD = {"07063181", "11022033", "05890038"}
OBS = {
 "07063181": "Já tem cadastro na Nitron, sem compra nos últimos 24 meses: perguntar o que faltou.",
 "30679326": "Já tem cadastro na Nitron (Mahex Atacado), sem compra nos últimos 24 meses.",
 "11022033": "Já tem cadastro na Nitron, sem compra nos últimos 24 meses: perguntar o que faltou.",
 "05890038": "Já tem cadastro na Nitron (JN Bauru), sem compra nos últimos 24 meses. Distribuidora de armarinhos.",
 "15281596": "Filial de distribuidora com matriz fora de SP (telefone DDD 47).",
 "04511084": "E-mail da Receita é de outro domínio: confirmar o contato do comprador.",
 "07489844": "E-mail da Receita é de outro domínio: confirmar o contato do comprador.",
 "10684754": "Central de distribuição de rede de supermercados (Rede Star).",
 "11164349": "Marca Duratto: distribuidora de artigos para casa.",
}
def canal(x): return "whatsapp" if x["cel"] else ("email" if x["mail"] else "ligacao")
DIAS = [("qua", "2026-10-28"), ("qui", "2026-10-29"), ("sex", "2026-10-30")]
grupos = collections.defaultdict(list)
for b in sel: grupos[canal(P[b])].append(P[b])
ordem = []
k = 0
for c in ("whatsapp", "email", "ligacao"):
    for x in sorted(grupos[c], key=lambda x: (-x["score"], x["porte"] != "05", -x["idade"])):
        ordem.append((x, DIAS[k % 3])); k += 1
out = []
for x, (dia, data) in ordem:
    pr = "8%" if x["onda_origem"] == "onda2-8pct" else "sem adicional"
    minimo = 3570 if (x["onda_origem"] == "onda2-8pct" or x["regiao"] in ("Extremo de Campinas", "Extremo de Sorocaba")) else 2500
    ativ = CNAE.get(x["cnae"], "")
    frete = "frete CIF com adicional de 8%" if pr == "8%" else "frete CIF sem adicional"
    mn = f"{minimo:,}".replace(",", ".")
    info = (f"Prospect frio (raspagem Receita out/2026, onda 2, envio {dia} {data[8:]}/{data[5:7]}). {x['razao']}, distribuidora/atacado em {x['cidade'].title()}/SP "
            f"({x['regiao']}, {frete}, pedido mínimo CIF R$ {mn}). {round(x['idade'])} anos de empresa. "
            + ("Tem cadastro antigo na Nitron, sem compra em 24 meses. " if x["base"] in CAD else "Nunca comprou da Nitron. ")
            + "Objetivo: qualificar (marcas que distribui, cidades que atende, volume) e enviar tabela de distribuidor.")
    out.append(dict(base=x["base"], cnpj=x["cnpj"], razao=x["razao"], fantasia=x["fantasia"], cidade=x["cidade"].title(), regiao=x["regiao"],
        bairro=x["bairro"].strip().title(), cep=x["cep"], end=re.sub(r"\s+", " ", x["end"]).title(), cel=x["cel"], fixo=x["fixo"], mail=x["mail"],
        canal=canal(x), dia=dia, data=data, minimo=minimo, cif=pr, idade=round(x["idade"]), obs=OBS.get(x["base"], ""), info=info, ativ=ativ, score=x["score"]))
json.dump(out, open("out2/onda2.json", "w"), ensure_ascii=False, indent=1)
print(sorted(collections.Counter((o["dia"], o["canal"]) for o in out).items()))
