import pygame
from constantes import *    

class Avisos():
    def __init__(self):
        self.img = pygame.transform.scale((pygame.image.load('imgBatalhas/barraVazia.png')),(360, 95))
        self.fonte = pygame.font.Font('imgBatalhas/fontes.ttf', 13)
        self.texto1 = self.fonte.render('Cure seus pokemons em um CP para batalhar!', True, PRETO)

    def aviso_vida(self, window, bool):
        if bool:
            window.blit(self.img, (16, 8))
            window.blit(self.texto1, (35, 45))