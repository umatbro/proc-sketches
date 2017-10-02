from vehicle import Vehicle

v = None

def setup():
    size(1280, 800)
    global v
    v = Vehicle(width/2, height/2)

def draw():
    global v
    background(255)
    mouse = PVector(mouseX, mouseY)
    
    # draw an ellipse at the mouse location 
    fill(200)
    stroke(0)
    strokeWeight(2)
    ellipse(mouse.x, mouse.y, 48, 48)
    
    v.seek(mouse)
    v.update()
    v.display()