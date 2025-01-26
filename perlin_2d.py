import numpy as np
import pygame
from perlin_noise import PerlinNoise

WIDTH, HEIGHT = 800, 600
TILE_SIZE = 20

NOISE_SCALE = 100

COLORS = {
    'water': (0, 0, 255),
    'sand': (225, 225, 0),
    'grass': (0, 255, 0),
    'rock': (192, 192, 192),
    'snow': (255, 255, 255),
}

pygame.init()
noise = PerlinNoise(octaves=1, seed=1)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Real-Time Terrain Generation')
def generate_terrain(screen, width, height, tile_size, camera_x, camera_y):
    for y in range(0, height, tile_size):
        for x in range(0, width, tile_size):

            global_x = (x + camera_x) / NOISE_SCALE
            global_y = (y + camera_y) / NOISE_SCALE

            noise_val = noise([global_x, global_y])
            if noise_val < -0.05:
                color = COLORS['water']
            elif noise_val < 0:
                color = COLORS['sand']
            elif noise_val < 0.35:
                color = COLORS['grass']
            elif noise_val < 0.6:
                color = COLORS['rock']
            else:
                color = COLORS['snow']

            pygame.draw.rect(screen, color, (x, y, tile_size, tile_size))
def main():
    clock = pygame.time.Clock()
    running = True

    camera_x, camera_y = 0, 0
    camera_speed = 10

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: 
            camera_x -= camera_speed
        if keys[pygame.K_RIGHT]: 
            camera_x += camera_speed
        if keys[pygame.K_UP]: 
            camera_y -= camera_speed
        if keys[pygame.K_DOWN]: 
            camera_y += camera_speed
        if keys[pygame.K_ESCAPE]:
            break

        generate_terrain(screen, WIDTH, HEIGHT, TILE_SIZE, camera_x, camera_y)

        pygame.display.flip()

        clock.tick(30)

    pygame.quit()
if __name__ == '__main__':
    main()