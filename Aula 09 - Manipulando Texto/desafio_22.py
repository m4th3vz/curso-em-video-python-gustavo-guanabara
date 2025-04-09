# Crie um programa que leia o nome completo de uma pessoa:
nome = str(input("Digite seu nome: \n")).strip()

# O nome com todas as letras maiúsculas
print(f"Nome em maiúsculas: {nome.upper()}.")

# O nome com todas minúsculas
print(f"Nome em minúsculas: {nome.lower()}.")

# Quantas letras ao todo (sem considerar espaços)
print(f"Letras ao todo: {len(nome) - nome.count(' ')}.")

# Quantas letras tem o primeiro nome:
nome = nome.split()
print(f'O primeiro nome é "{nome[0]}" e ele tem {len(nome[0])} letras.')
