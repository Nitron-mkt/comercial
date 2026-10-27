"""Gera o md da Nina para a onda 2 (90 contatos, 30 por dia) a partir de out2/onda2.json e out2/ghl_ids.txt."""
import json, re, sys, datetime as dt

base_dir, out_md, out_csv = sys.argv[1], sys.argv[2], sys.argv[3]
d = json.load(open(f"{base_dir}/onda2.json"))
ids = dict(l.split() for l in open(f"{base_dir}/ghl_ids.txt"))
nome_ghl = {b: body["name"] for b, body in json.load(open(f"{base_dir}/ghl_payloads.json"))}
nome_ghl["27919813"] = "Nobe Utensílios Domésticos"  # nome usado no cadastro do GHL
brl = lambda v: f"{v:,}".replace(",", ".")
assert len(d) == 90 and all(x["base"] in ids for x in d)

FERIADOS = {dt.date(2026, 11, 2)}  # Finados (seg)
def uteis(ini, n):
    x, k = ini, 0
    while k < n:
        x += dt.timedelta(days=1)
        if x.weekday() < 5 and x not in FERIADOS:
            k += 1
    return x
fmt = lambda x: x.strftime("%d/%m")

ADM = re.compile(r"^(fiscal|financeiro|nfe|tesouraria|adm|contabil)", re.I)
def obs(x):
    o = []
    if x["obs"] and not x["obs"].startswith("Marca Duratto"):
        o.append(x["obs"].rstrip("."))
    if x["mail"] and ADM.match(x["mail"]) and "outro domínio" not in (x["obs"] or ""):
        o.append("E-mail é do " + ("fiscal" if x["mail"].lower().startswith(("fiscal", "nfe")) else "financeiro/adm") + ": pedir o contato do comprador")
    if x["cif"] == "8%":
        o.insert(0, "Frete +8%")
    return ". ".join(o)

DIAS = [("qua", "Quarta 28/10"), ("qui", "Quinta 29/10"), ("sex", "Sexta 30/10")]
canal_txt = {"whatsapp": "**WhatsApp**", "email": "E-mail"}

cal = []
for dia, nome in DIAS:
    d0 = dt.date.fromisoformat(next(x["data"] for x in d if x["dia"] == dia))
    cal.append((dia, nome, d0, uteis(d0, 3), uteis(d0, 7)))
rel = uteis(cal[-1][2], 10)

L = []
w = L.append
w("# Ação Nina: prospecção de distribuidoras (raspagem, onda 2)\n")
w("**Para:** Nina (agente de IA da Nitron no GHL)  ")
w("**Ação:** primeiro contato com 90 distribuidoras que nunca compraram da Nitron, 30 por dia  ")
w("**Público:** tags `raspagem-onda2-qua`, `raspagem-onda2-qui` e `raspagem-onda2-sex` (90 cadastros criados em 27/10/2026)  ")
w("**Dono da ação:** Marketing Nitron\n")
w("---\n")
w("## 0. Agenda de envio\n")
w("| Lote | Tag do lote | Primeiro contato | Contatos | WhatsApp | E-mail | 1º follow-up (dia 3 útil) | 2º follow-up (dia 7 útil) |")
w("|---|---|---|---|---|---|---|---|")
for dia, nome, d0, f3, f7 in cal:
    s = [x for x in d if x["dia"] == dia]
    w(f"| {nome} | `raspagem-onda2-{dia}` | {fmt(d0)} | {len(s)} | {sum(x['canal']=='whatsapp' for x in s)} | {sum(x['canal']=='email' for x in s)} | {fmt(f3)} | {fmt(f7)} |")
w("")
w("- **Envie cada lote só no seu dia.** Não antecipe o lote de quinta ou sexta.")
w("- **02/11 (segunda) é feriado de Finados:** não envie nada e não conte como dia útil. As datas de follow-up acima já consideram isso.")
w("- Envio em **dia útil, das 9h às 17h** (horário de Brasília). Espalhe os envios ao longo do dia (não dispare os 30 no mesmo minuto).\n")
w("## 1. Objetivo\n")
w("Abrir conversa com distribuidoras e atacados do interior de SP que **nunca compraram da Nitron** e levar as interessadas até o envio da **tabela de distribuidor** e o cadastro.\n")
w("A meta é a **conversa qualificada**, não fechar pedido. Preço, prazo e pedido ficam com uma pessoa do time comercial (seção 7).\n")
w("## 2. Quem são esses contatos (importante)\n")
w("- **Não são lojistas.** São **distribuidores/atacadistas** de utilidades domésticas, embalagens, descartáveis, produtos de limpeza e armarinhos: compram em volume e revendem para lojas, bazares e mercados. Não use o roteiro de anúncio para lojista.")
w("- Vieram da **base pública de CNPJ da Receita Federal**. **Nunca falaram com a Nitron**: é contato frio.")
w("- Muitos são distribuidores de **embalagens e descartáveis** ou de **limpeza**. Para eles, o gancho é **completar o mix** com potes, organizadores, lixeiras e utilidades plásticas.")
w("- Os contatos são os **declarados na Receita**. Muitos e-mails são do financeiro ou fiscal. Quem responde pode não ser o comprador: sempre peça o contato de quem compra.")
w("- O campo **\"Informações para AI\"** de cada contato traz cidade, região, frete, pedido mínimo, tempo de empresa e observações. **Leia antes de cada contato.**")
w("- 3 contatos **já têm cadastro antigo na Nitron** e não compram há mais de 24 meses (Du Chapéu, JFZ e JN Distribuidora). Com eles, a abordagem é: \"vocês já foram nossos clientes; o que faltou para voltarem a comprar?\".\n")
w("## 3. Regras de canal (uma mensagem por contato no primeiro envio)\n")
w("| Situação do contato | Canal | Contatos |\n|---|---|---|")
w(f"| Campo **WhatsApp** preenchido (celular) | **WhatsApp**, usando template aprovado | {sum(x['canal']=='whatsapp' for x in d)} (11 por dia) |")
w(f"| Sem WhatsApp, **com e-mail** | **E-mail** | {sum(x['canal']=='email' for x in d)} (19 por dia) |\n")
w("- **Nunca mande WhatsApp para o campo Telefone** quando o campo WhatsApp estiver vazio: são números **fixos** e a mensagem não chega.")
w("- Os 33 contatos de WhatsApp também têm e-mail cadastrado. **Não mande os dois no primeiro contato.** O e-mail só entra se o WhatsApp falhar (número inválido ou não entregue): nesse caso aplique `raspagem-contato-invalido` ao número e envie o e-mail no mesmo dia.")
w("- Contato com **DND ativo** ou tag `raspagem-optout`: não enviar nada.")
w("- Nenhum contato desta onda está na **Região Central SP** (área da Modenuti). Se aparecer algum, **não envie** e avise o Marketing.\n")
w("## 4. Mensagens do primeiro contato\n")
w("Variáveis do GHL: `{{contact.company_name}}` (razão social), `{{contact.city}}` (cidade) e `{{contact.praca}}` (região de entrega).\n")
w("### Frete e pedido mínimo: confira o campo Praça antes de escrever\n")
w("| Praça (campo Praça) | Frete CIF | Pedido mínimo CIF | Contatos |\n|---|---|---|---|")
w("| Campinas e Região, Região de Sorocaba, Região de S.J Campos | **sem adicional** | R$ 2.500 | 46 |")
w("| Extremo de Campinas, Extremo de Sorocaba | **sem adicional** | R$ 3.570 | 17 |")
w("| Região S.J.R. Preto, Rib. Preto, Bauru, Marília, Barretos, Franca | **com adicional de 8%** | R$ 3.570 | 27 |\n")
w("> **Atenção:** nas praças com adicional de 8%, **nunca escreva \"frete sem adicional\"**. Use a versão B das mensagens.\n")
w("### 4.1 WhatsApp (dentro do template aprovado)\n")
w("**Versão A (frete sem adicional):**\n")
w("> Olá! Aqui é a Nina, da Nitron, fabricante de potes, organizadores e utilidades domésticas. Estamos buscando distribuidores em {{contact.city}} e a {{contact.company_name}} chamou nossa atenção. Posso te enviar nossa condição para distribuidor? O frete é CIF sem adicional para a sua cidade.\n")
w("**Versão B (praças com 8%):**\n")
w("> Olá! Aqui é a Nina, da Nitron, fabricante de potes, organizadores e utilidades domésticas. Estamos buscando distribuidores em {{contact.city}} e a {{contact.company_name}} chamou nossa atenção. Posso te enviar nossa condição para distribuidor? Entregamos com frete CIF na sua região.\n")
w("Se o template aprovado tiver outro texto, use o template e mantenha a ideia: quem somos, por que estamos falando com eles e a pergunta final.\n")
w("### 4.2 E-mail\n")
w("**Assunto:** Nitron: condição para distribuidores em {{contact.city}}\n")
w("> Olá, tudo bem?\n>")
w("> Aqui é a Nina, da Nitron, fabricante de potes, organizadores, lixeiras e utilidades plásticas.\n>")
w("> Estamos ampliando nossa rede de distribuidores no interior de SP e a {{contact.company_name}} chamou nossa atenção como distribuidora em {{contact.city}}.\n>")
w("> - **[Versão A]** Frete CIF **sem adicional** para {{contact.city}}, pedido mínimo de R$ [2.500 ou 3.570, conforme a tabela acima]")
w(">   **[Versão B]** Frete CIF para {{contact.city}}, pedido mínimo de R$ 3.570")
w("> - Tabela específica para distribuidor")
w("> - Linha que completa o mix de quem já vende embalagens, descartáveis, limpeza ou utilidades: potes, organizadores, lixeiras, cozinha e banheiro\n>")
w("> Posso te enviar a tabela e o catálogo? Se não for com você, pode me indicar quem cuida das compras?\n>")
w("> Nina · Nitron  \n> [WhatsApp comercial]\n>")
w("> *Se não quiser receber nossos contatos, é só responder \"sair\".*\n")
w("Envie só uma das versões (A ou B). Nunca deixe os colchetes no texto enviado.\n")
w("## 5. Acompanhamento (se não houver resposta)\n")
w("| Quando | Canal | Mensagem |\n|---|---|---|")
w("| Dia 0 | Canal da seção 3 | Primeiro contato (seção 4) |")
w("| Dia 3 útil | Mesmo canal | \"Oi! Passando para saber se faz sentido te enviar nossa condição para distribuidor em {{contact.city}}. Se não for com você, me indica quem cuida das compras?\" |")
w("| Dia 7 útil | Mesmo canal | \"Última mensagem por aqui: se em algum momento quiser conhecer a linha Nitron para distribuidor, é só responder. Obrigada!\" e encerrar |\n")
w("- As datas de cada lote estão na seção 0.")
w("- **Parar a sequência assim que houver qualquer resposta.** No máximo **3 mensagens** por contato.")
w("- Sem resposta depois do dia 7: aplicar `raspagem-sem-resposta` e criar tarefa de ligação para o time (usar o campo Telefone).\n")
w("## 6. Como conduzir quando responderem\n")
w("**Objetivo da conversa:** descobrir se é distribuidor de verdade, quem é o comprador e se há interesse em receber a tabela.\n")
w("Perguntas de qualificação (uma por vez, sem interrogatório):")
w("1. Vocês revendem para lojas, mercados e bazares da região?")
w("2. Quais linhas e marcas trabalham hoje (utilidades, embalagens, limpeza)?")
w("3. Quais cidades vocês atendem?")
w("4. Quem decide as compras? (nome e cargo)")
w("5. Qual o melhor contato direto dessa pessoa? (WhatsApp ou e-mail)\n")
w("**Pode falar:**")
w("- A Nitron é fabricante de potes, organizadores, lixeiras, linha cozinha, banheiro e frasqueiras.")
w("- O frete e o pedido mínimo da praça do contato (seção 4).")
w("- Existe tabela específica para distribuidor, que o time comercial envia.\n")
w("**Não pode:**")
w("- Informar preço, desconto, prazo de pagamento ou prazo de entrega. Diga que o time comercial envia junto com a tabela.")
w("- Dizer \"frete sem adicional\" para praças com 8%.")
w("- Prometer exclusividade de região.")
w("- Citar outros clientes da Nitron pelo nome.")
w("- Insistir depois de um \"não\".\n")
w("**Respostas prontas:**")
w("- *\"Já temos fornecedor.\"* → \"Entendo! Muitas distribuidoras trabalham com mais de uma marca para completar o mix. Posso te mandar a tabela só para comparar?\"")
w("- *\"Só trabalhamos com embalagem / limpeza.\"* → \"Faz sentido! Vários distribuidores desse segmento usam a linha Nitron para completar o mix com os mesmos clientes. Posso te mandar a tabela para avaliar?\"")
w("- *\"Manda por e-mail.\"* → Pedir o e-mail do comprador, registrar no contato e passar para o time (seção 7).")
w("- *\"Quanto custa?\"* → \"Os preços dependem do mix e do volume. Vou pedir para o nosso comercial te enviar a tabela de distribuidor. Qual o melhor contato para isso?\"")
w("- *\"Já compramos de vocês\" (Du Chapéu, JFZ, JN).* → \"Que bom! Vi que faz um tempo que não compram. O que faltou? Quero entender para te mandar uma condição melhor.\" e passar para o time.")
w("- *\"Somos fábrica / supermercado / não revendemos.\"* → Agradecer, encerrar e aplicar `raspagem-fora-do-perfil`.")
w("- *\"Sair\" / \"não quero receber\".* → Confirmar o descadastro, ativar DND em todos os canais, aplicar `raspagem-optout` e encerrar.\n")
w("## 7. Quando passar para uma pessoa do time\n")
w("Passar a conversa (atribuir ao responsável e criar tarefa) quando:")
w("- pedirem tabela, preço, catálogo ou condição de pagamento;")
w("- quiserem fazer pedido ou cadastro;")
w("- o comprador for identificado e topar receber contato;")
w("- responderem Du Chapéu, JFZ ou JN (clientes antigos);")
w("- houver reclamação ou dúvida que você não saiba responder.\n")
w("Na passagem, escrever em **Comentario** um resumo de 2 linhas: quem respondeu, o que quer e as marcas que trabalha.\n")
w("## 8. Tags e campos de resultado\n")
w("| Situação | Tag | Atualizar campo |\n|---|---|---|")
w("| Qualquer resposta | `raspagem-respondeu` | — |")
w("| Distribuidor e quer receber tabela | `raspagem-qualificado` | Cargo (Comprador/Proprietário), Comentario |")
w("| Não tem interesse | `raspagem-sem-interesse` | Comentario com o motivo |")
w("| Não é distribuidor / é fábrica | `raspagem-fora-do-perfil` | Comentario |")
w("| Número ou e-mail errado | `raspagem-contato-invalido` | — |")
w("| Pediu para sair | `raspagem-optout` | DND em todos os canais |")
w("| Sem resposta após o dia 7 | `raspagem-sem-resposta` | — |\n")
w("**Não remova** as tags `raspagem`, `raspagem-onda2` e `raspagem-onda2-qua/qui/sex`. Elas medem o resultado da ação.\n")
w("## 9. Lista de contatos por dia\n")
w("Coluna **Mín.**: pedido mínimo CIF. **Frete +8%** na observação indica praça com adicional (usar versão B).\n")
for dia, nome, d0, f3, f7 in cal:
    s = sorted([x for x in d if x["dia"] == dia], key=lambda x: (x["canal"] != "whatsapp", x["regiao"], x["cidade"]))
    w(f"### {nome} · tag `raspagem-onda2-{dia}` ({sum(x['canal']=='whatsapp' for x in s)} WhatsApp + {sum(x['canal']=='email' for x in s)} e-mail)\n")
    w("| # | Empresa | Cidade | Praça | Canal | Mín. | Observação |\n|---|---|---|---|---|---|---|")
    for i, x in enumerate(s, 1):
        w(f"| {i} | {nome_ghl[x['base']]} | {x['cidade']} | {x['regiao']} | {canal_txt[x['canal']]} | {brl(x['minimo'])} | {obs(x)} |")
    w("")
w(f"## 10. Relatório ao final da ação ({fmt(rel)})\n")
w("Mandar para o Marketing, separado por lote (qua/qui/sex):")
w("- total enviado por canal;")
w("- respostas, qualificados, sem interesse, fora do perfil, contato inválido e opt-out (contagem por tag);")
w("- lista dos qualificados com nome do comprador, marcas que trabalha e próximo passo.\n")
w("## 11. Cuidados (LGPD e reputação)\n")
w("- É prospecção B2B para contato comercial da empresa, com base em dado público (Receita Federal). Sempre ofereça a opção de sair e respeite na hora.")
w("- Não peça CPF nem dados pessoais. Pergunte só nome e cargo de quem compra.")
w("- Se perguntarem de onde veio o contato: \"encontramos a empresa no cadastro público de CNPJ como distribuidora da região\".")
open(out_md, "w").write("\n".join(L) + "\n")

import csv
with open(out_csv, "w", newline="") as f:
    cw = csv.writer(f)
    cw.writerow(["dia", "data", "ghl_contact_id", "cnpj", "empresa", "razao_social", "cidade", "praca", "frete_cif", "pedido_minimo", "canal", "whatsapp", "telefone_fixo", "email", "observacao"])
    for x in sorted(d, key=lambda x: (x["data"], x["canal"] != "whatsapp", nome_ghl[x["base"]])):
        cw.writerow([x["dia"], x["data"], ids[x["base"]], x["cnpj"], nome_ghl[x["base"]], x["razao"], x["cidade"], x["regiao"], x["cif"], x["minimo"], x["canal"], x["cel"] or "", x["fixo"] or "", x["mail"] or "", obs(x)])
print("ok", [(c[0], fmt(c[3]), fmt(c[4])) for c in cal], fmt(rel))
