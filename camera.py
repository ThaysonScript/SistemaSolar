import math
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *

camera_angle_x = 15.0 
camera_angle_y = 0.0 
camera_distance = 10.0 

def setup_camera():
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    gluLookAt(camera_distance * math.sin(math.radians(camera_angle_y)),
              camera_distance * math.sin(math.radians(camera_angle_x)),
              camera_distance * math.cos(math.radians(camera_angle_y)),
              0.0, 1, 0,
              0.0, 1.0, 0.0)

def handle_camera_movement(keys):
    global camera_angle_x, camera_angle_y, camera_distance

    camera_speed = 0.5
    zoom_speed = 0.1

    if keys[K_LEFT]:
        camera_angle_y -= camera_speed
    if keys[K_RIGHT]:
        camera_angle_y += camera_speed
    if keys[K_UP]:
        camera_angle_x -= camera_speed
    if keys[K_DOWN]:
        camera_angle_x += camera_speed
    if keys[K_w]:
        camera_distance -= zoom_speed
    if keys[K_s]:
        camera_distance += zoom_speed