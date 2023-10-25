import pygame
from constantes import *

class Cura_pokemon():
    def __init__(self):
        self.img_box = pygame.transform.scale((pygame.image.load('imgBatalhas/barraVazia.png')),(640, 150))
        self.img_pc = pygame.transform.scale((pygame.image.load('img/pokemonCenter.png')),(640, 400))
        self.fonte = pygame.font.Font('imgBatalhas/fontes.ttf', 18)
        self.porta_pc = pygame.Rect(310, 460, 20, 10)
        self.balcao = pygame.Rect(185, 255, 272, 8)
        self.rect_sim = pygame.Rect(510, 488, 50, 30)
        self.rect_nao = pygame.Rect(510, 538, 50, 30)
        self.lista_paredes = [
            pygame.Rect(185, 250, 272, 5),
        ]
        self.texto1 = self.fonte.render('Você gostaria de curar seus pokemons?', True, PRETO)
        self.texto_sim = self.fonte.render('SIM', True, PRETO)
        self.texto_nao = self.fonte.render('NÃO', True, PRETO)
        self.mouse = pygame.mouse.get_pos()

    def desenha_pc(self, window):
        window.fill((0, 0, 0))
        window.blit(self.img_pc, (0, 100))
        for parede in self.lista_paredes:
            pygame.draw.rect(window, CIANO, parede)
        pygame.draw.rect(window, PRETO, self.porta_pc)
        pygame.draw.rect(window, PRETO, self.balcao)

    def desenha_box(self, window):
        window.blit(self.img_box, (0, 450))
        window.blit(self.texto1, (30, 515))
        pygame.draw.rect(window, (188, 188, 188), self.rect_sim)
        pygame.draw.rect(window, (188, 188, 188), self.rect_nao)
        window.blit(self.texto_sim, (517, 490))
        window.blit(self.texto_nao, (517, 540))
    
    def verifica_click_sim(self, x, y):
        if self.rect_sim.collidepoint(x, y):
            return True
        
    def verifica_click_nao(self, x, y):
        if self.rect_nao.collidepoint(x, y):
            return True