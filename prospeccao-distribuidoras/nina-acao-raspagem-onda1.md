# Ação Nina: prospecção de distribuidoras (raspagem, onda 1)

**Para:** Nina (agente de IA da Nitron no GHL)
**Ação:** primeiro contato com distribuidoras que nunca compraram da Nitron
**Público:** contatos com a tag `raspagem-onda1` (29 cadastros, criados em 27/10/2026)
**Dono da ação:** Marketing Nitron

---

## 1. Objetivo

Abrir conversa com distribuidoras e atacados de utilidades domésticas do interior de SP que **nunca compraram da Nitron** e levar as interessadas até o envio da **tabela de distribuidor** e o cadastro.

A meta desta ação é a **conversa qualificada**, não fechar pedido. Preço, prazo e pedido ficam com uma pessoa do time comercial (ver seção 7).

## 2. Quem são esses contatos (importante)

- **Não são lojistas.** São **distribuidores/atacadistas**: compram em volume e revendem para lojas, bazares e mercados da região. Não use o roteiro de anúncio ("Sua loja está preparada para não perder vendas?").
- Vieram da **base pública de CNPJ da Receita Federal**, não de anúncio. **Nunca falaram com a Nitron**, então é um contato frio.
- Os dados de contato são os **declarados na Receita**. Podem estar desatualizados ou ser de um funcionário administrativo (fiscal, financeiro). Quem atende pode não ser o comprador.
- O campo **"Informações para AI"** de cada contato tem o resumo da empresa (cidade, região, tempo de empresa e observações). **Leia antes de cada contato.**

## 3. Regras de canal (uma mensagem por contato no primeiro envio)

| Situação do contato | Canal | Contatos |
|---|---|---|
| Campo **WhatsApp** preenchido (celular) | **WhatsApp**, usando template aprovado | 4 |
| Sem WhatsApp, **com e-mail** | **E-mail** | 18 |
| Sem WhatsApp e sem e-mail | **Não enviar.** Criar tarefa de ligação para o time | 7 |

- **Nunca mande WhatsApp para o campo Telefone** quando o campo WhatsApp estiver vazio. São números **fixos** e a mensagem não chega.
- Contato com **DND ativo** ou tag `raspagem-optout`: não enviar nada.
- Enviar só em **dia útil, das 9h às 17h** (horário de Brasília).

### Contatos em espera (não enviar até liberação)

Estes 3 ficam na **Região Central SP**, área da **Modenuti**, a maior distribuidora da Nitron. Só envie depois que o vendedor **Sebastião** liberar. Para liberar, remover este bloco.

- Favorito Atacado (Araraquara)
- Prado Produtos Nacionais e Importados (Matão)
- J. J. Distribuidora Araraquara (Araraquara)

## 4. Mensagens do primeiro contato

Variáveis do GHL: `{{contact.company_name}}` (razão social), `{{contact.city}}` (cidade) e `{{contact.praca}}` (região de entrega).

**Pedido mínimo CIF**, conforme o campo Praça:
- **R$ 3.570** em `Extremo de Campinas` e `Extremo de Sorocaba`
- **R$ 2.500** em todas as outras praças desta lista

### 4.1 WhatsApp (dentro do template aprovado)

> Olá! Aqui é a Nina, da Nitron, fabricante de potes, organizadores e utilidades domésticas. Estamos buscando distribuidores em {{contact.city}} e a {{contact.company_name}} chamou nossa atenção. Posso te enviar nossa condição para distribuidor? O frete é CIF sem adicional para a sua cidade.

Se o template aprovado tiver outro texto, use o template e mantenha a ideia: quem somos, por que estamos falando com eles e a pergunta final.

### 4.2 E-mail

**Assunto:** Nitron: condição para distribuidores em {{contact.city}}

> Olá, tudo bem?
>
> Aqui é a Nina, da Nitron, fabricante de potes, organizadores, lixeiras e utilidades plásticas.
>
> Estamos ampliando nossa rede de distribuidores no interior de SP e a {{contact.company_name}} chamou nossa atenção como distribuidora de utilidades em {{contact.city}}.
>
> - Frete CIF **sem adicional** para {{contact.city}} (pedido mínimo de R$ [2.500 ou 3.570, conforme a praça])
> - Tabela específica para distribuidor
> - Organização e Potes são as linhas que mais giram nas distribuidoras da região
>
> Posso te enviar a tabela e o catálogo? Se não for com você, pode me indicar quem cuida das compras?
>
> Nina · Nitron
> [WhatsApp comercial]
>
> *Se não quiser receber nossos contatos, é só responder "sair".*

## 5. Acompanhamento (se não houver resposta)

| Quando | Canal | Mensagem |
|---|---|---|
| Dia 0 | Canal da seção 3 | Primeiro contato (seção 4) |
| Dia 3 útil | Mesmo canal | "Oi! Passando para saber se faz sentido te enviar nossa condição para distribuidor em {{contact.city}}. Se não for com você, me indica quem cuida das compras?" |
| Dia 7 útil | Mesmo canal | "Última mensagem por aqui: se em algum momento quiser conhecer a linha Nitron para distribuidor, é só responder. Obrigada!" e encerrar |

- **Parar a sequência assim que houver qualquer resposta.**
- No máximo **3 mensagens** por contato nesta ação.
- Sem resposta depois do dia 7: aplicar a tag `raspagem-sem-resposta` e criar tarefa de ligação para o time.

## 6. Como conduzir quando responderem

**Objetivo da conversa:** descobrir se é distribuidor de verdade, quem é o comprador e se há interesse em receber a tabela.

Perguntas de qualificação (uma por vez, sem interrogatório):
1. Vocês distribuem utilidades domésticas para lojas e mercados da região?
2. Quais marcas trabalham hoje nessa linha?
3. Quais cidades vocês atendem?
4. Quem decide as compras? (nome e cargo)
5. Qual o melhor contato direto dessa pessoa? (WhatsApp ou e-mail)

**Pode falar:**
- A Nitron é fabricante de potes, organizadores, lixeiras, linha cozinha, banheiro e frasqueiras.
- Frete CIF sem adicional para a cidade deles e o pedido mínimo da seção 4.
- Existe tabela específica para distribuidor, que o time comercial envia.

**Não pode:**
- Informar preço, desconto, prazo de pagamento ou prazo de entrega. Diga que o time comercial envia junto com a tabela.
- Prometer exclusividade de região.
- Citar outros clientes da Nitron pelo nome (Modenuti, Millenium etc.).
- Insistir depois de um "não".

**Respostas prontas:**
- *"Já temos fornecedor."* → "Entendo! Muitas distribuidoras trabalham com mais de uma marca para completar o mix. Posso te mandar a tabela só para comparar?"
- *"Manda por e-mail."* → Pedir o e-mail do comprador, registrar no contato e passar para o time (seção 7).
- *"Quanto custa?"* → "Os preços dependem do mix e do volume. Vou pedir para o nosso comercial te enviar a tabela de distribuidor. Qual o melhor contato para isso?"
- *"Somos fábrica / não somos distribuidor."* → Agradecer, encerrar e aplicar a tag `raspagem-fora-do-perfil`.
- *"Sair" / "não quero receber".* → Confirmar o descadastro, ativar DND em todos os canais, aplicar a tag `raspagem-optout` e encerrar.

## 7. Quando passar para uma pessoa do time

Passar a conversa (atribuir ao responsável e criar tarefa) quando:
- pedirem tabela, preço, catálogo ou condição de pagamento;
- quiserem fazer pedido ou cadastro;
- o comprador for identificado e topar receber contato;
- qualquer contato da **Região Central SP** responder (avisar o **Sebastião**);
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

**Não remova** as tags `raspagem` e `raspagem-onda1`. Elas são usadas para medir o resultado da ação.

## 9. Lista de contatos desta ação

| # | Empresa | Cidade | Praça | Canal | Observação |
|---|---|---|---|---|---|
| 1 | Metaltru Distribuidora de UD | Porto Feliz | Região de Sorocaba | E-mail | |
| 2 | Marcamix (Utilidades Gourmet) | Jundiaí | Campinas e Região | E-mail | Pode ter marca própria (possível concorrente): confirmar se revende outras marcas |
| 3 | Apajo Distribuidora de UD | Valinhos | Campinas e Região | Tarefa de ligação | Só telefone fixo |
| 4 | Atacadão Montebello | Piracicaba | Campinas e Região | E-mail | |
| 5 | Distribuidora Minutti | Itapetininga | Extremo de Sorocaba | E-mail | Mínimo R$ 3.570 |
| 6 | G5S Comercial e Distribuidora | Piracaia | Campinas e Região | Tarefa de ligação | Só telefone fixo |
| 7 | Daterra Distribuidora de UD | Pereiras | Extremo de Sorocaba | E-mail | Mínimo R$ 3.570 |
| 8 | Grupo Zapala | Vinhedo | Campinas e Região | E-mail | |
| 9 | Tracionar Comércio de Utilidades | Mairinque | Região de Sorocaba | Tarefa de ligação | Só telefone fixo |
| 10 | MPlastic Store Distribuidora | Salto | Região de Sorocaba | E-mail | |
| 11 | Livale Distribuidora | São José dos Campos | Região de S.J Campos | Tarefa de ligação | Só telefone fixo |
| 12 | Fagundes e Fagundes Distribuidora | Indaiatuba | Campinas e Região | E-mail | Telefone da Receita inválido |
| 13 | IBAS Utensílios de Limpeza | Mairinque | Região de Sorocaba | **WhatsApp** | |
| 14 | Marília de Oliveira UD | Pedreira | Campinas e Região | E-mail | Pedreira é polo de fábricas: confirmar se revende ou fabrica |
| 15 | Maralar Distribuidora de UD | Iracemápolis | Extremo de Campinas | E-mail | Mínimo R$ 3.570. Já teve cadastro na Nitron (2022) e nunca comprou: perguntar o que faltou |
| 16 | Kako Atacado | São José dos Campos | Região de S.J Campos | E-mail | |
| 17 | Tukano UD Import | Rio Claro | Extremo de Campinas | Tarefa de ligação | Só telefone fixo |
| 18 | Jota Reis Atacado de Utilidades | Caçapava | Região de S.J Campos | **WhatsApp** | |
| 19 | Distribuidora Bressan | Pedreira | Campinas e Região | E-mail | Telefone da Receita inválido |
| 20 | J. J. Distribuidora Araraquara | Araraquara | Região Central SP | **Em espera** | Sem telefone e e-mail. Área da Modenuti |
| 21 | Du Lar Americana UD | Americana | Extremo de Campinas | E-mail | Mínimo R$ 3.570 |
| 22 | Vilar Utensílios | São Roque | Região de Sorocaba | **WhatsApp** | |
| 23 | Rema Utilidades | Sorocaba | Região de Sorocaba | E-mail | |
| 24 | Distribuidora Guimarães | Sorocaba | Região de Sorocaba | E-mail | |
| 25 | JP Artioli Distribuidora | Campinas | Campinas e Região | Tarefa de ligação | Só telefone fixo |
| 26 | Rede Bom Lugar (central de distribuição) | Sorocaba | Região de Sorocaba | E-mail | Já teve cadastro na Nitron (2023) e nunca comprou: perguntar o que faltou |
| 27 | Prado Produtos Nacionais e Importados | Matão | Região Central SP | **Em espera** | Área da Modenuti |
| 28 | Distribuidora Maestral | Jundiaí | Campinas e Região | E-mail | O e-mail é do fiscal: pedir o contato do comprador |
| 29 | Favorito Atacado | Araraquara | Região Central SP | **Em espera** (WhatsApp) | Área da Modenuti |

**Resumo:** 3 WhatsApp + 17 e-mails liberados para envio · 6 tarefas de ligação · 3 em espera (1 WhatsApp, 1 e-mail, 1 sem contato).

## 10. Relatório ao final da ação (dia 10)

Mandar para o Marketing:
- total enviado por canal;
- respostas, qualificados, sem interesse, fora do perfil, contato inválido e opt-out (contagem por tag);
- lista dos qualificados com nome do comprador, marcas que trabalha e próximo passo.

## 11. Cuidados (LGPD e reputação)

- É prospecção B2B para contato comercial da empresa, com base em dado público (Receita Federal). Sempre ofereça a opção de sair e respeite na hora.
- Não peça CPF nem dados pessoais. Pergunte só nome e cargo de quem compra.
- Se alguém perguntar de onde veio o contato, responda com transparência: "encontramos a empresa no cadastro público de CNPJ como distribuidora de utilidades da região".
