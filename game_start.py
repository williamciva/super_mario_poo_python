from pygame import init, display
from os import environ
from game_config.controlador import Controlador


class GameStart(object):
    def __init__(self) -> None:
        self.controlador = Controlador()

    def rodar(self):
        init()
        while True:
            
            
            self.controlador.teclas_gerais.mapa()
            self.controlador.fps.run_fps()
            display.update()