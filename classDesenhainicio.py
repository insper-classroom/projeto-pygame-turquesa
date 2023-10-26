import pygame
from constantes import *

class Inicio():
    def __init__(self):
        self.img = pygame.transform.scale((pygame.image.load('img/inicio.png')),(640, 600))
        self.rect_continuar = pygame.Rect(242, 471, 175, 20)
    
    def desenha_inicio(self, window):
        pygame.draw.rect(window, CIANO, self.rect_continuar)
        window.blit(self.img, (0, 0))

    def verifica_click_sim(self, x, y):
        if self.rect_continuar.collidepoint(x, y):
            return True