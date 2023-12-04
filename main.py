import pygame
import random
import time
from tilemap import *  # Importação de módulo externo (tilemap.py)
import math

# inicializando pygame
pygame.init()

clock = pygame.time.Clock()


# criando a janela
tela = pygame.display.set_mode((480, 480))

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
    draw_map(tela, map_data)
    mouse_x, mouse_y = pygame.mouse.get_pos()
    obterCelulaMouseOnHover(mouse_x,mouse_y)
    sprites_grupo.draw(tela)
    sprites_grupo.update()
    pygame.display.flip()
    


#comecando...
caminho = []
def depth_first_search(map_data, x, y, caminho):
    
    print("Pilha: ", caminho, end=' ')
    AtualizaGraficoDaTela()
    #time.sleep(0.1)

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

def find_start(map_data, valor=2):
    for i, row in enumerate(map_data):
        for j, celula in enumerate(row):
            if celula == valor:  # Encontrou a posição inicial (valor 2)
                return i, j
    return None

start_posicao = find_start(map_data)

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

def obterCelulaMouseOnHover(x,y,tamanhoCelula = TILE_SIZE):
    cell_x = math.floor(x/tamanhoCelula) 
    cell_y = math.floor(y/tamanhoCelula) 
    #print("Valor x:",cell_x," || Valor y:",cell_y)
    pygame.draw.rect(tela,BLUE,(cell_x*TILE_SIZE,cell_y*TILE_SIZE,TILE_SIZE,TILE_SIZE))
    return cell_x, cell_y

def main():
    global map_data, caminho
    running = True
    # the game loop

    # desenhar
    AtualizaGraficoDaTela()

    start_x, start_y = start_posicao
    

    while running:
        clock.tick(30)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    map_data[start_x][start_y] = 1
                    x, y = pygame.mouse.get_pos()
                    start_x, start_y = obterCelulaMouseOnHover(x,y)
                    map_data[start_y][start_x] = 2
                elif event.button == 3:
                    chegada_x, chegada_y = find_start(map_data, valor=3)
                    map_data[chegada_x][chegada_y] = 1
                    x, y = pygame.mouse.get_pos()
                    xx,yy= obterCelulaMouseOnHover(x,y)
                    map_data[xx][yy] = 3

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("Spacebar pressed!")
                    start_x, start_y = find_start(map_data)
                    depth_first_search(map_data, start_x, start_y, caminho)
                elif event.key == pygame.K_r:
                    map_data = generate_map(480,480)
                    print(map_data)
                    draw_map(tela, map_data)
                elif event.key == pygame.K_s:
                    start_x = int(input("Posição x inicial:"))
                    start_y = int(input("Posição y inicial:"))
                    map_data[start_x][start_y] = 2
                    draw_map(tela, map_data)

                    print("Agora, coletando dados da coordenade de chegada")
                    finish_x = int(input("Posição x final:"))
                    finish_y = int(input("Posição x final:"))
                    map_data[finish_x][finish_y] = 3
                    caminho = []
                    depth_first_search(map_data, start_x, start_y, caminho)


                    
        # update
        AtualizaGraficoDaTela()



if __name__ == "__main__":
    main()

pygame.quit()
