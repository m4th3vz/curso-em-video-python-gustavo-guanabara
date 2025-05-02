"""
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário,
incluindo o total de gols feitos durante o campeonato.
"""

dicionario = {}
gols_partidas = []

jogador = input("Qual o nome do jogador?: ")
dicionario["nome"] = jogador

partidas = int(input(f"Quantas partidas {jogador} jogou?: "))

for i in range(partidas):
    gols = int(input(f"Quantos gols na partida {i+1}?: "))
    gols_partidas.append(gols)

dicionario["gols"] = gols_partidas
dicionario["total_gols"] = sum(gols_partidas)

print("\nResumo do jogador:")
print(dicionario)

print(f"\nO campo nome tem o valor de {dicionario['nome']}")
print(f"O campo gols tem o valor de {dicionario['gols']}")
print(f"O campo total gols tem o valor de {dicionario['total_gols']}")

print(f"\nO jogador {jogador} jogou {partidas} partidas.\n")

print("Desempenho por partida:")
for i, gols in enumerate(dicionario["gols"]):
    print(f"  → Na partida {i+1}, fez {gols} {'gol' if gols == 1 else 'gols'}.")
