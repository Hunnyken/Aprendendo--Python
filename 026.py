def menu():
    r1 = float(input('Digite o valor da primeira reta:'))
    r2 = float(input('Digite o valor da segunda reta:'))
    r3 = float(input('Digite o valor da terceira reta:'))
    if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
        print()
        print('Com esses valores é possível fazer um triangulo.')
    else:
        print()
        print('Com essses valores não é possível de se fazer um triangulo.')
    print()
while True:
    menu()
