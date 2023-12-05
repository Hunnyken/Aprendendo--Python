n = int(input('Digite um número para saber se ele é ímpar ou par:'))
conta = n % 2 
if conta == 0:
    print(f'O número {n} é par!')
else:
    print(f'O número {n} é ímpar!')
