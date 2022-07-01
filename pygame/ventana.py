import pygame
import sys

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 480

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    pygame.display.set_caption("UNIVERSIDAD POLITÉCNICA SALESIANA")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

if __name__ == "__main__":
    main()
