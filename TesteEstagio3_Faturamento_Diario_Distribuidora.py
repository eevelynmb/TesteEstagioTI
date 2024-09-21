#3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
#• O menor valor de faturamento ocorrido em um dia do mês;
#• O maior valor de faturamento ocorrido em um dia do mês;
#• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

#--------------------------------------------------------------------------------------------------------------------------------------------------------

def analise_faturamento(faturamento_diario):

    faturamento_valido = [f for f in faturamento_diario if f >0]

    menor_faturamento = min (faturamento_valido)
    maior_faturamento = max (faturamento_valido)

    media_mensal = sum (faturamento_valido) / len (faturamento_valido)

    dias_acima_media = sum(1 for f in faturamento_diario if f  > media_mensal)
    
    return menor_faturamento, maior_faturamento, dias_acima_media

faturamento_diario = [
        1500,2300,0,1200,2500,2000,0,1750,3000,3200,0,2150,2900,
        4000,1500,1000,0,0,1800,900,2500,2700,1500,3100,3500,
        0,2900,2600,3400,0
]

resultado = analise_faturamento(faturamento_diario)

print(f"Menor valor de faturamento: {resultado[0]}")
print (f"Maior valor de faturamento: {resultado[1]}")
print(f"Número de dias acima da média: {resultado[2]}")

