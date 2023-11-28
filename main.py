import pygame
import random

from tilemap import *

# we initialize pygame module
pygame.init()

clock = pygame.time.Clock()


# create a surface represent our window
screen = pygame.display.set_mode((640, 480))

sprites_group = pygame.sprite.Group()

# map_data = generate_map(640, 480)

map_data = [
    [1, 2, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0],
    [1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1],
    [0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0],
    [1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 0, 3, 0, 1, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
    [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1],
    [0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0],
]
#comecando...
path = []
def depth_first_search(map_data, x, y, path):
    rows = len(map_data)
    cols = len(map_data[0])

    if (x < 0 or y < 0 or x >= rows or y >= cols or map_data[x][y] == 0 or map_data[x][y] == 4):
        return False

    path.append((x, y))  # Adiciona a célula ao caminho percorrido
    prev_value = map_data[x][y]
    map_data[x][y] = 4  # Marca a célula como visitada

    # Encontrou a célula de chegada (valor 3)
    if prev_value == 3:
        return True

    # Movimentos possíveis: cima, baixo, esquerda, direita
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for dx, dy in directions:
        if depth_first_search(map_data, x + dx, y + dy, path):
            return True

    # Se nenhum caminho foi encontrado a partir desta célula, remove-a do caminho
    path.pop()
    return False

def find_start(map_data):
    for i, row in enumerate(map_data):
        for j, cell in enumerate(row):
            if cell == 2:  # Encontrou a posição inicial (valor 2)
                return i, j
    return None

start_position = find_start(map_data)

if start_position:
    start_x, start_y = start_position
    if depth_first_search(map_data, start_x, start_y, path):
        print("Caminho encontrado!")
        print("Caminho percorrido:")
        for cell in path:
            print(cell)
    else:
        print("Não há caminho para a saída.")
else:
    print("Posição inicial não encontrada no mapa.")

#carregando iamgem do mapa
imgMapa = pygame.image.load('fundoMapa.png')

def main():
    running = True
    # the game loop

    while running:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # draw
        screen.fill((31, 106, 0))
        screen.blit(imgMapa, (480, 0))
        draw_map(screen, map_data)
        sprites_group.draw(screen)

        # update
        sprites_group.update()
        pygame.display.flip()


if __name__ == "__main__":
    main()

pygame.quit()
