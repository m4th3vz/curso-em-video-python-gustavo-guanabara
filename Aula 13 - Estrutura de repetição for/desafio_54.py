''' Crie um programa que leia o ano de nascimento de sete pessoas
No final, mostre quantas pessoas ainda não atingiram a maioridade
e quantas já são maiores'''
from datetime import date

atual = date.today().year
young = 0
adult = 0

# Coletando anos de nascimento e verificando a idade
for _ in range(3):
    num = int(input("Digite o ano de nascimento: \n"))
    if atual - num >= 21:
        adult += 1
    else:
        young += 1

# Ajuste dinâmico do singular/plural
if adult == 1:
    adult_text = "maior"
else:
    adult_text = "maiores"

if young == 1:
    young_text = "menor"
else:
    young_text = "menores"

# Exibindo o resultado
print(f"Ao todo tivemos {adult} {adult_text} e {young} {young_text} de idade.")

