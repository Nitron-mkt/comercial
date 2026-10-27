# Ação Nina: prospecção de distribuidoras (raspagem, onda 2)

**Para:** Nina (agente de IA da Nitron no GHL)  
**Ação:** primeiro contato com 90 distribuidoras que nunca compraram da Nitron, 30 por dia  
**Público:** tags `raspagem-onda2-qua`, `raspagem-onda2-qui` e `raspagem-onda2-sex` (90 cadastros criados em 27/10/2026)  
**Dono da ação:** Marketing Nitron

---

## 0. Agenda de envio

| Lote | Tag do lote | Primeiro contato | Contatos | WhatsApp | E-mail | 1º follow-up (dia 3 útil) | 2º follow-up (dia 7 útil) |
|---|---|---|---|---|---|---|---|
| Quarta 28/10 | `raspagem-onda2-qua` | 28/10 | 30 | 11 | 19 | 03/11 | 09/11 |
| Quinta 29/10 | `raspagem-onda2-qui` | 29/10 | 30 | 11 | 19 | 04/11 | 10/11 |
| Sexta 30/10 | `raspagem-onda2-sex` | 30/10 | 30 | 11 | 19 | 05/11 | 11/11 |

- **Envie cada lote só no seu dia.** Não antecipe o lote de quinta ou sexta.
- **02/11 (segunda) é feriado de Finados:** não envie nada e não conte como dia útil. As datas de follow-up acima já consideram isso.
- Envio em **dia útil, das 9h às 17h** (horário de Brasília). Espalhe os envios ao longo do dia (não dispare os 30 no mesmo minuto).

## 1. Objetivo

Abrir conversa com distribuidoras e atacados do interior de SP que **nunca compraram da Nitron** e levar as interessadas até o envio da **tabela de distribuidor** e o cadastro.

A meta é a **conversa qualificada**, não fechar pedido. Preço, prazo e pedido ficam com uma pessoa do time comercial (seção 7).

## 2. Quem são esses contatos (importante)

- **Não são lojistas.** São **distribuidores/atacadistas** de utilidades domésticas, embalagens, descartáveis, produtos de limpeza e armarinhos: compram em volume e revendem para lojas, bazares e mercados. Não use o roteiro de anúncio para lojista.
- Vieram da **base pública de CNPJ da Receita Federal**. **Nunca falaram com a Nitron**: é contato frio.
- Muitos são distribuidores de **embalagens e descartáveis** ou de **limpeza**. Para eles, o gancho é **completar o mix** com potes, organizadores, lixeiras e utilidades plásticas.
- Os contatos são os **declarados na Receita**. Muitos e-mails são do financeiro ou fiscal. Quem responde pode não ser o comprador: sempre peça o contato de quem compra.
- O campo **"Informações para AI"** de cada contato traz cidade, região, frete, pedido mínimo, tempo de empresa e observações. **Leia antes de cada contato.**
- 3 contatos **já têm cadastro antigo na Nitron** e não compram há mais de 24 meses (Du Chapéu, JFZ e JN Distribuidora). Com eles, a abordagem é: "vocês já foram nossos clientes; o que faltou para voltarem a comprar?".

## 3. Regras de canal (uma mensagem por contato no primeiro envio)

| Situação do contato | Canal | Contatos |
|---|---|---|
| Campo **WhatsApp** preenchido (celular) | **WhatsApp**, usando template aprovado | 33 (11 por dia) |
| Sem WhatsApp, **com e-mail** | **E-mail** | 57 (19 por dia) |

- **Nunca mande WhatsApp para o campo Telefone** quando o campo WhatsApp estiver vazio: são números **fixos** e a mensagem não chega.
- Os 33 contatos de WhatsApp também têm e-mail cadastrado. **Não mande os dois no primeiro contato.** O e-mail só entra se o WhatsApp falhar (número inválido ou não entregue): nesse caso aplique `raspagem-contato-invalido` ao número e envie o e-mail no mesmo dia.
- Contato com **DND ativo** ou tag `raspagem-optout`: não enviar nada.
- Nenhum contato desta onda está na **Região Central SP** (área da Modenuti). Se aparecer algum, **não envie** e avise o Marketing.

## 4. Mensagens do primeiro contato

Variáveis do GHL: `{{contact.company_name}}` (razão social), `{{contact.city}}` (cidade) e `{{contact.praca}}` (região de entrega).

### Frete e pedido mínimo: confira o campo Praça antes de escrever

| Praça (campo Praça) | Frete CIF | Pedido mínimo CIF | Contatos |
|---|---|---|---|
| Campinas e Região, Região de Sorocaba, Região de S.J Campos | **sem adicional** | R$ 2.500 | 46 |
| Extremo de Campinas, Extremo de Sorocaba | **sem adicional** | R$ 3.570 | 17 |
| Região S.J.R. Preto, Rib. Preto, Bauru, Marília, Barretos, Franca | **com adicional de 8%** | R$ 3.570 | 27 |

> **Atenção:** nas praças com adicional de 8%, **nunca escreva "frete sem adicional"**. Use a versão B das mensagens.

### 4.1 WhatsApp (dentro do template aprovado)

**Versão A (frete sem adicional):**

> Olá! Aqui é a Nina, da Nitron, fabricante de potes, organizadores e utilidades domésticas. Estamos buscando distribuidores em {{contact.city}} e a {{contact.company_name}} chamou nossa atenção. Posso te enviar nossa condição para distribuidor? O frete é CIF sem adicional para a sua cidade.

**Versão B (praças com 8%):**

> Olá! Aqui é a Nina, da Nitron, fabricante de potes, organizadores e utilidades domésticas. Estamos buscando distribuidores em {{contact.city}} e a {{contact.company_name}} chamou nossa atenção. Posso te enviar nossa condição para distribuidor? Entregamos com frete CIF na sua região.

Se o template aprovado tiver outro texto, use o template e mantenha a ideia: quem somos, por que estamos falando com eles e a pergunta final.

### 4.2 E-mail

**Assunto:** Nitron: condição para distribuidores em {{contact.city}}

> Olá, tudo bem?
>
> Aqui é a Nina, da Nitron, fabricante de potes, organizadores, lixeiras e utilidades plásticas.
>
> Estamos ampliando nossa rede de distribuidores no interior de SP e a {{contact.company_name}} chamou nossa atenção como distribuidora em {{contact.city}}.
>
> - **[Versão A]** Frete CIF **sem adicional** para {{contact.city}}, pedido mínimo de R$ [2.500 ou 3.570, conforme a tabela acima]
>   **[Versão B]** Frete CIF para {{contact.city}}, pedido mínimo de R$ 3.570
> - Tabela específica para distribuidor
> - Linha que completa o mix de quem já vende embalagens, descartáveis, limpeza ou utilidades: potes, organizadores, lixeiras, cozinha e banheiro
>
> Posso te enviar a tabela e o catálogo? Se não for com você, pode me indicar quem cuida das compras?
>
> Nina · Nitron  
> [WhatsApp comercial]
>
> *Se não quiser receber nossos contatos, é só responder "sair".*

Envie só uma das versões (A ou B). Nunca deixe os colchetes no texto enviado.

## 5. Acompanhamento (se não houver resposta)

| Quando | Canal | Mensagem |
|---|---|---|
| Dia 0 | Canal da seção 3 | Primeiro contato (seção 4) |
| Dia 3 útil | Mesmo canal | "Oi! Passando para saber se faz sentido te enviar nossa condição para distribuidor em {{contact.city}}. Se não for com você, me indica quem cuida das compras?" |
| Dia 7 útil | Mesmo canal | "Última mensagem por aqui: se em algum momento quiser conhecer a linha Nitron para distribuidor, é só responder. Obrigada!" e encerrar |

- As datas de cada lote estão na seção 0.
- **Parar a sequência assim que houver qualquer resposta.** No máximo **3 mensagens** por contato.
- Sem resposta depois do dia 7: aplicar `raspagem-sem-resposta` e criar tarefa de ligação para o time (usar o campo Telefone).

## 6. Como conduzir quando responderem

**Objetivo da conversa:** descobrir se é distribuidor de verdade, quem é o comprador e se há interesse em receber a tabela.

Perguntas de qualificação (uma por vez, sem interrogatório):
1. Vocês revendem para lojas, mercados e bazares da região?
2. Quais linhas e marcas trabalham hoje (utilidades, embalagens, limpeza)?
3. Quais cidades vocês atendem?
4. Quem decide as compras? (nome e cargo)
5. Qual o melhor contato direto dessa pessoa? (WhatsApp ou e-mail)

**Pode falar:**
- A Nitron é fabricante de potes, organizadores, lixeiras, linha cozinha, banheiro e frasqueiras.
- O frete e o pedido mínimo da praça do contato (seção 4).
- Existe tabela específica para distribuidor, que o time comercial envia.

**Não pode:**
- Informar preço, desconto, prazo de pagamento ou prazo de entrega. Diga que o time comercial envia junto com a tabela.
- Dizer "frete sem adicional" para praças com 8%.
- Prometer exclusividade de região.
- Citar outros clientes da Nitron pelo nome.
- Insistir depois de um "não".

**Respostas prontas:**
- *"Já temos fornecedor."* → "Entendo! Muitas distribuidoras trabalham com mais de uma marca para completar o mix. Posso te mandar a tabela só para comparar?"
- *"Só trabalhamos com embalagem / limpeza."* → "Faz sentido! Vários distribuidores desse segmento usam a linha Nitron para completar o mix com os mesmos clientes. Posso te mandar a tabela para avaliar?"
- *"Manda por e-mail."* → Pedir o e-mail do comprador, registrar no contato e passar para o time (seção 7).
- *"Quanto custa?"* → "Os preços dependem do mix e do volume. Vou pedir para o nosso comercial te enviar a tabela de distribuidor. Qual o melhor contato para isso?"
- *"Já compramos de vocês" (Du Chapéu, JFZ, JN).* → "Que bom! Vi que faz um tempo que não compram. O que faltou? Quero entender para te mandar uma condição melhor." e passar para o time.
- *"Somos fábrica / supermercado / não revendemos."* → Agradecer, encerrar e aplicar `raspagem-fora-do-perfil`.
- *"Sair" / "não quero receber".* → Confirmar o descadastro, ativar DND em todos os canais, aplicar `raspagem-optout` e encerrar.

## 7. Quando passar para uma pessoa do time

Passar a conversa (atribuir ao responsável e criar tarefa) quando:
- pedirem tabela, preço, catálogo ou condição de pagamento;
- quiserem fazer pedido ou cadastro;
- o comprador for identificado e topar receber contato;
- responderem Du Chapéu, JFZ ou JN (clientes antigos);
- houver reclamação ou dúvida que você não saiba responder.

Na passagem, escrever em **Comentario** um resumo de 2 linhas: quem respondeu, o que quer e as marcas que trabalha.

## 8. Tags e campos de resultado

| Situação | Tag | Atualizar campo |
|---|---|---|
| Qualquer resposta | `raspagem-respondeu` | — |
| Distribuidor e quer receber tabela | `raspagem-qualificado` | Cargo (Comprador/Proprietário), Comentario |
| Não tem interesse | `raspagem-sem-interesse` | Comentario com o motivo |
| Não é distribuidor / é fábrica | `raspagem-fora-do-perfil` | Comentario |
| Número ou e-mail errado | `raspagem-contato-invalido` | — |
| Pediu para sair | `raspagem-optout` | DND em todos os canais |
| Sem resposta após o dia 7 | `raspagem-sem-resposta` | — |

**Não remova** as tags `raspagem`, `raspagem-onda2` e `raspagem-onda2-qua/qui/sex`. Elas medem o resultado da ação.

## 9. Lista de contatos por dia

Coluna **Mín.**: pedido mínimo CIF. **Frete +8%** na observação indica praça com adicional (usar versão B).

### Quarta 28/10 · tag `raspagem-onda2-qua` (11 WhatsApp + 19 e-mail)

| # | Empresa | Cidade | Praça | Canal | Mín. | Observação |
|---|---|---|---|---|---|---|
| 1 | Purificar | Itatiba | Campinas e Região | **WhatsApp** | 2.500 |  |
| 2 | Gois De Lima Comercio Atacadista | Piracicaba | Campinas e Região | **WhatsApp** | 2.500 |  |
| 3 | Zeno Comercial Atacadista De Embalagens | Engenheiro Coelho | Extremo de Campinas | **WhatsApp** | 3.570 |  |
| 4 | Finamore | Limeira | Extremo de Campinas | **WhatsApp** | 3.570 |  |
| 5 | Rover Distribuidora De Embalagens | Rio Claro | Extremo de Campinas | **WhatsApp** | 3.570 |  |
| 6 | Mega Plas Sacos Plasticos Em Geral | Catanduva | Região S.J.R. Preto | **WhatsApp** | 3.570 | Frete +8% |
| 7 | Avanco Produtos Praticos | Sao Jose Do Rio Preto | Região S.J.R. Preto | **WhatsApp** | 3.570 | Frete +8%. E-mail da Receita é de outro domínio: confirmar o contato do comprador |
| 8 | Miracom - Distribuidora De Utilidades Domesticas | Bauru | Região de Bauru | **WhatsApp** | 3.570 | Frete +8% |
| 9 | Inter Atacadista | Ribeirao Preto | Região de Rib. Preto | **WhatsApp** | 3.570 | Frete +8% |
| 10 | Tda Distribuidora Acessorios E Descartaveis | Sao Jose Dos Campos | Região de S.J Campos | **WhatsApp** | 2.500 |  |
| 11 | Clean Express | Tremembe | Região de S.J Campos | **WhatsApp** | 2.500 |  |
| 12 | Clean Up | Braganca Paulista | Campinas e Região | E-mail | 2.500 |  |
| 13 | Natocamp | Campinas | Campinas e Região | E-mail | 2.500 |  |
| 14 | Prestes-Maia Embalagens | Campinas | Campinas e Região | E-mail | 2.500 | E-mail é do financeiro/adm: pedir o contato do comprador |
| 15 | Spilpack | Campinas | Campinas e Região | E-mail | 2.500 |  |
| 16 | New Star Embalagens | Campinas | Campinas e Região | E-mail | 2.500 | E-mail é do financeiro/adm: pedir o contato do comprador |
| 17 | Renova Imports E Distribuidora | Campo Limpo Paulista | Campinas e Região | E-mail | 2.500 |  |
| 18 | Economisa Comercio E Distribuidora De Produtos Em Geral | Itupeva | Campinas e Região | E-mail | 2.500 |  |
| 19 | Infinite Home | Piracicaba | Campinas e Região | E-mail | 2.500 |  |
| 20 | Flex Plus Comercio De Plasticos | Valinhos | Campinas e Região | E-mail | 2.500 |  |
| 21 | Duratto | Americana | Extremo de Campinas | E-mail | 3.570 |  |
| 22 | Wg Distribuidora De Embalagens | Itobi | Extremo de Campinas | E-mail | 3.570 |  |
| 23 | Jfz Importacao E Distribuicao | Rio Claro | Extremo de Campinas | E-mail | 3.570 | Já tem cadastro na Nitron, sem compra nos últimos 24 meses: perguntar o que faltou |
| 24 | Armarinhos Filie | Sao Jose Do Rio Preto | Região S.J.R. Preto | E-mail | 3.570 | Frete +8% |
| 25 | Comercial Gaviao | Bebedouro | Região de Barretos | E-mail | 3.570 | Frete +8% |
| 26 | Silverio Distribuidora | Ituverava | Região de Franca | E-mail | 3.570 | Frete +8%. E-mail da Receita é de outro domínio: confirmar o contato do comprador |
| 27 | Glauber Atacadista | Sao Jose Dos Campos | Região de S.J Campos | E-mail | 2.500 |  |
| 28 | Scarcelli Logistica E Distribuicao | Avare | Região de Sorocaba | E-mail | 2.500 |  |
| 29 | Art Injet - Distribuidora | Salto | Região de Sorocaba | E-mail | 2.500 | E-mail é do financeiro/adm: pedir o contato do comprador |
| 30 | Total Qually Atacadista | Sorocaba | Região de Sorocaba | E-mail | 2.500 | E-mail é do financeiro/adm: pedir o contato do comprador |

### Quinta 29/10 · tag `raspagem-onda2-qui` (11 WhatsApp + 19 e-mail)

| # | Empresa | Cidade | Praça | Canal | Mín. | Observação |
|---|---|---|---|---|---|---|
| 1 | Vn Atacado E Varejo | Louveira | Campinas e Região | **WhatsApp** | 2.500 |  |
| 2 | Lov Comercio E Distribuicao | Piracicaba | Campinas e Região | **WhatsApp** | 2.500 |  |
| 3 | Atend Distribuidora | Tatui | Extremo de Sorocaba | **WhatsApp** | 3.570 |  |
| 4 | R. T. Distribuidora | Fernandopolis | Região S.J.R. Preto | **WhatsApp** | 3.570 | Frete +8% |
| 5 | Jn Distribuidora De Armarinhos | Bauru | Região de Bauru | **WhatsApp** | 3.570 | Frete +8%. Já tem cadastro na Nitron (JN Bauru), sem compra nos últimos 24 meses. Distribuidora de armarinhos |
| 6 | Ad & Ad Comercio | Bauru | Região de Bauru | **WhatsApp** | 3.570 | Frete +8%. E-mail é do financeiro/adm: pedir o contato do comprador |
| 7 | Distribuidora Arantes | Bauru | Região de Bauru | **WhatsApp** | 3.570 | Frete +8% |
| 8 | Ras Dist De Produtos De Higiene Limpeza E Descartaveis | Bauru | Região de Bauru | **WhatsApp** | 3.570 | Frete +8% |
| 9 | Nova Importadora E Distribuidora De Utilidades | Ribeirao Preto | Região de Rib. Preto | **WhatsApp** | 3.570 | Frete +8%. E-mail é do financeiro/adm: pedir o contato do comprador |
| 10 | Brtl Distribuicao E Comercio | Ribeirao Preto | Região de Rib. Preto | **WhatsApp** | 3.570 | Frete +8% |
| 11 | Limpa Maxx | Tremembe | Região de S.J Campos | **WhatsApp** | 2.500 |  |
| 12 | Atimil | Atibaia | Campinas e Região | E-mail | 2.500 |  |
| 13 | Almaplast | Campinas | Campinas e Região | E-mail | 2.500 |  |
| 14 | Madu Distribuidora E Comercio | Campinas | Campinas e Região | E-mail | 2.500 |  |
| 15 | Spumadist Distribuidora De Embalagens | Jundiai | Campinas e Região | E-mail | 2.500 |  |
| 16 | Deslimpex | Louveira | Campinas e Região | E-mail | 2.500 |  |
| 17 | Decor Home | Pedreira | Campinas e Região | E-mail | 2.500 |  |
| 18 | Bid Import | Piracicaba | Campinas e Região | E-mail | 2.500 | E-mail é do financeiro/adm: pedir o contato do comprador |
| 19 | Plastfen Embalagens Flexiveis Em Geral | Araras | Extremo de Campinas | E-mail | 3.570 |  |
| 20 | Fozbra Distribuidora De Pilhas | Mogi Mirim | Extremo de Campinas | E-mail | 3.570 |  |
| 21 | Granpel Embalagens | Nova Granada | Região S.J.R. Preto | E-mail | 3.570 | Frete +8% |
| 22 | Cristo Rei Comercial De Armarinhos | Sao Jose Do Rio Preto | Região S.J.R. Preto | E-mail | 3.570 | Frete +8%. E-mail é do fiscal: pedir o contato do comprador |
| 23 | Rodos Tanabi | Tanabi | Região S.J.R. Preto | E-mail | 3.570 | Frete +8% |
| 24 | West Sun | Santa Cruz Do Rio Pardo | Região de Marília | E-mail | 3.570 | Frete +8% |
| 25 | Campeao Distribuidora De Manufaturados | Taruma | Região de Marília | E-mail | 3.570 | Frete +8% |
| 26 | Cacola Distribuidora | Ribeirao Preto | Região de Rib. Preto | E-mail | 3.570 | Frete +8% |
| 27 | Quicklog Comercio Atacadista E Logistica | Igarata | Região de S.J Campos | E-mail | 2.500 |  |
| 28 | Plastroma | Lorena | Região de S.J Campos | E-mail | 2.500 |  |
| 29 | Du Chapeu Presentes | Sao Jose Dos Campos | Região de S.J Campos | E-mail | 2.500 | Já tem cadastro na Nitron, sem compra nos últimos 24 meses: perguntar o que faltou. E-mail é do financeiro/adm: pedir o contato do comprador |
| 30 | Lider Comercial | Sorocaba | Região de Sorocaba | E-mail | 2.500 |  |

### Sexta 30/10 · tag `raspagem-onda2-sex` (11 WhatsApp + 19 e-mail)

| # | Empresa | Cidade | Praça | Canal | Mín. | Observação |
|---|---|---|---|---|---|---|
| 1 | Embalaplast Comercial | Campinas | Campinas e Região | **WhatsApp** | 2.500 |  |
| 2 | Cultura Dab | Americana | Extremo de Campinas | **WhatsApp** | 3.570 |  |
| 3 | Sp Home Distribuidora | Americana | Extremo de Campinas | **WhatsApp** | 3.570 |  |
| 4 | Fortlux Atacadista | Mogi Mirim | Extremo de Campinas | **WhatsApp** | 3.570 |  |
| 5 | Js Comercio Atacadista E Varejista De Embalagens | Vargem Grande Do Sul | Extremo de Campinas | **WhatsApp** | 3.570 |  |
| 6 | Himerus Importadora E Distribuidora De Produtos Pessoais | Colina | Região de Barretos | **WhatsApp** | 3.570 | Frete +8% |
| 7 | Moyses, Loyolla & Cia Distribuidora De Produtos De Higiene | Agudos | Região de Bauru | **WhatsApp** | 3.570 | Frete +8% |
| 8 | Shogum Comercio E Distribuidora De Embalagens | Ribeirao Preto | Região de Rib. Preto | **WhatsApp** | 3.570 | Frete +8% |
| 9 | Comercial Diogo & Silva Embalagens | Sao Jose Dos Campos | Região de S.J Campos | **WhatsApp** | 2.500 | E-mail é do financeiro/adm: pedir o contato do comprador |
| 10 | Reino Lar | Ibiuna | Região de Sorocaba | **WhatsApp** | 2.500 |  |
| 11 | Dck Comercio Atacadista De Embalagens | Salto | Região de Sorocaba | **WhatsApp** | 2.500 |  |
| 12 | Fwm Distribuidora | Campinas | Campinas e Região | E-mail | 2.500 |  |
| 13 | Prolog Comercio E Distribuicao | Jundiai | Campinas e Região | E-mail | 2.500 |  |
| 14 | Pps Distribuicao E Comercio | Monte Mor | Campinas e Região | E-mail | 2.500 | Filial de distribuidora com matriz fora de SP (telefone DDD 47) |
| 15 | Lf Comercio E Distribuidora De Artigos Domesticos | Pedreira | Campinas e Região | E-mail | 2.500 |  |
| 16 | Neves | Casa Branca | Extremo de Campinas | E-mail | 3.570 |  |
| 17 | Str Importacoes | Santa Barbara D'Oeste | Extremo de Campinas | E-mail | 3.570 |  |
| 18 | Juni Embalagens | Santa Barbara D'Oeste | Extremo de Campinas | E-mail | 3.570 | E-mail é do fiscal: pedir o contato do comprador |
| 19 | Rio Pardo Distribuidora De Atacado | Sao Jose Do Rio Pardo | Extremo de Campinas | E-mail | 3.570 |  |
| 20 | Panamais | Catanduva | Região S.J.R. Preto | E-mail | 3.570 | Frete +8% |
| 21 | Rede Star | Pederneiras | Região de Bauru | E-mail | 3.570 | Frete +8%. Central de distribuição de rede de supermercados (Rede Star). E-mail é do financeiro/adm: pedir o contato do comprador |
| 22 | Delta Distribuidora Comercial | Marilia | Região de Marília | E-mail | 3.570 | Frete +8% |
| 23 | Distribuidora Faiana | Ribeirao Preto | Região de Rib. Preto | E-mail | 3.570 | Frete +8% |
| 24 | Plastic Atacado | Taubate | Região de S.J Campos | E-mail | 2.500 |  |
| 25 | Plan Comercio De Descartaveis Boituva | Boituva | Região de Sorocaba | E-mail | 2.500 | E-mail é do financeiro/adm: pedir o contato do comprador |
| 26 | G.D. Comercio De Produtos De Papelao E Plasticos | Porto Feliz | Região de Sorocaba | E-mail | 2.500 |  |
| 27 | Nobe Utensílios Domésticos | Sorocaba | Região de Sorocaba | E-mail | 2.500 |  |
| 28 | Jl Distribuidora De Embalagens E Descartaveis | Sorocaba | Região de Sorocaba | E-mail | 2.500 |  |
| 29 | Ag Distribuidora De Produtos Em Geral | Sorocaba | Região de Sorocaba | E-mail | 2.500 |  |
| 30 | Dsa Distribuidora De Produtos | Votorantim | Região de Sorocaba | E-mail | 2.500 |  |

## 10. Relatório ao final da ação (16/11)

Mandar para o Marketing, separado por lote (qua/qui/sex):
- total enviado por canal;
- respostas, qualificados, sem interesse, fora do perfil, contato inválido e opt-out (contagem por tag);
- lista dos qualificados com nome do comprador, marcas que trabalha e próximo passo.

## 11. Cuidados (LGPD e reputação)

- É prospecção B2B para contato comercial da empresa, com base em dado público (Receita Federal). Sempre ofereça a opção de sair e respeite na hora.
- Não peça CPF nem dados pessoais. Pergunte só nome e cargo de quem compra.
- Se perguntarem de onde veio o contato: "encontramos a empresa no cadastro público de CNPJ como distribuidora da região".
