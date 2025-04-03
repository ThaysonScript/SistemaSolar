from OpenGL.GL import *
from OpenGL.GLU import *
import math

def draw_planet(size, texture):
    """Desenha um planeta com iluminação e textura"""
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture)
    
    # Configuração de materiais para resposta à luz
    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, [1.0, 1.0, 1.0, 1.0])
    glMaterialfv(GL_FRONT, GL_SPECULAR, [0.5, 0.5, 0.5, 1.0])
    glMateriali(GL_FRONT, GL_SHININESS, 50)
    
    quadric = gluNewQuadric()
    gluQuadricTexture(quadric, GL_TRUE)
    gluQuadricNormals(quadric, GLU_SMOOTH)
    gluSphere(quadric, size, 32, 32)
    
    glDisable(GL_TEXTURE_2D)
    

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