"""
Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário
e todos os dicionários em uma lista.

No final, mostre:
a. Quantas pessoas foram cadastradas
b. A média de idade do grupo
c. uma lista com todas as mulheres
d. uma lista com todas as pessoas com idade acima da média.
"""

pessoas = []
soma_idades = 0

while True:
    pessoa = {}
    pessoa["Nome"] = input("Nome: ")

    while True:
        sexo = input("Sexo [M/F]: ").strip().upper()
        if sexo in ['M', 'F']:
            pessoa["Sexo"] = sexo
            break
        print("Erro! Digite apenas M ou F.")

    idade = int(input("Idade: "))
    pessoa["Idade"] = idade
    soma_idades += idade

    pessoas.append(pessoa)

    continuar = input("Deseja continuar? [S/N]: ").strip().upper()
    if continuar != 'S':
        break

# Cálculos e separações usando for tradicional
total_cadastradas = len(pessoas)
media_idade = soma_idades / total_cadastradas

mulheres = []
for p in pessoas:
    if p["Sexo"] == 'F':
        mulheres.append(p["Nome"])

acima_da_media = []
for p in pessoas:
    if p["Idade"] > media_idade:
        acima_da_media.append(p)

# Resultados
print("\n=== RESULTADOS ===")
print(f"a. Total de pessoas cadastradas: {total_cadastradas}")
print(f"b. Média de idade do grupo: {media_idade:.2f} anos")
print(f"c. Mulheres cadastradas: {mulheres}")

print("d. Pessoas com idade acima da média:")
for p in acima_da_media:
    print(f"   - {p['Nome']} ({p['Idade']} anos)")
