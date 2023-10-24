import pygame
from constantes import *
from classGym import *
from classPersonagem import *

class Jogo:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('pokemon-gym')

        self.window_gym = pygame.display.set_mode((640, 600), vsync= True, flags=pygame.SCALED)
        self.personagem = pygame.transform.scale((pygame.image.load('img/personagem.png')),(30, 30))

        self.rodando_jogo = True
        self.tela_gym_jogo = True
        self.treinador_1 = False
        self.treinador_2 = False
        self.treinador_3 = False
        self.treinador_4 = False

    def iniciar_jogo(self):
        tela_gym = Desenha_fundo()
        personagem = Personagem()

        while self.rodando_jogo:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.rodando_jogo = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                        personagem.velocidade[1] += -1
                elif event.type == pygame.KEYUP and event.key == pygame.K_w:
                        personagem.velocidade[1] += 1
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                    personagem.velocidade[1] += 1
                elif event.type == pygame.KEYUP and event.key == pygame.K_s:
                    personagem.velocidade[1] += -1
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                    personagem.velocidade[0] += -1
                elif event.type == pygame.KEYUP and event.key == pygame.K_a:
                    personagem.velocidade[0] += 1
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                    personagem.velocidade[0] += 1
                elif event.type == pygame.KEYUP and event.key == pygame.K_d:
                    personagem.velocidade[0] += -1
            

            if not personagem.verifica_colisao(tela_gym.lista_paredes):
                personagem.pos_antiga = [personagem.rect.x, personagem.rect.y]
            else:
                personagem.rect.x = personagem.pos_antiga[0] 
                personagem.rect.y = personagem.pos_antiga[1] 

            if self.tela_gym_jogo:
                tela_gym.desenha_mapa(self.window_gym)
                personagem.altera_sprite_vertical()
                personagem.altera_sprite_horizontal()
                personagem.desenha_personagem(self.window_gym)
                

            pygame.display.update()

game = Jogo()
game.iniciar_jogo()