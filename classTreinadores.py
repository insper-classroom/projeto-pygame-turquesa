import pygame
class Treinador1:
    def __init__(self):
        self.treinador1_img = pygame.transform.scale((pygame.image.load('img/trainer-1.png')),(30, 30))
        self.rect = pygame.Rect(35, 185, 30, 30)
    
    def desenha_treinador1(self, window):
        window.blit(self.treinador1_img, (35, 185))

class Treinador2:
    def __init__(self):
        self.trainer2_img = pygame.transform.scale((pygame.image.load('img/trainer-2.png')),(30, 30))
        self.rect = pygame.Rect(430, 492, 30, 30)

    def desenha_treinador2(self, window):
        window.blit(self.trainer2_img, (430, 492))

class Treinardor3:
    def __init__(self):
        self.trainer3_img = pygame.transform.scale((pygame.image.load('img/trainer-2.png')),(30, 30))
        self.rect = pygame.Rect(72, 335, 30, 30)
    
    def desenha_treinador3(self, window):
        window.blit(self.trainer3_img, (72, 335))

class Treinador4:
    def __init__(self):
        self.trainer4_img = pygame.transform.scale((pygame.image.load('img/trainer-2.png')),(30, 30))
        self.rect = pygame.Rect(483, 68, 30, 30)
    
    def desenha_treinador4(self, window):
        window.blit(self.trainer4_img, (483, 68))