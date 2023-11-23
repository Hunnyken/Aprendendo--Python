nome = input('Digite seu nome:').strip()
div = nome.split()
print('Bem-vindo {}!'.format(nome))
print('Seu primeiro nome é {}'.format(div[0]))
print('seu último nome é {}'.format(div[-1]))


#outra forma de se fazer o ultimo topico é utilizando a função len() Ex: print('seu último nome é {}'.format(div[len(div)-1]))