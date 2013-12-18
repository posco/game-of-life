__author__ = '@drscake'

import sys
from pygame.locals import *
from golui import *

gol = GolBoard()
gol.init_game_view()
gol.set_evolving_rate(5)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    gol.run_game()
