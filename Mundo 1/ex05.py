#Faça um progama que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
aux = int(input('Informe um numero '))
ant = aux - 1
suc = aux + 1
print('O numero que você digitou é o {} e o antecessor dele é {} e o sucessor é o {}'.format(aux,ant,suc))