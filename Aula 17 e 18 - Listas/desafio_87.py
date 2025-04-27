"""
Aprimore o desafio anterior, mostrando no final:

a: a soma de todos os valores pares digitados
b: a soma dos valores da terceira coluna
c: o maior valor da segunda linha
"""

"""
Aprimore o desafio anterior, mostrando no final:

a: a soma de todos os valores pares digitados
b: a soma dos valores da terceira coluna
c: o maior valor da segunda linha
"""

listas = []  # Primeiro cria uma lista vazia
soma = 0

# Agora usa o for para adicionar 9 listas vazias dentro de listas
for _ in range(9):
    listas.append([])

# Agora preenche cada lista com um número
for i in range(9):
    num = int(input(f"Digite um número ({i+1}/9): "))
    listas[i].append(num) # [i] percorre as 9 listas colocando dentro delas os números digitados

    if num % 2 == 0:
        soma += num

coluna_3 = listas[2] + listas[5] + listas[8]
soma_coluna = sum(coluna_3)

linha_2 = listas[3] + listas[4] + listas[5]
maior_valor = max(linha_2)

# Exibe as listas organizadas em linhas de três
print(listas[0], listas[1], listas[2])
print(listas[3], listas[4], listas[5])
print(listas[6], listas[7], listas[8])

print(f"A soma dos números pares é {soma}")
print(f"A soma da terceira coluna é {soma_coluna}")
print(f"O maior valor da segunda linha é {maior_valor}")
