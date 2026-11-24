import json,sys,unicodedata,re
src,out=sys.argv[1],sys.argv[2]
d=json.load(open(src))
def norm(s): return unicodedata.normalize('NFKD',s or '').encode('ascii','ignore').decode().upper()
ZL=['VL MATILDE','VL GUILHERMINA','NHOCUNE','ITAQUERA','AGUA RASA','TATUAPE','SAO MIGUEL','TIRADENTES','PENHA','GUAIANASES','ERMELINO','ARICANDUVA','SAPOPEMBA','MOOCA']
ZN=['SANTANA','CASA VERDE','TUCURUVI','VL MARIA','JACANA','BRASILANDIA','FREGUESIA','CACHOEIRINHA','PIRITUBA']
OUT=['PINHEIROS','PERDIZES','MOEMA','BUTANTA','CAPAO','ITAIM BIBI','CAMPO BELO','LAPA','IPIRANGA','CURSINO','LEOPOLDIN','SAO BENTO','JD ANGELA','BROOKLYN','IBIRAPUERA','CANINDE']
rows=[]
for r in d['rows']:
    n=norm(r['LOJA']); cid=norm(r['CIDADE'])
    if cid=='SAO PAULO':
        z='A confirmar'
        if any(k in n for k in ZL): z='Zona Leste'
        elif any(k in n for k in ZN): z='Zona Norte'
        elif any(k in n for k in OUT): z='Fora da rota'
    else: z={'MOGI DAS CRUZES':'Mogi das Cruzes','GUARULHOS':'Guarulhos','ITAQUAQUECETUBA':'Itaquaquecetuba','SUZANO':'Suzano','ARUJA':'Arujá'}[cid]
    f12,f12a,f6=r['F12'],r['F12A'],r['F6']
    var=(f12/f12a-1) if f12a else None
    if f6==0 and f12a>=8: c='Reativar'
    elif f12>=20 and (var is None or var>=-0.10): c='Manter e crescer'
    elif f12>=10 and var is not None and var>=0.30: c='Em alta'
    elif f12a>=15 and var is not None and var<-0.20: c='Recuperar'
    else: c='Acompanhar'
    pot=max(f12,f12a)
    rows.append(dict(cod=r['COD'],loja=r['LOJA'].strip(),cnpj=r['CNPJ'],matriz=(r['MATRIZ'] or '').strip(),lojas=r['LOJAS'],ka=r['KA'],rep=r['REP'].title().replace('Gravinez','Gravinez'),cidade=r['CIDADE'].replace('Aruja','Arujá'),zona=z,f12=f12,f12a=f12a,f6=f6,meses=r['M'],ult=r['ULT'],classe=c,pot=pot))
rows.sort(key=lambda x:-x['pot'])
for i,x in enumerate(rows): x['onda1']= x['zona']!='Fora da rota' and x['classe']!='Acompanhar' and x['pot']>=20
json.dump(rows,open(out,'w'),ensure_ascii=False,separators=(',',':'))
from collections import Counter
print(len(rows)); print(Counter(x['zona'] for x in rows)); print(Counter(x['classe'] for x in rows))
print('onda1',sum(x['onda1'] for x in rows), Counter((x['rep'],x['zona']) for x in rows if x['onda1']))
print(Counter(x['classe'] for x in rows if x['onda1']))
