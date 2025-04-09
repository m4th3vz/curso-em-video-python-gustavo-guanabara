'''
Faça um programa que leia o sexo de uma pessoa
mas só aceite os valores "M" ou "F".
Caso esteja errado, peça a digitação novamente
até ter um valor correto.
'''

while True:
    a = input("Qual o sexo? ").upper()
    if a == 'M':
        print("O sexo é masculino")
        break
    elif a == 'F':
        print("O sexo é feminino")
        break
    else:
        print("Digite um sexo válido: M para masculino ou F para feminino")
