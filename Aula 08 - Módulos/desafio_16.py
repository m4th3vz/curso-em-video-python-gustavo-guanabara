# Desafio 16: Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
from math import trunc

num = float(input("Digite um número real: \n"))
# print(math.trunc(num))

print(f"O valor digitado é {num} e a sua porção inteira é {int(num)}.")

print(f"O valor digitado é {num} e a sua porção inteira é {trunc(num)}.")
