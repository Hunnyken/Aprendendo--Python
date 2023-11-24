import random
print('O computador irá sortear aleatóriamente um número entre 1 e 5, tente adivinhar qual será!')
n1 = int(input('Faça seu chute:'))
a = random.randint(1,5)
if n1 == a:
    print('Você adivinhou corretamente, PARABÉNS!!!')
else:
    print('Você errou :(, tente novamente!')
print('O número sorteado foi {}'.format(a))