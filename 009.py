nome = input('Digite seu nome completo:')
print('Bem-vindo, {}!!!'.format(nome))
print('Bem-vindo, {}!!!'.format(nome.upper()))
print('Bem-vindo, {}!!!'.format(nome.lower()))
div = nome.split()[0]
print('O seu primeiro nome tem {} letras.'.format(len(div)))