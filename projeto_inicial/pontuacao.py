def calcular_pontuacao(respostas, gabarito):
    pontos = 0
    for indice, correta in enumerate(gabarito):
        if indice < len(respostas) and respostas[indice] == correta:
            pontos += 1
    return pontos
