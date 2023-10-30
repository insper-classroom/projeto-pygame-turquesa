import pygame
import time
import random
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
            pygame.transform.scale((pygame.image.load('img/pikachujogador.png')),(200,200)),
            pygame.transform.scale((pygame.image.load('img/scizor.png')),(200,200)),
            pygame.transform.scale((pygame.image.load('img/venusaur.png')),(200,200)),
        ]
        tackle = {'dano': 35, 'precisao': 100, 'tipo': 'normal', 'pps': 30, 'nome': 'Tackle'}
        facade = {'dano': 50, 'precisao': 100, 'tipo': 'normal', 'pps': 10, 'nome': 'Facade'}
        slam = {'dano': 55, 'precisao': 90, 'tipo': 'normal', 'pps': 35, 'nome': 'Slam'}
        thunderbolt = {'dano': 60, 'precisao': 100, 'tipo': 'eletrico', 'pps': 35, 'nome': 'Thunderbolt'}
        cut = {'dano': 45, 'precisao': 95, 'tipo': 'normal', 'pps': 20, 'nome': 'Cut'}
        fury_cutter = {'dano': 80, 'precisao': 100, 'tipo': 'inseto', 'pps': 15, 'nome': 'Fury Cutter'}
        metal_claw = {'dano': 50, 'precisao': 90, 'tipo': 'metal', 'pps': 30, 'nome': 'Metal Claw'}
        pursuit = {'dano': 60, 'precisao': 100, 'tipo': 'escuridao', 'pps': 20, 'nome': 'Pursuit'}
        sludge_bomb = {'dano': 40, 'precisao': 100, 'tipo': 'veneno', 'pps': 10, 'nome': 'Sludge Bomb'}
        razor_leaf = {'dano': 50, 'precisao': 95, 'tipo': 'grama', 'pps': 25, 'nome': 'Razor Leaf'}
        earthquake = {'dano': 55, 'precisao': 100, 'tipo': 'terra', 'pps': 10, 'nome': 'Earthquake'}
        self.pokemons = [
            {'vida': 290, 'vida_max': 290, 'ataques': [tackle, thunderbolt, slam, facade], 'nome': 'PIKACHU'},
            {'vida': 250, 'vida_max': 250, 'ataques': [cut, fury_cutter, metal_claw, pursuit], 'nome': 'SCIZOR'},
            {'vida': 350, 'vida_max': 370, 'ataques': [razor_leaf, sludge_bomb, earthquake, cut], 'nome': 'VENUSAUR'},
        ]
        self.pokemonatual = 0
        self.botao = 1
        self.inimigo_compara = 0
        self.tela_atual = 'escolhendo'
        self.inimigo_atual = 0
        self.efetivo = ''
        self.crit =False
    def desenha_batalha(self, window, dicionario):
        self.inimigo_atual = 0
        if dicionario[self.inimigo_atual]['vida_pokemon'] <= 0 and len(dicionario) > 1:
            self.inimigo_atual += 1
        if dicionario[self.inimigo_atual]['vida_pokemon'] <= 0 and len(dicionario) > 2:
            self.inimigo_atual += 1
        #EVITA VIDA NEGATIVA
        if dicionario[self.inimigo_atual]['vida_pokemon'] < 0:
            dicionario[self.inimigo_atual]['vida_pokemon'] = 0
        if self.pokemons[self.pokemonatual]['vida'] < 0:
            self.pokemons[self.pokemonatual]['vida'] = 0
        #DESENHA A TELA DA BATALHA
        window.fill((188, 188, 188))
        window.blit(self.lista_imagens[1], (0, 400))
        window.blit(self.lista_imagens[2], (40, 90))
        window.blit(self.lista_imagens[2], (310, 290))
        window.blit(self.lista_imagens[1], (290, 230))
        window.blit(self.lista_imagens[6 + self.pokemonatual], (30, 300))
        #PARA DE DESENHAR O POKEMON INIMIGO SE ELE MORRER
        if dicionario[self.inimigo_atual]['vida_pokemon'] > 0:
            window.blit(dicionario[self.inimigo_atual]['imagem'], (370, 130))
        #DESENHA A VIDA DOS POKEMONS
        blit_inimigo = self.fonte.render(f'{dicionario[self.inimigo_atual]["nome"]}: {dicionario[self.inimigo_atual]["vida_pokemon"]}/{dicionario[self.inimigo_atual]["vida_max"]}', True, (0, 0, 0))
        window.blit(blit_inimigo, (80, 115))
        blit_jogador = self.fonte.render(f'{self.pokemons[self.pokemonatual]["nome"]}: {self.pokemons[self.pokemonatual]["vida"]}/{self.pokemons[self.pokemonatual]["vida_max"]}', True, (0, 0, 0))
        window.blit(blit_jogador, (350, 310))
        #DESENHA O ATAQUE DO JOGADOR
        if self.tela_atual == 'texto_batalha':
            window.blit(self.lista_imagens[4], (0, 450))
            ataque = self.fonteBatalha.render(f"{self.pokemons[self.pokemonatual]['nome']} used {self.pokemons[self.pokemonatual]['ataques'][self.botao - 1]['nome']}!", True, (0,0,0))
            window.blit(ataque, (50, 475))
            pygame.display.update()
            time.sleep(1)
            if self.efetivo == 'super':
                window.blit(self.lista_imagens[4], (0, 450))
                efetivo = self.fonteBatalha.render(f"It's super effective!", True, (0,0,0))
                window.blit(efetivo, (50, 475))
                pygame.display.update()
                time.sleep(1)
            elif self.efetivo == 'not':
                window.blit(self.lista_imagens[4], (0, 450))
                efetivo = self.fonteBatalha.render(f"It's not very effective...", True, (0,0,0))
                window.blit(efetivo, (50, 475))
                pygame.display.update()
                time.sleep(1)
            if self.crit == True:
                window.blit(self.lista_imagens[4], (0, 450))
                crit = self.fonteBatalha.render(f"A critical hit!", True, (0,0,0))
                window.blit(crit, (50, 475))
                pygame.display.update()
                time.sleep(1)
            #ATAQUE DO INIMIGO
            if dicionario[self.inimigo_atual]['vida_pokemon'] > 0:
                window.blit(self.lista_imagens[4], (0, 450))
                ataque_inimigo = self.inimigo_ataca(dicionario)
                ataque1 = self.fonteBatalha.render(f"Foe {dicionario[self.inimigo_atual]['nome']} used {ataque_inimigo[1]}!", True, (0,0,0))
                self.pokemons[self.pokemonatual]["vida"] -= ataque_inimigo[0]
                window.blit(ataque1, (50, 475))
                pygame.display.update()
                time.sleep(1)
                if ataque_inimigo[2] == 'super':
                    window.blit(self.lista_imagens[4], (0, 450))
                    efetivo = self.fonteBatalha.render(f"It's super effective!", True, (0,0,0))
                    window.blit(efetivo, (50, 475))
                    pygame.display.update()
                    time.sleep(1)
                elif ataque_inimigo[2] == 'not':
                    window.blit(self.lista_imagens[4], (0, 450))
                    efetivo = self.fonteBatalha.render(f"It's not very effective...", True, (0,0,0))
                    window.blit(efetivo, (50, 475))
                    pygame.display.update()
                    time.sleep(1)
                if ataque_inimigo[3] == True:
                    window.blit(self.lista_imagens[4], (0, 450))
                    crit = self.fonteBatalha.render(f"A critical hit!", True, (0,0,0))
                    window.blit(crit, (50, 475))
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
                dicionario[self.inimigo_atual]['vida_pokemon'] = dicionario[self.inimigo_atual]['vida_max']
                self.tela_atual = 'fim'
            #MUDA DE TELA QUANDO A LUTA ACABAR
            elif dicionario[self.inimigo_atual]['vida_pokemon'] <= 0:
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
            morte = self.fonteBatalha.render(f"Foe {dicionario[self.inimigo_atual]['nome']} Fainted!", True, (0,0,0))
            window.blit(morte, (50, 475))
            pygame.display.update()
            time.sleep(1)
            self.tela_atual = 'fim'
        self.inimigo_compara = dicionario[self.inimigo_atual]['vida_max']
        self.efetivo = ''
        self.crit = False

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
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and self.botao == 1 and self.pokemons[self.pokemonatual]['ataques'][0]['pps'] > 0:
            self.jogador_ataca(dicionario, 0)
            self.tela_atual = 'texto_batalha'
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and self.botao == 2 and self.pokemons[self.pokemonatual]['ataques'][0]['pps'] > 0:
            self.jogador_ataca(dicionario, 1)
            self.tela_atual = 'texto_batalha'
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and self.botao == 3 and self.pokemons[self.pokemonatual]['ataques'][0]['pps'] > 0:
            self.jogador_ataca(dicionario, 2)
            self.tela_atual = 'texto_batalha'
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and self.botao == 4 and self.pokemons[self.pokemonatual]['ataques'][0]['pps'] > 0:
            self.jogador_ataca(dicionario, 3)
            self.tela_atual = 'texto_batalha'

    def inimigo_ataca(self,dicionario):
        crit = False
        probab = random.random()
        efetivo = ''
        if dicionario[self.inimigo_atual]['nome'] == 'MAKUHITA':
            dano = dicionario[self.inimigo_atual]['ataques'][0]['dano']
            nome = dicionario[self.inimigo_atual]['ataques'][0]['nome']
            if self.pokemons[self.pokemonatual]['nome'] == 'SCIZOR':
                dano //= 2
                efetivo = 'not'
        elif dicionario[self.inimigo_atual]['nome'] == 'MACHOKE':
            if probab < 0.5:
                dano = dicionario[self.inimigo_atual]['ataques'][0]['dano']
                nome = dicionario[self.inimigo_atual]['ataques'][0]['nome']
            else:
                dano = dicionario[self.inimigo_atual]['ataques'][1]['dano']
                nome = dicionario[self.inimigo_atual]['ataques'][1]['nome']
            if self.pokemons[self.pokemonatual]['nome'] == 'SCIZOR' and nome == 'Facade':
                dano //= 2
                efetivo = 'not'
            elif self.pokemons[self.pokemonatual]['nome'] == 'VENUSAUR' and nome == 'Karate Chop':
                dano //= 2
                efetivo = 'not'
        elif dicionario[self.inimigo_atual]['nome'] == 'MEDITITE':
            dano = dicionario[self.inimigo_atual]['ataques'][0]['dano']
            nome = dicionario[self.inimigo_atual]['ataques'][0]['nome']
            if self.pokemons[self.pokemonatual]['nome'] == 'SCIZOR':
                dano //= 2
                efetivo = 'not'
            elif self.pokemons[self.pokemonatual]['nome'] == 'VENUSAUR':
                dano *= 2
                efetivo = 'super'
        elif dicionario[self.inimigo_atual]['nome'] == 'MEDICHAM':
            if dicionario[self.inimigo_atual]['vida_pokemon'] < 130:
                if probab < 0.8:
                    dano = dicionario[self.inimigo_atual]['ataques'][0]['dano']
                    nome = dicionario[self.inimigo_atual]['ataques'][0]['nome']
                else:
                    dano = dicionario[self.inimigo_atual]['ataques'][2]['dano']
                    nome = dicionario[self.inimigo_atual]['ataques'][2]['nome']
                    dicionario[self.inimigo_atual]['vida_pokemon'] += 120
            else:
                if probab < 0.65:
                    dano = dicionario[self.inimigo_atual]['ataques'][0]['dano']
                    nome = dicionario[self.inimigo_atual]['ataques'][0]['nome']
                else:
                    dano = dicionario[self.inimigo_atual]['ataques'][1]['dano']
                    nome = dicionario[self.inimigo_atual]['ataques'][1]['nome']
            if self.pokemons[self.pokemonatual]['nome'] == 'SCIZOR' and nome == 'Fire Punch':
                dano *= 4
                efetivo = 'super'
            elif self.pokemons[self.pokemonatual]['nome'] == 'VENUSAUR' and nome == 'Fire Punch':
                dano *= 2
                efetivo = 'super'
            elif self.pokemons[self.pokemonatual]['nome'] == 'VENUSAUR' and nome == 'Psybeam':
                dano *= 2
                efetivo = 'super'
            elif self.pokemons[self.pokemonatual]['nome'] == 'SCIZOR' and nome == 'Psybeam':
                dano //= 2
                efetivo = 'super'
        elif dicionario[self.inimigo_atual]['nome'] == 'MACHOP':
            dano = dicionario[self.inimigo_atual]['ataques'][0]['dano']
            nome = dicionario[self.inimigo_atual]['ataques'][0]['nome']
            if self.pokemons[self.pokemonatual]['nome'] == 'VENUSAUR':
                dano //= 2
                efetivo = 'not'
        elif dicionario[self.inimigo_atual]['nome'] == 'HARIYAMA':
            if probab < 0.45:
                dano = dicionario[self.inimigo_atual]['ataques'][0]['dano']
                nome = dicionario[self.inimigo_atual]['ataques'][0]['nome']
            else:
                dano = dicionario[self.inimigo_atual]['ataques'][1]['dano']
                nome = dicionario[self.inimigo_atual]['ataques'][1]['nome']
            if self.pokemons[self.pokemonatual]['nome'] == 'PIKACHU':
                dano = dicionario[self.inimigo_atual]['ataques'][1]['dano']
                nome = dicionario[self.inimigo_atual]['ataques'][1]['nome']
            if self.pokemons[self.pokemonatual]['nome'] == 'PIKACHU' and nome == 'Earthquake':
                dano *= 2
                efetivo = 'super'
            elif self.pokemons[self.pokemonatual]['nome'] == 'VENUSAUR' and nome == 'Karate Chop':
                dano //= 2
                efetivo = 'not'
        elif dicionario[self.inimigo_atual]['nome'] == 'HERACROSS':
            if probab < 0.5:
                dano = dicionario[self.inimigo_atual]['ataques'][0]['dano']
                nome = dicionario[self.inimigo_atual]['ataques'][0]['nome']
            else:
                dano = dicionario[self.inimigo_atual]['ataques'][1]['dano']
                nome = dicionario[self.inimigo_atual]['ataques'][1]['nome']
            if self.pokemons[self.pokemonatual]['nome'] == 'SCIZOR':
                dano //= 2
                efetivo = 'not'
        elif dicionario[self.inimigo_atual]['nome'] == 'MACHAMP':
            if probab < 0.65:   
                dano = dicionario[self.inimigo_atual]['ataques'][0]['dano']
                nome = dicionario[self.inimigo_atual]['ataques'][0]['nome']
            elif self.pokemons[self.pokemonatual]['nome'] != 'VENUSAUR':
                dano = dicionario[self.inimigo_atual]['ataques'][1]['dano']
                nome = dicionario[self.inimigo_atual]['ataques'][1]['nome']
            else:
                dano = dicionario[self.inimigo_atual]['ataques'][2]['dano']
                nome = dicionario[self.inimigo_atual]['ataques'][2]['nome']
            if self.pokemons[self.pokemonatual]['nome'] == 'SCIZOR':
                dano = dicionario[self.inimigo_atual]['ataques'][0]['dano']
                nome = dicionario[self.inimigo_atual]['ataques'][0]['nome']
            if self.pokemons[self.pokemonatual]['nome'] == 'SCIZOR' and nome == 'Fire Blast':
                dano *= 4
                efetivo = 'super'
            elif self.pokemons[self.pokemonatual]['nome'] == 'VENUSAUR' and nome == 'Fire Blast':
                dano *= 2
                efetivo = 'super'
        crit = random.random()
        if crit <= 0.0416:
            dano *= 1.5
            crit = True
        return int(dano), nome, efetivo, crit
    
    def jogador_ataca(self, dicionario, ataque):
        self.crit = random.random()
        qual_ataque = self.pokemons[self.pokemonatual]['ataques'][ataque]
        dano = qual_ataque['dano']
        if qual_ataque['tipo'] == 'escuridao':
            if dicionario[self.inimigo_atual]['nome'] != 'MEDITITE' or dicionario[self.inimigo_atual]['nome'] != 'MEDICHAM':
                dano //= 2
                self.efetivo = 'not'
        elif qual_ataque['tipo'] == 'grama':
            if dicionario[self.inimigo_atual]['nome'] == 'HERACROSS':
                dano //= 2
                self.efetivo = 'not'
        elif qual_ataque['tipo'] == 'terra':
            if dicionario[self.inimigo_atual]['nome'] == 'HERACROSS':
                dano //= 2
                self.efetivo = 'not'
        elif qual_ataque['tipo'] == 'inseto':
            if dicionario[self.inimigo_atual]['nome'] != 'MEDITITE' or dicionario[self.inimigo_atual]['nome'] != 'MEDICHAM':
                dano //= 2
                self.efetivo = 'not'
        if self.crit <= 0.0416:
            dano *= 1.5
            self.crit = True
        dicionario[self.inimigo_atual]['vida_pokemon'] -= int(dano)
        self.pokemons[self.pokemonatual]['ataques'][ataque]['pps'] -= 1
