from interfaces_jogo.menu_principal import MenuPrincipal
from game_config.fps_config import Fps_config
from game_config.mapa_teclas_gerais import MapaTeclasGerais

class Controlador:
    def __init__(self) -> None:
        self.tela_atual = TelaAtual()
        self.fps = Fps_config()
        self.teclas_gerais = MapaTeclasGerais()


class TelaAtual:
    def __init__(self) -> None:
        self.menu = MenuPrincipal()

    def troca_tela(self, nova_tela):
        pass