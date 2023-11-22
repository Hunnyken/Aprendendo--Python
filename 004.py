from math import sqrt
op = float(input('Digite o cateto oposto do triangulo retangulo:'))
ad = float(input('Digite o cateto adjascente do triangulo retangulo:'))
num = sqrt(op * op + ad * ad)
print('a hipotenusa do triangulo retangulo é igual a {}'.format(num))