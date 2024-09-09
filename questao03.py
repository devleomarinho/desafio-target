# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem
# que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

import json

with open('dados.json', 'r') as file:
    dados = json.load(file)


faturamentos = [dia['valor'] for dia in dados if dia['valor'] > 0]

menor_faturamento = min(faturamentos)
maior_faturamento = max(faturamentos)

soma_faturamentos = sum(faturamentos)
dias_faturamentos = len(faturamentos)
media_mensal = soma_faturamentos / dias_faturamentos if dias_faturamentos > 0 else 0


dias_acima_media = 0
for f in faturamentos:
    if f > media_mensal:
        dias_acima_media += 1

print(f"Menor valor de faturamento: R${menor_faturamento:.2f}")
print(f"Maior valor de faturamento: R${maior_faturamento:.2f}")
print(f"Dias com faturamento acima da média: {dias_acima_media}")