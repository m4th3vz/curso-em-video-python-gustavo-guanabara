''' Crie um programa que leia uma frase qualquer
E diga se ela é um palíndromo, desconsiderando os espaços'''
# Após a sopa
# A sacada da casa
# A torre da derrota
# o lobo ama o bolo
# Anotaram a data da maratona

frase = str(input("Palíndromo: \n")).upper()
frase = "".join(frase.split(" "))
print(f"A palavra {frase} ao contrário é {frase[::-1]} e ", end="")
if frase == frase[::-1]:
    print("é um palíndromo.")
else:
    print("não é um palíndromo.")

