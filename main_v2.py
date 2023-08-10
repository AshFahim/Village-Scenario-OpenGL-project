from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import cos, sin
import random



#Midpoint Line Drawing Algorithms
def midpointcircle(x, y, r):
    glPointSize(2) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    #N, S, E, W from center
    d = 1.25-r
    x1 = x 
    y1 = y
    x = 0 
    y = r 
    if x1 != 0 or y1!=0:
        glVertex2f(x+x1, y+y1)
        glVertex2f(y+y1, x+x1)
        glVertex2f(y+y1, -x+x1)
        glVertex2f(x+x1, -y+y1)
        glVertex2f(-x+x1, -y+y1)
        glVertex2f(-y+y1, -x+x1)
        glVertex2f(-y+y1, x+x1)
        glVertex2f(-x+x1, y+y1)
    else: 
        glVertex2f(x, y)
        glVertex2f(y, x)
        glVertex2f(y, -x)
        glVertex2f(x, -y)
        glVertex2f(-x, -y)
        glVertex2f(-y, -x)
        glVertex2f(-y, x)
        glVertex2f(-x, y)
    while x <= y:
        if d<0:
            #E
            d = d+2*x+3 
            x += 1  
        else:
            d = d + 2*x - 2*y + 5
            x = x + 1 
            y = y - 1 
        if x1 != 0 or y1!=0:
            glVertex2f(x+x1, y+y1)
            glVertex2f(y+y1, x+x1)
            glVertex2f(y+y1, -x+x1)
            glVertex2f(x+x1, -y+y1)
            glVertex2f(-x+x1, -y+y1)
            glVertex2f(-y+y1, -x+x1)
            glVertex2f(-y+y1, x+x1)
            glVertex2f(-x+x1, y+y1)
        else: 
            glVertex2f(x, y)
            glVertex2f(y, x)
            glVertex2f(y, -x)
            glVertex2f(x, -y)
            glVertex2f(-x, -y)
            glVertex2f(-y, -x)
            glVertex2f(-y, x)
            glVertex2f(-x, y)
    glEnd()
            
def draw_circle(x_center, y_center, radius, color):
    glColor3f(*color) # Set the color
    glBegin(GL_POLYGON)
    num_segments = 100 # Number of segments for smooth circle
    for i in range(num_segments):
        theta = 2.0 * 3.1415926 * i / num_segments
        dx = radius * cos(theta)
        dy = radius * sin(theta)
        glVertex2f(dx + x_center, dy + y_center)
    glEnd()



rain_animation = False
rain_timer = 0
rain_duration = 100  # Equivalent to 5 seconds if you're running at 20 FPS
raindrops = [(random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0)) for _ in range(500)]


def draw_raindrop(x, y):
    glColor3f(0.5, 0.5, 1.0)  # Light blue color for raindrops
    glBegin(GL_LINES)
    glVertex2f(x, y)
    glVertex2f(x, y + 0.05)
    glEnd()


# Function to draw sky (gradient background)
is_day = True
def draw_sky():
    glBegin(GL_QUADS)
    if is_day:
        glColor3f(0.4, 0.7, 1.0)  # Day sky color (top)
        glVertex2f(-1, 1)
        glVertex2f(1, 1)
        glColor3f(0.7, 0.9, 1.0)  # Day sky color (bottom)
    else:
        glColor3f(0.03, 0.03, 0.2)  # Darker night sky color (top)
        glVertex2f(-1, 1)
        glVertex2f(1, 1)
        glColor3f(0.1, 0.1, 0.3)  # Darker night sky color (bottom)
    glVertex2f(1, -0.5)
    glVertex2f(-1, -0.5)
    glEnd()

def draw_cloud(x, y):
    # Drawing three circles together to make a simple cloud shape
    glColor3f(1, 1, 1)  # White color for clouds
    draw_circle(x, y, 0.08, (1, 1, 1))
    draw_circle(x+0.05, y, 0.08, (1, 1, 1))
    draw_circle(x+0.025, y+0.04, 0.08, (1, 1, 1))

def draw_star(x, y):
    # Drawing a simple star using a point
    glColor3f(1, 1, 1)  # White color for stars
    glPointSize(2.0)  # Adjusting the size of the point
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()
star_positions = [(random.uniform(-1, 1), random.uniform(0, 1)) for _ in range(50)]


# Function to draw ground (flat surface)
def draw_ground():
    glColor3f(0.0, 0.6, 0.0)  # Green color for the ground
    glBegin(GL_QUADS)
    glVertex2f(-1, 0)
    glVertex2f(1, 0)
    glVertex2f(1, -1)
    glVertex2f(-1, -1)
    glEnd()

# Function to draw a simple house
def draw_house(x, y, width, height):
    # Draw main body of the house
    glColor3f(0.7, 0.4, 0.0)  # Brown color for the house
    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(x + width, y)
    glVertex2f(x + width, y - height)
    glVertex2f(x, y - height)
    glEnd()

    # Draw roof
    glColor3f(0.5, 0.0, 0.0)  # Dark red color for the roof
    glBegin(GL_TRIANGLES)
    glVertex2f(x, y)
    glVertex2f(x + width, y)
    glVertex2f(x + width / 2, y + height / 2)
    glEnd()

    # Draw windows
    glColor3f(0.0, 0.0, 0.0)  # Black color for windows
    glBegin(GL_QUADS)
    # Window 1
    glVertex2f(x + 0.05, y - 0.05)
    glVertex2f(x + 0.15, y - 0.05)
    glVertex2f(x + 0.15, y - 0.15)
    glVertex2f(x + 0.05, y - 0.15)
    # Window 2
    glVertex2f(x + width - 0.15, y - 0.05)
    glVertex2f(x + width - 0.05, y - 0.05)
    glVertex2f(x + width - 0.05, y - 0.15)
    glVertex2f(x + width - 0.15, y - 0.15)
    glEnd()

# Function to draw a simple tree
def draw_tree(x, y):
    # Draw trunk
    glColor3f(0.5, 0.25, 0.0)  # Brown color for the trunk
    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(x + 0.05, y)
    glVertex2f(x + 0.05, y + 0.15)
    glVertex2f(x, y + 0.15)
    glEnd()

    # Draw leaves
    glColor3f(0.0, 0.8, 0.0)  # Green color for the leaves
    for i in range(3):  # Three layers of leaves
        glBegin(GL_TRIANGLES)
        glVertex2f(x - 0.05, y + 0.15 + i * 0.05)
        glVertex2f(x + 0.1, y + 0.15 + i * 0.05)
        glVertex2f(x + 0.025, y + 0.25 + i * 0.05)
        glEnd()

def draw_bird(x, y):
    glColor3f(0, 0, 0)  # Black color for the bird
    glBegin(GL_LINES)
    glVertex2f(x, y)
    glVertex2f(x - 0.05, y + 0.05)
    glVertex2f(x, y)
    glVertex2f(x + 0.05, y + 0.05)
    glEnd()



# Global variable to hold bird positions
bird_positions = [
    (0.7, 0.6), (0.8, 0.65), (0.75, 0.7), 
    (0.9, 0.6), (0.85, 0.7), (0.95, 0.65),
    (1.0, 0.6), (1.05, 0.7)
] 
# Global variable to control bird animation
bird_animation = False

def animate_birds():
    global bird_positions
    # Move the birds to the left
    bird_positions = [(x - 0.01, y) for x, y in bird_positions]

'''
# Function to draw the sun using the midpoint circle drawing algorithm
def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
'''


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glLoadIdentity()

    

    # Draw sky and ground
    draw_sky()
    draw_ground()

    # Draw houses
    draw_house(-0.6, -0.2, 0.3, 0.3)
  

    # Draw trees
    draw_tree(-0.8, -0.2)  # First tree
    draw_tree(-0.6, -0.1)  # Second tree

    if bird_animation:
        global bird_positions
        bird_positions = [(x - 0.005, y) for x, y in bird_positions]  # Move birds to the left
        for x, y in bird_positions:
            draw_bird(x, y)
    
    global rain_timer, rain_animation

    if rain_animation:
        glColor3f(0.4, 0.4, 0.5)  # Darken sky color during rain
        rain_timer += 1
        if rain_timer > rain_duration:
            rain_animation = False
            rain_timer = 0
    else:
        glColor3f(0.529, 0.808, 0.922)  # Regular sky color

    if rain_animation:
        for x, y in raindrops:
            draw_raindrop(x, y)


    if is_day:
        draw_circle(0.7, 0.7, 0.08, (1.0, 0.843, 0.0)) # Sun coordinates, size, and color

        draw_cloud(0.4, 0.6)
        draw_cloud(-0.4, 0.5)
        draw_cloud(-0.6, 0.7)

        
    else:
        draw_circle(0.7, 0.7, 0.08, (1, 1, 1))
        
        for x, y in star_positions:
            draw_star(x, y)
            

    glutSwapBuffers()

def keyboard(key, x, y):
    global is_day, bird_animation
    global is_day, rain_animation, rain_timer

    if key == b'd':
        is_day = not is_day
    if key == b'b':
        bird_animation = not bird_animation

    if key == b'r' and not rain_animation:
        rain_animation = True
        rain_timer = 0

    glutPostRedisplay()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(800, 600)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("Village Scenario") #window name
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen) # Keep drawing the scene
glutKeyboardFunc(keyboard)
glutMainLoop()
