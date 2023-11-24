ano = int(input('Digite o ano para descobrir se le é um ano bissexto ou não:'))
conta = ano % 4
if conta == 0:
    print('O ano {} é um ano bissexto!'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))