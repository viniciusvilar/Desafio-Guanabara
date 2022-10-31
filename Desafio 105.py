def notas(*notaTurma, sit=False):
    """
    Analisar notas e situações de vários alunos
    :param notaTurma: Notas dos alunos
    :param sit: valor opcional, indicando se deve ou não add situação da turma
    :return: dicionario com varias informações sobre a situação da turma
    """
    avalTurma = dict()
    avalTurma['total'] = len(notaTurma)
    avalTurma['maior'] = max(notaTurma)
    avalTurma['menor'] = min(notaTurma)
    avalTurma['média'] = (sum(notaTurma)) / len(notaTurma)
    if sit:
        if avalTurma['média'] >= 7:
            avalTurma['situação'] = 'BOA'
        elif avalTurma['média'] >= 5:
            avalTurma['situação'] = 'RAZOÁVEL'
        else:
            avalTurma['situação'] = 'RUIM'
    return avalTurma



resp = notas(8, 9, 10, sit=True)
print(resp)
