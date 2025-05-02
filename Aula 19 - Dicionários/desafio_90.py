"""
Faça um programa que leia nome e média de um aluno,
guardando também a situação em um dicionário.

No final, mostre o conteúdo da estrutura na tela.
"""

# Criação do dicionário
dicionario = {}

# Coleta de dados
dicionario['nome'] = input("Nome: ")
dicionario['media'] = float(input(f"Média de {dicionario['nome']}: "))

# Determinando a situação
if dicionario['media'] >= 7:
    dicionario['situacao'] = 'Aprovado'
else:
    dicionario['situacao'] = 'Reprovado'

# Exibição dos resultados
print("-" * 30)
print(f"Nome: {dicionario['nome']}")
print(f"Média: {dicionario['media']}")
print(f"Situação: {dicionario['situacao']}")
print("-" * 30)
