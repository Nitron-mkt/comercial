"""Junta razao social, natureza, capital e porte (Empresas*.zip) aos estabelecimentos filtrados."""
import csv, io, sys, zipfile, glob
DATA, ESTAB, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
csv.field_size_limit(10**7)
bases = {r[0] for r in csv.reader(open(ESTAB, encoding="utf8"), delimiter=";")}
with open(OUT, "w", newline="", encoding="utf8") as fo:
    w = csv.writer(fo, delimiter=";")
    for z in sorted(glob.glob(f"{DATA}/Empresas*.zip")):
        zf = zipfile.ZipFile(z)
        with zf.open(zf.namelist()[0]) as raw:
            for r in csv.reader(io.TextIOWrapper(raw, encoding="latin1"), delimiter=";"):
                if r[0] in bases:
                    w.writerow(r)
        print(z, flush=True)
