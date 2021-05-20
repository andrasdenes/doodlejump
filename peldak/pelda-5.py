# képek beszúrása
# képek méretezése
# képek elhelyezése
# képek mozgatása
import pygame
from pygame.locals import *
import constants_example as const
import os

WINDOW = pygame.display.set_mode((const.WIDTH, const.HEIGHT))

# nézzünk meg egyet és a többi adja majd magát, egy kivételével:
# pygame.image.load segítségével tölthetünk be képeket.
# eléggé jól kompatibilis visszafele szóval ha valaki valami ősrégi képformátummal (bmp) 
# próbálkozna, lehet hogy megenné - fun fact: a JPEG első publikációja 1992 -
# én most png-nél maradok inkább
# új import: os
# ismeretes, az operációs rendszert utasíthgathatjuk vele
# os.path.join(*args) stringeket vár paraméterül, bármennyit és platformtól
# függetlenül helyesen foga összerakni az útvonalat.
# pl:
# windows: D:\\assets\\bck.png
# linux: /home/denesandras/assets/bck.png

# a háttérképünk picit kicsi szóval fel kellene skálázni. 
# egy pygame.transform.scale() függvénybe belerakjuk az eddigi betöltést és
# megadunk paraméternek két méretet
# hint: ha valaki esetleg cimbi Flutterrel, akkor nem ijed meg egy ilyen beágyazástól :D
BG = pygame.transform.scale(pygame.image.load(os.path.join("peldak","assets","bck.png")),(const.WIDTH, const.HEIGHT))

# Lik a karakterünk neve lesz most, valamilyen nyelven ez mást jelent de nekünk most csak egy név
# szóval Lik-et is kicsit át fogom méretezni a collision boxok miatt
# azért méretezek és nem megnézem mekkora a karakterről készült kép mert lusta vagyok és
# elég jól meg tudom becsülni a méretet
# ezeket a méreteket én ki is rakom a constants-ba (60)
LIK_LEFT = pygame.transform.scale(pygame.image.load(os.path.join("peldak", "assets","lik-left.png")),(const.LIK_WIDTH, const.LIK_HEIGHT))
LIK_RIGHT = pygame.transform.scale(pygame.image.load(os.path.join("peldak", "assets","lik-right.png")),(const.LIK_WIDTH, const.LIK_HEIGHT))
LIK_PUCA = pygame.transform.scale(pygame.image.load(os.path.join("peldak", "assets","lik-puca.png")),(const.LIK_WIDTH, const.LIK_HEIGHT))
LIK_NJUSKA = pygame.image.load(os.path.join("peldak", "assets","lik-njuska.png")) # őt még direkt nem méreteztem át
LIK_GHOST = pygame.transform.scale(pygame.image.load(os.path.join("peldak", "assets","ghost-left@2x.png")),(const.LIK_WIDTH, const.LIK_HEIGHT))

pygame.display.set_caption("Péld Ablak")
# kicsit megváltozott a draw_window
# eltűnt a színes kitöltés de lett helyette background image a blit metódus segítségével
# a blit egy képet és egy x,y koordináta-párt (tuple) vár
# az x,y nyilván a "rajzolás" kezdésének helye, ami a mi esetünkben 0,0 hiszen a teljes képernyőre szeretnénk a képet
# a pygame is a bal felső sarkot tekinti az origónak
# ezután látjátok, hogy a LIK_LEFT képet is hozzáadjuk az ablakhoz, lik_rect position-nel, erről pár sorral lejjebb
def draw_window(lik_rect):
    WINDOW.blit(BG,(0, 0))
    WINDOW.blit(LIK_LEFT, (lik_rect.x, lik_rect.y))
    pygame.display.update()

# a main legnagyobb változása egy rectangle bevezetése
# mellékeltem egy képet boundingbox néven, ezt érdemes megnézni
# ott igazából ugyanez a megoldás látható csak 3D-ben. Nem összekeverendő a hitbox-szal.
#   Fun fact: ha valaha elgondolkodtál már azon miért rossz a csgo hitbox, akkor a hitbox.jpg megmutatja
# szóval vissza az eredeti témára
# egy négyszöggel kicsit könnyebb bánni mint egy képpel, ezért inkább a négyszöggel fogunk dolgozni
# és a négyszög mozgását fogja lekövetni a kép, ezért adjuk át a draw_window függvényünknek paraméterként a négyszöget
# és ha már itt vagyunk, akkor másodpercenként 60 pixellel feljebb is toljuk a kis karakterünket: lik_rect.y -= 1
# NOTE: természetesen ha +=1 lenne, akkor lefele indulna el,
# a bal felső sarok az origo és jobbra ill. lefele növekednek az x és y értékek
def main():
    clock = pygame.time.Clock()
    lik_rect = pygame.Rect(210, 620, const.LIK_WIDTH, const.LIK_HEIGHT)
    running = True
    while running:
        clock.tick(const.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        lik_rect.y -= 1
        draw_window(lik_rect)
    pygame.quit()

if __name__ == "__main__":
    main()