__author__ = '@drscake'

import random

class GameOfLife(object):

    def __init__(self, num_col, num_row):
        self.num_col = num_col
        self.num_row = num_row
        self.game_grid = {}

        self.init_game_grid()
        self.get_random_population()

    def init_game_grid(self):
        for x in range (self.num_col):
            for y in range (self.num_row):
                self.game_grid[x,y] = 0  # all cells are initially dead

    def get_random_population(self):
        # cell structure: (x,y): value; 0 as dead, 1 as live
        for cell in self.game_grid:
            self.game_grid[cell] = random.randint(0, 1)

    def is_in_grid(self, cell):
        return 0 <= cell[0] < self.num_col and 0 <= cell[1] < self.num_row

    def is_live_cell(self, cell):
        return self.game_grid[cell] == 1

    def get_neighbours(self, cell):

        """
        Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically,
        or diagonally adjacent

        x-1,y+1 | x,y+1 | x+1,y+1
        --------|-------|---------
        x-1,y   |  x,y  | x+1,y
        --------|-------|---------
        x-1,y-1 | x,y-1 | x+1,y-1

        """

        list_neighbours=[]
        for x in range (-1, 2):
            for y in range (-1, 2):
                if x != 0 or y != 0:
                    list_neighbours.append((cell[0] + x, cell[1] + y))
        return list_neighbours

    def get_num_neighbours(self, cell):
        num_neighbours = 0
        list_neighbours = self.get_neighbours(cell)
        for neighbour_cell in list_neighbours:
            if self.is_in_grid(neighbour_cell):
                if self.is_live_cell(neighbour_cell):
                    num_neighbours += 1
        return num_neighbours

    """
    see: http://en.wikipedia.org/wiki/Conway's_Game_of_Life

    Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically,
    or diagonally adjacent. At each step in time, the following transitions occur:
    - Any live cell with fewer than two live neighbours dies, as if caused by under-population.
    - Any live cell with two or three live neighbours lives on to the next generation.
    - Any live cell with more than three live neighbours dies, as if by overcrowding.
    - Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction
    """
    def get_next_generation(self):
        next_generation = {}
        for cell in self.game_grid:
            #get number of neighbours for that item
            num_neighbours = self.get_num_neighbours(cell)
            if self.game_grid[cell] == 1:
                if num_neighbours < 2:
                    next_generation[cell] = 0   # under-population
                elif num_neighbours > 3:
                    next_generation[cell] = 0   # overcrowding
                else:
                    next_generation[cell] = 1   # lives on to the next generation.
            elif self.game_grid[cell] == 0:
                if num_neighbours == 3:
                    next_generation[cell] = 1   # reproduction
                else:
                    next_generation[cell] = 0   # remain dead

        self.game_grid = next_generation