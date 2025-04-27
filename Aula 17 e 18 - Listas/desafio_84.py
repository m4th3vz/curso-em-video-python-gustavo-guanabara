"""
Faça um programa que leia nome e peso de várias pessoas
guardando tudo em uma lista.
No final, mostre:

a: quantas pessoas foram cadastradas.
b: uma listagem com as pessoas mais pesadas
c: uma listagem com as pessoas mais leves

Obs.: Gerar uma lista com os mais leves e mais pesados
Vai depender de analisar qual é o mais leve e o mais pesado.
Se houver mais de um com esse peso, insere na lista.
O mais normal é que a lista de mais pesados tenha apenas 1 pessoa,
que é o motivo pelo qual a lista existe.
"""

pessoas = []
mais_pesados = []
mais_leves = []
maior_peso = menor_peso = 0

while True:
    nome = input("Nome: ").strip()
    peso = float(input("Peso (kg): "))
    
    pessoa = [nome, peso]
    pessoas.append(pessoa)

    if len(pessoas) == 1:
        maior_peso = menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso

    continuar = input("Deseja continuar? [S/N] ").strip().upper()
    if continuar == 'N':
        break

# Loop que percorre a lista 'pessoas', onde cada elemento é uma lista [nome, peso]
for p in pessoas:
    if p[1] == maior_peso:         # Verifica qual o nome da(s) pessoa(s) com o maior peso
        mais_pesados.append(p[0])  # Adiciona o nome da(s) pessoa(s) que tem o maior peso na lista 'mais_pesados'
    if p[1] == menor_peso:
        mais_leves.append(p[0])    # Faz o mesmo para o menor peso

print("\nRESULTADOS")
print(f"A) Total de pessoas cadastradas: {len(pessoas)}")
print(f"B) Peso máximo foi de {maior_peso:.2f}kg. Pessoa(s) com esse peso: {mais_pesados}")
print(f"C) Peso mínimo foi de {menor_peso:.2f}kg. Pessoa(s) com esse peso: {mais_leves}")
