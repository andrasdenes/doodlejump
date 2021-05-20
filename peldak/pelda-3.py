# színnel való kitöltés
# display update
# FPS

import pygame
from pygame.locals import *
import constants_example as const

WINDOW = pygame.display.set_mode((const.WIDTH, const.HEIGHT))

pygame.display.set_caption("Péld Ablak")

# Ez a fájl csak egy DLC az előző példához,
# kitöltjük egy színnel a teljes ablakot
# a szín a constants_example-ben definiált
# egyébként meg csak annyi pluszban, hogy egy függvénybe kiszerveztük,
# hogy ne legyen összehányva a game loop.
# Így is lesz benne elég dolog.
#
# nagyon fontos hogy a pygame.display.update() meghívásra kerüljön
# más esetben nem kerül kirajzolásra a frissebb window állapot
def draw_window():
    WINDOW.fill(const.LIK_GREEN)
    pygame.display.update()

# és kicsit lekorlátozzuk a while ciklusunkat, 
# pontosan másodpercenként 60 ismétlődésre: 60 FPS
# ez azért fontos mert ha rengeteg dolgot akarnánk kirajzolni a game loopban, 
# az előbb-utóbb problémás lenne,
# így max 60 fps-t tudunk biztosítani, kevesebb (teljesítménytől függően) lehet, 
# de több nem 
def main():
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(const.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw_window()
    pygame.quit()

if __name__ == "__main__":
    main()