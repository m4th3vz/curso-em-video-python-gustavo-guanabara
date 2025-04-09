'''

Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC
e mostre seu status, e acordo com a tabela abaixo:

- abaixo de 18.5: abaixo do peso
- entre 18.5 e 25: peso ideal
- 25 até 30: sobrepeso
- 30 até 40: obesidade
- acima de 40: obesidade mórbida
'''
m = float(input("Digite seu peso (em kg): \n"))
h = float(input("Digite sua altura (em m): \n"))

imc = (m / (h**2))

if imc < 18.5:
    print(f"Seu IMC é de: {imc:.1f}. Você está abaixo do peso.")
elif imc < 25:
    print(f"Seu IMC é de: {imc:.1f}. Você está no peso ideal.")
elif imc < 30:
    print(f"Seu IMC é de: {imc:.1f}. Você está com sobrepeso.")
elif imc < 40:
    print(f"Seu IMC é de : {imc:.1f}. Você está com obesidade.")
else:
    print(f"Seu IMC é de {imc:.1f}. Você está com obesidade mórbida.")

