import pygame
from constantes import *

class Desenha_fundo:
    def __init__(self):
        self.fundo = pygame.transform.scale((pygame.image.load('img/map-gym.png')),(640, 600))
        self.lista_paredes = [
            pygame.Rect(380, 20, 233, 5),
            pygame.Rect(612, 20, 5, 90),
            pygame.Rect(575, 111, 44, 6),
            pygame.Rect(575, 111, 5, 27),
            pygame.Rect(543, 133, 37, 5),
            pygame.Rect(543, 133, 5, 110),
            pygame.Rect(307, 243, 238, 5),
            pygame.Rect(307, 155, 5, 90),
            pygame.Rect(257, 155, 50, 5),
            pygame.Rect(252, 155, 5, 127),
            pygame.Rect(252, 282, 330, 5),
            pygame.Rect(577, 285, 5, 45),
            pygame.Rect(468, 330, 116, 5),#
            pygame.Rect(468, 331, 5, 197),
            pygame.Rect(419, 526, 54, 5),
            pygame.Rect(417, 484, 5, 45),
            pygame.Rect(290, 484, 127, 5),
            pygame.Rect(290, 484, 5, 65),
            pygame.Rect(253, 549, 42, 5),
            pygame.Rect(253, 549, 5, 50),
            pygame.Rect(173, 594, 81, 5),
            pygame.Rect(168, 552, 5, 47),
            pygame.Rect(130, 549, 42, 5),
            pygame.Rect(130, 507, 5, 43),
            pygame.Rect(93, 507, 37, 5),
            pygame.Rect(93, 487, 5, 20),
            pygame.Rect(57, 483, 40, 5),
            pygame.Rect(58, 416, 5, 68),
            pygame.Rect(58, 414, 55, 5),
            pygame.Rect(113, 414, 5, 23),
            pygame.Rect(113, 432, 160, 5),
            pygame.Rect(272, 394, 5, 43),
            pygame.Rect(272, 392, 53, 5),
        ]

    def desenha_mapa(self, window):
        window.blit(self.fundo, (0, 0))
        for parede in self.lista_paredes:
            pygame.draw.rect(window,PRETO, parede)