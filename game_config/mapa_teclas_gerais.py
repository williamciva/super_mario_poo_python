import pygame

class MapaTeclasGerais(object):
    def __init__(self) -> None:
        self.mapa()

    def mapa(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()