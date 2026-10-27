"""Monta o pool da onda 2 (90 distribuidoras): reserva da onda 1 + interior SP a 8%. Mesma pontuacao da onda 1."""
import csv, json, re, pickle, sys
MIN = int(sys.argv[1]) if len(sys.argv) > 1 else 5
from datetime import date
csv.field_size_limit(10**7)
TIER = {"4649499": 1}
POS_UD = r"UTILIDAD|UTENSIL|\bUD\b|BAZAR|DO LAR|PARA O LAR|1,99"
NEG = (r"INDUSTRIA|OPTIC|OTIC|ESPORT|FARMA|MEDIC|HOSPITAL|AUTO|PECAS|VEICUL|PISCINA|QUIMIC|DESENTUP|UNIFORM|AGRO|BEBIDA|ALIMENT|HORTI|CAFE|"
       r"SUPERMERC|MAQUINA|ELETRONIC|INFORMATIC|COSMETIC|LIVR|PAPELARIA|FERRAMENT|ELETRIC|CONSTRU|TECID|MINERAC|SEGURANCA|GASES|COBRANC|IMOBILI|"
       r"PARTICIPAC|FALIDO|RECUPERACAO|BRINQUED|TOYS|KIDS|SKATE|FESTA|PAPEL DE PAREDE|RELIGIOS|CLIPPER|CHEMICAL|LEGO|MUSICA|DRUMS|BALLOON|FOSFORO|"
       r"PERFUMARIA|COMUNICACAO|SUZANO|MAKRO|TENDA|FASTENAL|DESTRO|SCAPOL|PET\b|PETS|MADEIRA|VIDRO|EMBALAGENS INDUSTRIA|CONFEC|CALCADO|MOVEIS|COLCHO|AGROPEC|RACAO|VETERIN|ODONTO|LABORAT|TINTA|BORRACHA|PNEU|ACO\b|METALURG")
BAD_MAIL = r"contab|contador|escritorio|\.adv@|adv@|assessoria|fiscal@|cont\.|contabil|contax|\.aud@|consultoria|controller|controladoria|gestao|empresario|custodio|contmaster|admcont|contcarvalho|contecnica|escmodelo|escrimodelo|esclider|servcont|legalizacao|tributario|paralegal|ecregente|ecsaojose"

def load(estab, emp, onda):
    E = list(csv.reader(open(estab, encoding="utf8"), delimiter=";"))
    EMP = {r[0]: r for r in csv.reader(open(emp, encoding="utf8"), delimiter=";")}
    out = []
    for r in E:
        e = EMP.get(r[0])
        if not e: continue
        ini = r[10]
        idade = (date(2026, 10, 27) - date(int(ini[:4]), int(ini[4:6]), int(ini[6:]))).days / 365.25 if ini else 0
        out.append(dict(base=r[0], cnpj=r[0]+r[1]+r[2], matriz=r[3], fantasia=r[4], cnae=r[11], sec=r[12], end=f"{r[13]} {r[14]}, {r[15]} {r[16]}".strip(),
            bairro=r[17], cep=r[18], cidade=r[-1], regiao=r[-2], ddd1=r[21], tel1=r[22], ddd2=r[23], tel2=r[24], email=r[27].lower().strip(),
            razao=e[1], nat=e[2], cap=float(e[4].replace(",", ".") or 0), porte=e[5], idade=idade, onda_origem=onda))
    return out

def score(x):
    nome = f"{x['razao']} {x['fantasia']}"
    if re.search(NEG, nome): return -1
    s = 0
    if x["cnae"] == "4649499": s += 3
    elif x["cnae"] in ("4693100", "4686902"): s += 1
    elif "4649499" in x["sec"].split(","): s += 1
    if re.search(POS_UD, nome): s += 3
    if re.search(r"DISTRIBUID|ATACAD|DISTRIBUIC", nome): s += 2
    if re.search(r"PLASTIC|DESCARTAV|HOUSE|HOME|PRESENTE|IMPORTAD", nome): s += 1
    if x["porte"] == "05": s += 1
    if x["idade"] >= 10: s += 1
    return s

def phone(ddd, t):
    d = re.sub(r"\D", "", ddd + t)
    if len(d) < 10 or re.search(r"1111111|0000000", d): return None, None
    ddd, n = d[:2], d[2:]
    if len(n) == 8 and n[0] in "9876": return f"+55{ddd}9{n}", "celular"
    if len(n) == 9 and n[0] == "9": return f"+55{ddd}{n}", "celular"
    if len(n) == 8 and n[0] in "2345": return f"+55{ddd}{n}", "fixo"
    return None, None

rows = load("out/estab.csv", "out/empresas.csv", "onda1-reserva") + load("out2/estab.csv", "out2/empresas.csv", "onda2-8pct")
ONDA1 = set(json.load(open("out/onda1_bases.json")))
best = {}
for x in sorted(rows, key=lambda x: x["matriz"] != "1"):
    if x["nat"] == "2135" or x["porte"] not in ("03", "05") or x["idade"] < 3 or x["base"] in ONDA1: continue
    best.setdefault(x["base"], x)
pool = []
for x in best.values():
    s = score(x)
    if s < MIN: continue
    p1, k1 = phone(x["ddd1"], x["tel1"]); p2, k2 = phone(x["ddd2"], x["tel2"])
    cel = p1 if k1 == "celular" else (p2 if k2 == "celular" else None)
    fixo = p1 if k1 == "fixo" else (p2 if k2 == "fixo" else None)
    mail = x["email"] if x["email"] and "@" in x["email"] and not re.search(BAD_MAIL, x["email"]) else None
    x.update(score=s, cel=cel, fixo=fixo, mail=mail, mail_descartado=x["email"] if x["email"] and not mail else None)
    pool.append(x)
pool.sort(key=lambda x: (-x["score"], x["porte"] != "05", -x["idade"]))
json.dump(pool, open(f"out2/pool{MIN}.json", "w"), ensure_ascii=False)
import collections
print("pool", len(pool), collections.Counter(x["onda_origem"] for x in pool))
print("contactaveis (mail ou cel)", sum(1 for x in pool if x["mail"] or x["cel"]))
