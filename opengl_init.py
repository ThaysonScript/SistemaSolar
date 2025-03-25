from OpenGL.GL import *
from OpenGL.GLU import *
from lighting import setup_lighting

def init_opengl():
    glEnable(GL_DEPTH_TEST)
    glClearColor(0.2, 0.3, 0.3, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 800 / 600, 0.1, 50.0)
    setup_lighting()