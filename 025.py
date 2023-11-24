salario = float(input('Digite seu salário: R$'))
if salario > 1250:
    print('O seu salário de R${:.2f} passará a ser R${:.2f} com os 10% de aumento'.format(salario, (salario * 0.1) + salario))
else:
    print('O seu salário de R${:.2f} passará a ser R${:.2f} com um aumento de 15%'.format(salario, (salario * 0.15) + salario))