import pygame
from constantes import *

class Desenha_fundo:
    def __init__(self):
        self.fundo = pygame.transform.scale((pygame.image.load('img/floor.png')),(640, 600))
        self.lista_paredes = [
            pygame.Rect(360, 25, 200, 10),
            pygame.Rect(560, 25, 10, 135),
        ]

    def desenha_mapa(self, window):
        window.blit(self.fundo, (0, 0))

        for parede in self.lista_paredes:
            pygame.draw.rect(window, PRETO, parede)



class Jogo:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('pokemon-gym')

        self.window_gym = pygame.display.set_mode((640, 600), vsync= True, flags=pygame.SCALED)


        self.rodando_jogo = True
        self.tela_gym = True
        self.treinador_1 = False
        self.treinador_2 = False
        self.treinador_3 = False
        self.treinador_4 = False

    def iniciar_jogo(self):
        tela_gym = Desenha_fundo()

        while self.rodando_jogo:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.rodando_jogo = False
        

            if self.tela_gym:
                tela_gym.desenha_mapa(self.window_gym)

            pygame.display.update()

game = Jogo()
game.iniciar_jogo()