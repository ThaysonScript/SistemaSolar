from OpenGL.GL import *

def setup_lighting():
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    
    glShadeModel(GL_SMOOTH)
    
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
        
    # # Definições de luz para o Sol
    # light0_position = [0.0, 0.0, 0.0, 1.0]
    # light0_ambient = [0.2, 0.2, 0.2, 1.0]
    # light0_diffuse = [1.0, 1.0, 1.0, 1.0]
    # light0_specular = [1.0, 1.0, 1.0, 1.0]

    # glLightfv(GL_LIGHT0, GL_POSITION, light0_position)
    # glLightfv(GL_LIGHT0, GL_AMBIENT, light0_ambient)
    # glLightfv(GL_LIGHT0, GL_DIFFUSE, light0_diffuse)
    # glLightfv(GL_LIGHT0, GL_SPECULAR, light0_specular)

    # # Definições de outras fontes de luz 
    # glEnable(GL_LIGHT1)
    # glEnable(GL_LIGHT2)

    # global_ambient = [0.2, 0.2, 0.2, 1.0]
    # glLightModelfv(GL_LIGHT_MODEL_AMBIENT, global_ambient)
    
    
    
    
    # Configuração da luz ambiente
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.2, 0.2, 0.2, 1.0))
    # Luz difusa
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.8, 0.8, 0.8, 1.0))
    # Posição da luz (coloque perto do Sol)
    glLightfv(GL_LIGHT0, GL_POSITION, (0.0, 0.0, 0.0, 1.0))
    
    # Especular
    glMaterialfv(GL_FRONT, GL_SPECULAR, (1.0, 1.0, 1.0, 1.0))
    glMateriali(GL_FRONT, GL_SHININESS, 100)




# def init_lighting():
# def setup_lighting():
#     glEnable(GL_DEPTH_TEST)
#     glShadeModel(GL_SMOOTH)
#     glEnable(GL_LIGHTING)
#     glEnable(GL_LIGHT0)
#     glEnable(GL_COLOR_MATERIAL)
#     glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
    
#     # Configuração da luz ambiente
#     glLightfv(GL_LIGHT0, GL_AMBIENT, (0.2, 0.2, 0.2, 1.0))
#     # Luz difusa
#     glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.8, 0.8, 0.8, 1.0))
#     # Posição da luz (coloque perto do Sol)
#     glLightfv(GL_LIGHT0, GL_POSITION, (0.0, 0.0, 0.0, 1.0))
    
#     # Especular
#     glMaterialfv(GL_FRONT, GL_SPECULAR, (1.0, 1.0, 1.0, 1.0))
#     glMateriali(GL_FRONT, GL_SHININESS, 100)