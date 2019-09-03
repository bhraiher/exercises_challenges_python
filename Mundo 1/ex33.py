'''Leia um número e mostre qual é o maior e qual é o menor entre eles.'''
nmr1 = input('Iforme qual é o número 1: ')
nmr2 = input('Iforme qual é o número 2: ')
nmr3 = input('Iforme qual é o número 3: ')

#verificando o maior
if nmr1 > nmr2 and nmr1 > nmr3:
    print('O numero {} é o maior.'.format(nmr1))
elif nmr2 > nmr1 and nmr2 > nmr3:
    print('O numero {} é o maior.'.format(nmr2))
elif nmr3 > nmr1 and nmr3 > nmr2:
    print('O numero {} é o maior'.format(nmr3))

#verificando qual é o menor
if nmr1 < nmr2 and nmr1 < nmr3:
    print('O numero {} é o menor.'.format(nmr1))
elif nmr2 < nmr1 and nmr2 < nmr3:
    print('O numero {} é o menor.'.format(nmr2))
elif nmr3 < nmr1 and nmr3 < nmr2:
    print('O numero {} é o menor.'.format(nmr3))

