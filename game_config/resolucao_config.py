from pygame import display
from pygame.locals import *

# Essa classe se dedica a configurar a resolucao do jogo

class ResolucaoConfig:
    def __init__(self) -> None:
        

        # Tamanho da JANELA do jogo
        self.largura_janela, self.altura_janela = 1280, 720 # Largura  e altura de Incializacao do jogo

        # Cria-se a estrutura necessária para gerar uma janela do tamanho x ( especifico do pygames )
        proporcao_da_janela = (self.largura_janela, self.altura_janela) 
        self.display_proporcao_janela = display.set_mode(proporcao_da_janela)

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
        return self.display_proporcao_janela

    def calcula_proporcao_imagemXresolucao(self, largura_imagem, altura_imagem):
        razao_de_proporcao = ( self.altura_janela / altura_imagem )

        largura = largura_imagem * razao_de_proporcao
        altura = altura_imagem * razao_de_proporcao

        return (largura, altura)

    def get_resolucoes_possiveis(self):
        return self.dicionario_de_resolucoes

    def get_proporcoes_para_resolucao(self, dict_chave):
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

    def set_resolucao(self, largura, altura):
        pass