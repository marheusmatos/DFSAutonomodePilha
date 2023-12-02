import pygame
import random
import time
from tilemap import *  # Importação de módulo externo (tilemap.py)

# inicializando pygame
pygame.init()

clock = pygame.time.Clock()


# criando a janela
tela = pygame.display.set_mode((640, 480))

sprites_grupo = pygame.sprite.Group()


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

def AtualizaGraficoDaTela():
    tela.fill((31, 106, 0))
    tela.blit(imgMapa, (480, 0))
    draw_map(tela, map_data)
    sprites_grupo.draw(tela)
    


#comecando...
caminho = []
def depth_first_search(map_data, x, y, caminho):
    
    
    AtualizaGraficoDaTela()

    rows = len(map_data)
    cols = len(map_data[0])

    if (x < 0 or y < 0 or x >= rows or y >= cols or map_data[x][y] == 0 or map_data[x][y] == 4):
        return False

    caminho.append((x, y))  # Adiciona a célula ao caminho percorrido
    prev_value = map_data[x][y]
    map_data[x][y] = 4  # Marca a célula como visitada

    # Encontrou a célula de chegada (valor 3)
    if prev_value == 3:
        return True

    # Movimentos possíveis: cima, baixo, esquerda, direita
    direcoes = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for dx, dy in direcoes:
        if depth_first_search(map_data, x + dx, y + dy, caminho):
            return True

    # Se nenhum caminho foi encontrado a partir desta célula, remove-a do caminho
    caminho.pop()
    return False

def find_start(map_data):
    for i, row in enumerate(map_data):
        for j, celula in enumerate(row):
            if celula == 2:  # Encontrou a posição inicial (valor 2)
                return i, j
    return None

start_posicao = find_start(map_data)

#carregando iamgem do mapa
imgMapa = pygame.image.load('fundoMapa.png')

def desenharCaminhoDFS():
    if start_posicao:
        start_x, start_y = start_posicao
        if depth_first_search(map_data, start_x, start_y, caminho):
            print("Caminho encontrado!")
            print("Caminho percorrido:")
            for celula in caminho:
                print(celula)
        else:
            print("Não há caminho para a saída.")
    else:
        print("Posição inicial não encontrada no mapa.")



def main():
    running = True
    # the game loop

    # desenhar


    start_x, start_y = start_posicao
    depth_first_search(map_data, start_x, start_y, caminho)

    while running:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False



        # update
        sprites_grupo.update()
        pygame.display.flip()


if __name__ == "__main__":
    main()

pygame.quit()
