#Apresentar um programa que leia o quanto de dinheiro a pessoa tenha na carteira e mostre quantos doláres está pessoa pode comprar. (Considerar US$1 = R$ 3,27).
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
aux = float(input('Quantos reais você tem na carteira? R$'))
dolar = aux / 3.27
escreve = ('-'*20+' Realizando conversão '+'-'*20)
x = len(escreve)
print(escreve)
print('Com R${:.2f} você pode comprar U${:.2f} '.format(aux,dolar).replace('.',','))
print('-'*x)
formatado = locale.currency(dolar, grouping=True)
print('Forma mais adequada de formatar numeros monetários',formatado)
