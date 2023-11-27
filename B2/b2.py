import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


#CONTROLE DE CAMÊRA

# W -- Avança 
# S -- Recua
# D -- Direita 
# A -- Esquerda

# Seta para Cima Sobe a visão
# Seta para Baixo Desce a visão

# Mouse Direciona a camêra

# Espaço faz o movimento das aves

# Shift Esquerdo faz o movimento dos Flaps




aux= -1

def draw_bases():

    for i in range(2):   
        glColor3f(0.15, 0.15, 0.15)
        glBegin(GL_POLYGON)
        glVertex3f(0,0,i)      # A
        glVertex3f(6,6,i)      # B 
        glVertex3f(5,7,i)      # C
        glVertex3f(3,5,i)      # D
        glVertex3f(2,6,i)      # E
        glVertex3f(1,5,i)      # F
        glVertex3f(0,6,i)      # G
        glVertex3f(-1,5,i)     # H
        glVertex3f(-2,6,i)     # I
        glVertex3f(-3,5,i)     # J
        glVertex3f(-5,7,i)     # K
        glVertex3f(-6,6,i)     # L    
        glEnd()

   

def draw_liga():
    global aux
    glColor3f(0.15, 0.15, 0.15)
    glBegin(GL_QUADS)

    for i in range(2):
        
        # Lado Esquerdo
        glVertex3f(-6*aux, 6, 0)  # B
        glVertex3f(-6*aux, 6, 1)  # B
        glVertex3f(0, 0, 1)   # A
        glVertex3f(0, 0, 0)   # A

        # Lado Esquerdo atras
        glVertex3f(-5*aux, 7, 0)  # C
        glVertex3f(-5*aux, 7, 1)  # C
        glVertex3f(-6*aux, 6, 1)  # B
        glVertex3f(-6*aux, 6, 0)  # B

        # Lado Esquerdo atras
        glVertex3f(-5*aux, 7, 0)  # C
        glVertex3f(-5*aux, 7, 1)  # C
        glVertex3f(-3*aux, 5, 1)  # D
        glVertex3f(-3*aux, 5, 0)  # D

        # Lado Esquerdo atras
        glVertex3f(-3*aux, 5, 0)  # D
        glVertex3f(-3*aux, 5, 1)  # D
        glVertex3f(-2*aux, 6, 1)  # E
        glVertex3f(-2*aux, 6, 0)  # E


        # Lado Esquerdo atras
        glVertex3f(-2*aux, 6, 0)  # E
        glVertex3f(-2*aux, 6, 1)  # E
        glVertex3f(-1*aux, 5, 1)  # F
        glVertex3f(-1*aux, 5, 0)  # F

        # Lado Esquerdo atras
        glVertex3f(-1*aux, 5, 0)  # F
        glVertex3f(-1*aux, 5, 1)  # F
        glVertex3f(-0*aux, 6, 1)  # G
        glVertex3f(-0*aux, 6, 0)  # G


        aux = aux*(-1) 
    
    glEnd()

def draw_Window():
    global aux
    for i in range(2):
        glColor3f(0.10, 0.10, 0.10)
        
        
        glPushMatrix()  # Salva a matriz de transformação atual
        glTranslate(-1*aux, 4, 0.8) #LE e LD
        glRotate(90, 1, 0, 0)
        gluCylinder(gluNewQuadric(), 0.6, 0.6, 1.5, 20, 20)
        glPopMatrix()  # Restaura a matriz de transformação original

        glPushMatrix()  #Centro
        glTranslate(0, 3.5, 0.8)  # Translada para a direita do primeiro cilindro
        glRotate(90, 1, 0, 0)
        gluCylinder(gluNewQuadric(), 0.6, 0.6, 1.5, 20, 20)
        glPopMatrix()

        glPushMatrix()  #Centro Costa
        glTranslate(0, 4.5, 0.8)  
        glRotate(90, 1, 0, 0)
        gluCylinder(gluNewQuadric(), 0.005, 0.6, 1, 20, 20)
        glPopMatrix()

        glPushMatrix()  #LD e LE Costa
        glTranslate(1*aux, 5, 0.8)  
        glRotate(90, 1, 0, 0)
        gluCylinder(gluNewQuadric(), 0.005, 0.6, 1, 20, 20)
        glPopMatrix()

        aux = aux*(-1)


def draw_Wind():
    global aux
    for i in range(2):
        
        glColor3f(0.15,0.15,0.15)
        glPushMatrix()   #LE e LD Frente
        glTranslate(-1*aux, 1.5, 0.8)  
        glRotate(-90, 1, 0, 0)
        gluCylinder(gluNewQuadric(), 0.005, 0.6, 1, 20, 20)
        glPopMatrix()

        glPushMatrix()  #Centro Frente
        glTranslate(0, 1, 0.8)  
        glRotate(-90, 1, 0, 0)
        gluCylinder(gluNewQuadric(), 0.005, 0.6, 1, 20, 20)
        glPopMatrix()

        aux = aux*(-1)

flaps=0

def draw_Flap():
        global flaps
        glColor3f(0.2, 0.2, 0.2)
        glTranslatef( 3, 5, 1)
        glRotatef(45,0,0,1)
        glRotatef(flaps,1,0,0)
        glRotatef(-45,0,0,1)
        glTranslatef( -3, -5, -1)
        
        glBegin(GL_QUADS)
        # Asa Esquerda atras
        glVertex3f(3, 5, 1)   # Canto inferior esquerdo
        glVertex3f(4, 6, 1)   # Canto inferior direito
        glVertex3f(3.5, 6.5, 1)   # Canto superior direito
        glVertex3f(2.5, 5.5, 1)   # Canto superior esquerdo
        glEnd()

        glTranslatef(3, 5, 1)
        glRotatef(45,0,0,1)
        glRotatef(-flaps,1,0,0)
        glRotatef(-45,0,0,1)
        glTranslatef( -3, -5, -1)


        glColor3f(0.2, 0.2, 0.2)
        glTranslatef(-3,5, 1)
        glRotatef(-45,0,0,1)
        glRotatef(flaps,1,0,0)
        glRotatef(45,0,0,1)
        glTranslatef(3, -5, -1)
        glBegin(GL_QUADS)
        
        glVertex3f(-3, 5, 1)   # Canto inferior esquerdo
        glVertex3f(-4, 6, 1)   # Canto inferior direito
        glVertex3f(-3.5, 6.5, 1)   # Canto superior direito
        glVertex3f(-2.5, 5.5, 1)
        glEnd()
                            # Canto superior esquerdo
        glTranslatef(-3,5, 1)
        glRotatef(-45,0,0,1)
        glRotatef(-flaps,1,0,0)
        glRotatef(45,0,0,1)
        glTranslatef(3, -5, -1)

ave1 = 40
ave2 = 20
ave3 = 0
ave4 = -20
ave5 = -40
def cenario():
  
    glRotate(90,1,0,0)
    glPushMatrix()
    glColor3f(0.2, 0.2, 0.2)
    glTranslate(-2,4,1)
    glColor3f(0.8, 0.8, 0.8)
    glBegin(GL_POLYGON)
    glVertex3f(-0.5, -1, (ave1-1))
    glVertex3f(-0.5, 0, ave1)
    glVertex3f(0.5, -1, ave1)
    glVertex3f(-0.5, -1, (ave1-1))
    glEnd()
    glPopMatrix()
    
    glPushMatrix()
    glTranslate(2,4,-1)
    glBegin(GL_POLYGON)
    glVertex3f(-0.5, -1, (ave2-1))
    glVertex3f(-0.5, 0, ave2)
    glVertex3f(0.5, -1, ave2)
    glVertex3f(-0.5, -1, (ave2-1))
    glEnd()
    glPopMatrix()
    
    glPushMatrix()
    glTranslate(-2,4,-1)
    glBegin(GL_POLYGON)
    glVertex3f(-0.5, -1, (ave3-1))
    glVertex3f(-0.5, -0, ave3)
    glVertex3f(0.5, -1, ave3)
    glVertex3f(-0.5, -1, (ave3-1))
    glEnd()
    glPopMatrix()
    
    glPushMatrix()
    glTranslate(-5,1,-1)
    glBegin(GL_POLYGON)
    glVertex3f(-0.5, -1, (ave4-1))
    glVertex3f(-0.5, -0, ave4)
    glVertex3f(0.5, -1, ave4)
    glVertex3f(-0.5, -1, (ave4-1))
    glEnd()
    glPopMatrix()
    
    glPushMatrix()
    glBegin(GL_POLYGON)
    glVertex3f(-0.5, -1, (ave5-1))
    glVertex3f(-0.5, -0, ave5)
    glVertex3f(0.5, -1, ave5)
    glVertex3f(-0.5, -1, (ave5-1))
    glEnd()
    glPopMatrix()
    glFlush()

def main():
    pygame.init()
    display = (800, 600)
    screen = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_AMBIENT, [0.5, 0.5, 0.5, 1])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1])

    

    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    glMatrixMode(GL_MODELVIEW)
    gluLookAt(0, -8, 0, 0, 0, 0, 0, 0, 1)
    viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
    glLoadIdentity()

    glClearColor(0.0, 0.0, 0.90, 0.90)

    # init mouse movement and center mouse on screen
    displayCenter = [screen.get_size()[i] // 2 for i in range(2)]
    mouseMove = [0, 0]
    pygame.mouse.set_pos(displayCenter)

    up_down_angle = 0.0


    paused = False
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                    run = False
                if event.key == pygame.K_PAUSE or event.key == pygame.K_p:
                    paused = not paused
                    
            if not paused:

                glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
                
                if event.type == pygame.MOUSEMOTION:
                    mouseMove = [event.pos[i] - displayCenter[i] for i in range(2)]
                pygame.mouse.set_pos(displayCenter)

        if not paused:
            # get keys
            keypress = pygame.key.get_pressed()

            # init model view matrix
            glLoadIdentity()

            # apply the look up and down
            up_down_angle += mouseMove[1] * 0.1
            glRotatef(up_down_angle, 1.0, 0.0, 0.0)

            # init the view matrix
            glPushMatrix()
            glLoadIdentity()

            # apply the movement
            if keypress[pygame.K_w]:
                glTranslatef(0, 0, 0.1)
            if keypress[pygame.K_s]:
                glTranslatef(0, 0, -0.1)
            if keypress[pygame.K_d]:
                glTranslatef(-0.1, 0, 0)
            if keypress[pygame.K_a]:
                glTranslatef(0.1, 0, 0)
            if keypress[pygame.K_UP]:
                glTranslatef(0, -0.1, 0)
            if keypress[pygame.K_DOWN]:
                glTranslatef(0, 0.1, 0)

            if keypress[pygame.K_LSHIFT]:
                global flaps
                if flaps == 45:
                    flaps = flaps*-1
                else:
                    flaps = 45
            if keypress[pygame.K_SPACE]:
                global ave1
                global ave2
                global ave3
                global ave4
                global ave5
                ave1 -= 1
                ave2 -= 1
                ave3 -= 1
                ave4 -= 1
                ave5 -= 1

                if ave1 < -50:
                    ave1 = 50
                if ave2 < -50:
                    ave2 = 50
                if ave3 < -50:
                    ave3 = 50
                if ave4 < -50:
                    ave4 = 50
                if ave5 < -50:
                    ave5 = 50

                
            # apply the left and right rotation
            glRotatef(mouseMove[0] * 0.1, 0.0, 1.0, 0.0)

            # multiply the current matrix by the get the new view matrix and store the final view matrix
            glMultMatrixf(viewMatrix)
            viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)

            # apply view matrix
            glPopMatrix()
            glMultMatrixf(viewMatrix)

            glLightfv(GL_LIGHT0, GL_POSITION, [1, -1, 1, 0])

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            glPushMatrix()
            draw_bases()
            draw_liga()
            draw_Window()
            draw_Wind()
            draw_Flap()
            cenario()
            glTranslatef(0.0, 0.0, -1)
            glPopMatrix()
            

            pygame.display.flip()
            pygame.time.wait(10)
            
    pygame.quit()

main()
