"""
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros:
o nome de um jogador e quantos gols ele marcou.

O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
"""

def ficha(nome, gols):
    print(f"O jogador {nome} fez {gols} gol(s) no campeonato.")

a = input("Nome do jogador: ")
if a:
    nome = a
else:
    nome = "<desconhecido>"

b = input("Número de gols: ")
if b.isnumeric():
    numero = int(b)
else:
    numero = 0

ficha(nome, numero)
