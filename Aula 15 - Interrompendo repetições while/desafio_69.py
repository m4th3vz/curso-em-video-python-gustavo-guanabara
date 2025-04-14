''' Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar
se o usuário quer ou não continuar.
No final, mostra:
a) quantas pessoas têm mais de 18 anos
b) quantos homens foram cadastrados
c) quantas mulheres têm menos de 20 anos'''

maior_18 = 0
masculino = 0
feminino_menor_20 = 0

while True:
    try:
        idade = int(input("Idade: "))
    except ValueError:
        continue  # volta pro início se idade não for um número válido

    genero = input("Gênero (m ou f): ").strip().lower()
    while genero not in ('m', 'f'):
        genero = input("Gênero (m ou f): ").strip().lower()

    if idade > 18:
        maior_18 += 1
    if genero == 'm':
        masculino += 1
    if genero == 'f' and idade < 20:
        feminino_menor_20 += 1

    continuar = input("Quer continuar? (s ou n): ").strip().lower()
    while continuar not in ('s', 'n'):
        continuar = input("Quer continuar? (s ou n): ").strip().lower()

    if continuar == 'n':
        break

print(f"\nTotal de pessoas com mais de 18 anos: {maior_18}")
print(f"Ao todo temos {masculino} homens cadastrados")
print(f"Temos {feminino_menor_20} mulheres com menos de 20 anos")
