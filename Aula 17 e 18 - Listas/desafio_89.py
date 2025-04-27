"""
Crie um programa que leia nome e duas notas de vários alunos
e guarde tudo em uma lista composta.

No final, mostre um boletim contendo a média de cada um
e permita que o usuário possa mostrar as notas de cada aluno individualmente

Cria um programa que lê nome e duas notas de vários alunos
e guarda-os numa lista completa.
"""

lista = []

# Parte 1: Cadastro de alunos
while True:
    nome = input("Nome: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))

    lista.append([nome, [nota1, nota2]])

    continuar = input("Quer continuar? [S/N] ").strip().upper()
    if continuar == 'N':
        break

# Parte 2: Mostrar o boletim (nome e média)
print("\nBoletim:")
print(f"{'No.':<4}{'Nome':<10}{'Média':>8}")
print("-" * 25)

for i, aluno in enumerate(lista):
    media = sum(aluno[1]) / len(aluno[1])
    print(f"{i:<4}{aluno[0]:<10}{media:>8.2f}")

# Parte 3: Mostrar notas de um aluno específico
while True:
    opcao = int(input("\nMostrar notas de qual aluno? (Digite o número ou 999 para sair): "))
    
    if opcao == 999:
        print("Finalizando...")
        break

    if 0 <= opcao < len(lista):
        print(f"Notas de {lista[opcao][0]} são {lista[opcao][1]}")
    else:
        print("Número inválido, tente novamente.")
        