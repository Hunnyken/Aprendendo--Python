l = float(input('Largura da parede:'))
c = float(input('Comprimento da parede:'))
conta = c * l 
conta2 = conta / 2
print('A parede tem a dimensão de {:.1f}m² e você precisará de {:.1f}L de tinta para pinta-la.'.format(conta, conta2))