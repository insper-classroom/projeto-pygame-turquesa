import pygame
class Treinador1:
    def __init__(self):
        self.treinador1_img = pygame.transform.scale((pygame.image.load('img/trainer-1.png')),(30, 30))
        self.rect = pygame.Rect(35, 180, 30, 30)
    
    def deseja_treinador1(self, window):
        window.blit(self.treinador1_img, (35, 180))
    