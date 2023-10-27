import pygame
import time
class Batalha:
    def __init__(self):
        self.fonte = pygame.font.Font('imgBatalhas/fontes.ttf', 20)
        self.fonteMenu = pygame.font.Font('imgBatalhas/fontes.ttf', 50)
        self.fonteBatalha = pygame.font.Font('imgBatalhas/fontes.ttf', 25)
        self.lista_imagens = [
            pygame.transform.scale((pygame.image.load('img/Ataques pokemon.png')),(640, 150)),
            pygame.transform.scale((pygame.image.load('img/template.png')),(330, 60)),
            pygame.transform.scale((pygame.image.load('imgBatalhas/barraSemVida.png')),(290, 80)),
            pygame.transform.scale((pygame.image.load('imgBatalhas/seta.png')),(40, 40)),
            pygame.transform.scale((pygame.image.load('imgBatalhas/barraVazia.png')),(640, 150)),
            pygame.transform.scale((pygame.image.load('imgBatalhas/seta.png')),(20, 20)),
            pygame.transform.scale((pygame.image.load('img/Makuhita.webp')),(150,150)),
            pygame.transform.scale((pygame.image.load('img/pikachujogador.png')),(200,200))
        ]
        tackle = {'dano': 30, 'precisao': 100, 'tipo': 'normal', 'pps': 30, 'nome': 'Tackle'}
        facade = {'dano': 70, 'precisao': 100, 'tipo': 'normal', 'pps': 10, 'nome': 'Facade'}
        slam = {'dano': 30, 'precisao': 100, 'tipo': 'normal', 'pps': 35, 'nome': 'Slam'}
        thunderbolt = {'dano': 30, 'precisao': 100, 'tipo': 'eletrico', 'pps': 35, 'nome': 'Thunderbolt'}
        self.pokemons = {
            'PIKACHU': {'vida': 270, 'vida_max': 270, 'ataques': [tackle, thunderbolt, slam, facade]},
        }
        self.botao = 1
        self.inimigo_compara = 0
        self.tela_atual = 'escolhendo'
    
    def desenha_batalha(self, window, dicionario):
        if dicionario['vida_pokemon'] < 0:
            dicionario['vida_pokemon'] = 0
        window.fill((188, 188, 188))
        window.blit(self.lista_imagens[1], (0, 400))
        window.blit(self.lista_imagens[2], (40, 90))
        window.blit(self.lista_imagens[2], (310, 290))
        window.blit(self.lista_imagens[1], (290, 230))
        window.blit(self.lista_imagens[6], (370, 130))
        if dicionario['vida_pokemon'] > 0:
            window.blit(self.lista_imagens[7], (30, 300))
        blit_inimigo = self.fonte.render(f'MAKUHITA: {dicionario["vida_pokemon"]}/{dicionario["vidamax_pokemon"]}', True, (0, 0, 0))
        window.blit(blit_inimigo, (80, 115))
        blit_jogador = self.fonte.render(f'PIKACHU: {self.pokemons["PIKACHU"]["vida"]}/{self.pokemons["PIKACHU"]["vida_max"]}', True, (0, 0, 0))
        window.blit(blit_jogador, (350, 310))
        if self.tela_atual == 'texto_batalha':
            window.blit(self.lista_imagens[4], (0, 450))
            ataque1 = self.fonteBatalha.render(f"PIKACHU used {self.pokemons['PIKACHU']['ataques'][self.botao - 1]['nome']}!", True, (0,0,0))
            window.blit(ataque1, (50, 475))
            pygame.display.update()
            time.sleep(1)
            if dicionario['vida_pokemon'] > 0:
                window.blit(self.lista_imagens[4], (0, 450))
                ataque1 = self.fonteBatalha.render("Foe MAKUHITA used Tackle!", True, (0,0,0))
                self.pokemons["PIKACHU"]["vida"] -= 30
                window.blit(ataque1, (50, 475))
                pygame.display.update()
                time.sleep(1)
            if self.pokemons["PIKACHU"]["vida"] <= 0:
                self.tela_atual = 'morte'
                morte = self.fonteBatalha.render("PIKACHU Fainted!", True, (0,0,0))
                window.blit(morte, (50, 475))
                pygame.display.update()
                time.sleep(1)
            elif dicionario['vida_pokemon'] <= 0:
                self.tela_atual = 'vitória'
            else:
                self.tela_atual = 'escolhendo'
                self.botao = 1
        elif self.tela_atual == 'escolhendo':
            window.blit(self.lista_imagens[4], (0, 450))
            text_menu = self.fonteMenu.render('FIGHT', True, (0, 0, 0))
            window.blit(text_menu, (80, 485))
            text_pokemon = self.fonteMenu.render('POKéMON', True, (0, 0, 0))
            window.blit(text_pokemon, (330, 485))
            if self.botao == 1:
                window.blit(self.lista_imagens[3], (40, 505))
            if self.botao == 2:
                window.blit(self.lista_imagens[3], (290, 505))
        elif self.tela_atual == 'batalha':
            window.blit(self.lista_imagens[0], (0, 450))
            ataque1 = self.fonteBatalha.render("Tackle", True, (0,0,0))
            ataque2 = self.fonteBatalha.render("Thunderbolt", True, (0,0,0))
            ataque3 = self.fonteBatalha.render("Slam", True, (0,0,0))
            ataque4 = self.fonteBatalha.render("Facade", True, (0,0,0))
            window.blit(ataque1, (40, 475))
            window.blit(ataque2, (220, 475))
            window.blit(ataque3, (220, 525))
            window.blit(ataque4, (40, 525))
            if self.botao == 1:
                window.blit(self.lista_imagens[5], (20, 488))
            elif self.botao == 2:
                window.blit(self.lista_imagens[5], (200, 488))
            elif self.botao == 3:
                window.blit(self.lista_imagens[5], (200, 538))
            elif self.botao == 4:
                window.blit(self.lista_imagens[5], (20, 538))
        elif self.tela_atual =='vitória':
            window.blit(self.lista_imagens[4], (0, 450))
            morte = self.fonteBatalha.render("Foe MAKUHITA Fainted!", True, (0,0,0))
            window.blit(morte, (50, 475))
            pygame.display.update()
            time.sleep(1)
            self.tela_atual = 'fim'
        self.inimigo_compara = dicionario['vidamax_pokemon']

    def botoes_batalha(self, event, dicionario, window):
        if event.type == pygame.KEYDOWN and self.botao == 1 and event.key == pygame.K_RIGHT:
            self.botao = 2
        elif event.type == pygame.KEYDOWN and self.botao == 1 and event.key == pygame.K_DOWN:
            self.botao = 4
        elif event.type == pygame.KEYDOWN and self.botao == 2 and event.key == pygame.K_LEFT:
            self.botao = 1
        elif event.type == pygame.KEYDOWN and self.botao == 2 and event.key == pygame.K_DOWN:
            self.botao = 3
        elif event.type == pygame.KEYDOWN and self.botao == 3 and event.key == pygame.K_LEFT:
            self.botao = 4
        elif event.type == pygame.KEYDOWN and self.botao == 3 and event.key == pygame.K_UP:
            self.botao = 2
        elif event.type == pygame.KEYDOWN and self.botao == 4 and event.key == pygame.K_RIGHT:
            self.botao = 3
        elif event.type == pygame.KEYDOWN and self.botao == 4 and event.key == pygame.K_UP:
            self.botao = 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and self.botao == 1:
            dicionario['vida_pokemon'] -= 40
            self.tela_atual = 'texto_batalha'
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and self.botao == 2:
            dicionario['vida_pokemon'] -= 95
            self.tela_atual = 'texto_batalha'
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and self.botao == 3:
            dicionario['vida_pokemon'] -= 80
            self.tela_atual = 'texto_batalha'
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and self.botao == 4:
            dicionario['vida_pokemon'] -= 70
            self.tela_atual = 'texto_batalha'
    