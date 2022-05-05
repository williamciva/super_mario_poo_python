from interfaces_jogo.menu_principal import MenuPrincipal
from game_config.fps_config import Fps_config
from game_config.mapa_teclas_gerais import MapaTeclasGerais

class Controlador(object):
    def __init__(self) -> None:
        self.menu = MenuPrincipal()
        self.fps = Fps_config()
        self.teclas_gerais = MapaTeclasGerais()