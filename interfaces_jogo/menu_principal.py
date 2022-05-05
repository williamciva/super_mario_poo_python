from pygame import image, transform
from interfaces_jogo.interface import Interface
from game_config.resolucao_config import ResolucaoConfig

class MenuPrincipal(Interface):
    def __init__(self) -> None:
        super().__init__()
        self.display = ResolucaoConfig().get_pygame_display() # Renderiza Janela
        self.imagem_fundo = image.load('assets/menus/main_menu.jpg')
        self.propocao_reais_da_imagem = self.imagem_fundo.get_size()
        self.imagem = transform.scale(self.imagem_fundo, ResolucaoConfig().calcular_imagem_x_resolucao(self.propocao_reais_da_imagem)) # Redimencionar Imagem
        self.eixo_central_x_y = ResolucaoConfig().get_eixos_centrais(self.propocao_reais_da_imagem)
        self.eixo_x, self.eixo_y = self.eixo_central_x_y[0], self.eixo_central_x_y[1]
        self.display.blit(self.imagem_fundo, self.eixo_central_x_y)