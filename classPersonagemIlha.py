import pygame

class Personagem_ilha:
    '''
        Classe responsável por desenhar o personagem e entregar o rect do personagem,
        e realizar sua movimentção por todo o territorio da ILHA.
    '''
    def __init__(self) -> None:
        self.personagem = pygame.transform.scale((pygame.image.load('img/personagem.png')),(30, 35))
        self.rect = self.personagem.get_rect()
        self.rect.x = 280
        self.rect.y = 300
        self.velocidade = [0, 0]
        self.pos_antiga = [0, 0]
    
    def desenha_personagem(self, window):
        '''
            Função que desenha o personagem, imagem armazenada no init da classe.
        '''
        window.blit(self.personagem, (self.rect.x, self.rect.y))
        
    def altera_sprite_horizontal(self):
        '''
            Função que altera o sprite do personagem para a direção horizontal.
        '''
        
        next_pos = self.rect.x + self.velocidade[0]
        self.rect.x = next_pos
    
    def altera_sprite_vertical(self):
        '''
            Função que altera o sprite do personagem para a direção vertical.
        '''
        
        next_pos = self.rect.y + self.velocidade[1]
        self.rect.y = next_pos
    
    def verifica_colisao(self, lista_paredes):
        '''
            Função que recebe uma lista de rects (paredes)
            e verifica se o rect do personagem esta colidindo
            , caso sim retorna um boleano (True para hit / False
            para nao hit).
        '''

        is_hit = False
        for parede in lista_paredes:
            if parede.colliderect(self.rect):
                is_hit = True
                break

        return is_hit