def menu():
    r1 = float(input('Digite o valor da primeira reta:'))
    r2 = float(input('Digite o valor da segunda reta:'))
    r3 = float(input('Digite o valor da terceira reta:'))
    soma = r1 + r2
    if soma > r3:
        print()
        print('Com esses valores não é possível fazer um triangulo.')
    else:
        print()
        print('Com essses valores é possível de se fazer um triangulo.')
    print()
while True:
    menu()

