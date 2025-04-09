# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o do escolhido.

from random import choice

# Lista de alunos
nomes = ["Black Panther", "Solid Snake", "Kendrick Lamar", "Shadow the Hedgehog"]

# Sorteio usando o choice
escolhido = choice(nomes)

# Exibe o aluno escolhido
print(f"O aluno escolhido é {escolhido}.")
