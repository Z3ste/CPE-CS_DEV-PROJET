'''
Tout ce qui concerne le visuel
'''
from tkinter import *
from functions.graphics import load_image, ImageLabel
from constants import *

from classes.elements.badguys import alien
from classes.elements.goodguys import hero
from classes.elements.neutralguys import protection

class window:
    def clear_page(self):
        # destroy all widgets from frame
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.frame.pack_forget()


class main_menu(window):
    '''
    Responsable de l'affichage de l'écran d'acceuil du jeu

    :param main_window:     Fenetre racine
    '''
    def __init__(self, main_window : Tk):
        self.main_window = main_window
        self.frame = Frame(self.main_window,bg="black")
        self.frame.pack(side="top", expand=True, fill="both")
        self.screen_size = [self.main_window.winfo_screenwidth(),self.main_window.winfo_screenheight()]


    def __prepare(self):

        self.lbl = ImageLabel(self.frame, bd=0, highlightthickness=0, relief='ridge')
        self.lbl.pack()
        self.lbl.load('image/space_invaders.gif')

        '''
        # Le msg 
        self.score_label = Label(self.frame,text="Welcome to...", bg="black",fg="#ffe900",font=('Bauhaus 93', 20))
        self.score_label.pack(padx=20, pady=80)

        self.logo_img = load_image("image/logo.png",width=200,height=300)
        self.logo = Canvas(self.frame, width=200, height=400, bg="black", bd=0, highlightthickness=0, relief='ridge')
        self.logo.create_image(100, 130, image = self.logo_img)
        self.logo.pack(padx=0,pady=0)
        '''

        # Bouton lancer la partie
        self.buttons = PanedWindow(self.frame, orient=HORIZONTAL, bd=0, relief='ridge',bg="black")

        self.start_button = Button(self.buttons, text ="Start", command = self.start_game,height=2, 
                                    width=30, bg="black",fg="#ffe900",font=('Bauhaus 93', 30),
                                    bd=0, highlightthickness=0, relief='ridge')

        # Bouton options
        self.options_button = Button(self.buttons, text ="Options", command = self.main_window.destroy,height=2, 
                                    width=30, bg="black",fg="#ffe900",font=('Bauhaus 93', 20),
                                    bd=0, highlightthickness=0, relief='ridge')

        # Le bouton quitter
        self.leave_button = Button(self.buttons, text ="Quit", command = self.main_window.destroy,height=2, 
                                    width=30, bg="black",fg="#ffe900",font=('Bauhaus 93', 20),
                                    bd=0, highlightthickness=0, relief='ridge')


        self.buttons.pack(side=TOP, expand=Y, fill=BOTH, pady=2, padx=2)
        self.buttons.add(self.options_button)
        self.buttons.add(self.start_button)
        self.buttons.add(self.leave_button)
        


    def run(self):
        self.__prepare()
        self.main_window.mainloop()

    def start_game(self,level=1):
        print("[*] Starting...")
        self.clear_page()
        new_level = game(main_window=self.main_window,level=level)
        new_level.run()



class game(window):
    '''
    Lance un niveau du jeu en préparant l'environement graphique, les aliens, les protections et le héro

    :param main_window:     Fenetre racine
    :param level:           niveau du jeu à lancer
    :param score:           score réalisé durant le précedant niveau
    '''
    def __init__(self, main_window : Tk, level : int=1, score : int=0):

        self.level = level
        self.score = score
        
        self.main_window = main_window
        self.frame = Frame(self.main_window,bg="black")
        self.frame.pack(side="top", expand=True, fill="both")
        
        self.screen_size = [self.main_window.winfo_screenwidth(),self.main_window.winfo_screenheight()]
        

    def __prepare(self) -> bool:
        '''
        Prepare graphiquement l'espace de jeu
        '''
        if self.level <= 5:
            background = "image/level_%i.png" % self.level
        else:
            background = "image/background-game.png"
        try:
            # Espace de jeu
            game_size = [self.screen_size[0]-400,self.screen_size[1]]
            self.game_canvas = Canvas(self.frame, width=game_size[0], height=game_size[1], bg='black')
            self.game_background = load_image(background,width=game_size[0],height=game_size[1])
            self.game_canvas.create_image(0, 0,  image=self.game_background,anchor = NW)
            self.game_canvas.pack(side="left")



            
            self.logo_img = load_image("image/board.png",width=400,height=200)
            self.logo = Canvas(self.frame, width=400, height=200, bg="black", bd=0, highlightthickness=0, relief='ridge')
            self.logo.create_image(200, 150, image = self.logo_img)
            self.logo.pack()

            # Le score
            self.score_label = Label(self.frame,text="Score: %i" % self.score,bg="black",fg="#ffe900",font=('Bauhaus 93', 40))
            self.score_label.pack(padx=20, pady=20)

            # Nombre de vie
            self.life_zone = Canvas(self.frame, width=400, height=40, bg="black",
                                    bd=0, highlightthickness=0, relief='ridge')
            self.hearth_img = load_image("image/hearth.png",width=30,height=30)
            for i in range(0,11):
                self.life_zone.create_image(20+i*30, 20,  image=self.hearth_img)
            self.life_zone.pack(padx=20,pady=10)

            # Indication pour commencer la partie
            if self.level <= len(LEVEL_NAME):
                msg = "Localisation: %s" % LEVEL_NAME[self.level-1]
            else:
                msg = "Localisation: Inconnue"
            self.start_indication = Label(self.frame,text=msg,bg="black",fg="#ffe900",font=('Arial', 20))
            self.start_indication.pack(padx=20)

            # Regle du jeu
            self.rules_img = load_image("image/rules.png",width=200,height=200)
            self.rules = Canvas(self.frame, width=443, height=300, bg="black", bd=0, highlightthickness=0, relief='ridge')
            self.rules.create_image(100, 150, image = self.rules_img)
            self.rules.pack(padx=20)

            # Bouton quitter
            self.leave_button = Button(self.frame, text ="Quit", command = self.main_window.destroy,height=2, 
                                        width=400,bg="black",fg="#ffe900",font=('Bauhaus 93', 20), 
                                        bd=0, highlightthickness=0, relief='ridge')
            self.leave_button.pack(padx=20,pady=0)

            return True

        except Exception as e: 
            print("[x] Erreur: %s" % str(e))
            return False

    def refresh_life(self):
        n_hearth = self.hero.life
        self.life_zone.delete("all")
        for i in range(0,n_hearth):
            self.life_zone.create_image(20+i*30, 20,  image=self.hearth_img)
        self.life_zone.pack(padx=20,pady=10)
        self.game_canvas.after(100, self.refresh_life)

    def _prepare_aliens(self,n_aliens_tot=30) -> bool:
        '''
        Instancie les objets aliens

        :param n_aliens_tot:    nombre d'alien a faire spawn
        '''
        self.aliens = []
        if 1==1:
            n_aliens, counter = 0,0
            while n_aliens != n_aliens_tot:
                for i in range(0,10):
                    if n_aliens > 10*2-1:
                        skin = "image/invader_3.gif"
                    elif n_aliens > 10-1:
                        skin = "image/invader_2.gif"
                    else:
                        skin = "image/invader.gif"
                    self.aliens.append( alien(area=self.game_canvas,img=skin,pos=[i*100 + 50,counter * 100 + 50]) )
                    self.aliens[-1].run()
                    n_aliens += 1
                    if n_aliens == n_aliens_tot:
                        break
                counter += 1
            return True
        else:
            #except Exception as e: 
            print("[x] Erreur: %s" % str(e))
            return False

    def _prepare_hero(self) -> bool:
        '''
        Instancie l'objet hero
        '''
        try:
            self.hero = hero(area=self.game_canvas,level=self)
            self.main_window.bind("<KeyPress>", self.hero.key_event)
            self.hero.run()
            return True
        except Exception as e:
            print("[x] Erreur: " % str(e))
            return False

    def _prepare_protections(self) -> bool:
        '''
        Instancie les objets protections
        '''
        self.protections = []
        try:
            for i in range(0,4):
                pos_y = int(self.game_canvas['height'])-210
                self.protections.append( protection(area=self.game_canvas,pos=[100+i*300,pos_y]) )
                self.protections[-1].run()

            return True
        except Exception as e:
            print("[x] Erreur: %s" % str(e))
            return False

    def run(self):

        if not self.__prepare():
            print("[!] Impossible d'initialiser l'environement graphique")

        if not self._prepare_aliens(n_aliens_tot=10*self.level):
            print("[!] Impossible d'initaliser les aliens !")

        if not self._prepare_hero():
            print("[!] Impossible d'initaliser le hero !")

        if not self._prepare_protections():
            print("[!] Impossible d'initaliser les barrieres !")  
        
        self.refresh_life()
        self.hero.set_enemies(self.aliens + self.protections)

        for i in self.aliens:
            i.set_enemies([self.hero] + self.protections)
     
        self.check_end()

        print("[-] Chargement du niveau ok")
        self.main_window.mainloop()
    
    def check_number_aliens(self) -> int:
        n = 0
        for enemie in self.hero.enemies:
            if isinstance(enemie,alien):
                n += 1
        return n

    def check_end(self):
        '''
        Verifie que le niveau n'est pas terminé, c'est à dire que le hero n'a plus de vie ou bien que tout les aliens
        ont été éliminé
        '''
        if self.check_number_aliens() == 0:
            self.next_level()
        elif self.hero.life <= 0:
            self.game_over()
        else:
            self.game_canvas.after(100, self.check_end)

    def game_over(self):
        print("[*] Game over")
        self.clear_page()
        end_menu_ = end_menu(main_window=self.main_window,score=self.score, level=self.level)
        end_menu_.run()
    
    def next_level(self):
        print("[*] Level complete")
        self.clear_page()
        new_level = game(main_window=self.main_window,level=self.level+1, score=self.score+200)
        new_level.run()

    def close(self):
        print("[*] Closing level menu..")
        self.main_window.destroy()



class end_menu(window):
    '''
    Responsable de l'affichage du menu du jeu

    :param main_window:     Fenetre racine
    :param level:           dernier niveau réalisé
    :param score:           score réalisé durant le précedant niveau
    '''
    def __init__(self, main_window : Tk, score : int, level : int):

        self.score = score
        self.level = level

        self.main_window = main_window
        self.frame = Frame(self.main_window,bg="black")
        self.frame.pack(side="top", expand=True, fill="both")

        self.screen_size = [self.main_window.winfo_screenwidth(),self.main_window.winfo_screenheight()]


        
    def __prepare(self) -> None:

        self.logo_img = load_image("image/logo.png",width=200,height=300)
        self.logo = Canvas(self.frame, width=200, height=300, bg="black", bd=0, highlightthickness=0, relief='ridge')
        self.logo.create_image(100, 250, image = self.logo_img)
        self.logo.pack(padx=20)

        # Le msg 
        self.score_label = Label(self.frame,text="Game over...",bg="black",fg="#ffe900",font=('Bauhaus 93', 60))
        self.score_label.pack(padx=20, pady=20)

        # Le score
        self.score_label = Label(self.frame,text="Score: %i" % self.score,bg="black",fg="#ffe900",font=('Bauhaus 93', 40))
        self.score_label.pack(padx=20, pady=20)

        # Bouton relancer
        self.restart_button = Button(self.frame, text ="Restart", command = self.restart,height=2, 
                                    width=400,highlightthickness=0,bg="black",fg="#ffe900",font=('Bauhaus 93', 20),
                                    bd=0, relief='ridge')
        self.restart_button.pack(padx=20,pady=0)

        # Le bouton quitter
        self.leave_button = Button(self.frame, text ="Quit", command = self.main_window.destroy,height=2, 
                            width=400,highlightthickness=0,bg="black",fg="#ffe900",font=('Bauhaus 93', 20),
                            bd=0, relief='ridge')
        self.leave_button.pack(padx=20,pady=30)


        


    def restart(self) -> None:
        print("[*] Restarting...")
        self.clear_page()
        main = main_menu(main_window=self.main_window)
        main.run()
            
    def run(self) -> None:
        self.__prepare()
        self.main_window.mainloop()

    def close(self) -> None:
        print("[*] Leaving ...")
        self.main_window.destroy()


