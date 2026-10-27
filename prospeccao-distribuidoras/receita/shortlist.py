import pickle, re, json
rows = pickle.load(open("out/rows.pkl", "rb"))
ok = [x for x in rows if x["nat"] != "2135" and x["porte"] in ("03", "05") and x["idade"] >= 3]
best = {}
for x in sorted(ok, key=lambda x: x["matriz"] != "1"):
    best.setdefault(x["base"], x)
POS = r"UTILIDAD|UTENSIL|\bUD\b|BAZAR|PRESENTE|DO LAR|PARA O LAR|CASA E|HOUSE|HOME|PLASTIC|DESCARTAV|ATACAD|DISTRIBUID|DISTRIBUIC|1,99|IMPORTAD"
NEG = r"INDUSTRIA|OPTIC|OTIC|ESPORT|FARMA|MEDIC|HOSPITAL|AUTO|PECAS|VEICUL|PISCINA|QUIMIC|DESENTUP|UNIFORM|AGRO|BEBIDA|ALIMENTO|HORTI|CAFE|SUPERMERC|MAQUINA|ELETRONIC|INFORMATIC|COSMETIC|LIVR|PAPELARIA|FERRAMENT|ELETRIC|CONSTRU|TECID|MINERAC|SEGURANCA|GASES|COBRANC|IMOBILI|PARTICIPAC|FALIDO|RECUPERACAO"
out = []
for x in best.values():
    nome = f"{x['razao']} {x['fantasia']}"
    if re.search(NEG, nome): continue
    s = 0
    if x["cnae"] == "4649499": s += 3
    elif x["cnae"] in ("4693100", "4686902"): s += 1
    elif "4649499" in x["sec"].split(","): s += 1
    if re.search(r"UTILIDAD|UTENSIL|\bUD\b|BAZAR|DO LAR|PARA O LAR|1,99", nome): s += 3
    if re.search(r"DISTRIBUID|ATACAD|DISTRIBUIC", nome): s += 2
    if re.search(r"PLASTIC|DESCARTAV|HOUSE|HOME|PRESENTE|IMPORTAD", nome): s += 1
    if x["porte"] == "05": s += 1
    if x["idade"] >= 10: s += 1
    if s >= 5: out.append(dict(x, score=s))
out.sort(key=lambda x: (-x["score"], -x["cap"]))
json.dump(out, open("out/shortlist.json", "w"), ensure_ascii=False)
print(len(out))
for x in out[:130]:
    print(x["base"], x["score"], x["porte"], x["cnae"], int(x["cap"]), round(x["idade"]), x["cidade"][:16], "|", x["razao"][:52], "|", x["fantasia"][:22])
print("BASES:", ",".join("'"+x["base"]+"'" for x in out[:130]))
