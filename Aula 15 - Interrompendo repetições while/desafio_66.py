''' Crie um programa que leia vários números inteiros pelo teclado
O programa só vai parar quando o usuário digitar 999,
que é a condição de parada (flag).
No final, mostre quantos números foram digitados
e qual foi a acc entre eles (desconsiderando o flag)
'''
soma = 0
digitados = 0

while True:
    a = int(input("Digite um número ou '999' para parar: "))
    if a == 999:
        break
    soma += a
    digitados += 1

print(f"Você digitou {digitados} números e a soma deles é {soma}.")
