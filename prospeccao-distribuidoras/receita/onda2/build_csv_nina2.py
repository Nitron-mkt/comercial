"""CSV operacional da Nina para a onda 2: um contato por linha, com canal, data e mensagens prontas (frete e mínimo já resolvidos)."""
import csv, json, re, sys, datetime as dt

base_dir, out_dir = sys.argv[1], sys.argv[2]
d = json.load(open(f"{base_dir}/onda2.json"))
ids = dict(l.split() for l in open(f"{base_dir}/ghl_ids.txt"))
nome = {b: body["name"] for b, body in json.load(open(f"{base_dir}/ghl_payloads.json"))}
nome["27919813"] = "Nobe Utensílios Domésticos"  # nome usado no cadastro do GHL

ACENTO = {"Sao": "São", "Jose": "José", "Ribeirao": "Ribeirão", "Jundiai": "Jundiaí", "Avare": "Avaré",
          "Tatui": "Tatuí", "Taubate": "Taubaté", "Ibiuna": "Ibiúna", "Braganca": "Bragança", "Marilia": "Marília",
          "Fernandopolis": "Fernandópolis", "Igarata": "Igaratá", "Taruma": "Tarumã", "Tremembe": "Tremembé",
          "Barbara": "Bárbara", "Matao": "Matão", "Limeira": "Limeira", "Iracemapolis": "Iracemápolis",
          "Cacapava": "Caçapava", "Guaratingueta": "Guaratinguetá", "Itapetininga": "Itapetininga"}
MINUSC = {"Do", "Dos", "Da", "Das", "De", "D'Oeste"}
def cidade(c):
    out = []
    for i, p in enumerate(c.split()):
        p = ACENTO.get(p, p)
        if i and p in MINUSC:
            p = "d'Oeste" if p == "D'Oeste" else p.lower()
        out.append(p)
    return " ".join(out)

FERIADOS = {dt.date(2026, 11, 2)}
def uteis(ini, n):
    x, k = ini, 0
    while k < n:
        x += dt.timedelta(days=1)
        if x.weekday() < 5 and x not in FERIADOS:
            k += 1
    return x
br = lambda x: x.strftime("%d/%m/%Y")
brl = lambda v: f"{v:,}".replace(",", ".")
ADM = re.compile(r"^(fiscal|financeiro|nfe|tesouraria|adm|contabil)", re.I)

def linha(x):
    emp, cid = nome[x["base"]], cidade(x["cidade"])
    sem = x["cif"] == "sem adicional"
    d0 = dt.date.fromisoformat(x["data"])
    frete_wpp = "O frete é CIF sem adicional para a sua cidade." if sem else "Entregamos com frete CIF na sua região."
    frete_mail = (f"Frete CIF sem adicional para {cid}, pedido mínimo de R$ {brl(x['minimo'])}" if sem
                  else f"Frete CIF para {cid}, pedido mínimo de R$ {brl(x['minimo'])}")
    if x["canal"] == "whatsapp":
        m1 = (f"Olá! Aqui é a Nina, da Nitron, fabricante de potes, organizadores e utilidades domésticas. "
              f"Estamos buscando distribuidores em {cid} e a {emp} chamou nossa atenção. "
              f"Posso te enviar nossa condição para distribuidor? {frete_wpp}")
        assunto = ""
    else:
        assunto = f"Nitron: condição para distribuidores em {cid}"
        m1 = (f"Olá, tudo bem?\n\nAqui é a Nina, da Nitron, fabricante de potes, organizadores, lixeiras e utilidades plásticas.\n\n"
              f"Estamos ampliando nossa rede de distribuidores no interior de SP e a {emp} chamou nossa atenção como distribuidora em {cid}.\n\n"
              f"- {frete_mail}\n- Tabela específica para distribuidor\n"
              f"- Linha que completa o mix de quem já vende embalagens, descartáveis, limpeza ou utilidades: potes, organizadores, lixeiras, cozinha e banheiro\n\n"
              f"Posso te enviar a tabela e o catálogo? Se não for com você, pode me indicar quem cuida das compras?\n\n"
              f"Nina · Nitron\n\nSe não quiser receber nossos contatos, é só responder \"sair\".")
    m2 = (f"Oi! Passando para saber se faz sentido te enviar nossa condição para distribuidor em {cid}. "
          f"Se não for com você, me indica quem cuida das compras?")
    m3 = "Última mensagem por aqui: se em algum momento quiser conhecer a linha Nitron para distribuidor, é só responder. Obrigada!"
    obs = []
    if x["obs"] and not x["obs"].startswith("Marca Duratto"):
        obs.append(x["obs"].rstrip("."))
    if x["mail"] and ADM.match(x["mail"]) and "outro domínio" not in (x["obs"] or ""):
        obs.append("E-mail é do financeiro/fiscal: pedir o contato do comprador")
    first, _, last = emp.partition(" ")
    return {
        "Dia de envio": {"qua": "Quarta", "qui": "Quinta", "sex": "Sexta"}[x["dia"]],
        "Data envio": br(d0),
        "Follow-up 1": br(uteis(d0, 3)),
        "Follow-up 2": br(uteis(d0, 7)),
        "Canal": "WhatsApp" if x["canal"] == "whatsapp" else "E-mail",
        "GHL Contact ID": ids[x["base"]],
        "First Name": first,
        "Last Name": last,
        "Company Name": emp,
        "Razao Social": x["razao"],
        "CNPJ": x["cnpj"],
        "Phone": x["cel"] or x["fixo"] or "",
        "WhatsApp": x["cel"] or "",
        "Telefone Fixo": x["fixo"] or "",
        "Email": x["mail"] or "",
        "Address": x["end"],
        "Bairro": x["bairro"],
        "City": cid,
        "State": "SP",
        "Postal Code": x["cep"],
        "Praca": x["regiao"],
        "Frete CIF": "sem adicional" if sem else "com adicional de 8%",
        "Pedido Minimo CIF": f"R$ {brl(x['minimo'])}",
        "Tags": f"raspagem,raspagem-onda2,raspagem-onda2-{x['dia']}",
        "Observacao": ". ".join(obs),
        "Informacoes para AI": x["info"],
        "Assunto E-mail": assunto,
        "Mensagem 1 (primeiro contato)": m1,
        "Mensagem 2 (follow-up 1)": m2,
        "Mensagem 3 (follow-up 2)": m3,
    }

rows = [linha(x) for x in sorted(d, key=lambda x: (x["data"], x["canal"] != "whatsapp", nome[x["base"]]))]
def grava(path, rs):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rs[0]))
        w.writeheader(); w.writerows(rs)
grava(f"{out_dir}/nina-onda2-90-contatos.csv", rows)
for dia, nm in (("qua", "Quarta"), ("qui", "Quinta"), ("sex", "Sexta")):
    grava(f"{out_dir}/nina-onda2-{dia}.csv", [r for r in rows if r["Dia de envio"] == nm])
print(len(rows), {c: sum(r["Canal"] == c for r in rows) for c in ("WhatsApp", "E-mail")})
