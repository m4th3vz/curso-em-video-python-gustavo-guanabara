''' Melhore o jogo do DESAFIO 028 onde o computador vai "pensar"
em um número entre 0 e 10. 
Só que agora o jogador vai tentar adivinhar até acertar, 
mostrando no final quantos palpites foram necessários para vencer
'''

from random import randint

ran = randint(0, 10)
lista = []

while True:
    num = int(input("Em qual número você acha que eu pensei entre 0 e 10?: "))
    if num > 10 or num < 0:
        print("Digite um número entre 0 e 10!")
        continue
    lista.append(num)
    if num == ran:
        print(f"Número digitado: {num}.")
        print(f"Parabéns, você acertou! Foram necessários {len(lista)} palpites para vencer.")
        break
    else:
        print(f"Número digitado: {num}.")
        print("VOCÊ ERROU. Tente novamente.")


# Versão alternativa sem lista
'''from random import randint

ran = randint(0, 10)
tentativas = 0

while True:
    num = int(input("Em qual número você acha que eu pensei entre 0 e 10?: "))
    if num < 0 or num > 10:
        print("Digite um número entre 0 e 10!")
        continue
    tentativas += 1
    if num == ran:
        print(f"Número digitado: {num}.")
        print(f"Parabéns, você acertou! Foram necessários {tentativas} palpites para vencer.")
        break
    else:
        print(f"Número digitado: {num}.")
        print("VOCÊ ERROU. Tente novamente.")'''
