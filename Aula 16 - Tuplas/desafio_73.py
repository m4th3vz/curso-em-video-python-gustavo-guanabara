'''
Crie uma tupla preenchida com os 20 primeiros colocados
da Tabela do Campeonato Brasileiro,
na ordem de colocação.
Depois mostre:
a) apenas os 5 primeiros colocados
b) os últimos 4 colocados da tabela
c) uma lista com os times em ordem alfabética
d) em que posição na tabela está o time da Chapecoense
'''

times = (
    "Atlético", "Flamengo", "Corinthians", "Palmeiras", "Fluminense",
    "América-MG", "São Paulo", "Grêmio", "Vasco da Gama", "Botafogo",
    "Sport Recife", "Cruzeiro", "EC Vitória", "Santos", "Chapecoense",
    "Atlético-PR", "Internacional", "Bahia", "Ceará SC", "Paraná"
)

# a) os primeiros 5 colocados:
print("a) Primeiros 5 colocados do Brasileirão:")
for i, time in enumerate(times[:5], 1):
    print(f"{i}. {time}")

# b) os últimos 4 colocados:
print("\nb) Últimos 4 colocados do Brasileirão:")
for i, time in enumerate(times[-4:], len(times) - 3):
    print(f"{i}. {time}")

# c) Times em ordem alfabética:
print("\nc) Times em ordem alfabética:")
for i, time in enumerate(sorted(times), 1):
    print(f"{i}. {time}")

# d) em que posição da tabela está o time da Chapecoense:
chape = times.index("Chapecoense") + 1
print(f"\nd) A Chapecoense está na {chape}ª posição da tabela.")
