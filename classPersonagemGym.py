import pygame
from constantes import *

class Personagem:
    def __init__(self):
        self.personagem = pygame.transform.scale((pygame.image.load('img/personagem.png')),(30, 35))
        self.rect = self.personagem.get_rect()
        self.rect.x = 198
        self.rect.y = 500
        self.velocidade = [0, 0]
        self.pos_antiga = [0, 0]
    
    def desenha_personagem(self, window):
        window.blit(self.personagem, (self.rect.x, self.rect.y))
    
    def altera_sprite_horizontal(self):
        
        next_pos = self.rect.x + self.velocidade[0] 
        self.rect.x = next_pos 
    
    def altera_sprite_vertical(self):
        
        next_pos = self.rect.y + self.velocidade[1]
        self.rect.y = next_pos
    
    def verifica_colisao(self, lista_paredes):

        is_hit = False
        for parede in lista_paredes:
            if parede.colliderect(self.rect):
                is_hit = True
                break

        return is_hit