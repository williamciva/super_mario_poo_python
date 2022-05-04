from pygame import image, transform
from game_config.resolucao_config import ResolucaoConfig

# Essa classe se dedica a configurar a imagem da tela atual

class MenuPrincipal():
    def __init__(self) -> None:
        
        # Instancia a resolucao do jogo
        self.init_resolucao = ResolucaoConfig()
        
        # Carregamos o jogo com um fundo padrão
        self.carrega_imagem = "assets/world/fase_1/world.png"

        # Essa funcao retorna a resolucao ideal para o tamaho da janela 
        # e a resolucao da imagem usada de fundo
        # em uma tupla onde o index 0 e altura e 1 largura
        largura_imagem, altura_imagem = 3392, 232
        proporcao_imagem = self.init_resolucao.calcula_proporcao_imagemXresolucao(largura_imagem, altura_imagem)
        proporcao_largura, proporcao_altura = proporcao_imagem[0], proporcao_imagem[1]

        # Usamos nossa imagem e renderizamos sua escala conforme as 
        # proporcoes obtidas atraves da funcao get_resolucao_imagem()
        self.imagem_fundo = image.load(self.carrega_imagem)
        self.imagem_fundo = transform.scale(self.imagem_fundo, ( proporcao_largura , proporcao_altura))

        # Define a imagem de fundo e a posicao na imagem
        self.eixo_x, self.eixo_y = 0, 0

        self.pygame_display = self.init_resolucao.get_pygame_display()
        self.pygame_display.blit(self.imagem_fundo, (self.eixo_x, self.eixo_y))