# REPRODUTOR DE AUDIO MP3 #

import pygame 

pygame.init()
pygame.mixer.music.load('audio.mp3')
pygame.mixer.music.play()
input('Agora você está ouvindo um áudio. Pressione ENTER para parar. ')
pygame.mixer.music.stop()