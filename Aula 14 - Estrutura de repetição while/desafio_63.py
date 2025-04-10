'''
Escreva um programa que leia um número n inteiro qualquer
e mostre na tela os primeiros n elementos e uma sequência de Fibonacci

1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584 (...)

'''

n = int(input("Quantos termos da sequência de Fibonacci você quer ver? \nfn = "))

a, b = 0, 1
index = 0

while index < n:
    print(f"f{index} = {a}")
    a, b = b, a + b
    index += 1

print("Fim!")
