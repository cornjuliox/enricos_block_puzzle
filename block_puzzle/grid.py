import pygame

from .colors import Colors

class Grid:
    """ 
    This class represents the main game grid.
    By default it will be 20 rows high, 10 columns wide.
    """
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        self.grid = [
            [0 for _ in range(self.num_cols)]
            for _ in range(self.num_rows)
        ]
        self.colors = Colors.get_cell_colors()

    def reset(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                self.grid[row][column] = 0

    def print_grid(self):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                print(self.grid[row][col], end=" ")
            print()

    def is_inside(self, row, column):
        if row >= 0 and row < self.num_rows and column >= 0 and column < self.num_cols:
            return True
        return False
    
    def is_empty(self, row, column):
        if self.grid[row][column] == 0:
            return True
        return False
    
    def is_row_full(self, row):
        for column in range(self.num_cols):
            if self.grid[row][column] == 0:
                return False
        return True
    
    def clear_row(self, row):
        for column in range(self.num_cols):
            self.grid[row][column] = 0

    def clear_full_rows(self):
        completed = 0
        for row in range(self.num_rows - 1, 0, -1):
            if self.is_row_full(row):
                self.clear_row(row)
                completed += 1
            elif completed > 0:
                self.move_row_down(row, completed)
        return completed

    def move_row_down(self, row, num_rows):
        for column in range(self.num_cols):
            self.grid[row + num_rows][column] = self.grid[row][column]
            self.grid[row][column] = 0

    # NOTE: How Pygame draws things: 
    #       Display Surface - a blank canvas, you can only have one per game.
    #       It's created when you call `pygame.display.set_mode(...)`
    #       Surface - another canvas-like thing, you can have many surfaces per game.
    #       Rect - Used for positioning, collision detection, and drawing objects.
    #       A rect will be created to hold a cell, and then passed to pygame.draw.rect()
    def draw(self, screen):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                cell_value = self.grid[row][col]
                cell_rect = pygame.Rect(
                    col * self.cell_size + 11,
                    row * self.cell_size + 11,
                    self.cell_size - 1,
                    self.cell_size - 1
                )
                # NOTE: args are (pygame.surface, 3-tuple representing color, pygame.Rect)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)

            
