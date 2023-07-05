import pygame

from settings import RUN_SPEED
from settings import SPAWN_POSITION
from settings import SPRITE_SIZE
from settings import SPRITE_SCALE

from settings import SPRITES


class Player:
    def __init__(self, screen) -> None:
        self.sprite_size = int(SPRITE_SIZE * SPRITE_SCALE)
        
        self.screen = screen

        self.default_sprite = pygame.Surface((self.sprite_size, self.sprite_size))
        self.default_sprite.blit(SPRITES['player'], (0, 0))
        self.sprite = pygame.Surface((self.sprite_size, self.sprite_size))
        self.sprite.convert_alpha()
        self.sprite.set_colorkey((0, 0, 0))
        pygame.transform.scale(self.default_sprite, (self.sprite_size, self.sprite_size), self.sprite)

        self.position: tuple[float, float] = SPAWN_POSITION
        self.speed: float = RUN_SPEED
        self.diagonal_speed: float = self.speed * 0.70710678118

        self.keys_pressed = {
            'up': False,
            'down': False,
            'left': False,
            'right': False,
        }

    def update(self, dt):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.keys_pressed['up'] = True
                if event.key == pygame.K_s:
                    self.keys_pressed['down'] = True
                if event.key == pygame.K_a:
                    self.keys_pressed['left'] = True
                if event.key == pygame.K_d:
                    self.keys_pressed['right'] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.keys_pressed['up'] = False
                if event.key == pygame.K_s:
                    self.keys_pressed['down'] = False
                if event.key == pygame.K_a:
                    self.keys_pressed['left'] = False
                if event.key == pygame.K_d:
                    self.keys_pressed['right'] = False
        if self.keys_pressed['up']:
            if self.keys_pressed['left'] or self.keys_pressed['right']:
                self.position[1] -= self.diagonal_speed * dt
            else:
                self.position[1] -= self.speed * dt
        if self.keys_pressed['down']:
            if self.keys_pressed['left'] or self.keys_pressed['right']:
                self.position[1] += self.diagonal_speed * dt
            else:
                self.position[1] += self.speed * dt
        if self.keys_pressed['left']:
            if self.keys_pressed['up'] or self.keys_pressed['down']:
                self.position[0] -= self.diagonal_speed * dt
            else:
                self.position[0] -= self.speed * dt
        if self.keys_pressed['right']:
            if self.keys_pressed['up'] or self.keys_pressed['down']:
                self.position[0] += self.diagonal_speed * dt
            else:
                self.position[0] += self.speed * dt

    def draw(self):
        print(self.position)
        w, h = self.screen.get_size()
        self.screen.blit(
            self.sprite,
            (w//2-self.sprite_size//2, h//2-self.sprite_size//2),
        )
