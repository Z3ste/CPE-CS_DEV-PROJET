from classes.windows.welcome import main_menu
from constants import *
from tkinter import Tk



print("""

  _________                           .__                         .___                   
 /   _____/__________    ____  ____   |__| _______  _______     __| _/___________  ______
 \_____  \\____ \__  \ _/ ___\/ __ \  |  |/    \  \/ /\__  \   / __ |/ __ \_  __ \/  ___/
 /        \  |_> > __ \\  \__\  ___/  |  |   |  \   /  / __ \_/ /_/ \  ___/|  | \/\___ \ 
/_______  /   __(____  /\___  >___  > |__|___|  /\_/  (____  /\____ |\___  >__|  /____  >
        \/|__|       \/     \/    \/          \/           \/      \/    \/           \/ 
                  ____  ___      .__                                                     
                  \   \/  /_____ |  |   ___________   ___________                        
                   \     /\____ \|  |  /  _ \_  __ \_/ __ \_  __ \                       
                   /     \|  |_> >  |_(  <_> )  | \/\  ___/|  | \/                       
                  /___/\  \   __/|____/\____/|__|    \___  >__|                          
                        \_/__|                           \/                              

""")
print("[-] Chargement...")   
main_window = Tk()
main_window.attributes("-fullscreen", True)
main_window.title(GAME_NAME)
main_window['bg'] = "black"
MAIN = main_menu(main_window=main_window)
MAIN.run()


