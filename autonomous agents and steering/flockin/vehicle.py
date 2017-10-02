class Vehicle(object):
    def __init__(self, x, y):
        self.position = PVector(0, 0)
        self.velocity = PVector(0, -2)
        self.acceleration = PVector(x, y)
        
        self.r = 6
        self.maxspeed = 10
        self.maxforce = 0.5
        
        
    def update(self):
        # update velocity
        self.velocity.add(self.acceleration)
        # limit speed
        self.velocity.limit(self.maxspeed)
        
        # reset acceleration to 0 each cycle
        self.acceleration.mult(0)
        
        self.position += self.velocity
        
        
    def applyForce(self, force):
        self.acceleration.add(force)
        
    def seek(self, target):
        """
        A method that calculates a steering force towards a target
        steer = desired - velocity
        """
        desired = target - self.position
        
        # scale to maximum speed
        desired.setMag(self.maxspeed)
        
        # steering = desired - velocity
        steer = desired - self.velocity
        steer.limit(self.maxforce)
        
        self.applyForce(steer)
        
        
    def display(self):
        theta = self.velocity.heading2D() + PI/2
        fill(127)
        stroke(0)
        strokeWeight(1)
        pushMatrix()
        translate(self.position.x, self.position.y)
        rotate(theta)
        beginShape()
        vertex(0, -self.r*2)
        vertex(-self.r, self.r*2)
        vertex(self.r, self.r*2)
        endShape(CLOSE)
        popMatrix()