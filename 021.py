n = int(input('Digite um número para saber se ele é ímpar ou par:'))
conta = n % 2 
if conta == 0:
    print('O número {} é par!'.format(n))
else:
    print('O número {} é ímpar!'.format(n))