nome = input('Digite seu nome:').strip()
div = nome.split()
print(f'Bem-vindo {nome}!')
print(f'Seu primeiro nome é {div[0]}')
print(f'seu último nome é {div[-1]}')


#outra forma de se fazer o ultimo topico é utilizando a função len() Ex: print('seu último nome é {}'.format(div[len(div)-1]))
