import pygame
from constantes import *

class Desenha_fundo:
    def __init__(self):
        self.fundo = pygame.transform.scale((pygame.image.load('img/map-gym.png')),(640, 600))
        self.lista_paredes = [
            pygame.Rect(380, 20, 233, 6),
            pygame.Rect(612, 20, 7, 90),
            pygame.Rect(575, 109, 44, 6),
            pygame.Rect(575, 109, 9, 30),
            pygame.Rect(536, 131, 41, 6),
            pygame.Rect(537, 131, 9, 113),
            pygame.Rect(307, 241, 238, 6),
            pygame.Rect(307, 155, 7, 90),
            pygame.Rect(257, 155, 50, 6),
            pygame.Rect(252, 155, 7, 127),
            pygame.Rect(252, 282, 330, 6),
            pygame.Rect(575, 282, 7, 45),
            pygame.Rect(465, 327, 120, 6),
            pygame.Rect(466, 327, 7, 200),
            pygame.Rect(419, 524, 54, 6),
            pygame.Rect(417, 482, 7, 47),
            pygame.Rect(290, 482, 127, 6),
            pygame.Rect(287, 482, 7, 65),
            pygame.Rect(250, 547, 45, 6),

        ]

    def desenha_mapa(self, window):
        window.blit(self.fundo, (0, 0))
        for parede in self.lista_paredes:
            pygame.draw.rect(window,PRETO, parede)
        


class Jogo:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('pokemon-gym')

        self.window_gym = pygame.display.set_mode((640, 600), vsync= True, flags=pygame.SCALED)
        self.personagem = pygame.transform.scale((pygame.image.load('img/personagem.png')),(30, 30))

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