# időzített ugrálás
# lövés
import pygame
from pygame.locals import *
import constants_example as const
import os

WINDOW = pygame.display.set_mode((const.WIDTH, const.HEIGHT))
#BUBBLE_HIT = pygame.USEREVENT + 1 # collisionhöz ha lesz idő enemy-re
MODIFY_JUMPSTATE_DOWN = pygame.USEREVENT + 2
MODIFY_JUMPSTATE_UP = pygame.USEREVENT + 3
MOVE_PLATFORMS_TO_670 = pygame.USEREVENT + 4
MODIFY_JUMPSTATE_DOWN_WITH_VALUE_CORRECTION = pygame.USEREVENT + 5
MODIFY_JUMPSTATE_UP_WITH_VALUE_CORRECTION = pygame.USEREVENT + 6

BG = pygame.transform.scale(pygame.image.load(os.path.join("peldak","assets","bck.png")),(const.WIDTH, const.HEIGHT))

LIK_LEFT = pygame.transform.scale(pygame.image.load(os.path.join("peldak", "assets","lik-left.png")),(const.LIK_WIDTH, const.LIK_HEIGHT))
LIK_RIGHT = pygame.transform.scale(pygame.image.load(os.path.join("peldak", "assets","lik-right.png")),(const.LIK_WIDTH, const.LIK_HEIGHT))
LIK_PUCA = pygame.transform.scale(pygame.image.load(os.path.join("peldak", "assets","lik-puca.png")),(const.LIK_WIDTH, const.LIK_HEIGHT))
LIK_NJUSKA = pygame.image.load(os.path.join("peldak", "assets","lik-njuska.png")) # őt még direkt nem méreteztem át
LIK_GHOST = pygame.transform.scale(pygame.image.load(os.path.join("peldak", "assets","ghost-left@2x.png")),(const.LIK_WIDTH, const.LIK_HEIGHT))
PLATFORM = pygame.transform.scale(pygame.image.load(os.path.join("peldak", "assets","platform.png")),(const.PLATFORM_WIDTH, const.PLATFORM_HEIGHT))
BUBBLE = pygame.image.load(os.path.join("peldak", "assets","bubble.png"))

pygame.display.set_caption("Péld Ablak")

# változott kicsit a paraméterlistánk és a függvény body is
# ennek oka hogy Lik ha jobbra megy, akkor jobbra néz, ha balra megy, akkor balra néz
def draw_window(lik_rect, bubbles, platforms, lik_direction="left"):
    WINDOW.blit(BG,(0, 0))
    if lik_direction == "left":
        WINDOW.blit(LIK_LEFT, (lik_rect.x, lik_rect.y))
    if lik_direction == "right":
        WINDOW.blit(LIK_RIGHT, (lik_rect.x, lik_rect.y))

    for bubble in bubbles:
        pygame.draw.rect(WINDOW, const.BLUE, bubble)

    for platform in platforms:
        WINDOW.blit(PLATFORM, (platform.x, platform.y))
    
    pygame.display.update()

def handle_lik_movements(keys_pressed, lik_rect, lik_direction):
    # A vagy BALRA NYÍL lenyomása esetén 4 pixelt megyünk framenként, 
    # amennyiben pedig elérjük a játéktér végét, visszajövünk a másik oldalról
    # és természetesen besetteljük a mozgás irányát megmondó stringet
    if keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]:
        lik_rect.x -= 4
        if lik_rect.x <= -(const.LIK_WIDTH):
            lik_rect.x = const.WIDTH+(const.LIK_WIDTH/2)
        lik_direction="left"

    # az előző esethez hasonlóan csak D vagy JOBBRA NYÍL gombokkal
    if keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]:
        lik_rect.x += 4
        if lik_rect.x > const.WIDTH:
            lik_rect.x = -(const.LIK_WIDTH)
        lik_direction="right"

    return lik_direction

def handle_bubbles(bubbles):
    for bubble in bubbles:
        bubble.y -= const.BUBBLE_VELOCITY
        #if bubble.collide(enemy): # collision check
            #bubbles.remove(bubble)
            #pygame.event.post(pygame.event.Event(BUBBLE_HIT))
        if bubble.y < -5:
            bubbles.remove(bubble)

def handle_jump_up(lik_rect, HB):
    lik_rect.y -= 5
    if lik_rect.y > 200 and lik_rect.y < 300:
        pygame.event.post(pygame.event.Event(MOVE_PLATFORMS_TO_670))
    if lik_rect.y <= HB:
        pygame.event.post(pygame.event.Event(MODIFY_JUMPSTATE_DOWN))
    

def handle_jump_down(lik_rect, LB):
    lik_rect.y += 5
    if lik_rect.y >= LB:
        pygame.event.post(pygame.event.Event(MODIFY_JUMPSTATE_UP))

def handle_platform_movement(platforms):
    for platform in platforms:
        if platform.y < 670:
            platform.y += 20

def handle_platforms_collision(platforms, lik_rect):
    for platform in platforms:
        if platform.colliderect(lik_rect):
            pygame.event.post(pygame.event.Event(MODIFY_JUMPSTATE_UP_WITH_VALUE_CORRECTION))

# elég sokminden történt
# már kicsit hasznosabb lenne a kódban kommentelnem, szóval a részletek lejjebb

# Lik már mozog jobbra és balra az A és D gombok vagy nyilak segítségével
# emellett ha a képernyő oldalára érünk, Lik felbukkan a másik oldalon
# Lik még arra is képes hogy mindig arra nézzen amerre megy, de ettől függetlenül a bal profilját szereti mutogatni

# rendkívül pontos mérések segítségével megállapítottam, hogy a karakterünk két platformérintése között maximum 1 másodperc telik el
# ez az egyhelyben ugrálsára igaz
# egy kis matekkal megkapjuk hogy egy frame alatt mennyit kellene tehát mozdulni ahhoz hogy 0,5 másodperc alatt felugorjunk,
# aztán 0,5 alatt leessünk.
# ez persze a legkevésbé sem pontos, mert egy ugrás sebessége nem lineáris de most az lesz
# kis matekozás után tehát az egy frame alatti elmozdulás mértéke, ha 180 pixel egy teljes ugrás: 180/30 = 6 mert 30 frame ugye fél másodperc
def main():
    clock = pygame.time.Clock()
    lik_rect = pygame.Rect(210, 620, const.LIK_WIDTH-10, const.LIK_HEIGHT-10)
    platform1 = pygame.Rect(100, 480, const.PLATFORM_WIDTH, const.PLATFORM_HEIGHT)
    platform2 = pygame.Rect(210, 480, const.PLATFORM_WIDTH, const.PLATFORM_HEIGHT)
    platform3 = pygame.Rect(320, 480, const.PLATFORM_WIDTH, const.PLATFORM_HEIGHT)
    running = True
    bubbles = []
    platforms = [platform1, platform2, platform3]
    jump_state = "up"
    LB = 620
    HB = 440

    while running:
        clock.tick(const.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bubble = pygame.Rect(lik_rect.x, lik_rect.y, const.BUBBLE_WIDTH, const.BUBBLE_HEIGHT)
                    bubbles.append(bubble)
            #if evenet.type == BUBBLE_HIT:
            #   handle enemy collision
            
            if event.type == MODIFY_JUMPSTATE_DOWN:
                jump_state = "down"

            if event.type == MODIFY_JUMPSTATE_UP:
                jump_state = "up"
            
            if event.type == MODIFY_JUMPSTATE_DOWN_WITH_VALUE_CORRECTION:
                jump_state = "down"
                print("max height modified")
                HB = lik_rect.y - 180

            if event.type == MODIFY_JUMPSTATE_UP_WITH_VALUE_CORRECTION:
                jump_state = "up"
                LB = lik_rect.y + 190
                pygame.event.post(pygame.event.Event(MODIFY_JUMPSTATE_DOWN_WITH_VALUE_CORRECTION))
            
            if event.type == MOVE_PLATFORMS_TO_670:
                handle_platform_movement(platforms)

        handle_platforms_collision(platforms, lik_rect)
        # az alábbi metódus segítségével ellenőrízhetjük milyen gombok kerültek lenyomásra
        # ez a metódus több gombot is érzékel
        keys_pressed = pygame.key.get_pressed()
        # mint említettem, Lik kedvenc profilja a bal
        lik_direction = handle_lik_movements(keys_pressed, lik_rect, lik_direction="left")

        if jump_state == "up":
            handle_jump_up(lik_rect, HB)
        
        if jump_state == "down":
            handle_jump_down(lik_rect, LB)

        handle_bubbles(bubbles)

        draw_window(lik_rect, bubbles, platforms, lik_direction=lik_direction)
        
    pygame.quit()


if __name__ == "__main__":
    main()