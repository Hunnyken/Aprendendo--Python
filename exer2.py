n = input('Digite algo:')
print('O seu tipo? ',type(n))
print('Ele é númerico? ',n.isnumeric())
print('Há letras? ',n.isalpha())
print('Está escrito em letras pequenas? ',n.islower())
print('Está escrito com letras grandes? ',n.isupper())
print('Há números? ',n.isalnum())
print('Está capitalizada? ',n.istitle())