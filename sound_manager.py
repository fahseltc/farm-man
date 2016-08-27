import pygame
from utils import load_sound

class SoundManager:
    def __init__(self):
        #pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.mixer.init()
        if pygame.mixer:
            self.waka = load_sound('sounds/waka.wav')
            self.waka.set_volume(0.01)
            self.fruit = load_sound('sounds/fruit.wav')
            self.fruit.set_volume(0.01)

    def play_waka(self):
        var = self.waka
        var.play()

    def play_fruit(self):
        var = self.waka
        var.play()
