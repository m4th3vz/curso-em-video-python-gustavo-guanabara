"""
Crie um programa que tenha a função leia_int(), 
que vai funcionar de forma semelhante à função input do Python,
só que fazendo a validação para aceitar apenas um valor numérico.

ex.:
n = leia_int("Digite um n")
"""

def leia_int(mensagem):
    while True:
        entrada = input(mensagem)
        if entrada.strip().lstrip('-').isdigit():
            return int(entrada)
        else:
            print("\033[0;31mERRO! Digite um número inteiro válido!\033[m")

n = leia_int("Digite um número: ")
print(f"Você digitou o número {n}.")
