'''Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária
para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
1L = 2² e quantos litros para cubrir a área digitada '''
#Coleta de informação da area
larg = float(input('Informe qual é a largura da parede: '))
alt = float(input('Informe qual é a altura da parede: '))
#verifica quantos m² tem a parede informada
m2 = larg * alt
#verifica quantos litros de tinta é necessário para pintar a parede.
litros = m2 / 2

print('Esta parede tem uma medida de {} x {} e tem {}m².'.format(larg,alt,m2))
print('Para pintar esta parede, você precisará de {} litros de tinta.'.format(litros))

