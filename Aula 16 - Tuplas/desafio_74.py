'''
Crie um programa que vai gerar cinco números aleatórios 
e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados
e também indice o menor e o maior valor que estão na tupla
'''

import random

lista_numeros = []

for _ in range(5):
    numero = random.randint(1, 100)
    lista_numeros.append(numero)

numeros = tuple(lista_numeros)

print(f"Os valores sorteados foram: {numeros}")
print(f"O menor valor sorteado foi {min(numeros)}")
print(f"O maior valor sorteado foi {max(numeros)}")
