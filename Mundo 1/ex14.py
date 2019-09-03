'''Escreva um programa que converta uma temperatura digitada em ºC em ºF'''
print('             .:Este é seu conversor de temperatura:.\n')
c = float(input('Favor, informe qual é a temperatura medida em ºC: '))
f = (c * (9 / 5) + 32)
k = c + 273.15
print('A temperatura digitada foi {:.0f}ºC.\n '
      'Conversão em Fahrenheit: {:.0f}ºF\n'
      'Conversão em Kelvin: {:.0f}ºK '.format(c,f,k))

