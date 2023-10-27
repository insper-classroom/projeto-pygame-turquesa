import pygame
from constantes import *    

class Telahp():
    def __init__(self):
        self.img_fundo = pygame.transform.scale((pygame.image.load('img/fundo-hp.png')),(640, 400))
        self.fonte = pygame.font.Font('imgBatalhas/fontes.ttf', 18)
        self.texto1 = self.fonte.render('Sair', True, PRETO)
        self.rect_sair = pygame.Rect(517, 460, 105, 28)
        self.Scizor = pygame.transform.scale((pygame.image.load('img/Scizor.png')),(150, 100))
        self.venusaur = pygame.transform.scale((pygame.image.load('img/venusaur.png')),(150, 120))
        self.pikachu = pygame.transform.scale((pygame.image.load('img/pikachulivre.png')),(100, 70))

    def desenha(self, window):
        window.fill((188, 188, 188))
        window.blit(self.img_fundo, (-2, 100))
        window.blit(self.texto1, (548, 460))
        window.blit(self.Scizor, (395, 100))
        window.blit(self.venusaur, (80, 205))
        window.blit(self.pikachu, (415, 352))
                    
    def verifica_click_sim(self, x, y):
        if self.rect_sair.collidepoint(x, y):
            return True