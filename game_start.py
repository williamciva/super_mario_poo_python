from pygame import init, display
from pygame.locals import *
from game_config.controlador import Controlador


class GameStart:
    def __init__(self) -> None:
        self.controlador = Controlador()

    def rodar(self):
        init()
        while True:
            
            
            self.controlador.teclas_gerais.mapa()
            self.controlador.fps.run_fps()
            display.update()