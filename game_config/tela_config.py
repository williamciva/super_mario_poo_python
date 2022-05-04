import pygame
from pygame.locals import *
from game_config.resolucao_config import *

# Essa classe se dedica a configurar a imagem da tela atual

class tela_jogo():
    def __init__(self) -> None:
        
        # Instancia a resolucao do jogo
        self.init_resolucao = resolucao_jogo()

        
        # Carregamos o jogo com um fundo padrão
        self.carrega_imagem = "assets/world/fase_1/world.png"

        # Essa funcao retorna a resolucao ideal para o tamaho da janela 
        # e a resolucao da imagem usada de fundo
        # em uma tupla onde o index 0 e altura e 1 largura
        proporcao_imagem = self.init_resolucao.calcula_proporcao_imagemXresolucao()
        largura = proporcao_imagem[0]
        altura = proporcao_imagem[1]

        # Usamos nossa imagem e renderizamos sua escala conforme as 
        # proporcoes obtidas atraves da funcao get_resolucao_imagem()
        self.imagem_fundo = pygame.image.load(self.carrega_imagem)
        self.imagem_fundo = pygame.transform.scale(self.imagem_fundo, ( largura , altura))


        self.eixo_x = 0
        self.eixo_y =  0

        # Define a imagem de fundo e a posicao na imagem
        self.pygame_display = self.init_resolucao.get_pygame_display()
        self.pygame_display.blit(self.imagem_fundo, (self.eixo_x, self.eixo_y))


    def definir_imagem_fundo(self, nome_imagem):
        self.image = nome_imagem