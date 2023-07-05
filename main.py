import pygame

from map import Map
from player import Player
from skybox import SkyBox
from settings import *

class Game:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("Core Defender")
        
        self.screen = pygame.display.set_mode((800, 600))
        self.screen.fill('#000000')

        for sprite in SPRITES:
            SPRITES[sprite] = pygame.image.load(f'assets/sprites/{sprite}.png')

        self.clock = pygame.time.Clock()
        self.dt = 0

        self.skybox = SkyBox(self.screen)
        self.map = Map(self.screen, 20)
        self.player = Player(self.screen)
    
    def draw(self):
        self.screen.fill('#000000')
        self.skybox.draw(self.player.position)
        self.map.draw(self.player.position)
        self.player.draw()
        pygame.display.flip()

    def run(self):
        while True:
            self.dt = self.clock.tick(60)
            self.player.update(self.dt)
            self.draw()


if __name__=='__main__':
    game = Game()
    game.run()
