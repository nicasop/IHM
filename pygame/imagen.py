import pygame
import sys

SCREEN_WIDTH = 850
SCREEN_HEIGHT = 480

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Interaccion Humano Maquina")
    fond = pygame.image.load("fondoups.jpg").convert()
    tux = pygame.image.load("tux.png").convert_alpha()

    screen.blit(fond,(0, 0))
    screen.blit(tux,(425, 200))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

if __name__ == "__main__":
    main()

