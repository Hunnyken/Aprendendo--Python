def menu():
    n1 = int(input('Digite um número inteiro qualquer:'))
    n2 = int(input('O numero digitado foi {}\n1 para esse número ser convertido em binário.\n2 para octa.\n3 para hexadecimal.\n'.format(n1)))
    binario = bin(n1)
    octa = oct(n1)
    hexa = hex(n1)
    if n2 == 1:
        print('O número {} convertido para binário será {}'.format(n1, binario[2::]))
    elif n2 == 2:
        print('O número {} convertido para octadecimal é {}'.format(n1, octa[2::]))
    elif n2 == 3:
        print('O número {} convertido para octadecimal é {}'.format(n1, hexa[2::]))
    print('')
while True:
    menu()