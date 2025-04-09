# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

n = float(input("Digite o preço de um produto: \nR$"))
desconto = n * 5 / 100
print(f"Na liquidação da loja, esse produto de R${n:.2f} está com desconto de 5%, \nou seja, vai custar só R${n - desconto:.2f}.")

