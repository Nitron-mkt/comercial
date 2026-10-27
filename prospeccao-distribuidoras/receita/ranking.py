import csv, sys
from datetime import date
csv.field_size_limit(10**7)
E = list(csv.reader(open("out/estab.csv", encoding="utf8"), delimiter=";"))
EMP = {r[0]: r for r in csv.reader(open("out/empresas.csv", encoding="utf8"), delimiter=";")}
TIER = {"4649499": 1, "4686902": 2, "4693100": 2, "4649408": 3, "4649409": 3, "4672900": 3}
rows = []
for r in E:
    emp = EMP.get(r[0])
    if not emp: continue
    razao, nat, cap, porte = emp[1], emp[2], float(emp[4].replace(",", ".") or 0), emp[5]
    ini = r[10]; idade = (date(2026, 10, 27) - date(int(ini[:4]), int(ini[4:6]), int(ini[6:]))).days / 365.25 if ini else 0
    tier = TIER.get(r[11], 2)
    rows.append(dict(base=r[0], cnpj=r[0]+r[1]+r[2], matriz=r[3], fantasia=r[4], cnae=r[11], sec=r[12], tier=tier,
        end=f"{r[13]} {r[14]}, {r[15]} {r[16]}".strip(), bairro=r[17], cep=r[18], cidade=r[-1], regiao=r[-2],
        tel1=f"({r[21]}) {r[22]}" if r[22] else "", tel2=f"({r[23]}) {r[24]}" if r[24] else "", email=r[27].lower(),
        razao=razao, nat=nat, cap=cap, porte=porte, idade=idade, ini=ini))
import collections
print("total", len(rows))
print("porte", collections.Counter(x["porte"] for x in rows))
print("nat top", collections.Counter(x["nat"] for x in rows).most_common(6))
print("cnae", collections.Counter(x["cnae"] for x in rows).most_common(8))
ok = [x for x in rows if x["nat"] not in ("2135",) and x["porte"] in ("03", "05") and x["idade"] >= 3]
print("apos filtro porte/idade/natureza", len(ok), collections.Counter(x["regiao"] for x in ok))
import pickle; pickle.dump(rows, open("out/rows.pkl", "wb"))
