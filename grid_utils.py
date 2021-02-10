import pygame
import math
import constants.colour_settings as colours

from node import Node
from queue import PriorityQueue


def make_grid(rows, width):
    grid = []
    gap = width // rows

    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, gap, rows)
            grid[i].append(node)

    return grid


def draw_grid(screen, rows, width):
    gap = width // rows

    for i in range(rows):
        pygame.draw.line(screen, colours.GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(screen, colours.GREY,
                             (j * gap, 0), (j * gap, width))


def draw(screen, grid, rows, width):
    screen.fill(colours.WHITE)

    for row in grid:
        for node in row:
            node.draw(screen)

    draw_grid(screen, rows, width)
    pygame.display.update()


def get_clicked_position(position, rows, width):
    gap = width // rows
    y, x = position

    row = y // gap
    col = x // gap

    return row, col
