'''
Crie um programa que vai ler vários números e colocá-los em uma lista
Depois disso, mostre:
a) quantos números foram digitados.
b) a lista de valores, ordenada de forma decrescente
c) se o valor 5 foi digitado e está ou não na lista.
'''

lista = []

while True:
    try:
        num = int(input("Número: "))
        lista.append(num)
    except ValueError:
        print("Por favor, digite um número válido.")
        continue

    resposta = ''
    while resposta not in ('s', 'n'):
        resposta = input("Quer continuar [s/n]?: ").strip().lower()

    if resposta == 'n':
        break

if 5 in lista:
    print("O número 5 está na lista")
else:
    print("O número 5 não está na lista")

print(f"Foram digitados {len(lista)} números")

# Usando fatiamento para inverter (não altera a lista original)
print(f"A lista em ordem reversa é: {lista[::-1]}")

# O método reverse() inverte a lista original diretamente (altera a lista in-place)
lista.reverse()
print(f"A ordem reversa é {lista}")
