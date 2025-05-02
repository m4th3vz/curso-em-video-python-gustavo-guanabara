"""
Aprimore o DESAFIO 093 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes de aproveitamento 
de cada jogador.
"""

time = []

while True:
    jogador = {}
    gols_partidas = []

    jogador['nome'] = input("Nome do jogador: ")
    partidas = int(input(f"Quantas partidas {jogador['nome']} jogou?: "))

    for i in range(partidas):
        gols = int(input(f"  Quantos gols na partida {i+1}?: "))
        gols_partidas.append(gols)

    jogador['gols'] = gols_partidas[:]
    jogador['total_gols'] = sum(gols_partidas)

    time.append(jogador.copy())

    continuar = input("Deseja continuar? [S/N]: ").strip().upper()
    if continuar != 'S':
        break

print("\n" + "-"*50)
print(f"{'Cod':<5}{'Nome':<15}{'Gols':<20}{'Total'}")
print("-"*50)

for i, jogador in enumerate(time):
    print(f"{i:<5}{jogador['nome']:<15}{str(jogador['gols']):<20}{jogador['total_gols']}")

# Visualização detalhada
while True:
    print("\nDigite o código do jogador para ver detalhes (999 para sair):")
    cod = int(input("Código: "))
    
    if cod == 999:
        break
    if cod < 0 or cod >= len(time):
        print("Código inválido. Tente novamente.")
    else:
        print(f"\n--- Levantamento do jogador {time[cod]['nome']} ---")
        for i, g in enumerate(time[cod]['gols']):
            print(f"  → Na partida {i+1} fez {g} {'gol' if g == 1 else 'gols'}.")

print("\n<< PROGRAMA ENCERRADO >>")
