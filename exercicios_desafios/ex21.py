'''Ler um arquivo mp3 e reproduzi-lo
import pygame
print('hi word')
pygame.init()
pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play()
pygame.mixer.music.set_volume(10)
x = input('Digite algo para encerrar')'''

from playsound import playsound
playsound('musica.mp3')
#faltou parar o som.

