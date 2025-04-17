'''
Desenvolva um programa que leia quatro valores pelo teclado
e guarde-os em uma tupla.
No final, mostre:

a) quantas vezes apareceu o valor 9
b) em que posição foi digitado o primeiro valor 3
b) quais foram os números pares
'''

# Leitura dos números
numeros = []
for i in range(1, 5):
    num = int(input(f"Digite o número ({i}/4): "))
    numeros.append(num)

# Conversão para tupla
tupla = tuple(numeros)

# Exibição da tupla
print(f"\nVocê digitou os valores: {tupla}")

# A) Quantas vezes apareceu o número 9
qtd_9 = tupla.count(9)
if qtd_9 == 1:
    print("O número 9 apareceu 1 vez.")
else:
    print(f"O número 9 apareceu {qtd_9} vezes.")

# B) Em que posição foi digitado o primeiro valor 3
tem_tres = 3 in tupla
if tem_tres:
    posicao_tres = tupla.index(3) + 1  # soma 1 para ficar humano-legível
    print(f"O número 3 aparece na {posicao_tres}ª posição.")
else:
    print("O número 3 não foi digitado.")

# C) Quais foram os números pares
pares = []
for numero in tupla:
    if numero % 2 == 0:
        pares.append(numero)

if len(pares) > 0:
    print("Os números pares digitados foram:", pares)
else:
    print("Nenhum número par foi digitado.")
