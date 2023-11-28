from datetime import date
ano = int(input('Em que ano você nasceu? '))
ano1 = date.today().year
ano_mes = date.today().month
if  ano1 - ano < 18 and ano_mes <= 12:
    print('Voê precisará se alistar nos próximo(s) {} ano(s) e {} mês(es).'.format(ano1 - ano ,12 - ano_mes))
elif ano1 - ano == 18 and ano_mes == 12:
    print('Você deverá se alistar AGORA!.')
elif ano1 - ano > 18:
    print('Você já passou {} anos e {} meses do tempo de alistamento, você deverá pagar uma multa.'.format((ano1 - ano) - 18, ano_mes))
