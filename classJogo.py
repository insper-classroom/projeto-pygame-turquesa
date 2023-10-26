import pygame
from constantes import *
from classGym import *
from classPersonagemGym import *
from classTreinadores import *
from classBatalhas import *
from classDesenhailha import *
from classPersonagemIlha import *
from classDesenhaCura import *
from classPersonagemPc import *
from classDesenhainicio import *
from classDesenhaInstrucao import *

class Jogo:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('pokemon-gym')

        #TELAS
        self.tela_inicial = pygame.display.set_mode((640, 600), vsync= True, flags=pygame.SCALED)
        self.tela_instrucao = pygame.display.set_mode((640, 600), vsync= True, flags=pygame.SCALED)
        self.window_ilha = pygame.display.set_mode((640, 600), vsync= True, flags=pygame.SCALED)
        self.window_gym = pygame.display.set_mode((640, 600), vsync= True, flags=pygame.SCALED)
        self.window_pc = pygame.display.set_mode((640, 600), vsync= True, flags=pygame.SCALED)
        self.windowt1 = pygame.display.set_mode((640, 600), vsync= True, flags=pygame.SCALED)
        self.windowt2 = pygame.display.set_mode((640, 600), vsync= True, flags=pygame.SCALED)
        self.windowt3 = pygame.display.set_mode((640, 600), vsync= True, flags=pygame.SCALED)
        self.windowt4 = pygame.display.set_mode((640, 600), vsync= True, flags=pygame.SCALED)

        #INFOS TELA INICIAL:
        self.tela_inicio = True
        self.tela_instrucoes = False
        #INFOS TELA ILHA:
        self.rodando_jogo = True
        self.tela_ilha = False
        #tela centro pokemon:
        self.tela_pc = False
        #INFOS TELA GYM:
        self.tela_gym_jogo = False
        #INFOS TELA BATALHA1:
        self.treinador_1 = False
        self.bol_batalha1 = False
        #INFOS TELA BATALHA2:
        self.treinador_2 = False
        self.bol_batalha2 = False
        #INFOS TELA BATALHA3:
        self.treinador_3 = False
        self.bol_batalha3 = False
        #INFOS TELA BATALHA4:
        self.treinador_4 = False
        self.bol_batalha4 = False


    def iniciar_jogo(self):
        desenha_inicio = Inicio()
        desenha_instrucao = Instrucao()
        tela_ilha = Desenha_ilha()
        personagem_ilha = Personagem_ilha()
        tela_gym = Desenha_fundo()
        personagem = Personagem()
        #STATS TREINADOR1
        treinador1 = Treinador1()
        dicionario1 = treinador1.pokemons_treinador1()
        #STATS TREINADOR2
        treinador2 = Treinador2()
        dicionario2 = treinador2.pokemons_treinador2()
        #STATS TREINADOR3
        treinador3 = Treinardor3()
        dicionario3 = treinador3.pokemons_treinador3()
        #STATS TREINADOR4
        treinador4 = Treinador4()
        dicionario4 = treinador4.pokemons_treinador4()

        batalha = Batalha()
        desenha_cura = Cura_pokemon()
        personagem_pc = Personagem_pc()

        while self.rodando_jogo:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.rodando_jogo = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                    personagem.velocidade[1] += -2
                    personagem_ilha.velocidade[1] += -2
                    personagem_pc.velocidade[1] += -2

                elif event.type == pygame.KEYUP and event.key == pygame.K_w:
                    personagem.velocidade[1] += 2
                    personagem_ilha.velocidade[1] += 2
                    personagem_pc.velocidade[1] += 2

                elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                    personagem.velocidade[1] += 2
                    personagem_ilha.velocidade[1] += 2
                    personagem_pc.velocidade[1] += 2

                elif event.type == pygame.KEYUP and event.key == pygame.K_s:
                    personagem.velocidade[1] += -2
                    personagem_ilha.velocidade[1] += -2
                    personagem_pc.velocidade[1] += -2

                elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                    personagem.velocidade[0] += -2
                    personagem_ilha.velocidade[0] += -2
                    personagem_pc.velocidade[0] += -2

                elif event.type == pygame.KEYUP and event.key == pygame.K_a:
                    personagem.velocidade[0] += 2
                    personagem_ilha.velocidade[0] += 2
                    personagem_pc.velocidade[0] += 2

                elif event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                    personagem.velocidade[0] += 2
                    personagem_ilha.velocidade[0] += 2
                    personagem_pc.velocidade[0] += 2

                elif event.type == pygame.KEYUP and event.key == pygame.K_d:
                    personagem.velocidade[0] += -2
                    personagem_ilha.velocidade[0] += -2
                    personagem_pc.velocidade[0] += -2
                #Verifica click do mouse
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if desenha_cura.verifica_click_sim(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                        print('sim')
                    elif desenha_cura.verifica_click_nao(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                        personagem_pc.rect.x = 305
                        personagem_pc.rect.y = 410
                    elif desenha_inicio.verifica_click_sim(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                        self.tela_inicio = False
                        self.tela_instrucoes = True
                    elif desenha_instrucao.verifica_click_sim(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                        self.tela_instrucoes =  False
                        self.tela_ilha = True
                #Arrumar para nao mudar todas as telas
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT and batalha.tela_atual == 'escolhendo':
                    batalha.botao = 1
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT and batalha.tela_atual == 'escolhendo':
                    batalha.botao = 2
                if event.type == pygame.KEYDOWN and batalha.tela_atual =='batalha':
                    if self.treinador_1:
                        batalha.botoes_batalha(event, dicionario1, self.windowt1)
                    elif self.treinador_2:
                        batalha.botoes_batalha(event, dicionario2, self.windowt2)
                    elif self.treinador_3:
                        batalha.botoes_batalha(event, dicionario3, self.windowt3)
                    elif self.treinador_4:
                        batalha.botoes_batalha(event, dicionario4, self.windowt4)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and batalha.botao == 1:
                    batalha.tela_atual = 'batalha'
                    batalha.botao = 1
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and batalha.tela_atual == 'batalha':
                    batalha.tela_atual = 'escolhendo'
                    batalha. botao = 1

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
            #verifica colisao no pc:
            if not personagem_pc.verifica_colisao(desenha_cura.lista_paredes):
                personagem_pc.pos_antiga = [personagem_pc.rect.x, personagem_pc.rect.y]
            else:
                personagem_pc.rect.x = personagem_pc.pos_antiga[0] 
                personagem_pc.rect.y = personagem_pc.pos_antiga[1]

            #verifica colisao com a porta ilha p gym:
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

            #verifica colisao com a porta ilha p pc:
            if personagem_ilha.rect.colliderect(tela_ilha.porta_pc) and self.tela_ilha:
                self.tela_ilha = False
                self.tela_pc = True
                personagem_pc.rect.x = 305
                personagem_pc.rect.y = 410
            elif personagem_pc.rect.colliderect(desenha_cura.porta_pc) and self.tela_pc:
                self.tela_pc = False
                self.tela_ilha = True
                personagem_ilha.rect.x = 63
                personagem_ilha.rect.y = 326

            #altera telas de batalha:
            if treinador1.rect.colliderect(personagem.rect) and not self.bol_batalha1:
                self.tela_gym_jogo = False
                self.treinador_1 = True
                # self.bol_batalha1 = True #teste para sair da batalha
            elif treinador2.rect.colliderect(personagem.rect) and not self.bol_batalha2:
                self.tela_gym_jogo = False
                self.treinador_2 = True
            elif treinador3.rect.colliderect(personagem.rect) and not self.bol_batalha3:
                self.tela_gym_jogo = False
                self.treinador_3 = True
            elif treinador4.rect.colliderect(personagem.rect) and not self.bol_batalha4:
                self.tela_gym_jogo = False
                self.treinador_4 = True
            if self.tela_inicio:
                desenha_inicio.desenha_inicio(self.tela_inicial)

            elif self.tela_instrucoes:
                desenha_instrucao.desenha_inicio(self.tela_inicial)
                
            elif self.tela_ilha:
                tela_ilha.desenha_fundo(self.window_ilha)
                personagem_ilha.desenha_personagem(self.window_ilha)
                personagem_ilha.altera_sprite_vertical()
                personagem_ilha.altera_sprite_horizontal()

            elif self.tela_pc:
                desenha_cura.desenha_pc(self.window_pc)
                personagem_pc.desenha_personagem(self.window_pc)
                personagem_pc.altera_sprite_vertical()
                personagem_pc.altera_sprite_horizontal()
                if personagem_pc.rect.colliderect(desenha_cura.balcao):
                    desenha_cura.desenha_box(self.window_pc)

            elif self.tela_gym_jogo:
                tela_gym.desenha_mapa(self.window_gym)
                treinador1.desenha_treinador1(self.window_gym)
                treinador2.desenha_treinador2(self.window_gym)
                treinador3.desenha_treinador3(self.window_gym)
                treinador4.desenha_treinador4(self.window_gym)
                personagem.desenha_personagem(self.window_gym)
                personagem.altera_sprite_vertical()
                personagem.altera_sprite_horizontal()

            elif self.treinador_1:
                batalha.desenha_batalha(self.windowt1,dicionario1)
            elif self.treinador_2:
                batalha.desenha_batalha(self.windowt2, dicionario2)
            elif self.treinador_3:
                batalha.desenha_batalha(self.windowt3, dicionario3)
            elif self.treinador_4:
                batalha.desenha_batalha(self.windowt4, dicionario4)
            #Alteração de tela no fim da batalha
            if batalha.tela_atual == 'fim':
                self.tela_gym_jogo = True
                if self.treinador_1 == True:
                    self.bol_batalha1 = True
                    self.treinador_1 = False
                    personagem.rect.x = 198
                    personagem.rect.y = 500
                if self.treinador_2 == True:
                    self.bol_batalha2 = True
                    self.treinador_2 = False
                    personagem.rect.x = 198
                    personagem.rect.y = 500
                if self.treinador_3 == True:
                    self.bol_batalha3 = True
                    self.treinador_3 = False
                    personagem.rect.x = 198
                    personagem.rect.y = 500
                if self.treinador_4 == True:
                    self.bol_batalha4 = True
                    self.treinador_4 = False
                    personagem.rect.x = 198
                    personagem.rect.y = 500
                batalha.tela_atual = 'escolhendo'
            pygame.display.update()

game = Jogo()
game.iniciar_jogo()