## INTEGRANTES: Anthony Grijalva - Sebastian Sandoval - Alexis Villavicencio

import pygame
from random import randint
import threading
import time

pygame.init()
ventana = pygame.display.set_mode((640,480))
pygame.display.set_caption("Interaccion Humano Maquina")
ball = pygame.image.load("ball.png")
ballrect = ball.get_rect()
speed = [3,3]
ballrect.move_ip(0,0)

bate = pygame.image.load("bate.png")
baterect = bate.get_rect()
baterect.move_ip(240,450)

bate1 = pygame.image.load("bate.png")
bate1 = pygame.transform.rotate(bate1,90)
bate1rect = bate1.get_rect()
print(bate1rect)
bate1rect.move_ip(10,240)

fuente = pygame.font.Font(None, 36)
jugando = True

def timer():
    while True:
        if speed[0] < 0:
            speed[0] -= 1
        else:
            speed[0] += 1
        if speed[1] < 0:
            speed[1] -= 1
        else:
            speed[1] += 1

        time.sleep(5)

t = threading.Thread(target=timer)
t.start()

while jugando:
    # print(speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        baterect = baterect.move(-6,0)
    if keys[pygame.K_RIGHT]:
        baterect = baterect.move(6,0)
    if keys[pygame.K_UP]:
        bate1rect = bate1rect.move(0,-6)
    if keys[pygame.K_DOWN]:
        bate1rect = bate1rect.move(0,6)

    if baterect.colliderect(ballrect):
        speed[1] = -speed[1]
    if bate1rect.colliderect(ballrect):
        speed[0] = -speed[0]
    if ballrect.right > ventana.get_width():
        speed[0] = -speed[0]

    if ballrect.top < 0:
        speed[1] = -speed[1]

    if ballrect.bottom > ventana.get_height() or ballrect.left < 0:
        texto = fuente.render("Game Over", True, (125,125,125))
        texto_rect = texto.get_rect()
        texto_x = ventana.get_width() / 2 - texto_rect.width / 2
        texto_y = ventana.get_height() / 2 - texto_rect.height / 2
        ventana.blit(texto, [texto_x, texto_y])   
    else:
        ventana.fill((0, 0, 255))
        ventana.blit(ball, ballrect)
        ventana.blit(bate, baterect)
        ventana.blit(bate1, bate1rect)

    ballrect = ballrect.move(speed)
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()