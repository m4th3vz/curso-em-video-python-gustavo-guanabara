"""
Crie um programa onde 4 jogadores joguem um dado
e tenham resultados aleatórios.
Guarde esses resultados em um dicionário.

No final, coloque esse dicionário em ordem,
sabendo que o vencedor tirou o maior número no dado
"""

import random

dicionario = {}

for i in range(4):
    chave = f"Jogador{i+1}"
    valor = random.randint(1, 6)
    dicionario[chave] = valor

# Mostrar os resultados sorteados
print("Resultados dos dados:")
for jogador, valor in dicionario.items():
    print(f"{jogador} tirou {valor}")

# Ordenar os jogadores pelo valor tirado, do maior para o menor
ranking = sorted(dicionario.items(), key=lambda item: item[1], reverse=True)

# Mostrar o ranking
print("\nRanking dos jogadores:")
for posicao, (jogador, valor) in enumerate(ranking, start=1):
    print(f"{posicao}º lugar: {jogador} com {valor}")
