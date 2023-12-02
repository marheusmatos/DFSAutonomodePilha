import pygame
import random

# dimension of each tiles
TILE_SIZE = 32

# texture of colors
YELLOW  = (255, 255, 0)
RED     = (255, 0, 0)
BLUE    = (0 , 0, 255)
GREEN   = (0, 255, 0)
BROWN   = (160, 82, 45)
DARKBORWN = (83, 42, 23)

def create_texture(color):
    image = pygame.Surface((TILE_SIZE, TILE_SIZE))
    image.fill(color)
    return image

# 0x0 -> grass
# 0xb -> dirt

textures = {
    0 : create_texture(GREEN),
    1 : create_texture(BROWN),
    2 : create_texture(BLUE),
    3 : create_texture(RED),
    4 : create_texture(DARKBORWN),
}

tiles = [0,1]

# generate with tiles randomly
def generate_map(width, height, tilesize = TILE_SIZE):
    map_data = []
    for i in range(height // tilesize):
        map_data.append([])
        for j in range(width // tilesize):
            rand_index = random.randint(0,1)
            # convert to hex from string value
            tile = tiles[rand_index]
            map_data[i].append(tile)
    return map_data


def draw_map(screen, map_data):
    MAP_HEIGHT = len(map_data) 
    MAP_WIDTH = len(map_data[0])
    for row in range(MAP_HEIGHT):
        for col in range(MAP_WIDTH):
            screen.blit(textures[map_data[row][col]],
                        (col*TILE_SIZE, row*TILE_SIZE))     