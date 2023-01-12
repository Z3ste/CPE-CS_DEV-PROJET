from tkinter import *
from constants import *
from itertools import count, cycle
from PIL import Image,ImageTk
from functions.graphics import load_image

class entity:
    '''
    Classe parent
    '''

    def left(self) -> bool:
        if (self.pos[0] - self.vitesse) >= 0:
            self.pos[0] -= self.vitesse
            self.display()
            return True
        return False  
    def right(self) -> bool:
        if (self.pos[0] + self.vitesse) <= int(self.area['width']):
            self.pos[0] += self.vitesse
            self.display()
            return True
        return False  
    def up(self) -> bool:
        if (self.pos[1] - self.vitesse) >= 0:
            self.pos[1] -= self.vitesse
            self.display()
            return True
        return False  
    def down(self) -> bool:
        if (self.pos[1] + self.vitesse) <= int(self.area['height']):
            self.pos[1] += self.vitesse
            self.display()
            return True
        return False    

    def display(self):
        #self.element.place(x=self.pos[0],y=self.pos[1])
        #print("[*] Moving object `%i` to (%i,%i) " % (self.element,self.pos[0],self.pos[1]))
        if len(self.pos) > 2:
            self.area.coords(self.element, self.pos[0], self.pos[1],self.pos[2],self.pos[3])
        else:
            self.area.coords(self.element, self.pos[0], self.pos[1])
        #self.area.create_image(self.pos[0], self.pos[1],  image=self.skin)
        self.area.update()


    def destruct(self, explode: bool = True) -> None:
        self.skin = load_image("image/explosion.png")
        
        #self.element = Label(image=self.skin,bg="black")
        if explode:
            explode = self.area.create_image(self.pos[0],self.pos[1], image=self.skin)
            self.area.pack(side="left")
            self.area.after(30, self.delete, explode)
        else:
            self.delete()
    
    def delete(self, explode : int = None) -> None:
        if explode:
            self.area.delete(explode)
        self.area.delete(self.element)
        self.alive = False
        
        while len(self.thread) != 0:
            print("[-] Closing threads...")
            thread = self.thread.pop(-1)
            self.area.after_cancel(thread)
        print("[-] All threads are closed")
        
        