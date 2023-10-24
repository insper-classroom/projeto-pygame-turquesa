import pygame

class Personagem_ilha:
    def __init__(self) -> None:
        self.personagem = pygame.transform.scale((pygame.image.load('img/personagem.png')),(30, 35))
        self.rect = self.personagem.get_rect()
        self.rect.x = 280
        self.rect.y = 300
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