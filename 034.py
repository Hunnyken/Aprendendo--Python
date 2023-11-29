peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
valor = peso / (altura * altura)
if valor < 18.5:
    print('Abaixo do peso.')
elif valor >= 18.5 and valor < 25:
    print('Peso ideal.')
elif valor >= 25 and valor < 40:
    print('Obesidade.')
else:
    print('Obesidade mórbida.')
