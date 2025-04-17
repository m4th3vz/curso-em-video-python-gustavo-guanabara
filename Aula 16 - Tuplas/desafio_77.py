'''
Crie um programa que tenha uma tupla com várias palavras
(não usar acentos).
Depois disso, você deve mostrar, para cada palavra,
quais são as suas vogais
'''

tupla = (
    "algoritmo",
    "inteligencia_artificial",
    "nuvem",
    "criptografia",
    "rede",
    "software",
    "hardware",
    "dados",
    "automacao",
    "ciberseguranca"
)

vogais = "aeiouAEIOU"

for palavra in tupla:
    vogais_na_palavra = []

    for letra in palavra:
        if letra in vogais:
            vogais_na_palavra.append(letra)

    vogais_formatadas = " ".join(vogais_na_palavra)
    print(f"Na palavra '{palavra}' temos {vogais_formatadas}")
