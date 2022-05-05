from pygame import time

class Fps_config(object):
    def __init__(self) -> None:
        # Define o FPS do Game
        self.fps = int(30)

        self.tick_rate = time.Clock()
        self.tick_rate.tick(self.fps)

    def set_fps(self, fps):
            self.fps = fps

    def run_fps(self):
        self.tick_rate.tick(self.fps)