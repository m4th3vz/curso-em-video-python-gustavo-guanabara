"""Faça um programa que tenha uma função chamada area(), que receba dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno
"""

def area(largura, comprimento):
    return largura * comprimento

largura = float(input("Largura: "))
comprimento = float(input("Comprimento: "))

print(f"A área de um terreno de {largura} por {comprimento} metros é de {area(largura, comprimento)}m²")
