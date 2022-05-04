import pygame
from pygame.locals import *

# Essa classe se dedica a configurar a resolucao do jogo

class resolucao_jogo:
    def __init__(self) -> None:

        # Tamanho da JANELA do jogo
        self.largura = 1920 # Largura de Incializacao do jogo
        self.altura = 1080 # Altura de Incializacao do jogo


        # Cria-se a estrutura necessária para gerar uma janela do tamanho x ( especifico do pygames )
        resolucao = (self.largura, self.altura) 
        self.resolucao_jogo = pygame.display.set_mode(resolucao)


        # Nesse dict temos uma razao onde a chave é o nome da resolucao 
        # e ao lado temos a largura e a altura respectivamente separadas por virgula
        # para adicionar uma nova resolucao deve-se adicionar uma nova chave junto dos valores
        self.dicionario_de_resolucoes = {
            'user_set':'',
            '240p':'426x240',
            '360p':'640x360',
            '480p':'854x480',
            '720p':'1280x720',
            '1080p':'1920x1080',
            '1440p':'2560x1440',
            '2160p':'3840x2160'
        }


    def get_pygame_display(self):
        return self.resolucao_jogo


    def calcula_proporcao_imagemXresolucao(self):

        self.proporcao_mapaXresolucao = self.altura / 232 # Esse numero magico e a razao de proporcao ente a resolucao e o tamanho do mapa 1

        largura = 3392 * self.proporcao_mapaXresolucao
        altura = 232 * self.proporcao_mapaXresolucao

        return (largura, altura)


    def get_resolcoes_possiveis(self):
        return self.dicionario_de_resolucoes


    def set_resolucao_jogo(self, dict_chave):
        valor = self.dicionario_de_resolucoes[dict_chave]
        achouX = False
        for i in valor:
            if i == 'x':
                achouX = True
                continue
            if achouX:
                altura += i
            else:
                largura += i

        return (largura, altura)