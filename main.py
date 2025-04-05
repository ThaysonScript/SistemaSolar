import pygame, random
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from lighting import init_lighting
from opengl_init import init_opengl
from graphics import *
from textures import load_texture
from camera import setup_camera, handle_camera_movement, movimento_mouse


# 🎶 Inicializando o mixer de áudio
pygame.mixer.init()
pygame.mixer.music.load('assets/space_ambient.mp3')  # Som ambiente espacial
pygame.mixer.music.set_volume(0.5)  # Ajustando volume
pygame.mixer.music.play(-1)  # 🔄 Reproduzir em loop infinito


class Sun:
    def __init__(self, distance, size, vel, texture):
        self.distance = distance
        self.size = size
        self.vel = vel
        self.texture = load_texture(texture)
        self.quadric = gluNewQuadric()  # Usado para desenhar o disco
        
    def draw(self):
        glPushMatrix()
        
        glDisable(GL_LIGHTING)
        glEnable(GL_TEXTURE_2D)
           
        draw_planet(self.size, self.texture) 
        
        glDisable(GL_TEXTURE_2D)
        glEnable(GL_LIGHTING)
        
        glPopMatrix()


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
   
        draw_planet(self.size, self.texture) 
                
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
    init_lighting()

    planets = [
    Planet(14.5, 0.49, 23.7, 'assets/mercury.jpg'), 
    Planet(27.0, 1.21, 17.5, 'assets/venus.jpg'),    
    Planet(37.4, 1.27, 14.9, 'assets/earth.jpg'),    
    Planet(57.0, 0.68, 12.0, 'assets/mars.jpg'),     
    Planet(194.6, 13.98, 6.6, 'assets/jupiter.jpg'),  
    Planet(257.5, 11.64, 4.85, 'assets/saturn.jpg', has_ring=True, ring_texture='assets/saturn_ring_alpha.png'),  
    Planet(317.5, 5.07, 3.4, 'assets/uranus.jpg'),  
    Planet(425.0, 4.92, 2.7, 'assets/neptune.jpg')  
    ]

    sun_texture = Sun(0, 20, 0, 'assets/sun.jpg')
    
    
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

        glLightfv(GL_LIGHT0, GL_POSITION, (0.0, 0.0, 0.0, 1.0))
        
        keys = pygame.key.get_pressed()
        handle_camera_movement(keys)

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
        # draw_sun(sun_texture) # Sol no centro
        sun_texture.draw()

        # Desenha os planetas
        for planet in planets:
            planet.draw()
            draw_orbit(planet.distance)

        # Atualiza a tela
        pygame.display.flip()
        pygame.time.wait(20)

if __name__ == "__main__":
    main()