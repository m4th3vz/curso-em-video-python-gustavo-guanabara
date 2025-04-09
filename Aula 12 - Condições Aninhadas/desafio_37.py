''' Escreva um programa que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base de conversão:
1 para binário
2 para octal
2 para hexadecimal
'''
num = int(input("Digite um número a ser convertido: \n"))
base = int(input('''Escolha a base da conversão:
Para binário digite: 1
Para octal digite: 2
Para hexadecimal digite: 3

Sua escolha: \n'''))

if base == 1:
    print("Você escolheu binário.")
    print(f"{num} convertido para binário é: {bin(num)[2:]}.")
elif base == 2:
    print("Você escolheu octal.")
    print(f"{num} convertido para octal é: {oct(num)[2:]}.")
elif base == 3:
    print("Você escolheu hexadecimal.")
    print(f"{num} convertido para hexadecimal é: {hex(num)[2:]}.")
else:
    print("Por favor, escolha apenas uma das 3 opções.")

