import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math
from opengl_init import init_opengl
from graphics import draw_planet
from textures import load_texture
from camera import setup_camera, handle_camera_movement

class Planet:
    def __init__(self, distance, size, speed, texture_file):
        self.distance = distance  
        self.size = size          
        self.angle = 0            
        self.speed = speed       
        self.texture = load_texture(texture_file)  

    def update(self, dt):
        self.angle += self.speed * dt  

    def draw(self):
        draw_planet(self.distance, self.size, self.angle, self.texture)  


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    init_opengl()

    # Planetas do sistema solar
    planets = [
        Planet(2.0, 0.3, 50, 'assets/mercury.jpg'), 
        Planet(3.5, 0.6, 35, 'assets/venus.jpg'),    
        Planet(5.0, 0.7, 30, 'assets/earth.jpg'),    
        Planet(7.0, 0.5, 25, 'assets/mars.jpg'),     
        Planet(9.0, 1.0, 20, 'assets/jupiter.jpg'),  
        Planet(12.0, 0.9, 15, 'assets/saturn.jpg'),  
        Planet(15.0, 0.6, 12, 'assets/uranus.jpg'),  
        Planet(19.0, 0.5, 10, 'assets/neptune.jpg')  
    ]

    # Textura do Sol (no centro)
    sun_texture = load_texture('assets/sun.jpg')

    last_time = pygame.time.get_ticks() / 1000.0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        keys = pygame.key.get_pressed()
        handle_camera_movement(keys)

        # Atualiza a rotação dos planetas
        current_time = pygame.time.get_ticks() / 1000.0
        dt = current_time - last_time
        last_time = current_time

        for planet in planets:
            planet.update(dt)

        # Limpa a tela e configura a câmera
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        setup_camera()

        # Desenha o Sol (centro do sistema solar)
        draw_planet(0, 1.2, 0, sun_texture)  # Sol no centro

        # Desenha os planetas
        for planet in planets:
            planet.draw()

        # Atualiza a tela
        pygame.display.flip()
        pygame.time.wait(20)

if __name__ == "__main__":
    main()
