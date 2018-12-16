class Gl:
    height = 10000
    g = 1.65
    window_height = 500

class LunarLander:
    def __init__(self):
        self.y = Gl.height
        self.vel = 0
        self.boost = 0
        self.fuel = 500
    def __str__(self):
        return "height={:7.3f}, v = {:7.3f}, boost={:7.3f} fuel={:7.3f}".format(
            self.y,self.vel,self.boost,self.fuel)
    def update(self):  #less than 1/10 per second
        self.vel -= Gl.g/10
        self.vel += self.boost/10
        self.y += self.vel
        self.fuel -= self.boost
        if self.fuel <= 0:
            self.boost = 0
            self.fuel = 0
        return self.y > 0
    def run(self):
        for _ in range(100):
            self.update()
            print(self)
    def increase_boost(self):
        if self.boost<= 4.5:
            self.boost += .5
    def decrease_boost(self):
        if self.boost>= .5:
            self.boost -= .5
    def get_coordinate(self):
        return round((Gl.height-self.y)*Gl.window_height/Gl.height)
if __name__=="__main__":
    ll = LunarLander()
    while True:
        print(ll)
        print(ll.get_coordinate())
        ui = str(input("increase or decrease boost"))
        if ui == "+":
            ll.increase_boost()
        if ui == "-":
            ll.decrease_boost()
        ll.run()
