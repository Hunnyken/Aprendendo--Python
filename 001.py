valor = float(input('Digite o valor em que será aplicado o desconto:'))
por = int(input('Digite o valor da porcentagem de desconto:'))
n = (valor * por) / 100
x = valor - n
print('O valor de R${} com {}% de desconto resultará em R${} de desconto. O resultado ficou em R${} depois dos descontos.'.format(valor, por, n, x))