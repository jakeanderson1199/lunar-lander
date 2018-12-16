from tkinter import *
from lunarlandermodule import *
import time

class GUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Lunar Lander")
        self.lander= LunarLander()
        self.define_widgets()
        self.window.bind("<Key>",self.key)
        self.window.after(0, self.animation)
        self.window.mainloop()
    def key(self,event):
        if event.char == "-":
            self.lander.decrease_boost()
        if event.char == "+":
            self.lander.increase_boost()
    def define_widgets(self):
        self.canvas = Canvas(height=Gl.window_height + 38, width = 800,
                             bg = "white")
        self.canvas.pack()
        self.image=PhotoImage(file="spaceship.png")
        self.canvas.create_image(100, self.lander.get_coordinate(),
                                 image = self.image)
    def animation(self):
        try:
            while True:
                self.canvas.delete(ALL)
                if not self.lander.update():
                    self.canvas.create(100, self.lander.get_coordinate(),
                                       image=self.image)
                    self.canvas.update()
                    break
                self.canvas.create_text(500,100, text = "Distance to surface {:6.1f}".format(self.lander.y))
                self.canvas.create_text(500,200, text = "Fuel left {:7.1f}".format(self.lander.fuel))
                self.canvas.create_text(500,300, text = "Current Velocity: {:7.3f} Current Boost: {:7.3f}".format(self.lander.vel,self.lander.boost))
                self.canvas.create_image(100, self.lander.get_coordinate(), image = self.image)
                self.canvas.update()
                time.sleep(0.1)
        except:
            if self.lander.vel < -20:
                self.canvas.create_text(200,200, text = "You crashed")
            else:
                self.canvas.create_text(200,200, text = "You landed safely NICE")

game = GUI()
