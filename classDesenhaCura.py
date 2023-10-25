import pygame

class Cura_pokemon():
    def __init__(self):
        self.img_box = pygame.transform.scale((pygame.image.load('imgBatalhas/barraVazia.png')),(640, 150))
        self.img_pc = pygame.transform.scale((pygame.image.load('img/pokemonCenter.png')),(640, 400))
        self.fonte = pygame.font.Font('imgBatalhas/fontes.ttf', 20)

    def desenha_pc(self, window):
        window.fill((0, 0, 0))
        window.blit(self.img_pc, (0, 100))

    def desenha_box(self, window):
        window.blit(self.img_box, (0, 450))