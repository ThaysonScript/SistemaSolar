import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from opengl_init import init_opengl
from graphics import *
from textures import load_texture
from camera import setup_camera, handle_camera_movement, movimento_mouse

class Planet:
    def __init__(self, distance, size, speed, texture_file, has_ring=False, ring_texture=None):
        self.distance = distance  
        self.size = size          
        self.angle = 0            
        self.speed = speed       
        self.texture = load_texture(texture_file) 
        self.has_ring = has_ring  
        self.ring_texture = load_texture(ring_texture) if has_ring else None 

    def update(self, dt):
        self.angle += self.speed * dt  

    def draw(self):
        glPushMatrix()
         
        glRotatef(self.angle, 0, 1, 0)  
        glTranslatef(self.distance, 0, 0)
   
        draw_planet(0, self.size, 0, self.texture) 
                
        if self.has_ring and self.ring_texture:
            draw_ring(self.size * 1.8, self.size * 2.5, self.ring_texture, self.angle)  
        
        glPopMatrix()


def main():
    display = (800, 600)
    
    pygame.init()
    pygame.display.set_caption('Sistema Solar')
    pygame.display.set_icon(pygame.image.load('assets/earth.webp'))
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL | RESIZABLE)
    init_opengl()

    planets = [
        Planet(2.0, 0.3, 50, 'assets/mercury.jpg'), 
        Planet(3.5, 0.6, 35, 'assets/venus.jpg'),    
        Planet(5.0, 0.7, 30, 'assets/earth.jpg'),    
        Planet(7.0, 0.5, 25, 'assets/mars.jpg'),     
        Planet(9.0, 1.0, 20, 'assets/jupiter.jpg'),  
        Planet(12.0, 0.9, 15, 'assets/saturn.jpg', has_ring=True, ring_texture='assets/saturn_ring_alpha.png'),  
        Planet(15.0, 0.6, 12, 'assets/uranus.jpg'),  
        Planet(19.0, 0.5, 10, 'assets/neptune.jpg')  
        
    ]

    sun_texture = load_texture('assets/sun.jpg')
    background_texture = load_texture('assets/space_bg.jpeg')

    last_time = pygame.time.get_ticks() / 1000.0
    
    move_active = False

    while True:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    move_active = True
                
            elif event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    move_active = False
                
            elif event.type == MOUSEMOTION and move_active:
                movimento_mouse(event.rel[0], event.rel[1])


        keys = pygame.key.get_pressed()
        handle_camera_movement(keys)
        import random

# Criamos um conjunto de partículas aleatórias
          
        dust_particles = []
        for _ in range(300):  # 300 grãos de poeira
            x = random.uniform(-20, 20)
            y = random.uniform(-10, 10)
            z = random.uniform(-20, 20)
            dust_particles.append((x, y, z))

        
        # Atualiza a rotação dos planetas
        current_time = pygame.time.get_ticks() / 1000.0
        dt = current_time - last_time
        last_time = current_time

        for planet in planets:
            planet.update(dt)
       
        # Limpa a tela e configura a câmera
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        setup_camera()
    
        #desenhando o plano de fundo 
        draw_background(background_texture)
  
        for planet in planets:
           draw_orbit(planet.distance)


         
        for planet in planets:
         planet.draw()
         
        # Desenha o Sol (centro do sistema solar)
        draw_planet(0, 1.2, 0, sun_texture) # Sol no centro

        # Desenha os planetas
        for planet in planets:
            planet.draw()
            draw_orbit(planet.distance)

        # Atualiza a tela
        pygame.display.flip()
        pygame.time.wait(20)

if __name__ == "__main__":
    main()
