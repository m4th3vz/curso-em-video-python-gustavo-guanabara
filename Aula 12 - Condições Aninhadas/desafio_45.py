from random import choice
from time import sleep

'''
Crie um programa que faça o computador jogar Jokenpô com você.
'''

lista = ["pedra", "papel", "tesoura"]

print('''
COMPUTADOR: Vamos jogar Pedra, Papel, Tesoura!
As regras são as seguintes:
- Papel vence Pedra e perde para Tesoura
- Pedra vence Tesoura e perde para Papel
- Tesoura vence Papel e perde para Pedra
''')

# Entrada do jogador
jogador = input("Você escolhe pedra, papel ou tesoura? \n").lower()

# Verificação de entrada inválida antes da contagem
if jogador not in lista:
    print(f"{jogador.capitalize()} não é uma opção válida. Escolha pedra, papel ou tesoura.")
else:
    # Adicionando a simulação de contagem
    print("JO")
    sleep(0.5)
    print("KEN")
    sleep(0.5)
    print("PÔ!!!")
    sleep(0.5)

    # Escolha do computador
    computador = choice(lista)

    # Exibição do resultado das escolhas
    print(f'\nJogador: {jogador.capitalize()}')
    print(f'Computador: {computador.capitalize()}')

    # Comparação das jogadas
    if jogador == computador:
        print("Empate. Vamos jogar novamente.")
    elif jogador == "pedra" and computador == "tesoura":  # Pedra x Tesoura: Pedra
        print("Pedra vence tesoura. Jogador ganhou.")
    elif jogador == "tesoura" and computador == "pedra":  # Tesoura x Pedra: Pedra
        print("Pedra vence tesoura. Computador ganhou.")
    elif jogador == "pedra" and computador == "papel":  # Pedra x Papel: Papel
        print("Papel vence pedra. Computador ganhou.")
    elif jogador == "papel" and computador == "pedra":  # Papel x Pedra: Papel
        print("Papel vence pedra. Jogador ganhou.")
    elif jogador == "tesoura" and computador == "papel":  # Tesoura x Papel: Tesoura
        print("Tesoura vence papel. Jogador ganhou.")
    elif jogador == "papel" and computador == "tesoura":  # Papel x Tesoura: Tesoura
        print("Tesoura vence papel. Computador ganhou.")
