from OpenGL.GL import *

def setup_lighting():
    glEnable(GL_LIGHTING)
    
    glEnable(GL_LIGHT0)  # Fonte de luz primária (o Sol)
    
    # Definições de luz para o Sol
    light0_position = [0.0, 0.0, 0.0, 1.0]
    light0_ambient = [0.2, 0.2, 0.2, 1.0]
    light0_diffuse = [1.0, 1.0, 1.0, 1.0]
    light0_specular = [1.0, 1.0, 1.0, 1.0]

    glLightfv(GL_LIGHT0, GL_POSITION, light0_position)
    glLightfv(GL_LIGHT0, GL_AMBIENT, light0_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light0_diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light0_specular)

    # Definições de outras fontes de luz 
    glEnable(GL_LIGHT1)
    glEnable(GL_LIGHT2)

    global_ambient = [0.2, 0.2, 0.2, 1.0]
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, global_ambient)
