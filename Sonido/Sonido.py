

import pygame

import sys

from pygame.locals import *

def main():

    pygame.init()

    Reloj = pygame.time.Clock()

    Ventana = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("Interacción Humano Maquina")

    Fondo = pygame.image.load("fondo.jpg")

    Imagen = pygame.image.load("rooster.png")
    transparente = Imagen.get_at((0, 0))
    Imagen.set_colorkey(transparente)


    Ruidito = pygame.mixer.Sound("ouch.wav")


    Musica = pygame.mixer.Sound("guitarra.wav")

    coordenadas_monigotillo= (300, 200)

    MiMonigotillo = Monigotillo(coordenadas_monigotillo, Imagen)

    # Bajamos el volumen de la música
    Musica.set_volume(0.5)

    # bucle infinito (-1)
    Musica.play(-1)

    while True:

        MiMonigotillo.update(coordenadas_monigotillo)

        Ventana.blit(Fondo, (0, 0))
        Ventana.blit(MiMonigotillo.image, MiMonigotillo.rect)

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    sys.exit()

            # Si el evento es una pulsación de ratón...
            elif evento.type == MOUSEBUTTONDOWN:


                coordenadas_monigotillo = pygame.mouse.get_pos()


                Ruidito.play(0)
        Reloj.tick(30)


class Monigotillo(pygame.sprite.Sprite):

    def __init__(self, coordenadas, imagen):
        pygame.sprite.Sprite.__init__(self)

        self.ImgCompleta = imagen
        a=0
        self.arrayAnim=[]
        while a < 6:
            self.arrayAnim.append(self.ImgCompleta.subsurface((a*20,100,32,64)))
            a= a + 1
        self.anim= 0

        self.actualizado = pygame.time.get_ticks()
        self.image = self.arrayAnim[self.anim]
        self.rect = self.image.get_rect()
        self.rect.center = coordenadas


    def update(self, nuevas_coordenadas):
        self.rect.center = nuevas_coordenadas
        if self.actualizado + 100 < pygame.time.get_ticks():
            self.anim= self.anim + 1
            if self.anim > 5:
                self.anim= 0
            self.image = self.arrayAnim[self.anim]
            self.actualizado= pygame.time.get_ticks()


main()