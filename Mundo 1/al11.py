'''Cores no terminal'''
#sempre que for representar uma cor no python com o ANSI, usa o contra barra + 033 mais abre colchetes. (\033[) e ai coloca o código da cor.
#Dentro do colchetes a orde é o seguinte: \033[Style;text;back ex \033[0;33;44m
'''Legenda:
Style: 0 = none, 1 = Negrito(bold), 4 = underline, 7 = Negativo (vai inverter).
Text = vai de 30 à 37
back = vai de 40 à 47. 

vermelho = '\033[31m'
verde = '\033[32m'
azul = '\033[34m'

ciano = '\033[36m'
magenta = '\033[35m'
amarelo = '\033[33m'
preto = '\033[30m'

branco = '\033[37m'

restaura cor original = '\033[0;0m'
negrito = '\033[1m'
reverso = '\033[2m'

fundo preto = '\033[40m'
fundo vermelho = '\033[41m'
fundo verde = '\033[42m'
fundo amarelo = '\033[43m'
fundo azul = '\033[44m'
fundo magenta = '\033[45m'
fundo ciano = '\033[46m'
fundo branco = '\033[47m'''

#lista de cores:
nome = 'Bruno'
cores = {'limpa': '\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m\033[m'}

print('Ola! Muito prazer emlhe conhecer {}{}'.format(cores['amarelo'],nome))