import pygame

from settings import SPRITE_SCALE
from settings import SPRITE_SIZE
from settings import SKYBOX_COLOR_A
from settings import SKYBOX_COLOR_B


class SkyBox:
    def __init__(self, screen) -> None:
        self.screen = screen

        self.sprite_size = int(SPRITE_SIZE * SPRITE_SCALE)
        
        self.surface = pygame.Surface((self.screen.get_width(), self.screen.get_height()))
        
        self.dark_tile = pygame.Surface((self.sprite_size, self.sprite_size))
        self.light_tile = pygame.Surface((self.sprite_size, self.sprite_size))
        self.dark_tile.fill(SKYBOX_COLOR_A)
        self.light_tile.fill(SKYBOX_COLOR_B)

    def draw(self, player_position):
        x_parity = player_position[0] // self.sprite_size
        y_parity = player_position[1] // self.sprite_size
        x_offset = player_position[0] % self.sprite_size
        y_offset = player_position[1] % self.sprite_size
        for y in range(self.screen.get_height() // self.sprite_size + 2):
            for x in range(self.screen.get_width() // self.sprite_size + 2):
                if (x + x_parity) % 2 == 0 and (y + y_parity) % 2 == 0:
                    self.surface.blit(self.light_tile, (x * self.sprite_size - x_offset, y * self.sprite_size - y_offset))
                elif (x + x_parity) % 2 == 1 and (y + y_parity) % 2 == 1:
                    self.surface.blit(self.light_tile, (x * self.sprite_size - x_offset, y * self.sprite_size - y_offset))
                else:
                    self.surface.blit(self.dark_tile, (x * self.sprite_size - x_offset, y * self.sprite_size - y_offset))
        self.screen.blit(self.surface, (0, 0))
