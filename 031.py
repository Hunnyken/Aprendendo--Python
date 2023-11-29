n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua primeira nota: '))
n3 = float(input('Digite a sua primeira nota: '))
media = (n1 + n2 + n3) / 3
if media >= float(7):
    print(f'Você teve a media de {media:.1f} e foi aprovado! PARABÉNS!')
elif media >= 5.1 and media <= 6.9:
    print(f'Você teve a média de {media:.1f} e está de recuperação!')
else:
    print(f'Sua média foi de {media:.1f} e você está reprovado! Estude mais!')