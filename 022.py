viagem = int(input('Digite a distância em Km da sua viagem:'))
if viagem <= 200:
    print(f'A passagem ficará em R${viagem * 0.50}')
else:
    print(f'A passagem ficará em R${viagem * 0.45}')
