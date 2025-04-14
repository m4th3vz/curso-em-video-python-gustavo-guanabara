''' Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou, 
no final do jogo.'''

from random import randint

vitorias = 0

while True:
    tipo = input("Par(p) ou Impar(i)? ").strip().lower()
    if tipo not in ('p', 'i'):
        print("Entrada inválida. Tente novamente!")
        continue

    jogador = int(input("Qual o número?: "))
    maquina = randint(1, 2)
    soma = jogador + maquina

    print(f"Você jogou {jogador}, a máquina jogou {maquina}. Soma: {soma}")

    if tipo == 'p' and soma % 2 == 0:
        print("O número é par, você venceu!")
        vitorias += 1
    elif tipo == 'i' and soma % 2 != 0:
        print("O número é ímpar, você venceu!")
        vitorias += 1
    elif tipo == 'p' and soma % 2 != 0:
        print(f"O número é ímpar, você perdeu! Vitórias consecutivas: {vitorias}")
        break
    elif tipo == 'i' and soma % 2 == 0:
        print(f"O número é par, você perdeu! Vitórias consecutivas: {vitorias}")
        break
