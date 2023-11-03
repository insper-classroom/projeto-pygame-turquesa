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
from classFundoHp import *
from classDesenhaAvisogym import *
from classAnimacoes import *

class Jogo:
    def __init__(self):
        '''
            Classe responsável por armazenar todas as informações necessarias para o funcionamento do jogo,
            inclusive todos argumentos solicitados pelas funcoes chamadas.
        '''
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
        self.windowHP = pygame.display.set_mode((640, 600), vsync= True, flags=pygame.SCALED)
        #Fonte:
        self.fonte = pygame.font.Font('imgBatalhas/fontes.ttf', 15)
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
        #INFOS TELA hp:
        self.tela_hp = False
        #BOLEANOS MUSICAS:

        self.inicial_tocando = False
        self.ilha_tocando = False
        self.batalha_tocando = False
        self.lider_tocando = False
        self.musica_gym = False
        self.musica_pc = False
        #BOLEANO AVISO:
        self.aviso_vida = False

    def iniciar_jogo(self):
        '''
            Função que inicia o jogo, chamando todas as classes e funções necessarias para o funcionamento do jogo
            verificando a logica de qual tela deve ser desenhada no momento, a função é responsavel tambem por receber
            todos os inputs, para um melhor entendimento, toda classe/funcao chamada está DOCUMENTADA, e pode ser 
            explicada por meio de DOCSTRINGS.
        '''
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

        tela_hp = Telahp()
        avisos = Avisos()
        animacao = Animacao()

        while self.rodando_jogo:
            
            #SISTEMA DE MUSICA:
            if self.tela_inicio and not self.inicial_tocando:
                pygame.mixer.music.load('snd/tela-inicial.wav')
                pygame.mixer.music.play(-1)
                self.inicial_tocando = True
            elif self.tela_ilha and not self.ilha_tocando:
                pygame.mixer.music.stop()
                self.inicial_tocando = False
                pygame.mixer.music.load('snd/musica-cidade.wav')
                pygame.mixer.music.play(-1)
                self.musica_pc = False
                self.ilha_tocando = True
                self.musica_gym = False
            elif self.tela_gym_jogo and not self.musica_gym:
                pygame.mixer.music.stop()
                self.ilha_tocando = False
                pygame.mixer.music.load('snd/musica-gym.wav')
                pygame.mixer.music.play(-1)
                self.batalha_tocando = False
                self.lider_tocando = False
                self.musica_gym = True
            elif self.treinador_1 and not self.batalha_tocando:
                pygame.mixer.music.stop()
                pygame.mixer.music.load('snd/batalha-comum.wav')
                pygame.mixer.music.play(-1)
                self.musica_gym = False
                self.batalha_tocando = True
            elif self.treinador_2 and not self.batalha_tocando:
                pygame.mixer.music.stop()
                pygame.mixer.music.load('snd/batalha-comum.wav')
                pygame.mixer.music.play(-1)
                self.musica_gym = False
                self.batalha_tocando = True
            elif self.treinador_3 and not self.batalha_tocando:
                pygame.mixer.music.stop()
                pygame.mixer.music.load('snd/batalha-comum.wav')
                pygame.mixer.music.play(-1)
                self.musica_gym = False
                self.batalha_tocando = True
            elif self.treinador_4 and not self.lider_tocando:
                pygame.mixer.music.stop()
                self.batalha_tocando = False
                pygame.mixer.music.load('snd/batalha-lider.wav')
                pygame.mixer.music.play(-1)
                self.musica_gym = False
                self.lider_tocando = True
            elif self.tela_pc and not self.musica_pc:
                pygame.mixer.music.stop()
                pygame.mixer.music.load('snd/pokemon-center.wav')
                pygame.mixer.music.play(-1)
                self.ilha_tocando = False
                self.musica_pc = True


            #EVENTOS / INPUTS:
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
                        batalha.pokemons[0]['vida'] = 290
                        batalha.pokemons[1]['vida'] = 250
                        batalha.pokemons[2]['vida'] = 330
                    elif desenha_cura.verifica_click_nao(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                        personagem_pc.rect.x = 305
                        personagem_pc.rect.y = 410
                    elif desenha_inicio.verifica_click_sim(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                        self.tela_inicio = False
                        self.tela_instrucoes = True
                    elif desenha_instrucao.verifica_click_sim(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                        self.tela_instrucoes =  False
                        self.tela_ilha = True
                    elif tela_hp.verifica_click_sim(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                        self.tela_hp = False
                        self.tela_pc = True

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
                if batalha.tela_atual != 'animando' or batalha.tela_atual != 'texto_batalha':
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and batalha.botao == 1 and batalha.atacou == False:
                        batalha.tela_atual = 'batalha'
                        batalha.botao = 1
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and batalha.tela_atual == 'batalha':
                        batalha.tela_atual = 'escolhendo'
                        batalha.botao = 1
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and batalha.botao == 2 and batalha.tela_atual == 'escolhendo':
                        if batalha.pokemonatual == 0 and batalha.pokemons[1]['vida'] <= 0 and batalha.pokemons[2]['vida'] > 0:
                            batalha.pokemonatual = 2
                        elif batalha. pokemons[1]['vida'] > 0 and batalha.pokemonatual == 0:
                            batalha.pokemonatual = 1
                        elif batalha.pokemonatual == 1 and batalha.pokemons[2]['vida'] <= 0 and batalha.pokemons[0]['vida'] > 0:
                            batalha.pokemonatual = 0
                        elif batalha.pokemons[2]['vida'] > 0 and batalha.pokemonatual == 1:
                            batalha.pokemonatual = 2
                        elif batalha.pokemonatual == 2 and batalha.pokemons[0]['vida'] <= 0 and batalha.pokemons[1]['vida'] > 0:
                            batalha.pokemonatual = 1
                        elif batalha.pokemons[0]['vida'] > 0 and batalha.pokemonatual == 2:
                            batalha.pokemonatual = 0

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
                if (batalha.pokemons[0]['vida'] > 0 or batalha.pokemons[1]['vida'] > 0 or batalha.pokemons[2]['vida'] > 0):
                    self.tela_gym_jogo = False
                    self.treinador_1 = True
                    # self.aviso_vida = False
                else:
                    self.aviso_vida = True       
            elif treinador2.rect.colliderect(personagem.rect) and not self.bol_batalha2:
                if (batalha.pokemons[0]['vida'] > 0 or batalha.pokemons[1]['vida'] > 0 or batalha.pokemons[2]['vida'] > 0):
                    self.tela_gym_jogo = False
                    self.treinador_2 = True
                else:
                    self.aviso_vida = True
            elif treinador3.rect.colliderect(personagem.rect) and not self.bol_batalha3:
                if (batalha.pokemons[0]['vida'] > 0 or batalha.pokemons[1]['vida'] > 0 or batalha.pokemons[2]['vida'] > 0):                        
                    self.tela_gym_jogo = False
                    self.treinador_3 = True
                else:
                    self.aviso_vida = True
            elif treinador4.rect.colliderect(personagem.rect) and not self.bol_batalha4:
                if (batalha.pokemons[0]['vida'] > 0 or batalha.pokemons[1]['vida'] > 0 or batalha.pokemons[2]['vida'] > 0):
                    self.tela_gym_jogo = False
                    self.treinador_4 = True
                else:
                    self.aviso_vida = True
            else:
                self.aviso_vida = False

            #desenha telas:
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
                elif personagem_pc.rect.colliderect(desenha_cura.rect_pc):
                    self.tela_pc = False
                    self.tela_hp = True
                    personagem_pc.rect.x = 468
                    personagem_pc.rect.y = 240
                
            elif self.tela_gym_jogo:
                tela_gym.desenha_mapa(self.window_gym)
                treinador1.desenha_treinador1(self.window_gym, self.bol_batalha1)
                treinador2.desenha_treinador2(self.window_gym, self.bol_batalha2)
                treinador3.desenha_treinador3(self.window_gym, self.bol_batalha3)
                treinador4.desenha_treinador4(self.window_gym, self.bol_batalha4)
                personagem.desenha_personagem(self.window_gym)
                personagem.altera_sprite_vertical()
                personagem.altera_sprite_horizontal()
                avisos.aviso_vida(self.window_gym, self.aviso_vida)

            elif self.treinador_1:
                batalha.desenha_batalha(self.windowt1,dicionario1)
                animacao.desenha_slude(self.windowt1, batalha.sludge_bol)
                animacao.desenha_thunder(self.windowt1, batalha.thunder_bol)
                animacao.desenha_leaf(self.windowt1, batalha.leaf_bol)
                if animacao.slude_rect.x > 439:
                    batalha.sludge_bol = False
                    animacao.slude_rect.x = 160
                    animacao.slude_rect.y = 330
                    batalha.tela_atual = 'texto_batalha'
                elif animacao.thunder_rect_x >= 535:
                    batalha.thunder_bol = False
                    animacao.thunder_rect_x = 385
                    batalha.tela_atual = 'texto_batalha'
                elif batalha.tackle_bol == True:
                    animacao.desenha_tackle(self.windowt1, batalha.tackle_bol)
                    if animacao.tackle_cont * 3 > 9:
                        batalha.tackle_bol = False
                        batalha.tela_atual = 'texto_batalha'
                        animacao.tackle_cont = 0
                elif batalha.cut_bol == True:
                    animacao.desenha_cut(self.windowt1, batalha.cut_bol)
                    if animacao.cut_cont * 4 > 20:
                        batalha.cut_bol = False
                        batalha.tela_atual = 'texto_batalha'
                        animacao.cut_cont = 0
                elif animacao.leaf_rect.x > 439:
                    batalha.leaf_bol = False
                    animacao.leaf_rect.x = 160
                    animacao.leaf_rect.y = 330
                    batalha.tela_atual = 'texto_batalha'
            elif self.treinador_2:
                batalha.desenha_batalha(self.windowt2, dicionario2)
                animacao.desenha_slude(self.windowt2, batalha.sludge_bol)
                animacao.desenha_thunder(self.windowt2, batalha.thunder_bol)
                animacao.desenha_leaf(self.windowt2, batalha.leaf_bol)
                if animacao.slude_rect.x > 439:
                    batalha.sludge_bol = False
                    animacao.slude_rect.x = 160
                    animacao.slude_rect.y = 330
                    batalha.tela_atual = 'texto_batalha'
                elif animacao.thunder_rect_x >= 535:
                    batalha.thunder_bol = False
                    animacao.thunder_rect_x = 385
                    batalha.tela_atual = 'texto_batalha'
                    animacao.tackle_cont = 0
                elif batalha.tackle_bol == True:
                    animacao.desenha_tackle(self.windowt2, batalha.tackle_bol)
                    if animacao.tackle_cont * 3 > 9:
                        batalha.tackle_bol = False
                        batalha.tela_atual = 'texto_batalha'
                        animacao.tackle_cont = 0
                elif batalha.cut_bol == True:
                    animacao.desenha_cut(self.windowt2, batalha.cut_bol)
                    if animacao.cut_cont * 4 > 20:
                        batalha.cut_bol = False
                        batalha.tela_atual = 'texto_batalha'
                        animacao.cut_cont = 0
                elif animacao.leaf_rect.x > 439:
                    batalha.leaf_bol = False
                    animacao.leaf_rect.x = 160
                    animacao.leaf_rect.y = 330
                    batalha.tela_atual = 'texto_batalha'
            elif self.treinador_3:
                batalha.desenha_batalha(self.windowt3, dicionario3)
                animacao.desenha_slude(self.windowt3, batalha.sludge_bol)
                animacao.desenha_thunder(self.windowt3, batalha.thunder_bol)
                animacao.desenha_leaf(self.windowt3, batalha.leaf_bol)
                if animacao.slude_rect.x > 439:
                    batalha.sludge_bol = False
                    animacao.slude_rect.x = 160
                    animacao.slude_rect.y = 330
                    batalha.tela_atual = 'texto_batalha'
                elif animacao.thunder_rect_x >= 535:
                    batalha.thunder_bol = False
                    animacao.thunder_rect_x = 385
                    batalha.tela_atual = 'texto_batalha'
                elif batalha.tackle_bol == True:
                    animacao.desenha_tackle(self.windowt3, batalha.tackle_bol)
                    if animacao.tackle_cont * 3 > 9:
                        batalha.tackle_bol = False
                        batalha.tela_atual = 'texto_batalha'
                        animacao.tackle_cont = 0
                elif batalha.cut_bol == True:
                    animacao.desenha_cut(self.windowt3, batalha.cut_bol)
                    if animacao.cut_cont * 4 > 20:
                        batalha.cut_bol = False
                        batalha.tela_atual = 'texto_batalha'
                        animacao.cut_cont = 0
                elif animacao.leaf_rect.x > 439:
                    batalha.leaf_bol = False
                    animacao.leaf_rect.x = 160
                    animacao.leaf_rect.y = 330
                    batalha.tela_atual = 'texto_batalha'
            elif self.treinador_4:
                batalha.desenha_batalha(self.windowt4, dicionario4)
                animacao.desenha_slude(self.windowt4, batalha.sludge_bol)
                animacao.desenha_thunder(self.windowt4, batalha.thunder_bol)
                animacao.desenha_leaf(self.windowt4, batalha.leaf_bol)
                if animacao.slude_rect.x > 439:
                    batalha.sludge_bol = False
                    animacao.slude_rect.x = 160
                    animacao.slude_rect.y = 330
                    batalha.tela_atual = 'texto_batalha'
                elif animacao.thunder_rect_x >= 535:
                    batalha.thunder_bol = False
                    animacao.thunder_rect_x = 385
                    batalha.tela_atual = 'texto_batalha'
                elif batalha.tackle_bol == True:
                    animacao.desenha_tackle(self.windowt4, batalha.tackle_bol)
                    if animacao.tackle_cont * 3 > 9:
                        batalha.tackle_bol = False
                        batalha.tela_atual = 'texto_batalha'
                        animacao.tackle_cont = 0
                elif batalha.cut_bol == True:
                    animacao.desenha_cut(self.windowt4, batalha.cut_bol)
                    if animacao.cut_cont * 4 > 20:
                        batalha.cut_bol = False
                        batalha.tela_atual = 'texto_batalha'
                        animacao.cut_cont = 0
                elif animacao.leaf_rect.x > 439:
                    batalha.leaf_bol = False
                    animacao.leaf_rect.x = 160
                    animacao.leaf_rect.y = 330
                    batalha.tela_atual = 'texto_batalha'
            elif self.tela_hp:
                tela_hp.desenha(self.windowHP)
                vida_1 = self.fonte.render(str(batalha.pokemons[1]['vida']), True, BRANCO)
                vida_2 = self.fonte.render(str(batalha.pokemons[2]['vida']), True, BRANCO)
                vida_3 = self.fonte.render(str(batalha.pokemons[0]['vida']), True, BRANCO)
                self.windowHP.blit(vida_1, (173, 176))
                self.windowHP.blit(vida_2, (511, 302))
                self.windowHP.blit(vida_3, (189, 422))
                
                #Desenhar as infos aqui

            #Alteração de tela no fim da batalha
            if batalha.tela_atual == 'fim':
                if self.treinador_1 == True:
                    if (batalha.pokemons[0]['vida'] > 0 or batalha.pokemons[1]['vida'] > 0 or batalha.pokemons[2]['vida'] > 0):
                        self.bol_batalha1 = True
                        self.treinador_1 = False
                    personagem.rect.x = 36
                    personagem.rect.y = 152
                if self.treinador_2 == True:
                    if (batalha.pokemons[0]['vida'] > 0 or batalha.pokemons[1]['vida'] > 0 or batalha.pokemons[2]['vida'] > 0):
                        self.bol_batalha2 = True
                        self.treinador_2 = False
                    personagem.rect.x = 430
                    personagem.rect.y = 454
                if self.treinador_3 == True:
                    if (batalha.pokemons[0]['vida'] > 0 or batalha.pokemons[1]['vida'] > 0 or batalha.pokemons[2]['vida'] > 0):
                        self.bol_batalha3 = True
                        self.treinador_3 = False
                    personagem.rect.x = 72
                    personagem.rect.y = 294
                if self.treinador_4 == True:
                    if (batalha.pokemons[0]['vida'] > 0 or batalha.pokemons[1]['vida'] > 0 or batalha.pokemons[2]['vida'] > 0):
                        self.bol_batalha4 = True
                        self.treinador_4 = False
                    personagem.rect.x = 486
                    personagem.rect.y = 132
                self.treinador_1 = False
                self.treinador_2 = False
                self.treinador_3 = False
                self.treinador_4 = False
                self.tela_gym_jogo = True
                batalha.tela_atual = 'escolhendo'

            pygame.display.update()

game = Jogo()
game.iniciar_jogo()