import time
valor = float(input('Digite o valor da compra:R$'))
pagamento = (input('Qual será a forma de pagamento? \nCheque/Dinheiro \nÀ vista no cartão \nParcelado\n')).lower()
if pagamento == 'parcelado':
    x = int(input('Digite em quantas vezes deseja parcelar: '))

print('PROCESSANDO...')
time.sleep(2)

if pagamento in ['cheque', 'dinheiro']:
    print('A sua compra saíra com desconto de 10%, de R${:.2f} foi para R${:.2f}.'.format(valor, valor - (valor * 0.1)))
elif 'cartão' in pagamento:
    print('A sua compra saíra com desconto de 5%, de R${:.2f} foi para R${:.2f}.'.format(valor, valor - (valor * 0.05)))
elif x == 2:
    print('A compra ficara em {:.2f}'.format(valor / 2))
elif x >= 3:
    print('A compra de R${:.2f} parcelada em {}, ficará em {:.2f}^.'.format(valor, x, valor + (valor * 0.2 * 6)))