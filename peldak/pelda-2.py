# Game Loop
# display
# konstansok
import pygame
from pygame.locals import *

# a pygame egy game loopban eventekkel dolgozik
# néhány konstanst előre definiáltam (constants_example.py)
import constants_example as const

# itt a width és a height konstansokkal definiálunk egy ablakot, 
# amiben a játék fut majd. Lehetne ez akár a constants-ban is,
# de egy függvény eredménye nem feltétlen konstans, 
# így inkább ezt itt tartanám

WINDOW = pygame.display.set_mode((const.WIDTH, const.HEIGHT))

# még egy pici apróságként adjunk az ablaknak egy nevet
pygame.display.set_caption("Péld Ablak")

# ez a main function lesz a játékunk.
# most elég gyér, de fontos részeket láthatunk benne
# 
# a running változó határozza meg, hogy a game loop (azaz maga a játék) fut-e
# ha ezt False-ra állítjuk, a játék leáll (az ablak bezáródik)
#
# ebben a game loop-ban folyamatosan figyeljük a pygame eventeket és ha quit eventet kapunk, akkor kilépünk
# a pygame eventekről bővebben kicsit később
#
# természetesen ha a loop futása leáll, akkor is kilépünk
#
def main():
    running = True

    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

if __name__ == "__main__":
    main()