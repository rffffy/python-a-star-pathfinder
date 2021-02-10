import pygame
import constants.colour_settings as colours


class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.colour = colours.WHITE
        self.neighbours = []
        self.width = width
        self.total_rows = total_rows

    def get_position(self):
        return self.row, self.col

    def is_closed(self):
        return self.colour == colours.RED

    def is_open(self):
        return self.colour == colours.GREEN

    def is_barrier(self):
        return self.colour == colours.BLACK

    def is_start(self):
        return self.colour == colours.ORANGE

    def is_end(self):
        return self.colour == colours.TURQUOISE

    def reset(self):
        self.colour = colours.WHITE

    def make_closed(self):
        self.colour = colours.RED

    def make_open(self):
        self.colour = colours.GREEN

    def make_barrier(self):
        self.colour = colours.BLACK

    def make_start(self):
        self.colour = colours.ORANGE

    def make_end(self):
        self.colour = colours.TURQUOISE

    def make_path(self):
        self.colour = colours.PURPLE

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour,
                         (self.x, self.y, self.width, self.width))

    def update_neighbours(self, grid):
        self.neighbours = []

        # Checking the neighbour that is Down
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier():
            self.neighbours.append(grid[self.row + 1][self.col])

        # Checking the neighbour that is Up
        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():
            self.neighbours.append(grid[self.row - 1][self.col])

        # Checking the neighbour that is Right
        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier():
            self.neighbours.append(grid[self.row][self.col + 1])

        # Checking the neighbour that is Left
        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():
            self.neighbours.append(grid[self.row][self.col - 1])

    def __lt__(self, other):
        return False
