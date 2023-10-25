import pygame
from constantes import *

class Cura_pokemon():
    def __init__(self):
        self.img_box = pygame.transform.scale((pygame.image.load('imgBatalhas/barraVazia.png')),(640, 150))
        self.img_pc = pygame.transform.scale((pygame.image.load('img/pokemonCenter.png')),(640, 400))
        self.fonte = pygame.font.Font('imgBatalhas/fontes.ttf', 20)
        self.porta_pc = pygame.Rect(310, 460, 20, 10)
        self.balcao = pygame.Rect(185, 255, 272, 8)
        self.lista_paredes = [
            pygame.Rect(185, 250, 272, 5),
        ]

    def desenha_pc(self, window):
        window.fill((0, 0, 0))
        window.blit(self.img_pc, (0, 100))
        for parede in self.lista_paredes:
            pygame.draw.rect(window, CIANO, parede)
        pygame.draw.rect(window, PRETO, self.porta_pc)
        pygame.draw.rect(window, PRETO, self.balcao)

    def desenha_box(self, window):
        window.blit(self.img_box, (0, 450))
        