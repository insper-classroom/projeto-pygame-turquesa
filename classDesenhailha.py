import pygame
from constantes import *

class Desenha_ilha:
    def __init__(self):
        self.fundo = pygame.transform.scale((pygame.image.load('img/ilha.png')),(640, 600))
        self.porta_pc = []
        self.porta_gym = pygame.Rect(257, 523, 29, 10)
        self.lista_paredes = [
            pygame.Rect(167, 510, 72, 10),
            pygame.Rect(167, 400, 10, 110),
            pygame.Rect(167, 395, 180, 10),
            pygame.Rect(340, 395, 10, 115),
            pygame.Rect(305, 510, 45, 10),

        ]
    
    def desenha_fundo(self, window):
        window.blit(self.fundo, (0, 0))
        for parede in self.lista_paredes:
            pygame.draw.rect(window, CIANO, parede)
        pygame.draw.rect(window,PRETO, self.porta_gym)