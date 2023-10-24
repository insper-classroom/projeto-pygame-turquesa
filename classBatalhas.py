import pygame

class Batalha:
    def __init__(self):
        self.fonte = pygame.font.Font('imgBatalhas/fontes.ttf', 20)
        self.fonteMenu = pygame.font.Font('imgBatalhas/fontes.ttf', 20)
        self.lista_imagens = [
            pygame.transform.scale((pygame.image.load('img/Ataques pokemon.png')),(640, 150)),
            pygame.transform.scale((pygame.image.load('img/template.png')),(330, 60)),
            pygame.transform.scale((pygame.image.load('imgBatalhas/barraSemVida.png')),(290, 80)),
            pygame.transform.scale((pygame.image.load('imgBatalhas/seta.png')),(40, 40)),
            pygame.transform.scale((pygame.image.load('imgBatalhas/barraVazia.png')),(640, 150)),
        ]
        self.vida_jogador = 90
        self.vida_j_max = 100
        self.vida_inimigo = 130
        self.vida_i_max = 130
        self.botao = 1
        self.tela_atual = 'escolhendo'
    
    def desenha_batalha(self, window):
        window.fill((188, 188, 188))
        window.blit(self.lista_imagens[1], (0, 400))
        window.blit(self.lista_imagens[1], (290, 230))
        window.blit(self.lista_imagens[2], (40, 90))
        window.blit(self.lista_imagens[2], (290, 230))

        vida_inimigo = self.fonte.render(f'PIKACHU: {self.vida_jogador}/{self.vida_j_max}', True, (0, 0, 0))
        window.blit(vida_inimigo, (80, 115))
        vida_jogador = self.fonte.render(f'CHARMANDER: {self.vida_inimigo}/{self.vida_i_max}', True, (0, 0, 0))
        window.blit(vida_jogador, (350, 315))

        if self.tela_atual == 'escolhendo':
            window.blit(self.lista_imagens[4], (0, 450))
            text_menu = self.fonteMenu.render('FIGHT', True, (0, 0, 0))
            window.blit(text_menu, (80, 485))
            text_pokemon = self.fonteMenu.render('POKEMON', True, (0, 0, 0))
            window.blit(text_pokemon, (330, 485))
            if self.botao == 1:
                window.blit(self.lista_imagens[3], (40, 505))
            if self.botao == 2:
                window.blit(self.lista_imagens[3], (290, 505))
        elif self.tela_atual == 'batalha':
            window.blit(self.lista_imagens[0], (0, 450))
    