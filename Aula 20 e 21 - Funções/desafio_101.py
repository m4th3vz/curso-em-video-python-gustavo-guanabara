"""
Crie um programa que tenha uma função chamada voto()
que vai receber como parâmetro o ano de nascimento de uma pessoa, 
retornando um valor literal indicando se uma pessoa tem voto 
NEGADO, OPCIONAL ou OBRIGATORIO nas eleições.
"""

from datetime import date

def voto(ano_nascimento):
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento

    if idade < 16:
        return f"Você tem {idade} anos: Não vota!"
    elif 18 <= idade <= 64:
        return f"Você tem {idade} anos: Voto obrigatório!"
    else:
        return f"Você tem {idade} anos: Voto facultativo!"

ano_nascimento = int(input('Ano de nascimento: '))
print(voto(ano_nascimento))
