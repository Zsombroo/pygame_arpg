import random

import numpy as np
import pygame

from settings import *


class Map:
    def __init__(self, screen, map_border_width) -> None:
        self.screen = screen
        self.map_border_width = map_border_width
        self.tiles = self._generate(size=(map_border_width*map_border_width)//4, walker_life=map_border_width)
        self._tileset = self._load_tiles()
        

    def _load_tiles(self):
        big_pic = pygame.image.load('assets/ground_tileset.png')
        ground_tiles = []
        for i in range(6):
            for j in range(3):
                ground_tiles.append(big_pic.subsurface((
                    i*SPRITE_SIZE, j*SPRITE_SIZE, SPRITE_SIZE, SPRITE_SIZE)))
        return ground_tiles

    def draw(self, player_position):
        for y, row in enumerate(self.tiles):
            for x, tile in enumerate(row):
                if tile == 0:
                    self.screen.blit(self._tileset[13], (x*SPRITE_SIZE-player_position[0], y*SPRITE_SIZE-player_position[1]))
                elif tile == 1:
                    self.screen.blit(self._tileset[4], (x*SPRITE_SIZE-player_position[0], y*SPRITE_SIZE-player_position[1]))

    def pad_map(self, map_tiles, colapsed, availables):
        map_tiles = np.pad(map_tiles, 1, mode='constant', constant_values=-1)
        colapsed = {(x+1, y+1) for x, y in colapsed}
        return map_tiles, colapsed
    
    def _generate(self, size=50, walker_life=20):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        probabilities = [0.25, 0.25, 0.25, 0.25]
        map_tiles = np.zeros((self.map_border_width, self.map_border_width), dtype=int)

        walker_position = (self.map_border_width//2, self.map_border_width//2)
        life = walker_life
        map_tiles[walker_position] = 1
        while True:
            unique, counts = np.unique(map_tiles, return_counts=True)
            if counts[np.where(unique == 1)] >= size:
                break

            # If the walker is dead, create a new one
            if life == 0:
                life = walker_life
                walker_position = (self.map_border_width//2,
                                   self.map_border_width//2)
                continue
            direction = random.choices(directions, probabilities)[0]
            
            # Stop the walker if it's going to go out of bounds
            if walker_position[0] + direction[0] < 0 \
            or walker_position[0] + direction[0] >= self.map_border_width \
            or walker_position[1] + direction[1] < 0 \
            or walker_position[1] + direction[1] >= self.map_border_width:
                life = 0
                continue

            tile_in_direction = map_tiles[walker_position[0] + direction[0],
                                          walker_position[1] + direction[1]]
            if tile_in_direction == 0:
                map_tiles[walker_position] = 1
                walker_position = (walker_position[0] + direction[0],
                                   walker_position[1] + direction[1])
                life -= 1
            elif tile_in_direction == 1:
                walker_position = (walker_position[0] + direction[0],
                                   walker_position[1] + direction[1])
                life -= 1
            else:
                life = 0
        map_tiles[self.map_border_width//2, self.map_border_width//2] = -1
        return map_tiles
            

if __name__ == '__main__':
    map_border_width = 30
    m = Map(None, map_border_width)
    m.tiles = m.generate(size=(map_border_width*map_border_width)//4, walker_life=map_border_width)
    import matplotlib.pyplot as plt
    plt.imshow(m.tiles)
    plt.show()
