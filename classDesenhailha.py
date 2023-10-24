import pygame
from constantes import *

class Desenha_ilha:
    def __init__(self):
        self.fundo = pygame.transform.scale((pygame.image.load('img/ilha.png')),(640, 600))
        self.porta_pc = []
        self.porta_gym = []
        self.lista_paredes = []
    
    def desenha_fundo(self, window):
        window.blit(self.fundo, (0, 0))