"""
Faça um programa que tenha uma função chamada contador(), que recebe três parâmetros:
início, fim e passo
E realize a contagem

Seu programa tem que realizar três contagens através da função criada

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) Uma contagem personalizada

--> print(f"{valor} ", end="")  # Exemplo de print espaçado
"""

from time import sleep

def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1  # Passo zero causaria loop infinito
    if passo < 0:
        passo = abs(passo)  # Transforma passo negativo em positivo, e o sentido da contagem será ajustado abaixo

    print(f"\nContando de {inicio} até {fim} de {passo} em {passo}:")
    sleep(1)

    if inicio < fim:
        for valor in range(inicio, fim + 1, passo):
            print(f"{valor} ", end="", flush=True)
            sleep(0.3)
    else:
        for valor in range(inicio, fim - 1, -passo):
            print(f"{valor} ", end="", flush=True)
            sleep(0.3)
    print("\n")


# Contagem padrão a)
contador(1, 10, 1)

# Contagem padrão b)
contador(10, 0, 2)

# Contagem personalizada c)
print("Agora é sua vez de personalizar a contagem:")
inicio = int(input("Início: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
contador(inicio, fim, passo)
