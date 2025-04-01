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

def draw_ring(inner_radius, outer_radius, angle, texture):
    glPushMatrix()
    
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture)
    
    # Aplica a mesma rotação que o planeta
    glRotatef(angle, 0, 1, 0)
    
    # Cria um disco (anel) para representar os anéis de Saturno
    quadric = gluNewQuadric()
    gluQuadricTexture(quadric, GL_TRUE)
    gluQuadricOrientation(quadric, GLU_OUTSIDE)
    gluDisk(quadric, inner_radius, outer_radius, 32, 1)
    
    # Desenha o outro lado do anel
    gluQuadricOrientation(quadric, GLU_INSIDE)
    gluDisk(quadric, inner_radius, outer_radius, 32, 1)
    
    glDisable(GL_TEXTURE_2D)
    
    glPopMatrix()



def draw_ring(inner_radius, outer_radius, texture):
    glPushMatrix()

    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture)

    quadric = gluNewQuadric()
    gluQuadricTexture(quadric, GL_TRUE)
    
    glRotatef(90, 1, 0, 0)  
    gluDisk(quadric, inner_radius, outer_radius, 50, 1)  

    glDisable(GL_TEXTURE_2D)
    
    glPopMatrix()
