import random
p = input('Digite o nome do primeiro aluno:')
s = input('Digite o nome do segundo aluno:')
t = input('Digite o nome do terceiro aluno:')
q = input('Digite o nome do quarto aluno:')
lista_de_alunos = [p, s, t, q]
print('O aluno sorteado foi {}'.format(random.choice(lista_de_alunos)))