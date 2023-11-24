viagem = int(input('Digite a distância em Km da sua viagem:'))
if viagem <= 200:
    print('A passagem ficará em R${}'.format(viagem * 0.50))
else:
    print('A passagem ficará em R${}'.format(viagem * 0.45))