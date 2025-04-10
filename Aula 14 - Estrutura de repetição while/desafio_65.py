''' Crie um programa que leia vários números inteiros pelo teclado
No final da execução, mostre a média entre todos os valores
e qual foi o maior e o menor valores lidos
O programa deve perguntar ao usuário se ele quer ou não continuar
a digitar valores
'''

numeros = []

while True:
    entrada = input("Digite um número inteiro ou 'sair' para encerrar: ")

    if entrada.lower() == 'sair':
        break

    if entrada.isdigit() or (entrada.startswith('-') and entrada[1:].isdigit()):
        numero = int(entrada)
        numeros.append(numero)
    else:
        print("Entrada inválida. Digite um número inteiro ou 'sair'.")

if numeros:
    media = sum(numeros) / len(numeros)
    maior = max(numeros)
    menor = min(numeros)
    print(f"\nVocê digitou {len(numeros)} números.")
    print(f"Média: {media}")
    print(f"Maior valor: {maior}")
    print(f"Menor valor: {menor}")
else:
    print("\nNenhum número foi digitado.")
