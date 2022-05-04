from pygame import init, display
from pygame.locals import *
import game_config.tela_config as modulo_tela


class gameStart:
    def __init__(self) -> None:
        self.init_tela = modulo_tela.tela_jogo()

    def rodar(self):
        init()
        while True:
            
            
            display.update()