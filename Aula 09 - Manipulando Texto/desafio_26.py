# Faça um programa que leia uma frase qualquer e mostre:
# Quantas vezes aparece a letra "a"
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a última vez

# Faça um programa que leia uma frase qualquer:
frase = str(input("Digite uma frase: \n")).lower().strip()

# Tamanho total da string (só porque eu quero mesmo):
print(f"Tamanho total da string: {len(frase)}")

# Quantas vezes aparece a letra "a":
print(f"A letra A aparece {frase.count('a')} vezes na frase.")

# Em que posição ela aparece a primeira vez:
print(f"A primeira letra A aparece na posição {frase.find('a')}.")

# Em que posição ela aparece a última vez:
print(f"A última letra A apareceu na posição {frase.rfind('a')}.")
