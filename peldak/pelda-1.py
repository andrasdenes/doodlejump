# Pygame játékkészítés
# importáljuk a pygame modult - ez bizonyos esetekben okozhat nehézségeket
# probléma esetén érdekes a dokumentációhoz nyúlni, szinte biztosan le van írva a fix
import pygame
from pygame.locals import * 

# ennek az initnek különleges funkciója nincs,
# mindössze megnézzük hogy használható-e a pygame
# egy barátságos hello üzenet és néhány verziószám fogad minket futtatáskor:
#
# pygame 2.0.0 (SDL 2.0.12, python 3.7.4)
# Hello from the pygame community. https://www.pygame.org/contribute.html
pygame.init()