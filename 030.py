from datetime import date
ano = int(input('Em que ano você nasceu?'))
ano1 = date.today().year
if  ano1 - ano < 18:
    print('Voê precisará se alistar nos próximo(s) ano(s).')
elif ano1 - ano == 18:
    print('Você se alistará ainda esse ano.')
elif ano1 - ano > 18:
    print('Você já passou do tempo de alistamento, em caso de não alistamento, deverá pagar uma multa.')