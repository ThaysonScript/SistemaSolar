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



def draw_orbit(distance, segments=100):
    glLineWidth(2)
    glColor4f(1.0, 1.0, 1.0, 0.5)
    
    glBegin(GL_LINE_LOOP)
    for i in range(segments):
        angle = 2 * math.pi * i / segments
        x = distance * math.cos(angle)
        z = distance * math.sin(angle)
        glVertex3f(x, 0, z)  # Desenha a órbita no plano XZ
    glEnd()