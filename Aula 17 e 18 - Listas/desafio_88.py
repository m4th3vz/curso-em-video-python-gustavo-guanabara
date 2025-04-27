"""
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.

O programa vai perguntar quantos jogos serão gerados
e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta.
"""

import random
from time import sleep

numeros = list(range(1, 61))

quantidade = int(input("Quantos jogos você quer que eu sorteie?: "))

for i in range(quantidade):
    jogo = sorted(random.sample(numeros, 6))
    print(f"Jogo {i + 1}: {jogo}")
    sleep(0.5)
