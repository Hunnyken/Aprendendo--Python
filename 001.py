valor = float(input('Digite o valor em que será aplicado o desconto:'))
por = int(input('Digite o valor da porcentagem de desconto:'))
n = (valor * por) / 100
x = valor - n
print(f'O valor de R${valor} com {por}% de desconto resultará em R${n} de desconto. O resultado ficou em R${x} depois dos descontos.')
