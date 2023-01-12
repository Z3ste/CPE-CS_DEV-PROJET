from classes.elements.entities import entity
from classes.elements.neutralguys import protection
from constants import *
from functions.graphics import load_image
from tkinter import *

class hero(entity):
    def __init__(self,area : Canvas, level : int, vaisseau:str="image/ship.png"):
        
        self.shoot_speed = SHOOT_SPEED
        self.shoot_damage = SHOOT_DAMAGE
        self.life = LIFE
        self.vitesse = SPEED

        self.img = vaisseau
        self.area = area
        self.pos = [0,0]
 

        self.enemies = []

        self.width = 50
        self.height = 50

        self.level = level

        self.thread = []

    def update_score(self, score : int) -> None:
        self.level.score += score
        self.level.score_label.config(text="Score: %i" % self.level.score)

    def set_enemies(self,enemies : list) -> None:
        '''
        Permet de set une liste contenant les objets enemies
        '''
        self.enemies = enemies

    def __prepare(self) -> None:
        self.skin = load_image(self.img)
        #self.element = Label(image=self.skin,bg="black")
        
        self.pos = self.__generate_start_point()
        self.element = self.area.create_image(self.pos[0],self.pos[1], image=self.skin)
        self.area.pack(side="left")

    def run(self) -> None:
        self.__prepare()
        self.display()

    def __generate_start_point(self) -> list:
        '''
        Genere le point de depart du vaisseau hero
        '''
        return [int(self.area['width'])/2 ,int(self.area['height'])-110]

    def key_event(self,event) -> None:
        if event.char == "d":
            self.right()
        if event.char == "q":
            self.left()
        if event.char == "z":
            self.up()
        if event.char == "s":
            self.down()
        if event.char == " ":
            shoot(area=self.area,hero=self, degat = self.shoot_damage, vitesse = self.shoot_speed,
                    pos=self.pos.copy(),enemies=self.enemies).run()

    def destruct(self) -> None:
        self.area.delete(self.element)
        self.alive = False
        print("[*] Joueur mort !")

class shoot(entity):

    def __init__(self,area : Canvas, hero : hero, degat : int,vitesse: int, img : str="image/shoot1.png", pos : list=[0,0], enemies : list=[]):

        self.img = img
        self.area = area
        self.hero = hero
        self.degat = degat

        self.pos = pos
        self.vitesse = vitesse
        self.enemies = enemies
        self.alive = True

        self.thread = []

    def __prepare(self):
        
        self.skin = load_image(self.img,width = 5, height=20)
        self.element = self.area.create_image(self.pos[0],self.pos[1], image=self.skin)
        self.area.pack(side="left")
    
    def run(self) -> None:
        self.__prepare()
        self.display()
        self.shoot()

    def shoot(self) -> None:
        if self.alive:
            if not self.up():
                self.destruct()
            else:
                for eid in range(0,len(self.enemies)):
                    '''
                    En cas de collision:
                        - on supprime l'enemie
                        - on supprime toutes references à l'enemie
                        - on detruit le laser
                    '''
                    if isinstance(self.enemies[eid],protection) and self.enemies[eid].pos[0] <= self.pos[0] <= self.enemies[eid].pos[2] and self.enemies[eid].pos[3] <= self.pos[1] <= self.enemies[eid].pos[1]:
                        # Protection utilise un systeme à 4 coordonnées
                        self.enemies[eid].life -= self.degat
                        if self.enemies[eid].life <= 0:
                            self.hero.update_score(self.enemies[eid].score)
                            self.enemies[eid].destruct()
                            del self.enemies[eid]
                            self.hero.set_enemies = self.enemies

                        self.destruct()
                        break
                    
                    elif not isinstance(self.enemies[eid],protection) and self.enemies[eid].pos[0] - self.enemies[eid].width <= self.pos[0] <= self.enemies[eid].pos[0] + self.enemies[eid].width and self.pos[1] -20 <= self.enemies[eid].pos[1] <= self.pos[1] + 20:
                        # Les autres objets utilise un systeme à 2 coordonnées
                        self.enemies[eid].life -= self.degat
                        if self.enemies[eid].life <= 0:
                            self.hero.update_score(self.enemies[eid].score)
                            self.enemies[eid].destruct()
                            del self.enemies[eid]
                            self.hero.set_enemies = self.enemies
                            

                        self.destruct()
                        break
                    
                self.thread.append(self.area.after(25, self.shoot))

 

