carro = int(input('Qual foi a velocidade do carro?'))
if carro > 80:
    print('Você ultrapassou o limite de velocidade estabelecido, a multa será de R${}'.format((carro - 80) * 7))
else:
    print('Tudo nos conformes!')