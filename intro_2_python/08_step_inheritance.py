#srbridge.com
#https://github.com/srbridgecom
#https://www.facebook.com/srbridge
#https://www.linkedin.com/in/r-bridge-3baa332a4/
#Python
#create or show inheritance......
#
class vehicle:
    def __inti__(self, started = False, speed = 0):
        self.started = started
        self.speed = speed
    def start(self):
        self.started = True
        print("started, go")
    def stop(self):
        seld.speed = 0
    def increase_speed(self, delta):
        if seld.started:
            self.speed = self.speed + delta
            print("vroom")
        else:
            print("You need to start 1st")

#car class will inherit from above vehicle.
class car(vehicle):
    trunk_open = False
    def open_trunk(self):
        self.trunk_open = True
    def close_trunk(self):
        self.trunk_open = False                  
                  
