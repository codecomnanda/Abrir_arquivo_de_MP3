#Faça um programa que abra e reproduza um arquivo em mp3.
import pygame

# Inicializar o mixer de áudio
pygame.mixer.init()

# Carregar o arquivo MP3
pygame.mixer.music.load('Construcao Chico Buarque de Holanda.mp3')

# Reproduzir o arquivo
pygame.mixer.music.play()

# Manter o programa rodando até o término da música
input("Pressione Enter para parar a reprodução...")




