'''
Crie um programa onde o usuário possa digitar vários valores numéricos
e cadastre-os em uma lista.

Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''

lista = []

while True:
    try:
        num = int(input("Número: "))
    except ValueError:
        print("Por favor, digite um número válido.")
        continue

    if num in lista:
        print("Valor duplicado! Não vou adicionar.")
    else:
        lista.append(num)

    resposta = ''
    while resposta not in ('s', 'n'):
        resposta = input("Quer continuar [s/n]?: ").strip().lower()

    if resposta == 'n':
        break

print(f"Você digitou os valores {sorted(lista)}")
