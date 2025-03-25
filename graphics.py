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
