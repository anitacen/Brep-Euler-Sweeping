import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from lib.util.Visual_util import VSolid

def display_solid(verts, edges, faces):

    glBegin(GL_QUADS)
    colors = (
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (0,1,0),
    (1,1,1),
    (0,1,1),
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (1,0,0),
    (1,1,1),
    (0,1,1),
    )

    for s in faces:
        x = 0
        for v in s:
            x+=1
            glColor3fv(colors[x])
            glVertex3fv(verts[v])

    glEnd()
    
    glBegin(GL_LINES)
    for e in edges:
        for v in e:
            glVertex3fv(verts[v])
    glEnd()

def visualize(solid):
    verts, edges, faces = get_face_vert_edge(solid)

    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        display_solid(verts, edges, faces)
        pygame.display.flip()
        pygame.time.wait(10)

    return 

def get_face_vert_edge(solid):
    vsolid = VSolid()
    for edge in solid.SEdges:
        vsolid.update(edge)
    for face in solid.SFaces:
        vsolid.update_face(face)
    return vsolid.verts, vsolid.edges, vsolid.faces