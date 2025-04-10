''' Faça um programa que leia um número qualquer e mostre
o seu fatorial 

exemplo: 5! = 5 * 4 * 3 * 2 * 1 = 120
'''

a = int(input("Digite um número: "))
fatorial = 1
contador = a

while contador > 0:
    fatorial *= contador
    contador -= 1

print(f"O fatorial de {a} é {fatorial}")
