'''Faça um programa que leia o ano para verificar se é bissexto, ou também verificar se o ano atual é BISSEXTO através da data do computador.'''
from datetime import datetime

ano = int(input('Informe o ano para verificar-mos se o mesmo é Bissexto, ou digite 0 para pegar o ano corrente: '))
now = datetime.now()
ano_ver = now.year if ano == 0 else ano

if ano_ver % 4 == 0:
    if ano_ver % 100 != 0:
        print('Este ano de {} é Bissexto!'.format(ano_ver))
elif ano_ver % 400 == 0:
    print('Este ano de ' + '\033[36m' + '{}' + '\033[0;0m é Bissexto!'.format(ano_ver))
else:
    print('Este ano de {} não é Bissexto!'.format(ano_ver))

