import pygame
from constantes import *

class Animacao():
    def __init__(self) -> None:
        self.rect_para_att = pygame.Rect(409, 167, 3, 120)
        #infos para o ataque sludge
        self.slude = pygame.transform.scale((pygame.image.load('img/sluge.jpeg')),(30, 30))
        self.slude_x = 160
        self.slude_y = 330
        self.slude_rect = self.slude.get_rect()
        self.slude_rect.topleft = (self.slude_x, self.slude_y)
        self.slud_counter = 0
        self.slud_animation_counter = 3
        #infos para Psybeam

    def movimenta_slude(self):
        self.slud_counter += 1
        if self.slud_counter == self.slud_animation_counter:
            self.slud_counter = 0
            self.slude_rect.x += 25
            self.slude_rect.y -= 13
    def desenha_slude(self, window, bool):
        if bool:
            self.movimenta_slude()
            window.blit(self.slude, (self.slude_rect.x, self.slude_rect.y))
        if self.slude_rect.x > 439:
            self.slude_x = 160
            self.slude_y = 330
            
        