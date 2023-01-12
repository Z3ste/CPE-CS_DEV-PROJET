
'''
Toutes les entités neutres
'''
from classes.elements.entities import entity
from constants import *
from functions.graphics import load_image
from tkinter import *

class protection(entity):
    def __init__(self, area : Canvas, pos : list=[0,0]):

        self.area = area
        
        self.life = 15

        self.width = 70
        self.height = 30
        self.pos = [pos[0]-self.width , pos[1], pos[0]+self.width , pos[1] - self.height]

        self.thread = []

        self.score = -30

    def __prepare(self) -> None:
        #self.element = Canvas(self.area, width=self.size_x, height=self.size_y)
        self.element = self.area.create_rectangle(self.pos[0],self.pos[1],self.pos[2],self.pos[3],
                                                    width=2,outline='blue',fill='black')
        self.element_text=self.area.create_text(self.pos[0]+self.width,self.pos[1]-self.height/2,text=str(self.life),fill='cyan')

    def display(self):
        #self.element.place(x=self.pos[0],y=self.pos[1])
        #print("[*] Moving object `%i` to (%i,%i) " % (self.element,self.pos[0],self.pos[1]))
        self.area.coords(self.element, self.pos[0], self.pos[1],self.pos[2],self.pos[3])
        self.area.itemconfig(self.element_text,text=str(self.life))
        #self.area.create_image(self.pos[0], self.pos[1],  image=self.skin)
        self.area.update()
        self.thread.append(self.area.after(100, self.display))

    def destruct(self) -> None:
        self.area.delete(self.element)
        self.area.delete(self.element_text)
        self.alive = False 

    def run(self) -> None:
        self.__prepare()
        self.display()