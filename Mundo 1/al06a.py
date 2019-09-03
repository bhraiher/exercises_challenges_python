n1 = int(input('Informe um valor '))
n2 = int(input('informe outro valor '))
#print(n1.isnumeric())
soma = n1+n2
print(str('A soma entre ') + str(n1) + str(' e ') + str(n2) + str(' vale ') + str(soma))
print('A soma entre {} e {} vale {}'.format(n1,n2,soma))
print(str(type(n1)) + str(type(n2)))
