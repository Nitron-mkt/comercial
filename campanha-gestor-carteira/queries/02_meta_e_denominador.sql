-- Achado 2: meta chapada e denominador contaminado.
-- 34 reps com cadastro ativo, meta somada de R$ 3,82 mi e faturamento zero em 8 meses.
WITH MET AS (
  SELECT M.CODVEND, SUM(M.PREVREC) META FROM TGMMET M
   WHERE M.DTREF >= DATE '2026-01-01' AND M.DTREF < DATE '2026-09-01' GROUP BY M.CODVEND
), FAT AS (
  SELECT N.CODVEND, SUM(N.VALOR_NOTA) FAT FROM AD_VW_COM_NOTAS N
   WHERE N.DATA >= DATE '2026-01-01' AND N.DATA < DATE '2026-09-01' GROUP BY N.CODVEND
), R AS (
  SELECT V.CODVEND, V.APELIDO, NVL(MET.META,0) META, NVL(FAT.FAT,0) FAT
    FROM TGFVEN V
    LEFT JOIN MET ON MET.CODVEND = V.CODVEND
    LEFT JOIN FAT ON FAT.CODVEND = V.CODVEND
   WHERE V.TIPVEND='R' AND V.ATIVO='S' AND V.CODVEND <> 137
)
SELECT CASE WHEN FAT = 0       THEN 'A. sem faturamento'
            WHEN FAT < 100000  THEN 'B. < 100k'
            WHEN FAT < 500000  THEN 'C. 100k-500k'
            WHEN FAT < 1000000 THEN 'D. 500k-1mi'
            ELSE                    'E. > 1mi' END FAIXA,
       COUNT(*) REPS,
       ROUND(SUM(META)/1000000,2) META_MI,
       ROUND(SUM(FAT)/1000000,2)  FAT_MI,
       ROUND(SUM(FAT)/NULLIF(SUM(META),0)*100,1) PCT_ATINGIMENTO
  FROM R
 GROUP BY CASE WHEN FAT = 0       THEN 'A. sem faturamento'
               WHEN FAT < 100000  THEN 'B. < 100k'
               WHEN FAT < 500000  THEN 'C. 100k-500k'
               WHEN FAT < 1000000 THEN 'D. 500k-1mi'
               ELSE                    'E. > 1mi' END
 ORDER BY 1;
