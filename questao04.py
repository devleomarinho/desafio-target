# 4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado.
# Escreva um programa na linguagem que desejar onde calcule o percentual de representação
# que cada estado teve dentro do valor total mensal da distribuidora. 

faturamento_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}


total_mensal = sum(faturamento_estados.values())

print(f"Faturamento mensal total: R$ {total_mensal:.2f}")
print("Percentual de cada estado: ")

for estado, valor in faturamento_estados.items():
    percentual = (valor / total_mensal) * 100
    print(f"{estado}: {percentual:.2f}%")