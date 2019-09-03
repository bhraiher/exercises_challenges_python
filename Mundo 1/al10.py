#Aula 10 referente à estrutura condicional (if). Segue um exemplo simples:

temp = int(input('Favor informar qual é a temperatura agora na sua cidade, em graus Celsius: '))

if temp > 20:
    print('Hoje está quente na sua cidade com {}ºC!'.format(temp))
else:
    print('Hoje está um pouco frio na sua cidade, com {}ºC.'.format(temp))
