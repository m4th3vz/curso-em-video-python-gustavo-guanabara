"""
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e soma_par(). 
A primeira função vai sortear 5 números e vai colocá-los dentro da lista 
e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
"""

from random import randint
from time import sleep

def sorteia():
    numeros = []
    for _ in range(5):
        numeros.append(randint(0, 99))
    print(f"Sorteando {len(numeros)} valores da lista: ", end="")
    for i in numeros:
        print(f"{i} ", end="", flush=True)
        sleep(0.5)
    return numeros

def soma_par(lista_numeros):
    pares = [n for n in lista_numeros if n % 2 == 0]
    soma = sum(pares)
    print(f"\nOs valores pares da lista são: {pares}")
    print(f"E a soma deles é: {soma}")
    print('-' * 40)

soma_par(sorteia())
