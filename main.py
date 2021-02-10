import pygame
import grid_utils
import a_star_algorithm as algo

from node import Node


WIDTH = 800
SCREEN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Path Finding Algorithm")


def main(screen, width):
    ROWS = 50

    start_node = None
    end_node = None
    run = True
    started = False

    grid = grid_utils.make_grid(ROWS, width)

    while run:
        grid_utils.draw(screen, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if started:
                continue

            if pygame.mouse.get_pressed()[0]:  # Left mouse button
                pos = pygame.mouse.get_pos()
                row, col = grid_utils.get_clicked_position(pos, ROWS, width)
                node = grid[row][col]

                if not start_node and node != end_node:
                    start_node = node
                    start_node.make_start()
                elif not end_node and node != start_node:
                    end_node = node
                    end_node.make_end()
                elif node != end_node and node != start_node:
                    node.make_barrier()

            elif pygame.mouse.get_pressed()[2]:  # right mouse button
                pos = pygame.mouse.get_pos()
                row, col = grid_utils.get_clicked_position(pos, ROWS, width)
                node = grid[row][col]
                node.reset()

                if node == start_node:
                    start_node = None
                elif node == end_node:
                    end_node = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start_node and end_node:
                    print('Hello')
                    for row in grid:
                        for node in row:
                            node.update_neighbours(grid)

                    algo.algorithm(lambda: grid_utils.draw(screen, grid,
                                                           ROWS, width), grid, start_node, end_node)

                if event.key == pygame.K_c:
                    start_node = None
                    end_node = None
                    grid = grid_utils.make_grid(ROWS, width)

    pygame.quit()


main(SCREEN, WIDTH)
