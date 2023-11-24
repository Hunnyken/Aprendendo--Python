def maior(x,y,z):
    max = x

    if max < y:
        max = y
    if max < z:
        max = z
    return max

def menor(x,y,z):
    min = x

    if y < min:
        min = y
    if z < min:
        min = z
    return min
def menu():
    x = int(input('Digite um numero:'))
    y = int(input('Digite outro numero:'))
    z = int(input('Digite mais um numero:'))
    print('Maior número: ',maior(x,y,z))
    print('Menor numero: ',menor(x,y,z))
    print()
while True:
    menu()