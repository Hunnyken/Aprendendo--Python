n1 = int(input('Digite um numero:'))
n2 = int(input('Digite outro valor:'))
print('Os valores sao: a soma  {}, multiplicacao  {}, subtraçao {} e exponenciaçao {}'.format(n1 + n2, n1 * n2, n1 - n2, n1 ** n2), end='')
print(' a divisao {:.3f}, a sobra {}, a divisao inteira {}'.format(n1 / n2, n1 % n2, n1 // n2))

#No exercicio foi usada muitas linhas para facer as somas, subtraçoes, divisoes e etc, entao fis de uma maneira onde tudo poderia ser feito em uma linha ou duas.