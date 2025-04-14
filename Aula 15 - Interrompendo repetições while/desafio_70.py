'''Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar.
No final, mostre:
a) qual é o total gasto na compra
b) quantos produtos custam mais de R$ 1000
c) qual é o nome do produto mais barato
'''

nome_mais_barato = ""
total = acima_mil = preco_mais_barato = 0

while True:
    nome = input("Nome do produto: ").strip()

    try:
        preco = float(input("Preço: R$ "))
    except ValueError:
        print("Preço inválido. Tente novamente.")
        continue

    total += preco

    if preco > 1000:
        acima_mil += 1

    if preco_mais_barato == 0 or preco < preco_mais_barato:
        preco_mais_barato = preco
        nome_mais_barato = nome

    continuar = input("Inserir mais produtos? [S / N] ").strip().lower()

    if continuar in ('n', 'nao', 'não'):
        break

print(f"\nTotal gasto: R${total:.2f}")
print(f"Produtos que custam mais do que R$1.000: {acima_mil}")
print(f"O produto mais barato é '{nome_mais_barato}', que custa R${preco_mais_barato:.2f}")
