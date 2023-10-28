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
            pygame.transform.scale((pygame.image.load('img/Makuhita.webp')),(200,200)),
            pygame.transform.scale((pygame.image.load('img/pikachujogador.png')),(200,200)),
            pygame.transform.scale((pygame.image.load('img/scizor.png')),(200,200)),
            pygame.transform.scale((pygame.image.load('img/venusaur.png')),(200,200)),
        ]
        tackle = {'dano': 30, 'precisao': 100, 'tipo': 'normal', 'pps': 30, 'nome': 'Tackle'}
        facade = {'dano': 50, 'precisao': 100, 'tipo': 'normal', 'pps': 10, 'nome': 'Facade'}
        slam = {'dano': 35, 'precisao': 100, 'tipo': 'normal', 'pps': 35, 'nome': 'Slam'}
        thunderbolt = {'dano': 55, 'precisao': 100, 'tipo': 'eletrico', 'pps': 35, 'nome': 'Thunderbolt'}
        cut = {'dano': 30, 'precisao': 95, 'tipo': 'normal', 'pps': 20, 'nome': 'Cut'}
        fury_cutter = {'dano': 40, 'precisao': 95, 'tipo': 'inseto', 'pps': 15, 'nome': 'Fury Cutter'}
        metal_claw = {'dano': 50, 'precisao': 95, 'tipo': 'metal', 'pps': 30, 'nome': 'Metal Claw'}
        pursuit = {'dano': 40, 'precisao': 100, 'tipo': 'escuridao', 'pps': 20, 'nome': 'Pursuit'}
        sludge_bomb = {'dano': 60, 'precisao': 100, 'tipo': 'veneno', 'pps': 10, 'nome': 'Sludge Bomb'}
        razor_leaf = {'dano': 35, 'precisao': 95, 'tipo': 'grama', 'pps': 25, 'nome': 'Razor Leaf'}
        earthquake = {'dano': 60, 'precisao': 100, 'tipo': 'Terra', 'pps': 10, 'nome': 'Earthquake'}
        cut = {'dano': 30, 'precisao': 95, 'tipo': 'normal', 'pps': 20, 'nome': 'Cut'}
        self.pokemons = [
            {'vida': 20, 'vida_max': 290, 'ataques': [tackle, thunderbolt, slam, facade], 'nome': 'PIKACHU'},
            {'vida': 20, 'vida_max': 270, 'ataques': [cut, fury_cutter, metal_claw, pursuit], 'nome': 'SCIZOR'},
            {'vida': 30, 'vida_max': 350, 'ataques': [razor_leaf, sludge_bomb, earthquake, cut], 'nome': 'VENUSAUR'},
        ]
        self.pokemonatual = 0
        self.botao = 1
        self.inimigo_compara = 0
        self.tela_atual = 'escolhendo'
    def desenha_batalha(self, window, dicionario):
        #EVITA VIDA NEGATIVA
        if dicionario['vida_pokemon'] < 0:
            dicionario['vida_pokemon'] = 0
        if self.pokemons[self.pokemonatual]['vida'] < 0:
            self.pokemons[self.pokemonatual]['vida'] = 0
        #DESENHA A TELA DA BATALHA
        window.fill((188, 188, 188))
        window.blit(self.lista_imagens[1], (0, 400))
        window.blit(self.lista_imagens[2], (40, 90))
        window.blit(self.lista_imagens[2], (310, 290))
        window.blit(self.lista_imagens[1], (290, 230))
        window.blit(self.lista_imagens[7 + self.pokemonatual], (30, 300))
        #PARA DE DESENHAR O POKEMON INIMIGO SE ELE MORRER
        if dicionario['vida_pokemon'] > 0:
            window.blit(self.lista_imagens[6], (370, 130))
        #DESENHA A VIDA DOS POKEMONS
        blit_inimigo = self.fonte.render(f'{dicionario["nome"]}: {dicionario["vida_pokemon"]}/{dicionario["vida_max"]}', True, (0, 0, 0))
        window.blit(blit_inimigo, (80, 115))
        blit_jogador = self.fonte.render(f'{self.pokemons[self.pokemonatual]["nome"]}: {self.pokemons[self.pokemonatual]["vida"]}/{self.pokemons[0]["vida_max"]}', True, (0, 0, 0))
        window.blit(blit_jogador, (350, 310))
        #DESENHA O ATAQUE DO JOGADOR
        if self.tela_atual == 'texto_batalha':
            window.blit(self.lista_imagens[4], (0, 450))
            ataque1 = self.fonteBatalha.render(f"{self.pokemons[self.pokemonatual]['nome']} used {self.pokemons[self.pokemonatual]['ataques'][self.botao - 1]['nome']}!", True, (0,0,0))
            window.blit(ataque1, (50, 475))
            pygame.display.update()
            time.sleep(1)
            #ATAQUE DO INIMIGO
            if dicionario['vida_pokemon'] > 0:
                window.blit(self.lista_imagens[4], (0, 450))
                ataque1 = self.fonteBatalha.render("Foe MAKUHITA used Tackle!", True, (0,0,0))
                self.pokemons[self.pokemonatual]["vida"] -= 30
                window.blit(ataque1, (50, 475))
                pygame.display.update()
                time.sleep(1)
            if self.pokemons[self.pokemonatual]['vida'] <= 0:
                if self.pokemons[self.pokemonatual]['vida'] < 0:
                    self.pokemons[self.pokemonatual]['vida'] = 0
                window.blit(self.lista_imagens[2], (310, 290))
                window.blit(self.lista_imagens[4], (0, 450))
                morte = self.fonteBatalha.render(f"{self.pokemons[self.pokemonatual]['nome']} Fainted!", True, (0,0,0))
                window.blit(morte, (50, 475))
                blit_jogador = self.fonte.render(f'{self.pokemons[self.pokemonatual]["nome"]}: {self.pokemons[self.pokemonatual]["vida"]}/{self.pokemons[0]["vida_max"]}', True, (0, 0, 0))
                window.blit(blit_jogador, (350, 310))
                pygame.display.update()
                time.sleep(1)
                for i in range(3):
                    if self.pokemons[self.pokemonatual]['vida'] <= 0:
                        if self.pokemonatual == 2:
                            self.pokemonatual = 0
                        else:
                            self.pokemonatual += 1
            #MORTE DOs POKEMONs DO JOGADOR
            if self.pokemons[0]["vida"] <= 0 and self.pokemons[1]["vida"] <= 0 and self.pokemons[2]["vida"] <= 0:
                dicionario['vida_pokemon'] = dicionario['vida_max']
                self.tela_atual = 'fim'
            #MUDA DE TELA QUANDO A LUTA ACABAR
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
            ataque1 = self.fonteBatalha.render(self.pokemons[self.pokemonatual]['ataques'][0]['nome'], True, (0,0,0))
            ataque2 = self.fonteBatalha.render(self.pokemons[self.pokemonatual]['ataques'][1]['nome'], True, (0,0,0))
            ataque3 = self.fonteBatalha.render(self.pokemons[self.pokemonatual]['ataques'][2]['nome'], True, (0,0,0))
            ataque4 = self.fonteBatalha.render(self.pokemons[self.pokemonatual]['ataques'][3]['nome'], True, (0,0,0))
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
            if self.botao == 1:
                pps = self.pokemons[self.pokemonatual]['ataques'][0]['pps']
                pps = self.fonteBatalha.render(f'{pps}', True, (0,0,0))
                window.blit(pps, (520, 475))
            elif self.botao == 2:
                pps = self.pokemons[self.pokemonatual]['ataques'][1]['pps']
                pps = self.fonteBatalha.render(f'{pps}', True, (0,0,0))
                window.blit(pps, (520, 475))
            elif self.botao == 3:
                pps = self.pokemons[self.pokemonatual]['ataques'][2]['pps']
                pps = self.fonteBatalha.render(f'{pps}', True, (0,0,0))
                window.blit(pps, (520, 475))
            elif self.botao == 4:
                pps = self.pokemons[self.pokemonatual]['ataques'][3]['pps']
                pps = self.fonteBatalha.render(f'{pps}', True, (0,0,0))
                window.blit(pps, (520, 475))
        elif self.tela_atual =='vitória':
            window.blit(self.lista_imagens[4], (0, 450))
            morte = self.fonteBatalha.render("Foe MAKUHITA Fainted!", True, (0,0,0))
            window.blit(morte, (50, 475))
            pygame.display.update()
            time.sleep(1)
            self.tela_atual = 'fim'
        self.inimigo_compara = dicionario['vida_max']

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
            self.pokemons[self.pokemonatual]['ataques'][0]['pps'] -= 1
            self.tela_atual = 'texto_batalha'
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and self.botao == 2:
            dicionario['vida_pokemon'] -= 95
            self.pokemons[self.pokemonatual]['ataques'][1]['pps'] -= 1
            self.tela_atual = 'texto_batalha'
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and self.botao == 3:
            dicionario['vida_pokemon'] -= 80
            self.pokemons[self.pokemonatual]['ataques'][2]['pps'] -= 1
            self.tela_atual = 'texto_batalha'
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and self.botao == 4:
            dicionario['vida_pokemon'] -= 70
            self.pokemons[self.pokemonatual]['ataques'][3]['pps'] -= 1
            self.tela_atual = 'texto_batalha'
