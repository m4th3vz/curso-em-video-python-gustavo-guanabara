'''
Crie um programa que tenha uma tupla única
com nomes de produtos e seus respectivos precos,
na sequência

No final, mostre uma listagem de precos,
organizando os dados em forma tabular
'''

produtos = (
    "Pão", 2.50,
    "Leite", 4.20,
    "Café", 8.90,
    "Arroz", 5.60,
    "Feijão", 6.30,
    "Macarrão", 3.20,
    "Açúcar", 2.80,
    "Sal", 1.50
)

print("-" * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print("-" * 40)

for i in range(0, len(produtos), 2):
    nome = produtos[i]
    preco = produtos[i + 1]
    print(f'{nome:.<30} R$ {preco:>6.2f}')

print("-" * 40)
