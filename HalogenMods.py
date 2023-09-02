import pygame
import random

def playButtonSound():
    sounds = ["meow1.mp3", "meow2.mp3", "meow3.mp3"] 
    buttonSound = pygame.mixer.Sound(f"resources\sounds\{random.choice(sounds)}")
    buttonSound.play()
