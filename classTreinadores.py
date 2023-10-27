import pygame
class Treinador1:
    def __init__(self):
        self.treinador1_img = pygame.transform.scale((pygame.image.load('img/trainer-1.png')),(30, 30))
        self.rect = pygame.Rect(35, 185, 30, 30)
        self.tackle = {'dano': 30, 'precisao': 100, 'tipo': 'normal', 'pps': 30, 'nome': 'Tackle'}
    
    def desenha_treinador1(self, window, bool):
        if not bool:
            window.blit(self.treinador1_img, (35, 185))
        
    def pokemons_treinador1(self):
        treinador1 = {'vida_pokemon': 290, 'vida_max': 290, 'ataques': [self.tackle], 'nome': 'MAKUHITA'}
        return treinador1

class Treinador2:
    def __init__(self):
        self.trainer2_img = pygame.transform.scale((pygame.image.load('img/trainer-2.png')),(30, 30))
        self.rect = pygame.Rect(430, 492, 30, 30)
        self.tackle = {'dano': 30, 'precisao': 100, 'tipo': 'normal', 'pps': 30, 'nome': 'Tackle'}

    def desenha_treinador2(self, window, bool):
        if not bool:
            window.blit(self.trainer2_img, (430, 492))

    def pokemons_treinador2(self):
        treinador1 = {'vida_pokemon': 290, 'vida_max': 290, 'ataques': [self.tackle], 'nome': 'MAKUHITA'}
        return treinador1

class Treinardor3:
    def __init__(self):
        self.trainer3_img = pygame.transform.scale((pygame.image.load('img/trainer-2.png')),(30, 30))
        self.rect = pygame.Rect(72, 335, 30, 30)
        self.tackle = {'dano': 30, 'precisao': 100, 'tipo': 'normal', 'pps': 30, 'nome': 'Tackle'}

    def desenha_treinador3(self, window, bool):
        if not bool:
            window.blit(self.trainer3_img, (72, 335))

    def pokemons_treinador3(self):
        treinador1 = {'vida_pokemon': 290, 'vida_max': 290, 'ataques': [self.tackle], 'nome': 'MAKUHITA'}
        return treinador1

class Treinador4:
    def __init__(self):
        self.trainer4_img = pygame.transform.scale((pygame.image.load('img/trainer-2.png')),(30, 30))
        self.rect = pygame.Rect(483, 68, 30, 30)
        self.tackle = {'dano': 30, 'precisao': 100, 'tipo': 'normal', 'pps': 30, 'nome': 'Tackle'}

    def desenha_treinador4(self, window, bool):
        if not bool:
            window.blit(self.trainer4_img, (483, 68))

    def pokemons_treinador4(self):
        treinador1 = {'vida_pokemon': 290, 'vida_max': 290, 'ataques': [self.tackle], 'nome': 'MAKUHITA'}
        return treinador1

    
        window.blit(self.trainer4_img, (483, 68))

    def pokemons_treinador4(self):
        dicionario = {
            'treinador': 4,
            'vidamax_pokemon': 130,
            'vida_pokemon': 130,
        }
        return dicionario
    