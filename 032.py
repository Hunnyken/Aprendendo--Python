from datetime import date
idade = int(input('Digite seu ano de nascimento: '))
ano = date.today().year
if ano - idade <= 9:
    print('Você é mirim!')
elif ano - idade <= 14:
    print('Você está na categoria infantil!')
elif ano - idade <= 19:
    print('Você é junior!')
elif ano - idade <= 20:
    print('Você é sênior!')
else:
    print('Você é Master!')