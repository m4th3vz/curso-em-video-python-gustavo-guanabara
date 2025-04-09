# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar

# Considere R$ 3.27 = US$ 1
n = float(input("Quanto dinheiro você tem? \nR$"))
dolar = 3.27
conversao = n / dolar
print(f"Com R${n} você pode comprar US$ {conversao:.2f}.")
