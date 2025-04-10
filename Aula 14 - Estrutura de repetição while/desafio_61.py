'''
Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando
a estrutura while
'''

prim = int(input("Primeiro termo: \n"))
raz = int(input("Razão da PA: \n"))

contador = 0
termo = prim

while contador < 10:
    print("{}".format(termo))
    termo += raz
    contador += 1
