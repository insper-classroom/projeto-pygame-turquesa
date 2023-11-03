import pygame
from constantes import *
from classBatalhas import *
import time
class Animacao():
    def __init__(self) -> None:
        self.rect_para_att = pygame.Rect(409, 167, 3, 120)
        #infos para o ataque sludge
        self.slude = pygame.transform.scale((pygame.image.load('img/sluge.jpeg')),(30, 30))
        self.leaf = pygame.transform.scale((pygame.image.load('img/leaf_2.png')),(80, 80))
        self.thunder = pygame.transform.scale((pygame.image.load('img/Thunderboltsprite.png')), (30,110))
        self.tackle = pygame.transform.scale((pygame.image.load('img/Tackle.png')), (60,60))
        self.cut1 = pygame.transform.scale((pygame.image.load('img/Cut1.png')), (100,100))
        self.cut2 = pygame.transform.scale((pygame.image.load('img/Cut2.png')), (100,100))
        self.cut3 = pygame.transform.scale((pygame.image.load('img/Cut3.png')), (100,100))
        self.cut4 = pygame.transform.scale((pygame.image.load('img/Cut4.png')), (100,100))
        self.tackle_mini = pygame.transform.scale((pygame.image.load('img/Tackle.png')), (30,30))
        self.tackle_cont = 0
        self.cut_cont = 0
        self.slude_x = 160
        self.slude_y = 330
        self.leaf_x = 160
        self.leaf_y = 330
        self.thunder_rect_x = 385
        self.slude_rect = self.slude.get_rect()
        self.slude_rect.topleft = (self.slude_x, self.slude_y)
        self.slud_counter = 0
        self.leaf_rect = self.slude.get_rect()
        self.leaf_rect.topleft = (self.leaf_x, self.leaf_y)
        self.leaf_counter = 0
        self.leaf_animation_counter = 3
        self.thunder_counter = 0
        self.slud_animation_counter = 3
        self.thunder_animation_counter = 12
        self.tackle_counter = 0
        self.tackle_animation_counter = 6
        self.cut_counter = 0
        self.cut_animation_counter = 5
        #outro ataque aqui
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

    def movimenta_thunder(self):
        self.thunder_counter += 1
        if self.thunder_counter == self.thunder_animation_counter:
            self.thunder_counter = 0
            self.thunder_rect_x += 50

    def desenha_thunder(self, window, bool):
        if bool:
            self.movimenta_thunder()
            window.blit(self.thunder, (self.thunder_rect_x, 150))

    def desenha_tackle(self, window, bool):
        if bool:
            if self.tackle_cont == 2:
                window.blit(self.tackle_mini, (440, 235))
            else:
                window.blit(self.tackle, (425, 220))
            self.tackle_counter += 1
            if self.tackle_counter == self.tackle_animation_counter:
                self.tackle_counter = 0
                self.tackle_cont += 1

    def desenha_cut(self, window, bool):
        if bool:
            if self.cut_cont == 1:
                window.blit(self.cut1, (425, 190))
            elif self.cut_cont == 2:
                window.blit(self.cut2, (425, 190))
            elif self.cut_cont == 3:
                window.blit(self.cut3, (425, 190))
            elif self.cut_cont == 4:
                window.blit(self.cut4, (425, 190))
            self.cut_counter += 1
            if self.cut_counter == self.cut_animation_counter:
                self.cut_counter = 0
                self.cut_cont += 1
    def movimenta_leaf(self):
        self.leaf_counter += 1
        if self.leaf_counter == self.leaf_animation_counter:
            self.leaf_counter = 0
            self.leaf_rect.x += 25
            self.leaf_rect.y -= 13
    def desenha_leaf(self, window, bool):
        if bool:
            self.movimenta_leaf()
            window.blit(self.leaf, (self.leaf_rect.x, self.leaf_rect.y))
        if self.leaf_rect.x > 439:
            self.leaf_x = 160
            self.leaf_y = 330