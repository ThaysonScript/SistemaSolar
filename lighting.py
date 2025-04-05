from OpenGL.GL import *

def setup_lighting():
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glShadeModel(GL_SMOOTH)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

    glLightfv(GL_LIGHT0, GL_POSITION, (0.0, 0.0, 0.0, 1.0))
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.1, 0.1, 0.1, 1.0))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (4.0, 4.0, 3.5, 1.0))
    glLightfv(GL_LIGHT0, GL_SPECULAR, (2.0, 2.0, 2.0, 1.0))

    # Atenuação para simular intensidade realista
    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 1.0)
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.005)
    glLightf(GL_LIGHT0, GL_QUADRATIC_ATTENUATION, 0.0001)


def init_lighting():
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

    # 💡 Posição da luz (coloque no centro do sol)
    glLightfv(GL_LIGHT0, GL_POSITION, (0.0, 0.0, 0.0, 1.0))

    # ✨ Componentes da luz
    glLightfv(GL_LIGHT0, GL_AMBIENT,  (0.1, 0.1, 0.1, 1.0))    # Luz ambiente
    glLightfv(GL_LIGHT0, GL_DIFFUSE,  (1.0, 1.0, 0.8, 1.0))    # Luz difusa (espalhada)
    glLightfv(GL_LIGHT0, GL_SPECULAR, (1.0, 1.0, 1.0, 1.0))    # Reflexo brilhante
