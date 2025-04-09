'''
Escreva um programa para aprovar o empréstimo bancário
para a compra de uma casa
O programa vai perguntar o valor da casa, o salário do comprador e em quantos
anos ele vai pagar

Calcule o valor da prestação mensal,
sabendo que ela não pode exceder 30% do salário
ou então o empréstimo será negado
'''
preco = float(input("Qual o valor da casa? \n"))
sal = float(input("Qual é o seu salário? \n"))
tempo = int(input("Em quantos anos você vai pagar? \n"))

mensalidade = (preco / (tempo * 12))
print(f"Valor da casa: R${preco:.2f}")
print(f"Prestação: R${mensalidade:.2f}")

if mensalidade >= (sal * 30 / 100):
    print("Empréstimo negado.")
else:
    print(f"Empréstimo concedido.\nMensalidade durante {tempo} anos: R${mensalidade:.2f}.")

