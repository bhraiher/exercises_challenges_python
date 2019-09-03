'''Faça um programa que leia uma frase pelo teclado e mostr:
- Quantas vezes aparece a letra A
- Em que posição ela aparece a primeira vez
- Em que posição ela aparece a última vez'''

frase = input('Informe uma frase: ')
#Tratamento para eliminar espaços e deixar a frase maiuscula.
frase_ok = frase.upper().strip()
teste = 'A' in frase_ok
if bool('A' in frase_ok) == True:
    print('A letra "a" teve um total de {} ocorrências.'.format(frase_ok.count('A')))
    print('A primeira ocorrência da letra "a" foi na posição {}'.format(frase_ok.find('A')+1))
    print('A ultima ocorrência da letra "a" foi na posição {}'.format(frase_ok.rfind('A')+1))
    #print(frase_ok.split()[0])
else:
    print('A frase em que você digitou, não contém a letra "A".')

