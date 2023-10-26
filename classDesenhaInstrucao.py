import pygame
from constantes import *

class Instrucao():
    def __init__(self):
        self.img_fundo = pygame.transform.scale((pygame.image.load('img/instrucoes.png')),(640, 600))
        self.rect_jogar = []
    
    def desenha_inicio(self, window):
        window.blit(self.img_fundo, (0,0))

    def verifica_click_sim(self, x, y):
        if self.rect_jogar.collidepoint(x, y):
            return True