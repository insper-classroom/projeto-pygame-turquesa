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
        self.fcut1 = pygame.transform.scale((pygame.image.load('img/FCut1.png')), (100,100))
        self.fcut2 = pygame.transform.scale((pygame.image.load('img/FCut2.png')), (100,100))
        self.fcut3 = pygame.transform.scale((pygame.image.load('img/FCut3.png')), (100,100))
        self.fcut4 = pygame.transform.scale((pygame.image.load('img/FCut4.png')), (100,100))
        self.slam1 = pygame.transform.scale((pygame.image.load('img/Slam1.png')), (100,100))
        self.slam2 = pygame.transform.scale((pygame.image.load('img/Slam2.png')), (100,100))
        self.slam3 = pygame.transform.scale((pygame.image.load('img/Slam3.png')), (100,100))
        self.slam4 = pygame.transform.scale((pygame.image.load('img/Slam4.png')), (100,100))
        self.slam5 = pygame.transform.scale((pygame.image.load('img/Tackle.png')), (135,135))
        self.facade1 = pygame.transform.scale((pygame.image.load('img/Facade1.png')), (100,100))
        self.facade2 = pygame.transform.scale((pygame.image.load('img/Facade2.png')), (100,100))
        self.facade3 = pygame.transform.scale((pygame.image.load('img/Facade3.png')), (100,100))
        self.facade4 = pygame.transform.scale((pygame.image.load('img/Facade4.png')), (100,100))
        self.facade5 = pygame.transform.scale((pygame.image.load('img/Facade5.png')), (100,100))
        self.metal1 = pygame.transform.scale((pygame.image.load('img/Metal1.png')), (100,100))
        self.metal2 = pygame.transform.scale((pygame.image.load('img/Metal2.png')), (100,100))
        self.metal3 = pygame.transform.scale((pygame.image.load('img/Metal3.png')), (100,100))
        self.metal4 = pygame.transform.scale((pygame.image.load('img/Metal4.png')), (100,100))
        self.metal5 = pygame.transform.scale((pygame.image.load('img/Metal5.png')), (100,100))
        self.tackle_mini = pygame.transform.scale((pygame.image.load('img/Tackle.png')), (30,30))
        self.tackle_cont = 0
        self.cut_cont = 0
        self.fcut_cont = 0
        self.slam_cont = 0
        self.facade_cont = 0
        self.metal_cont = 0
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
        self.fcut_counter = 0
        self.fcut_animation_counter = 4
        self.slam_counter = 0
        self.slam_animation_counter = 4
        self.facade_counter = 0
        self.facade_animation_counter = 4
        self.metal_counter = 0
        self.metal_animation_counter = 3
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
    def desenha_slam(self, window, bool):
        if bool:
            if self.slam_cont == 1:
                window.blit(self.slam1, (405, 170))
            elif self.slam_cont == 2:
                window.blit(self.slam2, (405, 170))
            elif self.slam_cont == 3:
                window.blit(self.slam3, (405, 170))
            elif self.slam_cont == 4:
                window.blit(self.slam4, (405, 170))
            elif self.slam_cont == 5 or self.slam_cont == 6:
                window.blit(self.slam5, (405, 170))
            self.slam_counter += 1
            if self.slam_counter == self.slam_animation_counter:
                self.slam_counter = 0
                self.slam_cont += 1

    def desenha_facade(self, window, bool):
        if bool:
            if self.facade_cont == 1:
                window.blit(self.facade1, (425, 190))
            elif self.facade_cont == 2:
                window.blit(self.facade2, (425, 190))
            elif self.facade_cont == 3:
                window.blit(self.facade3, (425, 190))
            elif self.facade_cont == 4:
                window.blit(self.facade4, (425, 190))
            elif self.facade_cont == 5:
                window.blit(self.facade5, (425, 190))
            self.facade_counter += 1
            if self.facade_counter == self.facade_animation_counter:
                self.facade_counter = 0
                self.facade_cont += 1
    def desenha_metal(self, window, bool):
        if bool:
            if self.metal_cont == 1:
                window.blit(self.metal1, (425, 190))
            elif self.metal_cont == 2:
                window.blit(self.metal2, (425, 190))
            elif self.metal_cont == 3:
                window.blit(self.metal3, (425, 190))
            elif self.metal_cont == 4:
                window.blit(self.metal4, (425, 190))
            elif self.metal_cont == 5:
                window.blit(self.metal5, (425, 190))
            self.metal_counter += 1
            if self.metal_counter == self.metal_animation_counter:
                self.metal_counter = 0
                self.metal_cont += 1
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

    def desenha_fcut(self, window, bool):
        if bool:
            if self.fcut_cont == 1 or self.fcut_cont == 9:
                window.blit(self.cut1, (415, 175))
            elif self.fcut_cont == 2 or self.fcut_cont == 10:
                window.blit(self.cut2, (415, 175))
            elif self.fcut_cont == 3 or self.fcut_cont == 11:
                window.blit(self.cut3, (415, 175))
            elif self.fcut_cont == 4 or self.fcut_cont == 12:
                window.blit(self.cut4, (415, 175))
            if self.fcut_cont == 5 or self.fcut_cont == 13:
                window.blit(self.fcut1, (415, 175))
            elif self.fcut_cont == 6 or self.fcut_cont == 14:
                window.blit(self.fcut2, (415, 175))
            elif self.fcut_cont == 7 or self.fcut_cont == 15:
                window.blit(self.fcut3, (415, 175))
            elif self.fcut_cont == 8 or self.fcut_cont == 16:
                window.blit(self.fcut4, (415, 175))
            self.fcut_counter += 1
            if self.fcut_counter == self.fcut_animation_counter:
                self.fcut_counter = 0
                self.fcut_cont += 1