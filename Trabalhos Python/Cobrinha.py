#Jogo_da_cobrinha
import pygame
from pygame.locals import *
from sys import exit 
from random import randint
pygame.font.init()
pygame.mixer.init()
pygame.init

barulhocolisao = pygame.mixer.Sound('smw_coin.wav')

x = 500
y = 252

xcobrinha = x/2
ycobrinha = y/2

velocidade = 5
xcontrole = velocidade
ycontrole = 0

xmaça = randint(30, 470)
ymaça= randint(30, 222)

pontos = 0
fonte = pygame.font.SysFont('arial', 20, True, True)

tela = pygame.display.set_mode((x, y))
pygame.display.set_caption('Jogo')
relogio = pygame.time.Clock()
listacobrinha = []
tamanhoinicial = 10

morreu = False

def aumentacobra(listacobrinha):
    for XeY in listacobrinha:
        pygame.draw.rect(tela, (255,120,0), (XeY[0], XeY[1], 20, 20))

def reiniciarjogo():
    global pontos, tamanhoinicial, xcobrinha, ycobrinha, listacobrinha,listacabeça, xmaça, ymaça, morreu
    pontos = 0
    tamanhoinicial = 10
    xcobrinha = int(x/2)
    ycobrinha = int(y/2)
    listacobrinha = []
    listacabeça = []
    xmaça = randint(30, 470)
    ymaça = randint(30, 222)
    morreu = False


while True:
    relogio.tick(30)
    tela.fill((255,255,255))
    mensagem = f'Pontos: {pontos}'
    textofinal = fonte.render(mensagem, False, (0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type ==  KEYDOWN:
            if event.key == K_a:
                if xcontrole == velocidade:
                    pass
                else:
                    xcontrole = -velocidade
                    ycontrole = 0

            if event.key == K_d:
                if xcontrole == -velocidade:
                    pass
                else:
                    xcontrole = velocidade
                    ycontrole = 0

            if event.key == K_w:
                if ycontrole == velocidade:
                    pass
                else:
                   ycontrole = -velocidade
                   xcontrole = 0
            
            if event.key == K_s:
                if ycontrole == -velocidade:
                   pass
                else:
                    ycontrole = velocidade
                    xcontrole = 0


    xcobrinha = xcobrinha + xcontrole
    ycobrinha = ycobrinha + ycontrole

    cobrinha = pygame.draw.rect(tela, (255,120,0), (xcobrinha, ycobrinha, 20, 20))
    maça = pygame.draw.rect(tela, (0,0,130), (xmaça, ymaça, 20, 20))

    if cobrinha.colliderect(maça):
        xmaça = randint(30, 470)
        ymaça = randint(30, 222)
        pontos = pontos + 1
        barulhocolisao.play()
        tamanhoinicial = tamanhoinicial + 1

    listacabeça = []
    listacabeça.append(xcobrinha)
    listacabeça.append(ycobrinha)
    listacobrinha.append(listacabeça)

    if listacobrinha.count(listacabeça) > 1:
        fonte2 = pygame.font.SysFont('arial', 20, True, True)
        mensagem = 'Asta la vista baby! Aperte R para jogar novamente'
        textofinal2 = fonte2.render(mensagem, True, (0,0,0))

        morreu = True
        while morreu:
            tela.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciarjogo()
           
            tela.blit(textofinal2, (10, 30))
            pygame.display.update()

    if xcobrinha > x:
        xcobrinha = 0
    if xcobrinha < 0:
        xcobrinha = x
    if ycobrinha < 0:
        ycobrinha = x
    if ycobrinha > x:
        ycobrinha = 0

    if len(listacobrinha) > tamanhoinicial:
        del listacobrinha [0]
    
    aumentacobra(listacobrinha)
    
    tela.blit(textofinal, (390, 20))
    pygame.display.update()

