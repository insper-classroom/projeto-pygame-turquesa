import pygame

def inicializa_batalha():
    pygame.init()
    imagens = []
    pygame.display.set_caption('Pokemon Battle')
    imagem = pygame.image.load('img/Ataques pokemon.png')
    imagem = pygame.transform.scale(imagem, (640, 130))
    imagens.append(imagem)
    imagem = pygame.image.load('img/barra de vida.png')
    imagem = pygame.transform.scale(imagem, (290, 80))
    imagens.append(imagem)
    imagem = pygame.image.load('img/template.png')
    imagem = pygame.transform.scale(imagem, (330, 60))
    imagens.append(imagem)
    return imagens

def desenha_batalha(window, imagens):
    pygame.display.update()
    window.fill((188, 188, 188))
    window.blit(imagens[2], (0, 310))
    window.blit(imagens[0], (0, 350))
    window.blit(imagens[1], (40, 40))
    window.blit(imagens[1], (310, 250))
    window.blit(imagens[2], (290, 190))
    
def eventos_batalha():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True
        
def battle_loop(tupla):
    window = tupla[0]
    imagem = tupla[1]
    while eventos_batalha():
        desenha_batalha(window, imagem)

battle_loop(inicializa_batalha())