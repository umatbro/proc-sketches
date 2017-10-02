from vehicle import Vehicle
from time import time

v = None
v_pursuing = None

def setup():
    size(1280, 800)
    global v
    global v_pursuing
    
    v = Vehicle(width/2, height/2)
    v.maxspeed = 10
    v.maxforce = 0.5
    v_pursuing = Vehicle(30, 30)
    background(255)
    v.display()
    v_pursuing.display()
    delay(1000)


def draw():
    background(255)
    global v
    global v_pursuing
    mouse = PVector(mouseX, mouseY)
    
    # draw an ellipse at the mouse location 
    fill(200)
    stroke(0)
    strokeWeight(2)
    ellipse(mouse.x, mouse.y, 48, 48)
    
    # v.seek(mouse)
    v.arrive(mouse)
    v.update()
    v.display()
    
    v_pursuing.pursuit(v)
    v_pursuing.update()
    v_pursuing.display()