 #srbridge.com
#https://github.com/srbridgecom
#https://www.facebook.com/srbridge
#https://www.linkedin.com/in/r-bridge-3baa332a4/
#Python
 #create a python constructor
class car:
    def __init__(self, started = False, speed = 0):
        self.started = started
        self.speed = speed
        
    def start(self):
        self.started = True
        print("car started, ride!")
        
    def increase_speed(self, delta):
        if self.started:
            self.speed = self.speed + delta
            print("GO")
        else:
            print("you need to start the car")
            
    def stop(self):
        self.speed = 0
        
c1 = car()
c2 = car(True)
c3 = car(True, 50)
c4 = car(started=True, speed=40)

