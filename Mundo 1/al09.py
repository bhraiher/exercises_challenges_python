frase = '  Curso em video python  '#['C','u','r','s','o','','e','m','','V','i','d','e','o']
frase.strip()
print('Quebra de 0 a 11: ', frase[:11]) #Do inicio até o elemento 11.
print('Pulando de 2 em 2 o texto inteiro: ',frase[::2])
print('De 0 à 10 pulando de 2 em 2: ',frase[0:10:2]) #Elemento do 0 ao 10 pulando de 2 em 2
print('Da posição 1 à 9: ', frase[1:9])
print(len(frase))
print(frase.count('o'))
print(frase.find('py'))
print('Aqui com strip', frase.strip()) #Para tirar os espaços
print('python' in frase)
dividido = frase.split()  #para quebrar (divisão de string)(cada palavra recebe uma lista nova, com indices novo.
print(dividido[2][3])
'-'.join(frase) #para juntar algo ao texto.



