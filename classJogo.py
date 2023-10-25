import pygame
from constantes import *
from classGym import *
from classPersonagemGym import *
from classTreinadores import *
from classBatalhas import *
from classDesenhailha import *
from classPersonagemIlha import *

class Jogo:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('pokemon-gym')

        #TELAS
        self.window_ilha = pygame.display.set_mode((640, 600), vsync= True, flags=pygame.SCALED)
        self.window_gym = pygame.display.set_mode((640, 600), vsync= True, flags=pygame.SCALED)
        self.windowt1 = pygame.display.set_mode((640, 600), vsync= True, flags=pygame.SCALED)
        self.windowt2 = pygame.display.set_mode((640, 600), vsync= True, flags=pygame.SCALED)
        self.windowt3 = pygame.display.set_mode((640, 600), vsync= True, flags=pygame.SCALED)
        self.windowt4 = pygame.display.set_mode((640, 600), vsync= True, flags=pygame.SCALED)

        #INFOS TELA ILHA:
        self.rodando_jogo = True
        self.tela_ilha = True
        #INFOS TELA GYM:
        self.tela_gym_jogo = False
        #INFOS TELA BATALHA1:
        self.treinador_1 = False
        self.bol_batalha1 = False
        #INFOS TELA BATALHA2:
        self.treinador_2 = False
        #INFOS TELA BATALHA3:
        self.treinador_3 = False
        #INFOS TELA BATALHA4:
        self.treinador_4 = False

    def iniciar_jogo(self):
        tela_ilha = Desenha_ilha()
        personagem_ilha = Personagem_ilha()
        tela_gym = Desenha_fundo()
        personagem = Personagem()
        treinador1 = Treinador1()
        treinador2 = Treinador2()
        treinador3 = Treinardor3()
        treinador4 = Treinador4()
        batalha = Batalha()
        

        while self.rodando_jogo:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.rodando_jogo = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                    personagem.velocidade[1] += -2
                    personagem_ilha.velocidade[1] += -2

                elif event.type == pygame.KEYUP and event.key == pygame.K_w:
                    personagem.velocidade[1] += 2
                    personagem_ilha.velocidade[1] += 2

                elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                    personagem.velocidade[1] += 2
                    personagem_ilha.velocidade[1] += 2

                elif event.type == pygame.KEYUP and event.key == pygame.K_s:
                    personagem.velocidade[1] += -2
                    personagem_ilha.velocidade[1] += -2

                elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                    personagem.velocidade[0] += -2
                    personagem_ilha.velocidade[0] += -2

                elif event.type == pygame.KEYUP and event.key == pygame.K_a:
                    personagem.velocidade[0] += 2
                    personagem_ilha.velocidade[0] += 2

                elif event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                    personagem.velocidade[0] += 2
                    personagem_ilha.velocidade[0] += 2

                elif event.type == pygame.KEYUP and event.key == pygame.K_d:
                    personagem.velocidade[0] += -2
                    personagem_ilha.velocidade[0] += -2
                #Arrumar para nao mudar todas as telas
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                    batalha.botao = 1
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    batalha.botao = 2
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and batalha.botao == 1:
                    batalha.tela_atual = 'batalha'
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and batalha.tela_atual == 'batalha':
                    batalha.tela_atual = 'escolhendo'
                #TESTE
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    self.treinador_1 = False
                    self.tela_gym_jogo = True

            #verifica colisao no ginasio
            if not personagem.verifica_colisao(tela_gym.lista_paredes):
                personagem.pos_antiga = [personagem.rect.x, personagem.rect.y]
            else:
                personagem.rect.x = personagem.pos_antiga[0] 
                personagem.rect.y = personagem.pos_antiga[1] 
            #verifica colisao na ilha:
            if not personagem_ilha.verifica_colisao(tela_ilha.lista_paredes):
                personagem_ilha.pos_antiga = [personagem_ilha.rect.x, personagem_ilha.rect.y]
            else:
                personagem_ilha.rect.x = personagem_ilha.pos_antiga[0] 
                personagem_ilha.rect.y = personagem_ilha.pos_antiga[1]
            #altera tela ilha para tela gym:
            if personagem_ilha.rect.colliderect(tela_ilha.porta_gym) and self.tela_ilha:
                self.tela_ilha = False
                self.tela_gym_jogo = True
                personagem.rect.x = 198
                personagem.rect.y = 500
            elif personagem.rect.colliderect(tela_gym.porta_gym) and self.tela_gym_jogo:
                self.tela_gym_jogo = False
                self.tela_ilha = True
                personagem_ilha.rect.x = 205 
                personagem_ilha.rect.y = 523

            #altera telas de batalha:
            if treinador1.rect.colliderect(personagem.rect) and not self.bol_batalha1:
                self.tela_gym_jogo = False
                self.treinador_1 = True
                self.bol_batalha1 = True #teste para sair da batalha
            elif treinador2.rect.colliderect(personagem.rect):
                self.tela_gym_jogo = False
                self.treinador_2 = True
            elif treinador3.rect.colliderect(personagem.rect):
                self.tela_gym_jogo = False
                self.treinador_3 = True
            elif treinador4.rect.colliderect(personagem.rect):
                self.tela_gym_jogo = False
                self.treinador_4 = True


            if self.tela_ilha:
                tela_ilha.desenha_fundo(self.window_ilha)
                personagem_ilha.desenha_personagem(self.window_ilha)
                personagem_ilha.altera_sprite_vertical()
                personagem_ilha.altera_sprite_horizontal()

            elif self.tela_gym_jogo:
                tela_gym.desenha_mapa(self.window_gym)
                treinador1.desenha_treinador1(self.window_gym)
                treinador2.desenha_treinador2(self.window_gym)
                treinador3.desenha_treinador3(self.window_gym)
                treinador4.desenha_treinador4(self.window_gym)
                personagem.altera_sprite_vertical()
                personagem.altera_sprite_horizontal()
                personagem.desenha_personagem(self.window_gym)

            elif self.treinador_1:
                batalha.desenha_batalha(self.windowt1)
            elif self.treinador_2:
                batalha.desenha_batalha(self.windowt2)
            elif self.treinador_3:
                batalha.desenha_batalha(self.windowt3)
            elif self.treinador_4:
                batalha.desenha_batalha(self.windowt4)

            pygame.display.update()

game = Jogo()
game.iniciar_jogo()