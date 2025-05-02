"""
Crie um programa que leia nome, ano de nascimento e carteira de trabalho
e cadastre-os (com idade) em um dicionário. 
Se por acaso a CTPS for diferente de zero, o dicionário receberá também
o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos
a pessoa vai se aposentar.

Obs.: aposentadoria em 35 anos de contribuição.
"""

from datetime import date

dado = {}
ano_atual = date.today().year

dado["nome"] = input("Nome: ")
ano_nascimento = int(input("Ano de nascimento: "))
dado["idade"] = ano_atual - ano_nascimento

tem_carteira = input("Tem carteira de trabalho? [S/N]: ").strip().lower()
dado["carteira"] = tem_carteira

if tem_carteira == 's':
    dado["contratação"] = int(input("Ano de contratação: "))
    dado["salário"] = float(input("Salário: R$ "))
    
    idade_aposentadoria = (dado["contratação"] + 35) - ano_nascimento
    dado["aposentadoria"] = idade_aposentadoria

# Exibição formatada
print("\n--- DADOS CADASTRADOS ---")
for chave, valor in dado.items():
    print(f"{chave.capitalize()}: {valor}")
