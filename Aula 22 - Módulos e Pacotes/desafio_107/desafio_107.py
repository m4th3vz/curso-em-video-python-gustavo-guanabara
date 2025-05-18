"""
Crie um módulo chamado moeda.py que tenha as funções incorporadas 'aumentar()', 'diminuir()', 'dobro()' e 'metade()'.

Faça também um programa que importe esse módulo e use algumas dessas funções.

Obs.: por exemplo, o 'aumentar()' recebe o preço e uma porcentagem, e calcula.

o 'diminuir()', mesma coisa.

"""

import moeda

num = int(input("Digite um valor: "))

a = moeda.metade(num)
b = moeda.dobro(num)
c = moeda.aumentar(num, 15)
d = moeda.diminuir(num, 15)

print(f"A metade de {num} é {a}")
print(f"O dobro de {num} é {b}")
print(f"O aumento de 15% de {num} é {c}")
print(f"A diminuição de 15% de {num} é {d}")
