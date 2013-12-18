__author__ = '@drscake'

import pygame
from gol import *

class GolBoard(GameOfLife):
    "The game board for game of life"

    WHITE = (255, 255, 255)
    BLACK = (0,  0,  0)
    BLUE = (0, 0, 255)

    def __init__(self, board_width=640, board_height=480, cell_size=10):
        #use default values if there is no user input
        self.board_width = board_width
        self.board_height = board_height
        self.cell_size = cell_size    # square cell

        #calculate cell width and height
        num_col = self.board_width / self.cell_size
        num_row = self.board_height / self.cell_size

        #override user's input to draw a proportionally scaled game board
        self.board_width = num_col * cell_size
        self.board_height = num_row * cell_size

        super(GolBoard,self).__init__(num_col,num_row)

        self.evolving_rate = 10  # frames per second
        self.init_game_view()

    def init_game_view(self):
        #setup the gameboard/window/display
        pygame.display.set_mode((self.board_width,self.board_height))
        pygame.display.get_surface().fill(GolBoard.WHITE)
        pygame.display.set_caption('Game of Life')

        #inital view of the game
        pygame.init()
        self.draw_board_grid()
        self.display_current_board()
        pygame.display.update()

    def draw_board_grid(self):
        for x in range(0, self.board_width, self.cell_size): # draw vertical lines
            pygame.draw.line(pygame.display.get_surface(), GolBoard.BLACK, (x,0),(x,self.board_height))
        for y in range (0, self.board_height, self.cell_size): # draw horizontal lines
            pygame.draw.line(pygame.display.get_surface(), GolBoard.BLACK, (0,y), (self.board_width, y))

    def color_live_cells(self,cell):
        #find coordinates
        x = cell[0] * self.cell_size
        y = cell[1] * self.cell_size

        #reset dead cells
        if self.game_grid[cell] == 0:
            pygame.draw.rect(pygame.display.get_surface(), GolBoard.WHITE, (x, y, self.cell_size, self.cell_size))
        #colour live cells
        if self.game_grid[cell] == 1:
            pygame.draw.rect(pygame.display.get_surface(), GolBoard.BLUE, (x, y, self.cell_size, self.cell_size))

    def display_current_board(self):
        for cell in self.game_grid:
            self.color_live_cells(cell)

    def set_evolving_rate(self, rate):
        self.evolving_rate = rate

    def run_game(self):
        #evolving
        self.get_next_generation()
        self.display_current_board()
        self.draw_board_grid()
        pygame.display.update()
        pygame.time.Clock().tick(self.evolving_rate)
