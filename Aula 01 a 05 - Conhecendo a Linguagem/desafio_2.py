# Crie um script Python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada

ano = int(input("Ano de nascimento: \n"))
mes = int(input("Mês de nascimento: \n"))
dia = int(input("Dia de nascimento: \n"))

print(f"A pessoa nasceu em: {dia}/{mes}/{ano}")
print(f"A pessoa nasceu no dia {dia} do mês {mes} do ano de {ano}.")
