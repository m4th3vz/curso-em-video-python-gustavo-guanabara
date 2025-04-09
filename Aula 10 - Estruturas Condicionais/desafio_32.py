"""
Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO
"""

# Programa que verifica se um ano é bissexto
ano = int(input("Descubra se um ano é bissexto: \n"))

# Verificando se o ano é bissexto
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"{ano} é bissexto.")
else:
    print(f"{ano} não é bissexto.")
