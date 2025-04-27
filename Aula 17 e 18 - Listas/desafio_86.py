"""
Crie um programa que crie uma matriz 3.3
e preencha com valores lidos pelo teclado.

No final, mostre a matriz na tela com a formatação correta
"""

listas = []  # Primeiro cria uma lista vazia

# Agora usa o for para adicionar 9 listas vazias dentro de listas
for _ in range(9):
    listas.append([])

# Agora preenche cada lista com um número
for i in range(9):
    num = int(input(f"Digite um número ({i+1}/9): "))
    listas[i].append(num) # [i] percorre as 9 listas colocando dentro delas os números digitados

# Exibe as listas organizadas em linhas de três
print(listas[0], listas[1], listas[2])
print(listas[3], listas[4], listas[5])
print(listas[6], listas[7], listas[8])
