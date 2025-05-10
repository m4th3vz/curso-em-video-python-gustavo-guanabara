"""
Faça um programa que tenha uma função notas()
que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

quantidade de notas
a maior nota
a menor nota
a média da turma
a situação (opcional)

Adicione tambeem as docstrings da função
"""

def notas(*valores, situacao=False):
    """
    Calcula estatísticas sobre as notas de uma turma.

    Parâmetros:
    - *valores (float): uma ou mais notas dos alunos.
    - situacao (bool): valor opcional. Se True, adiciona a situação da turma com base na média.

    Retorna:
    dict: um dicionário com:
        - total (int): quantidade de notas recebidas
        - maior (float): a maior nota
        - menor (float): a menor nota
        - media (float): a média das notas
        - situacao (str, opcional): 'Boa', 'Razoável' ou 'Ruim', dependendo da média
    """
    if not valores:
        return {"erro": "Nenhuma nota foi informada."}

    resultado = {}
    resultado['total'] = len(valores)
    resultado['maior'] = max(valores)
    resultado['menor'] = min(valores)
    resultado['media'] = sum(valores) / len(valores)

    if situacao:
        media = resultado['media']
        if media >= 7:
            resultado['situacao'] = 'Boa'
        elif media >= 5:
            resultado['situacao'] = 'Razoável'
        else:
            resultado['situacao'] = 'Ruim'

    return resultado


# Exemplo de uso:
resposta = notas(8.5, 6.0, 7.5, 9.0, situacao=True)
print(resposta)
