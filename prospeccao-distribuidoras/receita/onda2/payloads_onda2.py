import json, re
o = json.load(open("out2/onda2.json"))
def nome(x):
    f = x["fantasia"].strip()
    n = f if f and not f.startswith("*") else x["razao"]
    n = re.sub(r"\s+(LTDA|EIRELI|ME|EPP|S/?A)\.?(\s*-\s*\w+)?$", "", n.strip(), flags=re.I).strip(" -.")
    return n.title()[:60]
pl = []
for x in o:
    cf = [["TLRZeTrxxPBsMNRqbdHO", x["cnpj"]], ["AaHCXUJOMzy0JzZdPgGl", x["razao"]], ["Jh8SJfxj2WGlKxaloxTn", "Atacado e Distribuidor"],
          ["422b44jihaUhT41AWq22", x["regiao"]], ["dDlZtl9xsCdQYNXov8eQ", x["bairro"]], ["VW17KuURFzkYahSCUpgr", x["info"] + (" " + x["obs"] if x["obs"] else "")]]
    b = {"name": nome(x), "companyName": x["razao"], "address1": x["end"], "city": x["cidade"], "state": "SP", "postalCode": x["cep"], "country": "BR",
         "source": "raspagem receita onda 2", "tags": ["raspagem", "raspagem-onda2", f"raspagem-onda2-{x['dia']}"]}
    if x["cel"]:
        b["phone"] = x["cel"]; cf.append(["yAsQNjO4m5dl7lBKOs1h", x["cel"]])
        if x["fixo"]: cf.append(["OjT8IXkXH9rjEH4kbY3H", x["fixo"]])
    elif x["fixo"]:
        b["phone"] = x["fixo"]
    if x["mail"]: b["email"] = x["mail"]
    b["customFields"] = [{"id": i, "field_value": v} for i, v in cf]
    x["nome_ghl"] = b["name"]
    pl.append((x["base"], b))
json.dump(o, open("out2/onda2.json", "w"), ensure_ascii=False, indent=1)
json.dump(pl, open("out2/ghl_payloads.json", "w"), ensure_ascii=False)
