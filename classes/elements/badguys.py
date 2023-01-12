from classes.elements.entities import entity
from functions.graphics import load_image
from constants import *
from tkinter import *
from itertools import count, cycle
from PIL import Image,ImageTk, ImageSequence, GifImagePlugin
import random

class alien(entity):
    
    def __init__(self, area : Canvas, img : str="image/invader.gif", pos : list=[0,0], fall_speed : int = 5000, score : int = 20):


        self.life = ALIEN_LIFE
        self.vitesse = ALIEN_SPEED
        self.shoot_damage = ALIEN_SHOOT_DAMAGE
        self.shoot_speed = ALIEN_SHOOT_SPEED
        self.fall_speed = fall_speed
        self.probability_shoot = ALIEN_PROBABILITY_SHOOT

        self.img = img
        self.area = area
        self.pos = pos

        self.score = score
        
        self.element = None
        self.time_counter = 0

        self.enemies = []

        self.width = 50
        self.height = 50

        self.alive = True

        self.thread = []
    
    def __prepare(self) -> None:
        self.load_gif(im=self.img, width=self.width, height=self.height)
        self.movement0()
        self.movement1()

    def load_gif(self,im : str, width: int = 50, height: int = 50) -> None:
        '''
        Preparation du gif. Extrait les frames et appel la fonction de gestion du gif
        '''
        if isinstance(im, str):
            im = Image.open(im)

        frames = []
        try:
            for idx, frame in enumerate(ImageSequence.Iterator(im)):
                frame = Image.new('RGBA', (width, height), color=(255,0,0,0))
                frame.paste(ImageSequence.Iterator(im)[idx].resize((width,height), Image.ANTIALIAS))
                frames.append(ImageTk.PhotoImage(frame))
                
        except EOFError:
            pass

        self.frames = cycle(frames)
 
        if len(frames) == 1:
            pass
        else:
            self.refresh_img()
        

    def refresh_img(self) -> None:
        '''
        Gestion du gif
        '''
        if self.alive:
            if self.frames:
                if self.element:
                    self.area.delete(self.element)
                self.element = self.area.create_image(self.pos[0],self.pos[1], image=next(self.frames))
                self.area.pack(side="left")
                
                self.thread.append(self.area.after(500, self.refresh_img))

    def movement0(self) -> None:
        '''
        Mouvement horizontal des aliens. Agit comme une animation
        '''
        if self.alive:
            if self.time_counter % 2 == 0:
                self.right()
            else:
                self.left()
            self.time_counter += 1
            
            if random.randrange(self.probability_shoot) == 0:
                shoot(area=self.area,alien=self, degat = self.shoot_damage, vitesse = self.shoot_speed,
                        pos=self.pos.copy(),enemies=self.enemies).run()

            
            self.thread.append(self.area.after(1000, self.movement0))

    def movement1(self) -> None:
        '''
        Mouvement vertical des aliens. Chute progressive vers le héros
        '''
        if self.alive:
            self.down()
            self.thread.append(self.area.after(self.fall_speed, self.movement1))

    def run(self) -> None:
        self.__prepare()
        self.display()

    def set_enemies(self, enemies : list) -> None:
        '''
        Permet de set une liste contenant les objets enemies
        '''
        self.enemies = enemies

class shoot(entity):

    def __init__(self,area : Canvas, alien : alien, degat : int,vitesse: int, img : str="image/shoot2.png", pos : list=[0,0], enemies : list=[]):
        self.img = img
        self.area = area
        self.alien = alien
        self.degat = degat

        self.pos = pos
        self.vitesse = vitesse
        self.enemies = enemies
        self.alive = True

        self.thread = []

    def __prepare(self) -> None:
        
        self.skin = load_image(self.img,width = 5, height=20)
        self.element = self.area.create_image(self.pos[0],self.pos[1], image=self.skin)
        self.area.pack(side="left")
    
    def run(self) -> None:
        self.__prepare()
        self.display()
        self.shoot()

    def shoot(self) -> None:
        if self.alive:
            if not self.down():
                self.destruct()
            else:
                for eid in range(0,len(self.enemies)):
                    '''
                    En cas de collision:
                        - on supprime l'enemie
                        - on supprime toutes references à l'enemie
                        - on detruit le laser
                    '''
                    if len(self.enemies[eid].pos) == 4 and self.enemies[eid].pos[0] <= self.pos[0]  <= self.enemies[eid].pos[2] and self.pos[1] -20 <= self.enemies[eid].pos[1] <= self.pos[1] + 40:
                        self.enemies[eid].life -= self.degat
                        if self.enemies[eid].life <= 0:
                            self.enemies[eid].destruct()
                            del self.enemies[eid]
                            self.alien.set_enemies(self.enemies)


                        self.destruct()
                        break
                    elif len(self.enemies[eid].pos) == 2 and self.enemies[eid].pos[0] - self.enemies[eid].width <= self.pos[0] <= self.enemies[eid].pos[0] + self.enemies[eid].width and self.pos[1] -20 <= self.enemies[eid].pos[1] <= self.pos[1] + 20:
                        self.enemies[eid].life -= self.degat
                        if self.enemies[eid].life <= 0:
                            self.enemies[eid].destruct()
                            del self.enemies[eid]
                            self.alien.set_enemies(self.enemies)


                        self.destruct()
                        break

                self.thread.append(self.area.after(25, self.shoot))

 



