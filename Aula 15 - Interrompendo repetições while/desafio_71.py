'''
Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.

Obs.: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
'''

numero = int(input("Qual valor você quer sacar? R$"))

notas = [50, 20, 10, 1]
contagem = {}

i = 0
while numero > 0:
    nota = notas[i]
    qtd = numero // nota
    numero = numero % nota
    if qtd > 0:
        contagem[nota] = qtd
    i += 1

for nota in notas:
    if nota in contagem:
        print(f"Total de {contagem[nota]} cédulas de R${nota}")

