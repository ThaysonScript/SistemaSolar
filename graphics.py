from OpenGL.GL import *
from OpenGL.GLU import *
import math

def draw_planet(distance, size, angle, texture):
    glPushMatrix()
    
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture)
    
    # Aplica a rotação no eixo Y e a translação para a órbita
    glRotatef(angle, 0, 1, 0)
    glTranslatef(distance, 0, 0)  # Distância do planeta em relação ao Sol

    # Cria a esfera para representar o planeta
    quadric = gluNewQuadric()
    gluQuadricTexture(quadric, GL_TRUE)
    gluSphere(quadric, size, 20, 20)

    glDisable(GL_TEXTURE_2D)
    
    glPopMatrix()

def draw_ring(inner_radius, outer_radius, texture, angle=0):
    glPushMatrix()
    
    # Aplicar a rotação do planeta ao anel
    glRotatef(angle, 0, 1, 0)  # Faz o anel girar com o planeta

    if texture:
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, texture)

    quadric = gluNewQuadric()
    gluQuadricTexture(quadric, GL_TRUE)

    glRotatef(90, 1, 0, 0)  
    gluDisk(quadric, inner_radius, outer_radius, 50, 1)  

    if texture:
        glDisable(GL_TEXTURE_2D)

    glPopMatrix()

# funççao para criar o bg
def draw_background(texture):
    glDisable(GL_DEPTH_TEST) 
    glPushMatrix()
    glLoadIdentity()

    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture)

    glBegin(GL_QUADS)
    

    glTexCoord2f(0, 0); glVertex3f(-20, -20, -20)
    glTexCoord2f(1, 0); glVertex3f( 20, -20, -20)
    glTexCoord2f(1, 1); glVertex3f( 20,  20, -20)
    glTexCoord2f(0, 1); glVertex3f(-20,  20, -20)
    
    glEnd()
    
    glDisable(GL_TEXTURE_2D)
    glEnable(GL_DEPTH_TEST)
    glPopMatrix()


def draw_orbit(radius):
    glPushMatrix()
    glColor3f(0.5, 0.5, 0.5)  
    glBegin(GL_LINE_LOOP)

   
    for i in range(100):
        angle = 2 * math.pi * i / 100 
        x = radius * math.cos(angle)
        z = radius * math.sin(angle)
        glVertex3f(x, 0, z) 

    glEnd()
    glPopMatrix()
