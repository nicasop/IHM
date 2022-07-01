# Integrantes: Anthony Grijalva - Sebastian Sandoval - Alexis Villavicencio
import pygame
import sys

SCREEN_WIDTH = 850
SCREEN_HEIGHT = 480

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Interaccion Humano Maquina")

    fond = pygame.image.load("fondoups.jpg").convert()
    fond = pygame.transform.scale(fond,(SCREEN_WIDTH,SCREEN_HEIGHT))
    tux = pygame.image.load("tux.png").convert_alpha()

    tux_pos_x = 850
    tux_pos_y = 0

    screen.blit(fond,(0, 0))
    screen.blit(tux,(tux_pos_x, tux_pos_y))

    pygame.display.flip()
    clock = pygame.time.Clock()

    while True:
        clock.tick(200)
        tux_pos_x = tux_pos_x - 1
        if tux_pos_x < -1:
            tux_pos_x = 850
            tux_pos_y += 100
        if tux_pos_y > 400:
            tux_pos_x = 850
            tux_pos_y = 0
            
        screen.blit(fond,(0, 0))
        screen.blit(tux,(tux_pos_x, tux_pos_y))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

if __name__ == "__main__":
    main()