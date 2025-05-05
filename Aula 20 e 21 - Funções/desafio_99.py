"""
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.

Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""

from time import sleep

def linha():
    print('-' * 30)

def encontrar_maior(*valores):
    print("Analisando os valores passados...")
    print("Valores informados: ", end="")
    for valor in valores:
        print(f"{valor} ", end="")
        sleep(0.2)
    print()

    total = len(valores)
    print(f"Ao todo são {total} valores.")

    if total == 0:
        print("Nenhum valor foi informado.")
    else:
        maior_valor = max(valores)
        print(f"O maior valor informado foi {maior_valor}.")
    
    linha()
    print()

# Testes
linha()
encontrar_maior(2, 9, 4, 5, 7, 1)
encontrar_maior(4, 7, 0)
encontrar_maior(1, 2)
encontrar_maior(6)
encontrar_maior()
