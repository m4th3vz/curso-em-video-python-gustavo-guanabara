'''Faça um programa em Python que abra e reproduza um arquivo mp3'''
import pygame
import time
import os

# Caminho do arquivo MP3
mp3_file = "musica.mp3"  # Substitua pelo nome do seu arquivo

# Verifica se o arquivo existe
if not os.path.exists(mp3_file):
    print(f"Arquivo '{mp3_file}' não encontrado.")
    exit()

# Inicializa o mixer
pygame.mixer.init()

# Carrega o arquivo de música
pygame.mixer.music.load(mp3_file)

# Toca o arquivo
pygame.mixer.music.play()

print(f"Tocando: {mp3_file}")

# Aguarda até que a música termine
while pygame.mixer.music.get_busy():
    time.sleep(1)
