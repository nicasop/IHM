"""
Elaborado por
    Anthony Grijalva
    Sebastian Sandoval
    Alexis Villavicencio
"""

import pygame
import random

FRAME_REFRESH_RATE = 20
DISPLAY_WIDTH = 1200
DISPLAY_HEIGHT = 600

BACKGROUND = (255, 255, 255)
STARSHIP_SPEED = 30
INITIAL_NUMBER_OF_METEORS = 3
INITIAL_METEOR_Y_LOCATION = 10
MAX_METEOR_SPEED = 5

MAX_NUMBER_CYCLES = 500
NEW_METEOR_CYCLE_INTERVAL = 60

BLUE = (0, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class JuegoObject:
    def lee_imagen(self, filename):
        self.image = pygame.image.load(filename).convert_alpha()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
    
    def rectangulo(self):
        return pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

    def dibuja(self):
        self.juego.display_surface.blit(self.image, (self.x, self.y))

class Nave(JuegoObject):
    def __init__(self, juego):
        self.juego = juego
        self.x = DISPLAY_WIDTH / 2
        self.y = DISPLAY_HEIGHT - 100
        self.lee_imagen("nave.png")

    def mover_derecha(self):
        self.x = self.x + STARSHIP_SPEED
        if self.x + self.width > DISPLAY_WIDTH:
            self.x = DISPLAY_WIDTH - self.width

    def mover_izquierda(self):
        self.x = self.x - STARSHIP_SPEED
        if self.x < 0:
            self.x = 0

    def mover_arriba(self):
        self.y = self.y - STARSHIP_SPEED
        if self.y < 0:
            self.y = 0

    def mover_abajo(self):
        self.y = self.y + STARSHIP_SPEED
        if self.y + self.height > DISPLAY_HEIGHT:
            self.y = DISPLAY_HEIGHT - self.width

    def __str__(self):
        return 'Nave(' + str(self.x) + ',' + str(self.y) + ')'

class Meteoro(JuegoObject):
    def __init__(self, juego):
        self.juego = juego
        self.x = random.randint(0, DISPLAY_WIDTH)
        self.y = INITIAL_METEOR_Y_LOCATION
        self.speed = random.randint(1, MAX_METEOR_SPEED)
        self.lee_imagen("meteor.png")

    def mover_down(self):
        self.y = self.y + self.speed
        if self.y > DISPLAY_HEIGHT:
            self.y = 5

    def __str__(self):
        return 'Meteoro(' + str(self.x) + ',' + str(self.y) + ')'

class Juego:
    def __init__(self):
        print("Inicializando Pygame")
        pygame.init()
        self.display_surface = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
        pygame.display.set_caption("Meteoritos y espacial")
        self.fond = pygame.image.load("fondo.jpg").convert()
        self.fond = pygame.transform.scale(self.fond,(DISPLAY_WIDTH,DISPLAY_HEIGHT))
        self.display_surface.blit(self.fond,(0,0))
        self.clock = pygame.time.Clock()
        # Setea la nave
        self.nave = Nave(self)
        self.meteoros = [Meteoro(self) for _ in range(0, INITIAL_NUMBER_OF_METEORS)]
    
    def _pause(self):
        paused = True
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        paused = False
                        break

    def desplegar_mensage(self, mensaje):
        texto_font = pygame.font.Font("freesansbold.ttf", 48)
        texto_surface = texto_font.render(mensaje, True, (125, 125, 125))
        texto_rectangle = texto_surface.get_rect()
        texto_rectangle.center = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2)
        self.display_surface.blit(texto_surface, texto_rectangle)

    def desplegar_tiempo(self,cont):
        texto_font = pygame.font.SysFont("candara", 20)
        texto_font.set_bold(True)
        texto_surface = texto_font.render('Tiempo: '+str(cont), True, (255, 255, 255))
        texto_rectangle = texto_surface.get_rect()
        texto_rectangle.center = (DISPLAY_WIDTH-texto_rectangle.width,texto_rectangle.height)
        self.display_surface.blit(texto_surface, texto_rectangle)

    def desplegar_Creditos(self,mensaje):
        texto_font = pygame.font.SysFont("candara", 20)
        texto_surface = texto_font.render(mensaje, True, (255, 255, 255))
        texto_rectangle = texto_surface.get_rect()
        texto_rectangle.center = (texto_rectangle.width,DISPLAY_HEIGHT-texto_rectangle.height)
        self.display_surface.blit(texto_surface, texto_rectangle)
    
    def control_colision(self):
        for meteoro in self.meteoros:
            if self.nave.rectangulo().colliderect(meteoro.rectangulo()):
                return True
        return False
                
    def play(self):
        is_running = True
        contador_c = 0
        while is_running:
            contador_c = contador_c + 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.nave.mover_derecha()
                    elif event.key == pygame.K_LEFT:
                        self.nave.mover_izquierda()
                    elif event.key == pygame.K_UP:
                        self.nave.mover_arriba()
                    elif event.key == pygame.K_DOWN:
                        self.nave.mover_abajo()
                    elif event.key == pygame.K_q:
                        is_running = False
                    elif event.key == pygame.K_p:
                        self._pause()

             
            if self.control_colision():
                self.display_surface.fill(BLACK)
                self.desplegar_mensage('Perdiste, Intenta Nuevamente')
                self.desplegar_Creditos('ELABORADO POR: Anthony Grijalva - Sebastian Sandoval - Alexis Villavicencio')
            elif contador_c >= MAX_NUMBER_CYCLES:
                self.display_surface.fill(BLACK)
                self.desplegar_mensage('Ganaste Felicitaciones')
                self.desplegar_Creditos('ELABORADO POR: Anthony Grijalva - Sebastian Sandoval - Alexis Villavicencio')
            else:
                self.display_surface.blit(self.fond,(0,0))
                for meteoro in self.meteoros:
                    meteoro.dibuja()
                # Dibuja la nave
                self.nave.dibuja()
                for meteoro in self.meteoros:
                    meteoro.mover_down()
                self.desplegar_tiempo(contador_c)

                if contador_c % NEW_METEOR_CYCLE_INTERVAL == 0:
                    self.meteoros.append(Meteoro(self))

                # define la velocidad de fotogramas
                self.clock.tick(FRAME_REFRESH_RATE)
            pygame.display.update()
        pygame.quit()

def main():
    print("Iniciando juego")
    print('Elaborado por:')
    print('Anthony Grijalva\nSebastian Sandoval\nAlexis Villavicencio')
    juego = Juego()
    juego.play()
    print("Juego Terminado")

if __name__ == '__main__':
    main()
