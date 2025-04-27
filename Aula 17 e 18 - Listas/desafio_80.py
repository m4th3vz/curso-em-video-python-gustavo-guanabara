'''
Crie um programa onde o usuário possa digitar cinco valores numéricos
e cadastre-os em uma lista, já na posição correta de inserção
(sem usar o sort()).

No final, mostre a lista ordenada na tela.
'''

lista = []

for i in range(1, 6):
    num = int(input(f"Número ({i}/5): "))

    if not lista:
        lista.append(num)
    else:
        inserido = False
        for i in range(len(lista)):
            if num < lista[i]:
                lista.insert(i, num)
                inserido = True
                break
        if not inserido:
            lista.append(num)

print(lista)
