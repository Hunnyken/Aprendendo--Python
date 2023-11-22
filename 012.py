cidade = input('Digite o nome da sua cidade:')
cidade_m = cidade.lower()
div = cidade_m.split()
if div[0] == 'santo':
    print('tem santo')
else:
    print('nao tem')
