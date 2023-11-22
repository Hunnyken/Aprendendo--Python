import math
ang = float(input('Digite o angulo:'))
sen = math.sin(math.radians(ang))
cos = math.cos((math.radians(ang)))
tang = math.tan((math.radians(ang)))
print('O seno de {} é {:.2f}\nO cosseno de {} é {:.2f}\nA tangente de {} é {:.2f}.'.format(ang, sen, ang, cos, ang, tang))