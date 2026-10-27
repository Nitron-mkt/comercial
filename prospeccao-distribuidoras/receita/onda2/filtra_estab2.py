"""Filtra Estabelecimentos*.zip da Receita: SP, ativos, cidades da onda 1, CNAEs de atacado do segmento."""
import csv, io, sys, zipfile, glob, os
sys.path.insert(0, os.path.dirname(__file__))
from cidades2 import CIDADE_REGIAO, norm

DATA, REF, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
mun = {}
with open(glob.glob(f"{REF}/*MUNICCSV")[0], encoding="latin1") as f:
    for cod, nome in csv.reader(f, delimiter=";"):
        mun[cod] = nome
# a tabela da Receita nao tem UF: o filtro UF=SP vem do estabelecimento
alvo_mun = {cod: CIDADE_REGIAO[norm(n)] for cod, n in mun.items() if norm(n) in CIDADE_REGIAO}

PRINC = {"4649499", "4693100", "4686902", "4649408", "4649409", "4672900"}
csv.field_size_limit(10**7)
done = set(open(OUT + ".done").read().split()) if os.path.exists(OUT + ".done") else set()
with open(OUT, "a", newline="", encoding="utf8") as fo:
    w = csv.writer(fo, delimiter=";")
    for z in sorted(glob.glob(f"{DATA}/Estabelecimentos*.zip")):
        name = os.path.basename(z)
        if name in done:
            continue
        try:
            zf = zipfile.ZipFile(z)
        except zipfile.BadZipFile:
            print("incompleto:", name); continue
        n = 0
        with zf.open(zf.namelist()[0]) as raw:
            for r in csv.reader(io.TextIOWrapper(raw, encoding="latin1"), delimiter=";"):
                if r[19] != "SP" or r[5] != "02" or r[20] not in alvo_mun:
                    continue
                sec = r[12].split(",") if r[12] else []
                if r[11] in PRINC or (r[11].startswith("46") and "4649499" in sec):
                    w.writerow(r + [alvo_mun[r[20]], mun[r[20]]]); n += 1
        open(OUT + ".done", "a").write(name + "\n")
        print(name, n, flush=True)
print("municipios alvo:", len(alvo_mun))
